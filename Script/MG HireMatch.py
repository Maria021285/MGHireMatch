import pandas as pd
import sqlite3

# 1. Caricamento File CSV creati con funzione Random in Excel 

Operatori = pd.read_csv("https://github.com/Maria021285/MGHireMatch/blob/main/Data/Dim_Operatori.csv")
Clienti = pd.read_csv("https://github.com/Maria021285/MGHireMatch/blob/main/Data/Dim_Clienti.csv")
Fornitori = pd.read_csv("https://github.com/Maria021285/MGHireMatch/blob/main/Data/Dim_Fornitori.csv")
Richieste = pd.read_csv("https://github.com/Maria021285/MGHireMatch/blob/main/Data/Fact_Richieste.csv")

# 1.1 Testing funzionamento
print("File caricati")
print(Richieste.head())


# 2. Pulizia di sicurezza alle colonne

Operatori.columns = Operatori.columns.str.strip().str.lower().str.replace(" ", "_")
Clienti.columns = Clienti.columns.str.strip().str.lower().str.replace(" ", "_")
Fornitori.columns = Fornitori.columns.str.strip().str.lower().str.replace(" ", "_")
Richieste.columns = Richieste.columns.str.strip().str.lower().str.replace(" ", "_")


# 3. Creazioni di dimensioni per dare significato ai dati

dim_operatore = Operatori[[ 

    "operatore_id",
    "nome_operatore",
    "ruolo",
    "categoria_servizio",
    "zona",
    "seniority",
    "capacita_massima",
    "richieste_attive",
    "saturazione",
    "latitudine",
    "longitudine"
                                
]].drop_duplicates()

dim_cliente = Clienti[[
    "cliente_id",
    "zona",
    "settore",
    "data_iscrizione",
    "fascia_cliente"

]].drop_duplicates()

dim_fornitore = Fornitori[[
    "fornitore_id",
    "nome",
    "categoria_servizio",
    "zona"
]].drop_duplicates()

# 4. FACT con aggiunzione di un prolungamento della risorsa (tabella centrale del Data Ware House)


fact_richieste = Richieste[[


    "richiesta_id",
    "cliente_id",
    "fornitore_id",
    "operatore_id",
    "data_apertura",
    "data_chiusura",
    "stato",
    "priorita_richiesta",
    "importo_base",
    "iva_22",
    "importo_totale",
    "tempo_chiusura_giorni",
    "prolungata"
]]


# Prolungamento di una risorsa 
fact_richieste["prolungata"] = fact_richieste["tempo_chiusura_giorni"] > 20

# 4.1 Testing funzionamento FACT

print("\n FACT creata con prolungamento di una risorsa")


# 5. Creazione database SQLite

conn = sqlite3.connect("https://github.com/Maria021285/MGHireMatch/blob/main/Database/dw.sqlite")

# salvataggio tabelle
dim_operatore.to_sql("dim_operatore", conn, if_exists="replace", index=False)
dim_cliente.to_sql("dim_cliente", conn, if_exists="replace", index=False)
dim_fornitore.to_sql("dim_fornitore", conn, if_exists="replace", index=False)
fact_richieste.to_sql("fact_richieste", conn, if_exists="replace", index=False)

# Testing salvataggio SQL
print("Data Warehouse creato in SQLite")


# 6. Tabella Aanalisi (MERGE)


df = fact_richieste.merge(dim_operatore, on="operatore_id", how="left")
df = df.merge(dim_cliente, on="cliente_id", how="left")
df = df.merge(dim_fornitore, on="fornitore_id", how="left")

#6.1 Testing del Merge

print("\n Merge completato")
print(df.head())


# 7. KPI (SATURAZIONE OPERATORE)


if "carico_operatore" in Operatori.columns:

    df = df.merge(
        Operatori[["operatore_id", "carico_operatore"]],
        on="operatore_id",
        how="left"
    )

    df["saturazione"] = df["carico_operatore"] / df["capacita_massima"]

    df["stato_carico"] = df["saturazione"].apply(
        lambda x: "OVERLOAD" if x > 1 else ("SATURATO" if x >= 0.8 else "OK")
    )

    print("\n KPI calcolati")
    print(df[["operatore_id", "saturazione", "stato_carico"]].head())


# 8. Query SQL KPI

query_kpi = """
SELECT 
    COUNT(*) AS numero_richieste,
    SUM(importo_totale) AS incasso_totale,
    AVG(tempo_chiusura_giorni) AS tempo_medio
FROM fact_richieste;
"""

kpi = pd.read_sql(query_kpi, conn)
print("\n KPI PRINCIPALI:")
print(kpi)

# 9. KPI AVANZATO (clienti ricorrenti in numero)


query_clienti = """
SELECT 
    COUNT(*) AS clienti_ricorrenti
FROM (
    SELECT cliente_id
    FROM fact_richieste
    GROUP BY cliente_id
    HAVING COUNT(*) > 1
);
"""

clienti_ricorrenti = pd.read_sql(query_clienti, conn)

#9.1 Testing funzionamento dei KPI

print("\n Clienti Ricorrenti:")
print(clienti_ricorrenti)


#10. clienti ricorrenti in percentuale

query_percentuale_clienti = """
SELECT 
    100.0 * SUM(CASE WHEN conteggio > 1 THEN 1 ELSE 0 END) / COUNT(*) 
    AS percentuale_clienti_ricorrenti
FROM (
    SELECT cliente_id, COUNT(*) as conteggio
    FROM fact_richieste
    GROUP BY cliente_id

);
"""

percentuale_clienti = pd.read_sql(query_percentuale_clienti, conn)

#10.1 Testing funzionamento percentuali dei clienti ricorrenti
print("\n Percentuale Clienti Ricorrenti:")
print(percentuale_clienti)

# 11. KPI per il prolungamento in Phyton

percentuale_prolungate = df["prolungata"].mean() * 100

#testing prolungamento Phyton

print("\n Percentuale richieste prolungate (Python):")
print(round(percentuale_prolungate, 2), "%")

# 12.EXPORT PER POWER BI con testing

df.to_csv("dataset_powerbi.csv", index=False)

print("\n File per Power BI creato: dataset_powerbi.csv")


# 13. Chiususra database


conn.close()

print("\n Processo completato")
