# MGHireMatch
MG HireMatch – Soluzione di Data Warehouse e Business Intelligence per l’analisi dei processi di recruiting, il monitoraggio dei KPI e il supporto decisionale

## Origine del Nome del Progetto


Il nome **MG HireMatch** identifica la piattaforma sviluppata nell'ambito del progetto di Business Intelligence.

- **MG** richiama le iniziali dell'autrice del progetto, Maria Giano.
- **Hire** rappresenta il processo di recruiting e selezione del personale.
- **Match** richiama l'incontro tra le esigenze delle aziende e le competenze dei candidati.

Il nome **MG HireMatch** sintetizza la missione del sistema: favorire l'incontro tra domanda e offerta di competenze professionali attraverso un'infrastruttura di Business Intelligence in grado di trasformare i dati operativi in informazioni strategiche a supporto del monitoraggio delle performance, del controllo direzionale e dei processi decisionali.

---

## Descrizione del Progetto

**MG HireMatch** rappresenta un sistema di Business Intelligence progettato per l'analisi e il monitoraggio dei processi di recruiting e selezione del personale.

La soluzione è basata su un'architettura composta da sorgenti dati strutturate, processi ETL sviluppati in Python, un Data Warehouse realizzato in SQLite e dashboard interattive costruite in Power BI.

L'obiettivo del progetto è fornire agli utenti strumenti di analisi in grado di trasformare i dati operativi in conoscenza a valore aggiunto, favorendo il monitoraggio delle performance, il controllo direzionale e il supporto ai processi decisionali attraverso un approccio data-driven.


---

## Fonti dei Dati


Le fonti dati utilizzate sono dataset simulati in formato CSV generati tramite Excel mediante le funzioni CASUALE() e CASUALE.TRA(), integrate con formule personalizzate per rappresentare clienti, fornitori, operatori e richieste di recruiting.

I dati simulati sono stati successivamente elaborati attraverso processi ETL sviluppati in Python e caricati nel Data Warehouse realizzato in SQLite.

---

## Obiettivi

L'obiettivo finale del progetto è trasformare i dati operativi in informazioni significative e facilmente interpretabili, promuovendo un approccio data-driven ai processi di recruiting e gestione delle risorse.

Per approccio data-driven si intende un modello decisionale basato sull'analisi dei dati e sull'utilizzo di indicatori di performance, finalizzato a supportare decisioni fondate su evidenze oggettive.

A tal fine, il sistema consente di:

- Analizzare le richieste di recruiting e il loro andamento nel tempo.
- Monitorare le performance operative di operatori, clienti e fornitori.
- Valutare l'efficienza dei processi di selezione attraverso specifici indicatori di performance.
- Supportare il processo decisionale mediante KPI, dashboard interattive e strumenti di Business Intelligence.


---

## Architettura del Sistema

```text
Dati sorgente (CSV)
        ↓
Python (ETL)
        ↓
SQLite Data Warehouse
        ↓
Dataset Analitico
        ↓
Power BI
        ↓
Dashboard Direzionale
Dashboard Operativa
        ↓
Supporto Decisionale
```
---

## Struttura del Data Warehouse

Il Data Warehouse è stato progettato secondo uno schema relazionale composto da tre tabelle dimensionali e una Fact Table centrale.

### Dimensioni

#### Dim_Operatori

Contiene le informazioni anagrafiche e operative relative agli operatori coinvolti nel processo di recruiting.

Campi principali:

- operatore_id
- nome_operatore
- ruolo
- categoria_servizio
- zona
- seniority
- capacita_massima
- richieste_attive
- saturazione
- latitudine
- longitudine

#### Dim_Clienti

Contiene le informazioni relative ai clienti che utilizzano i servizi di recruiting.

Campi principali:

- cliente_id
- zona
- settore
- data_iscrizione
- fascia_cliente

#### Dim_Fornitori

Contiene le informazioni relative ai fornitori coinvolti nell'erogazione dei servizi.

Campi principali:

- fornitore_id
- nome
- categoria_servizio
- zona

