# Pendolo numerico

## Descrizione

Questo progetto simula numericamente il moto di un pendolo semplice senza
attrito, usando il modello non lineare. A differenza del caso delle piccole
oscillazioni, qui non si sostituisce `sin(theta)` con `theta`: l'equazione viene
integrata direttamente nella sua forma non lineare.

Il progetto contiene sia uno script Python sia un notebook Jupyter.

## Modello fisico

L'equazione del pendolo semplice non lineare e':

```text
theta''(t) + (g/L) sin(theta(t)) = 0
```

dove:

- `theta`: angolo del pendolo rispetto alla verticale, in radianti;
- `omega`: velocita' angolare, cioe' `theta'(t)`;
- `L`: lunghezza del pendolo;
- `g`: accelerazione di gravita';
- `t`: tempo.

Per usare un integratore numerico, l'equazione del secondo ordine viene scritta
come sistema di due equazioni del primo ordine:

```text
theta' = omega
omega' = -(g/L) sin(theta)
```

## Metodo numerico

Il codice usa `scipy.integrate.solve_ivp`, una funzione di SciPy per risolvere
problemi differenziali con condizioni iniziali.

Nel file `pendolo_semplice.py`, lo stato iniziale e':

```python
stato_iniziale = [theta0, omega0]
```

dove `theta0` e' l'angolo iniziale e `omega0` e' la velocita' angolare iniziale.

Lo script calcola:

- posizione angolare `theta(t)`;
- velocita' angolare `omega(t)`;
- accelerazione angolare `alpha(t) = -(g/L) sin(theta)`.

Poi salva tre grafici separati.

## Struttura del progetto

File principali:

```text
pendolo_semplice_numerico/
├── pendolo_semplice.py
├── pendolo_semplice.ipynb
└── output_grafici/
    ├── posizione_angolare.png
    ├── velocita_angolare.png
    └── accelerazione_angolare.png
```

Il notebook `.ipynb` contiene codice e celle Markdown, ma al momento non contiene
output salvati. I grafici nella cartella `output_grafici/` sono file PNG prodotti
dallo script.

## Installazione

Dalla cartella principale della repository:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

In questa repository non e' ancora presente un `requirements.txt`. I pacchetti
minimi rilevati dal codice di questo progetto sono:

```bash
pip install numpy matplotlib scipy jupyter
```

`jupyter` serve solo se vuoi aprire ed eseguire il notebook.

## Esecuzione

Per eseguire lo script da terminale:

```bash
cd pendolo_semplice_numerico
python3 pendolo_semplice.py
```

Per aprire il notebook:

```bash
jupyter notebook pendolo_semplice.ipynb
```

oppure:

```bash
jupyter lab pendolo_semplice.ipynb
```

Da GitHub puoi visualizzare il notebook, ma non eseguirlo cella-per-cella nella
normale pagina del repository. Per eseguire le celle serve Jupyter, VS Code con
estensione Jupyter, Codespaces, Colab o Binder.

## Output attesi

Lo script genera la cartella:

```text
output_grafici/
```

e salva tre grafici:

- `posizione_angolare.png`: andamento di `theta(t)`;
- `velocita_angolare.png`: andamento di `omega(t)`;
- `accelerazione_angolare.png`: andamento di `alpha(t)`.

## Note fisiche

Il modello non lineare e' piu' generale del modello per piccole oscillazioni.
Per angoli piccoli, `sin(theta)` e' quasi uguale a `theta`, quindi il pendolo si
comporta quasi come un oscillatore armonico. Per angoli piu' grandi, invece, la
non linearita' diventa importante e l'integrazione numerica e' il metodo piu'
comodo per studiare il moto.

## Autore

Repository didattica per esercizi di fisica computazionale.
