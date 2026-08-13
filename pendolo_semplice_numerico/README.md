# Numerical Pendulum

## Description

This project numerically simulates the motion of a frictionless simple pendulum
using the nonlinear model. Unlike the small-oscillation case, `sin(theta)` is
not replaced with `theta`: the equation is integrated directly in its nonlinear
form.

The project contains both a Python script and a Jupyter notebook.

## Physical Model

The nonlinear simple pendulum equation is:

```text
theta''(t) + (g/L) sin(theta(t)) = 0
```

where:

- `theta`: pendulum angle from the vertical, in radians;
- `omega`: angular velocity, that is, `theta'(t)`;
- `L`: pendulum length;
- `g`: gravitational acceleration;
- `t`: time.

To use a numerical integrator, the second-order equation is written as a system
of two first-order equations:

```text
theta' = omega
omega' = -(g/L) sin(theta)
```

## Numerical Method

The code uses `scipy.integrate.solve_ivp`, a SciPy function for solving
differential equations with initial conditions.

In `pendolo_semplice.py`, the initial state is:

```python
stato_iniziale = [theta0, omega0]
```

where `theta0` is the initial angle and `omega0` is the initial angular velocity.

The script calculates:

- angular position `theta(t)`;
- angular velocity `omega(t)`;
- angular acceleration `alpha(t) = -(g/L) sin(theta)`.

It then saves three separate plots.

## Project Structure

Main files:

```text
pendolo_semplice_numerico/
├── pendolo_semplice.py
├── pendolo_semplice.ipynb
└── output_grafici/
    ├── posizione_angolare.png
    ├── velocita_angolare.png
    └── accelerazione_angolare.png
```

The `.ipynb` notebook contains code and Markdown cells, but currently has no
saved output. The plots in the `output_grafici/` directory are PNG files
produced by the script.

## Installation

From the repository's main directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

This repository does not yet contain a `requirements.txt`. The minimum packages
identified from this project's code are:

```bash
pip install numpy matplotlib scipy jupyter
```

`jupyter` is only required if you want to open and run the notebook.

## Running the Project

To run the script from the terminal:

```bash
cd pendolo_semplice_numerico
python3 pendolo_semplice.py
```

To open the notebook:

```bash
jupyter notebook pendolo_semplice.ipynb
```

or:

```bash
jupyter lab pendolo_semplice.ipynb
```

On GitHub, you can view the notebook but cannot run it cell by cell on the
standard repository page. Running the cells requires Jupyter, VS Code with the
Jupyter extension, Codespaces, Colab, or Binder.

## Expected Output

The script creates the directory:

```text
output_grafici/
```

and saves three plots:

- `posizione_angolare.png`: evolution of `theta(t)`;
- `velocita_angolare.png`: evolution of `omega(t)`;
- `accelerazione_angolare.png`: evolution of `alpha(t)`.

## Physical Notes

The nonlinear model is more general than the small-oscillation model. For small
angles, `sin(theta)` is nearly equal to `theta`, so the pendulum behaves almost
like a harmonic oscillator. For larger angles, however, the nonlinearity
becomes important, and numerical integration is the most convenient method for
studying the motion.

## Author

Educational repository for computational physics exercises.
