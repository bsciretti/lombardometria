# lombardometria
Il progetto _lombardometria_ riguarda la raccolta di dati in formato utilizzabile dal computer per lo studio delle varietà dialettali della lingua lombarda e per analizzare le differenze nelle ortografie e il loro rapporto con l'evoluzione e la diffusione della lingua.

## Dati che ci servono al momento
- Swadesh List 207 del dialetto bergamasco e milanese in quattro formati:
  - IPA
  - Ortografia locale (Milanese Classica per il milanese, Ortografia del Ducato per il bergamasco)
  - Ortografia _Noeuva Grafia Lombarda_
  - Ortografia _Scriver Lombard_

Sono, in ogni caso, graditi altri dati utilizzabili in futuro. Ogni dialetto dev'essere formattato in questo formato: IPA, ortografia locale, ortografia NOL e ortografia SL.

## Come fornire i dati
Poiché al momento li studiamo utilizzando librerie Python, i dati vanno inseriti come liste Python. Bisogna seguire l'ordine dato da [Wikipedia in lingua inglese](https://en.wikipedia.org/wiki/Swadesh_list) e utilizzare se possibile _cognates_ tra i due dialetti. Per chi non lo sapesse una lista Python si distingue dall'essere incapsulata da parentesi quadre e dall'avere ogni elemento separato da virgole e definito da virgolette.

Per la trascrizione IPA, consigliamo di segnare l'accento, ma al momento pensiamo di eliminarlo in fase di elaborazione, cosa che a quanto pare viene fatta dalla maggioranza degli studi dialettometrici.

## Obiettivi
Al momento puntiamo di studiare la differenza e il rapporto tra grafia e dialetto, utilizzando le distanze di Levenshtein, nei riguardi del milanese e del bergamasco.

## Contributori
Ringraziamo i seguenti contributori:
- StevanCO (dialetto comasco)
