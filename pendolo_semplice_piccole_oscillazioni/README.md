# Pendolo Semplice - Piccole Oscillazioni

Questo progetto contiene uno script Python che simula il moto di un pendolo
semplice nel caso di piccole oscillazioni.

Nel caso di angoli piccoli, l'equazione non lineare del pendolo:

```text
d²θ/dt² + (g/L) sin(θ) = 0
```

puo' essere approssimata con:

```text
d²θ/dt² + (g/L) θ = 0
```

Questa e' l'equazione di un oscillatore armonico. In questo caso non serve una
simulazione numerica: si puo' usare direttamente la soluzione analitica.

## Cosa Fa Lo Script

Lo script calcola nel tempo:

- la posizione angolare `θ(t)`;
- la velocita' angolare `ω(t)`;
- l'accelerazione angolare `α(t)`.

Alla fine salva tre grafici nella cartella:

```text
output_grafici/
```

## File Principale

```text
pendolo_semplice_piccole_oscillazioni.py
```

## Requisiti

Per eseguire lo script servono queste librerie Python:

```text
numpy
matplotlib
```

Puoi installarle con:

```bash
pip install numpy matplotlib
```

Se nel tuo sistema usi `python3`, puoi installarle con:

```bash
python3 -m pip install numpy matplotlib
```

## Come Eseguire Il Programma

Apri il terminale nella cartella di questo progetto:

```bash
cd pendolo_semplice_piccole_oscillazioni
```

Poi esegui:

```bash
python pendolo_semplice_piccole_oscillazioni.py
```

Se il comando `python` non funziona, prova:

```bash
python3 pendolo_semplice_piccole_oscillazioni.py
```

## Output Generato

Lo script crea automaticamente la cartella:

```text
output_grafici/
```

Dentro vengono salvati tre file:

```text
posizione_angolare.png
velocita_angolare.png
accelerazione_angolare.png
```

I tre grafici mostrano rispettivamente:

- come cambia l'angolo del pendolo nel tempo;
- come cambia la velocita' angolare;
- come cambia l'accelerazione angolare.

## Parametri Modificabili

All'inizio dello script si possono modificare alcuni parametri:

```python
L = 1.0
g = 9.81
theta0 = 0.1
omega0 = 0.0
n_points = 1000
```

Significato:

- `L`: lunghezza del pendolo in metri;
- `g`: accelerazione di gravita' in m/s²;
- `theta0`: angolo iniziale in radianti;
- `omega0`: velocita' angolare iniziale in rad/s;
- `n_points`: numero di punti usati per disegnare i grafici.

Il periodo del pendolo viene calcolato automaticamente con:

```text
T = 2π / ω
```

dove:

```text
ω = √(g/L)
```

Nel codice il tempo totale simulato e' pari a tre periodi.

## Nota Fisica

L'approssimazione delle piccole oscillazioni e' valida quando l'angolo iniziale
e' piccolo.

Nel codice viene usato:

```python
theta0 = 0.1
```

che corrisponde a circa 5.7 gradi.

Per angoli molto piu' grandi, l'approssimazione `sin(θ) ≈ θ` diventa meno
accurata. In quel caso conviene usare il modello non lineare del pendolo.

## Come Caricare Questo README Su GitHub

Dalla cartella principale del repository:

```bash
cd pendolo_semplice
```

controlla lo stato dei file:

```bash
git status
```

aggiungi il README:

```bash
git add pendolo_semplice_piccole_oscillazioni/README.md
```

crea un commit:

```bash
git commit -m "Aggiunge README per piccole oscillazioni"
```

e carica le modifiche su GitHub:

```bash
git push
```

Se il repository non e' ancora collegato a GitHub, bisogna prima creare un
repository su GitHub e collegarlo con `git remote add origin`.
