# ElevenTools - Rilevatore Avanzato di Executor

ElevenTools è un'applicazione avanzata per rilevare la presenza di executor Roblox sul tuo sistema. Utilizza metodi di scansione multipli per identificare file, processi e voci di registro associati a più di 30 executor noti.

## Caratteristiche

- **Database completo**: Rileva oltre 50 executor Roblox noti
- **Scansione multi-livello**: Controlla file, processi in esecuzione e voci di registro
- **Interfaccia grafica intuitiva**: Facile da usare con risultati chiari
- **Sistema di logging**: Registra tutte le attività per riferimento futuro

## Requisiti

Prima di utilizzare ElevenTools, assicurati di avere installato:

1. **Python 3.7+**: Scaricalo da [python.org](https://www.python.org/downloads/)
2. **Moduli Python richiesti**:
   - customtkinter
   - altri moduli standard (inclusi in Python)

## Versione Ottimizzata

Questa versione include importanti ottimizzazioni per migliorare le prestazioni e prevenire blocchi dell'interfaccia utente:

- **Sistema di timeout migliorato**: Previene il blocco dell'applicazione durante scansioni intensive
- **Feedback visivo avanzato**: Barra di progresso e indicatori percentuali durante la scansione
- **Scansione intelligente**: Prioritizzazione dei percorsi più comuni per risultati più rapidi
- **Gestione efficiente delle risorse**: Limitazione del carico di sistema durante le operazioni intensive

## Installazione

1. Assicurati che Python sia installato sul tuo sistema
2. Installa le dipendenze necessarie:

```
pip install -r requirements.txt
```

3. Esegui il programma:

```
python eleventools.py
```

## Utilizzo

1. Avvia l'applicazione
2. Clicca sul pulsante "SCANSIONE COMPLETA"
3. Attendi il completamento della scansione
4. Visualizza i risultati nell'area di testo

## Note sulla sicurezza

Questo strumento è progettato solo per scopi educativi e di sicurezza. Utilizzalo responsabilmente e solo sui tuoi dispositivi o su dispositivi per cui hai l'autorizzazione esplicita.

## Risoluzione dei problemi

Se riscontri problemi durante l'esecuzione:

1. Verifica che Python sia installato correttamente
2. Assicurati che il modulo customtkinter sia installato
3. Controlla i log nella cartella "logs" per dettagli sugli errori

## Miglioramenti recenti

- Database di executor ampliato a oltre 50 programmi noti
- Migliorata l'affidabilità della scansione dei file
- Aggiunto il rilevamento dei processi in esecuzione
- Implementata la scansione del registro di sistema
- Aggiunto sistema di logging dettagliato
- Migliorata l'interfaccia utente con indicatori di stato
