# Pendolo per piccole oscillazioni

## Descrizione

Questo progetto studia il pendolo semplice nel limite delle piccole
oscillazioni. In questo caso l'angolo e' abbastanza piccolo da poter usare
l'approssimazione:

```text
sin(theta) ~= theta
```

Con questa approssimazione il moto del pendolo diventa quello di un oscillatore
armonico e puo' essere descritto con una soluzione analitica.

Il progetto contiene sia uno script Python sia un notebook Jupyter.

## Modello fisico

L'equazione linearizzata del pendolo e':

```text
theta''(t) + (g/L) theta(t) = 0
```

La frequenza angolare naturale e':

```text
omega = sqrt(g/L)
```

La soluzione generale puo' essere scritta come:

```text
theta(t) = A cos(sqrt(g/L) t) + B sin(sqrt(g/L) t)
```

Nel codice, usando le condizioni iniziali `theta0` e `omega0`, la soluzione e':

```text
theta(t) = theta0 cos(omega t) + (omega0 / omega) sin(omega t)
```

Il periodo del moto e':

```text
T = 2 pi sqrt(L/g)
```

## Validita' dell'approssimazione

L'approssimazione `sin(theta) ~= theta` e' valida quando `theta` e' piccolo ed e'
espresso in radianti.

Nel codice viene usato:

```python
theta0 = 0.1
```

che corrisponde a circa 5.7 gradi. Per angoli piu' grandi, l'errore
dell'approssimazione cresce e conviene confrontare questo modello con il pendolo
non lineare.

## Struttura del progetto

File principali:

```text
pendolo_semplice_piccole_oscillazioni/
├── pendolo_semplice_piccole_oscillazioni.py
├── pendolo_semplice_piccole_oscillazioni.ipynb
└── README.md
```

Lo script crea anche una cartella `output_grafici/` quando viene eseguito.

Il notebook `.ipynb` contiene celle Markdown e celle di codice, ma al momento
non contiene output salvati.

## Installazione

Dalla cartella principale della repository:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

In questa repository non e' ancora presente un `requirements.txt`. I pacchetti
minimi rilevati dal codice di questo progetto sono:

```bash
pip install numpy matplotlib jupyter
```

`jupyter` serve solo se vuoi aprire ed eseguire il notebook.

## Esecuzione

Per eseguire lo script da terminale:

```bash
cd pendolo_semplice_piccole_oscillazioni
python3 pendolo_semplice_piccole_oscillazioni.py
```

Per aprire il notebook:

```bash
jupyter notebook pendolo_semplice_piccole_oscillazioni.ipynb
```

oppure:

```bash
jupyter lab pendolo_semplice_piccole_oscillazioni.ipynb
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
- `velocita_angolare.png`: andamento della velocita' angolare;
- `accelerazione_angolare.png`: andamento dell'accelerazione angolare.

Nel modello implementato, le tre grandezze vengono calcolate con formule
analitiche, non con un integratore numerico.

## Confronto con il pendolo numerico

Il modello per piccole oscillazioni e' linearizzato ed e' risolubile
analiticamente. Il modello non lineare, invece, mantiene il termine
`sin(theta)` e in generale viene studiato con integrazione numerica.

Per angoli piccoli, i due modelli devono produrre risultati molto simili. Per
angoli piu' grandi, il modello linearizzato diventa meno accurato.

## Autore

Repository didattica per esercizi di fisica computazionale.
