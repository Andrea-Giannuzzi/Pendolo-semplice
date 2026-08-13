# Pendulum for Small Oscillations

## Description

This project studies the simple pendulum in the small-oscillation limit. In
this case, the angle is small enough to use the approximation:

```text
sin(theta) ~= theta
```

With this approximation, the pendulum's motion becomes that of a harmonic
oscillator and can be described by an analytical solution.

The project contains both a Python script and a Jupyter notebook.

## Physical Model

The linearized pendulum equation is:

```text
theta''(t) + (g/L) theta(t) = 0
```

The natural angular frequency is:

```text
omega = sqrt(g/L)
```

The general solution can be written as:

```text
theta(t) = A cos(sqrt(g/L) t) + B sin(sqrt(g/L) t)
```

In the code, using the initial conditions `theta0` and `omega0`, the solution is:

```text
theta(t) = theta0 cos(omega t) + (omega0 / omega) sin(omega t)
```

The period of the motion is:

```text
T = 2 pi sqrt(L/g)
```

## Validity of the Approximation

The approximation `sin(theta) ~= theta` is valid when `theta` is small and is
expressed in radians.

The code uses:

```python
theta0 = 0.1
```

which corresponds to approximately 5.7 degrees. For larger angles, the
approximation error increases, and it is useful to compare this model with the
nonlinear pendulum.

## Project Structure

Main files:

```text
pendolo_semplice_piccole_oscillazioni/
├── pendolo_semplice_piccole_oscillazioni.py
├── pendolo_semplice_piccole_oscillazioni.ipynb
└── README.md
```

The script also creates an `output_grafici/` directory when it is run.

The `.ipynb` notebook contains Markdown and code cells, but currently has no
saved output.

## Installation

From the repository's main directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

This repository does not yet contain a `requirements.txt`. The minimum packages
identified from this project's code are:

```bash
pip install numpy matplotlib jupyter
```

`jupyter` is only required if you want to open and run the notebook.

## Running the Project

To run the script from the terminal:

```bash
cd pendolo_semplice_piccole_oscillazioni
python3 pendolo_semplice_piccole_oscillazioni.py
```

To open the notebook:

```bash
jupyter notebook pendolo_semplice_piccole_oscillazioni.ipynb
```

or:

```bash
jupyter lab pendolo_semplice_piccole_oscillazioni.ipynb
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
- `velocita_angolare.png`: evolution of the angular velocity;
- `accelerazione_angolare.png`: evolution of the angular acceleration.

In the implemented model, the three quantities are calculated with analytical
formulas rather than a numerical integrator.

## Comparison with the Numerical Pendulum

The small-oscillation model is linearized and can be solved analytically. The
nonlinear model, in contrast, retains the `sin(theta)` term and is generally
studied through numerical integration.

For small angles, the two models should produce very similar results. For
larger angles, the linearized model becomes less accurate.

## Author

Educational repository for computational physics exercises.
