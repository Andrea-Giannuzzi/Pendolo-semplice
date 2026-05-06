"""
Simulazione del moto di un pendolo semplice per piccole oscillazioni.

Nel caso di piccoli angoli, l'equazione differenziale non lineare:

    d^2(theta)/dt^2 + (g/L) * sin(theta) = 0

si approssima con la forma lineare (approssimazione sin(theta) ≈ theta):

    d^2(theta)/dt^2 + (g/L) * theta = 0

Questa è l'equazione di un oscillatore armonico con soluzione analitica chiusa:

    theta(t) = theta_0 * cos(omega * t) + (omega_0 / omega) * sin(omega * t)
    
dove omega = sqrt(g/L) è la frequenza angolare naturale.
"""

from pathlib import Path
import os
import shutil
import numpy as np
import matplotlib

SCRIPT_DIR = Path(__file__).resolve().parent
MPL_CACHE_DIR = SCRIPT_DIR / ".matplotlib_cache"
MPL_CACHE_DIR.mkdir(exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPL_CACHE_DIR))

matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# Parametri fisici e numerici modificabili
# ---------------------------------------------------------------------------

# Lunghezza del pendolo in metri.
L = 1.0

# Accelerazione di gravita' in m/s^2.
g = 9.81

# Frequenza angolare naturale (rad/s) per un pendolo semplice.
omega = np.sqrt(g / L)

# Condizioni iniziali: angolo theta in radianti e velocita' angolare omega_0.
theta0 = 0.1  # Piccolo angolo (< 0.1 rad ≈ 5.7 gradi per validare l'approssimazione)
omega0 = 0.0

# Intervallo di simulazione: da t = 0 a t = t_max.
# Per visualizzare qualche oscillazione, usiamo 3 periodi: T = 2*pi/omega.
T = 2 * np.pi / omega  # Periodo in secondi
t_max = 3 * T

# Numero di punti temporali in cui valutare la soluzione.
n_points = 1000


def theta_analitica(t):
    """Soluzione analitica chiusa della posizione angolare theta(t).
    
    Per piccole oscillazioni, theta(t) = theta_0 * cos(omega*t) + (omega_0/omega) * sin(omega*t)
    """
    return theta0 * np.cos(omega * t) + (omega0 / omega) * np.sin(omega * t)


def velocita_angolare(t):
    """Soluzione analitica della velocita' angolare omega(t) = d(theta)/dt.
    
    omega(t) = -theta_0 * omega * sin(omega*t) + omega_0 * cos(omega*t)
    """
    return -theta0 * omega * np.sin(omega * t) + omega0 * np.cos(omega * t)


def accelerazione_angolare(t):
    """Soluzione analitica dell'accelerazione angolare alpha(t) = d(omega)/dt.
    
    alpha(t) = -(g/L) * theta(t)  [dall'equazione del moto lineare]
    """
    return -(g / L) * theta_analitica(t)


def salva_grafico(t, y, titolo, ylabel, legenda, nome_file, output_dir):
    """Produce e salva un singolo grafico in formato PNG."""
    plt.figure(figsize=(10, 6))
    plt.plot(t, y, label=legenda, linewidth=2, color="steelblue")
    plt.title(titolo, fontsize=14, fontweight="bold")
    plt.xlabel("Tempo t (s)", fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=11)
    plt.tight_layout()
    plt.savefig(output_dir / nome_file, dpi=150)
    plt.close()


def main():
    """Calcola la soluzione analitica e salva i tre grafici."""
    script_dir = Path(__file__).resolve().parent
    output_dir = script_dir / "output_grafici"

    # Rimuovere cartella output_grafici se esiste, per eliminare i grafici precedenti
    if output_dir.exists():
        shutil.rmtree(output_dir)

    # Creare cartella output_grafici
    output_dir.mkdir(exist_ok=True)

    # Vettore dei tempi in cui valutare la soluzione.
    t_eval = np.linspace(0.0, t_max, n_points)

    # Calcolare le tre quantita' usando le soluzioni analitiche.
    theta = theta_analitica(t_eval)
    omega_t = velocita_angolare(t_eval)
    alpha = accelerazione_angolare(t_eval)

    # Produzione e salvataggio dei tre grafici separati.
    salva_grafico(
        t_eval,
        theta,
        "Pendolo semplice (piccole oscillazioni): posizione angolare",
        "Posizione angolare θ (rad)",
        "θ(t) [soluzione analitica]",
        "posizione_angolare.png",
        output_dir,
    )

    salva_grafico(
        t_eval,
        omega_t,
        "Pendolo semplice (piccole oscillazioni): velocita' angolare",
        "Velocita' angolare ω (rad/s)",
        "ω(t) [soluzione analitica]",
        "velocita_angolare.png",
        output_dir,
    )

    salva_grafico(
        t_eval,
        alpha,
        "Pendolo semplice (piccole oscillazioni): accelerazione angolare",
        "Accelerazione angolare α (rad/s²)",
        "α(t) [soluzione analitica]",
        "accelerazione_angolare.png",
        output_dir,
    )

    # Informazioni sulla simulazione
    print("=" * 70)
    print("SIMULAZIONE PENDOLO SEMPLICE - PICCOLE OSCILLAZIONI")
    print("=" * 70)
    print(f"Approssimazione lineare valida per theta < 0.1 rad (< 5.7 gradi)")
    print(f"\nParametri fisici:")
    print(f"  Lunghezza pendolo L = {L} m")
    print(f"  Accelerazione di gravita g = {g} m/s²")
    print(f"  Frequenza angolare ω = √(g/L) = {omega:.4f} rad/s")
    print(f"  Periodo T = 2π/ω = {T:.4f} s")
    print(f"\nCondizioni iniziali:")
    print(f"  Angolo iniziale θ₀ = {theta0} rad ({np.degrees(theta0):.2f}°)")
    print(f"  Velocita' angolare iniziale ω₀ = {omega0} rad/s")
    print(f"\nSimulazione:")
    print(f"  Tempo simulato: da 0 a {t_max:.4f} s ({t_max/T:.1f} periodi)")
    print(f"  Numero di punti: {n_points}")
    print(f"\nGrafici salvati in: {output_dir}")
    print("=" * 70)


if __name__ == "__main__":
    main()
