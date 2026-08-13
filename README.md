# Simple Pendulum

This repository contains small Python/Jupyter projects dedicated to the study
of the simple pendulum. The goal is to use code, plots, and notebooks to connect
the physical model with its computational implementation.

## Available Projects

- [Numerical pendulum](./pendolo_semplice_numerico/README.md): numerical
  integration of the nonlinear pendulum equation.
- [Pendulum for small oscillations](./pendolo_semplice_piccole_oscillazioni/README.md):
  analytical solution in the limit where `sin(theta) ~= theta`.

## Available Notebooks

The repository contains these Jupyter notebooks:

- `pendolo_semplice_numerico/pendolo_semplice.ipynb`
- `pendolo_semplice_piccole_oscillazioni/pendolo_semplice_piccole_oscillazioni.ipynb`

At the time of analysis, the notebooks contain Markdown and code cells but no
saved output. This means that GitHub can display their structure, but it will
not show plots calculated within the notebooks until they are run and saved.

## How GitHub Displays Notebooks

When you upload an `.ipynb` file to GitHub, visitors see a rendered version of
the notebook:

- formatted Markdown cells;
- code cells;
- any saved output, such as tables, text, or plots.

This view is static. Viewing a notebook on GitHub does not mean running it:
GitHub displays the content saved in the file, but it does not normally provide
a complete Jupyter environment in which cells can be run individually.

## Running the Notebooks

To run the cells, you can use one of these solutions:

- Jupyter Notebook or JupyterLab installed locally;
- VS Code with the Jupyter extension;
- GitHub Codespaces with a configured Python/Jupyter environment;
- Google Colab, by adding a compatible link;
- Binder, by configuring the project dependencies;
- JupyterLite/GitHub Pages for specific, more advanced use cases.

For a physics student, the simplest and most robust solution is to:

1. keep the notebooks on GitHub for static display;
2. add instructions to the READMEs for running them locally;
3. use Colab or Binder only if execution needs to be more readily available in
   the browser.

## Recommended Local Installation

After cloning the repository:

```bash
git clone https://github.com/Andrea-Giannuzzi/Pendolo-semplice.git
cd Pendolo-semplice
```

you can create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

This repository does not yet contain a `requirements.txt`. The minimum
dependencies identified from the code are:

```bash
pip install numpy matplotlib scipy jupyter
```

`scipy` is required for the numerical pendulum project, while `jupyter` is only
needed to open and run the notebooks.

## Notes

Automatically generated files, such as Python or Matplotlib caches, are not an
essential part of the scientific documentation. The plots can be regenerated
by running the scripts or notebooks for the individual projects.
