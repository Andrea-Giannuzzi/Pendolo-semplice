# Pendolo semplice

Questa repository raccoglie piccoli progetti Python/Jupyter dedicati allo studio
del pendolo semplice. L'obiettivo e' usare codice, grafici e notebook per
collegare il modello fisico alla sua implementazione computazionale.

## Progetti disponibili

- [Pendolo numerico](./pendolo_semplice_numerico/README.md): integrazione
  numerica dell'equazione non lineare del pendolo.
- [Pendolo per piccole oscillazioni](./pendolo_semplice_piccole_oscillazioni/README.md):
  soluzione analitica nel limite in cui `sin(theta) ~= theta`.

## Notebook presenti

La repository contiene questi notebook Jupyter:

- `pendolo_semplice_numerico/pendolo_semplice.ipynb`
- `pendolo_semplice_piccole_oscillazioni/pendolo_semplice_piccole_oscillazioni.ipynb`

Al momento dell'analisi, i notebook contengono celle Markdown e celle di codice,
ma non contengono output salvati. Questo significa che GitHub puo' mostrarne la
struttura, ma non mostrera' grafici gia' calcolati dentro il notebook finche' non
vengono eseguiti e salvati.

## Come GitHub visualizza i notebook

Quando carichi un file `.ipynb` su GitHub, un visitatore vede una versione
renderizzata del notebook:

- celle Markdown formattate;
- celle di codice;
- eventuali output salvati, come tabelle, testo o grafici.

Questa visualizzazione e' statica. Vedere un notebook su GitHub non significa
eseguirlo: GitHub mostra il contenuto salvato nel file, ma normalmente non offre
un ambiente Jupyter completo in cui eseguire una cella alla volta.

## Come eseguire i notebook

Per eseguire davvero le celle, puoi usare una di queste soluzioni:

- Jupyter Notebook o JupyterLab installato localmente;
- VS Code con estensione Jupyter;
- GitHub Codespaces con ambiente Python/Jupyter configurato;
- Google Colab, aggiungendo un link compatibile;
- Binder, configurando le dipendenze del progetto;
- JupyterLite/GitHub Pages per casi particolari e piu' avanzati.

Per uno studente di fisica, la soluzione piu' semplice e robusta e':

1. tenere i notebook su GitHub per mostrarli in modo statico;
2. aggiungere istruzioni nei README per eseguirli localmente;
3. usare eventualmente Colab o Binder solo se si vuole rendere l'esecuzione piu'
   immediata dal browser.

## Installazione locale consigliata

Dopo aver clonato la repository:

```bash
git clone https://github.com/Andrea-Giannuzzi/Pendolo-semplice.git
cd Pendolo-semplice
```

puoi creare un ambiente virtuale:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

In questa repository non e' ancora presente un `requirements.txt`. Le dipendenze
minime rilevate dal codice sono:

```bash
pip install numpy matplotlib scipy jupyter
```

`scipy` serve per il progetto del pendolo numerico, mentre `jupyter` serve solo
se vuoi aprire ed eseguire i notebook.

## Note

I file generati automaticamente, come cache Python o cache Matplotlib, non sono
parte essenziale della documentazione scientifica. I grafici possono essere
rigenerati eseguendo gli script o i notebook dei singoli progetti.