---

### Fact Table

#### Fact_Richieste

Rappresenta la tabella centrale del Data Warehouse e contiene tutte le informazioni relative alle richieste di recruiting.

Campi principali:

- richiesta_id
- cliente_id
- fornitore_id
- operatore_id
- data_apertura
- data_chiusura
- stato
- priorita_richiesta
- importo_base
- iva_22
- importo_totale
- tempo_chiusura_giorni
- prolungata

---

### Relazioni

La Fact Table Fact_Richieste è collegata alle dimensioni Dim_Operatori, Dim_Clienti e Dim_Fornitori mediante le rispettive chiavi identificative, consentendo analisi multidimensionali e il calcolo dei KPI utilizzati nelle dashboard Power BI.

---

## KPI Implementati

I KPI (Key Performance Indicators) sono stati progettati per fornire una visione sia direzionale sia operativa delle attività di recruiting, consentendo il monitoraggio delle performance e il supporto ai processi decisionali.

### Dashboard Direzionale

Indicatori utilizzati per il monitoraggio delle performance aziendali e dei risultati economici:

- Richieste Totali
- Ricavi Totali
- Tempo Medio di Chiusura
- Clienti Attivi

### Analisi Operativa

Indicatori utilizzati per il monitoraggio delle attività operative e del carico di lavoro degli operatori:

- Saturazione Media Operatori
- Richieste Medie per Operatore
- Percentuale Richieste Prolungate
- Percentuale Clienti Ricorrenti
---

## Dashboard

Le dashboard sviluppate in Power BI consentono una lettura complementare delle informazioni, distinguendo tra analisi direzionale e analisi operativa.

### Dashboard Direzionale

| KPI / Visualizzazione | Tipologia |
|----------------------|-----------|
| Richieste Totali | Card KPI |
| Ricavi Totali | Card KPI |
| Tempo Medio di Chiusura | Card KPI |
| Clienti Attivi | Card KPI |
| Andamento delle Richieste nel Tempo | Grafico a linee |
| Top 5 Fornitori per Incasso | Grafico a barre orizzontali |
| Richieste per Zona Fornitore | Grafico a colonne |
| Distribuzione delle Richieste per Categoria di Servizio | Treemap |

### Analisi Operativa

| KPI / Visualizzazione | Tipologia |
|----------------------|-----------|
| Saturazione Media | Card KPI |
| Richieste Medie per Operatore | Card KPI |
| % Richieste Prolungate | Card KPI |
| % Clienti Ricorrenti | Card KPI |
| Operatori e Carico di Lavoro sul Territorio | ArcGIS Map |
| Saturazione Media per Seniority | Grafico a colonne |
| Stato delle Richieste | Grafico a barre |
| Top 5 Clienti per Incasso | Grafico a barre orizzontali |

---

## Tecnologie Utilizzate


Il progetto è stato sviluppato utilizzando le seguenti tecnologie:

- **Python** per l'implementazione dei processi ETL e la preparazione dei dati.
- **Pandas** per la manipolazione, trasformazione e analisi dei dataset.
- **SQLite** per la realizzazione del Data Warehouse relazionale.
- **Power BI Desktop** per la progettazione delle dashboard e la visualizzazione dei KPI.
- **ArcGIS for Power BI** per la rappresentazione geografica degli operatori e del carico di lavoro sul territorio.


---

## Risultati

### Dashboard Direzionale

### Dashboard Operativa
---

## Output Generati

Il processo ETL produce i seguenti output:

- **dw.sqlite**: database relazionale utilizzato come Data Warehouse.
- **dataset_powerbi.csv**: dataset integrato destinato alla realizzazione delle dashboard Power BI.

---

## Autore


Maria Giano

MG HireMatch rappresenta un progetto applicativo finalizzato all'integrazione di tecniche di Data Warehousing, Business Intelligence e Data Analytics nel contesto dei processi di recruiting e selezione del personale, con l'obiettivo di supportare il controllo direzionale e operativo attraverso un approccio data-driven. 
