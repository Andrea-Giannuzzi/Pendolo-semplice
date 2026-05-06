"""
Simulazione numerica del moto di un pendolo semplice senza attrito.

Il modello usa l'equazione differenziale non lineare:

    d^2(theta)/dt^2 + (g/L) * sin(theta) = 0

dove theta e' l'angolo rispetto alla verticale.
"""

from pathlib import Path
import os
import shutil

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR / "output_grafici"

# Rimuovere cartella output_grafici se esiste, per eliminare i grafici precedenti
if OUTPUT_DIR.exists():
    shutil.rmtree(OUTPUT_DIR)

# Creare cartella output_grafici
OUTPUT_DIR.mkdir(exist_ok=True)

MPL_CACHE_DIR = SCRIPT_DIR / ".matplotlib_cache"
MPL_CACHE_DIR.mkdir(exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPL_CACHE_DIR))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


# ---------------------------------------------------------------------------
# Parametri fisici e numerici modificabili
# ---------------------------------------------------------------------------

# Lunghezza del pendolo in metri.
L = 1.0

# Accelerazione di gravita' in m/s^2.
g = 9.81

# Condizioni iniziali: angolo theta in radianti e velocita' angolare omega.
theta0 = 0.3
omega0 = 0.0

# Intervallo di simulazione: da t = 0 a t = t_max.
t_max = 10.0

# Numero di punti temporali in cui valutare la soluzione.
n_points = 1000


def pendolo_non_lineare(t, stato):
    """Restituisce le derivate del sistema del primo ordine.

    L'equazione del pendolo e' del secondo ordine perche' contiene la
    derivata seconda dell'angolo, cioe' l'accelerazione angolare.

    Per usare solve_ivp, la trasformiamo in due equazioni del primo ordine:

        dtheta/dt = omega
        domega/dt = -(g/L) * sin(theta)

    dove omega e' la velocita' angolare.
    """
    theta, omega = stato
    dtheta_dt = omega
    domega_dt = -(g / L) * np.sin(theta)
    return [dtheta_dt, domega_dt]


def salva_grafico(t, y, titolo, ylabel, legenda, nome_file, output_dir):
    """Produce e salva un singolo grafico in formato PNG."""
    plt.figure(figsize=(8, 5))
    plt.plot(t, y, label=legenda, linewidth=2)
    plt.title(titolo)
    plt.xlabel("Tempo t (s)")
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / nome_file, dpi=150)
    plt.close()


def main():
    """Integra l'equazione del pendolo e salva i tre grafici richiesti."""
    output_dir = OUTPUT_DIR

    # Vettore dei tempi in cui vogliamo conoscere posizione e velocita'.
    t_eval = np.linspace(0.0, t_max, n_points)

    # Stato iniziale del sistema: [theta(0), omega(0)].
    stato_iniziale = [theta0, omega0]

    soluzione = solve_ivp(
        pendolo_non_lineare,
        t_span=(0.0, t_max),
        y0=stato_iniziale,
        t_eval=t_eval,
        rtol=1e-9,
        atol=1e-11,
    )

    if not soluzione.success:
        raise RuntimeError(f"Integrazione fallita: {soluzione.message}")

    t = soluzione.t
    theta = soluzione.y[0]
    omega = soluzione.y[1]

    # L'accelerazione angolare si ricava direttamente dall'equazione del moto:
    # alpha = domega/dt = -(g/L) * sin(theta).
    alpha = -(g / L) * np.sin(theta)

    # Produzione e salvataggio dei tre grafici separati.
    salva_grafico(
        t,
        theta,
        "Pendolo semplice: posizione angolare",
        "Posizione angolare theta (rad)",
        "theta(t)",
        "posizione_angolare.png",
        output_dir,
    )

    salva_grafico(
        t,
        omega,
        "Pendolo semplice: velocita' angolare",
        "Velocita' angolare omega (rad/s)",
        "omega(t)",
        "velocita_angolare.png",
        output_dir,
    )

    salva_grafico(
        t,
        alpha,
        "Pendolo semplice: accelerazione angolare",
        "Accelerazione angolare alpha (rad/s^2)",
        "alpha(t)",
        "accelerazione_angolare.png",
        output_dir,
    )

    print("Simulazione completata.")
    print(f"Grafici salvati in: {output_dir}")


if __name__ == "__main__":
    main()
