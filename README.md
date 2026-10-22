# Student Digital Life — Screen Time & Academic Performance

**Python · Exploratory Data Analysis · Pandas · Matplotlib · Seaborn · Plotly · Dash**

Exploratory analysis of a **synthetic dataset containing 15,000 student records and 18 columns**. This project investigates how study time, digital habits, sleep, and other lifestyle factors relate to final exam scores. It includes a Jupyter notebook and an interactive Plotly Dash dashboard.

> **Scope:** Exploratory data analysis and visualization, **not** a trained machine-learning prediction model. Correlations are descriptive and do not establish causal effects.

## At a glance

- **Dataset:** 15,000 rows × 18 columns; source: [Digital Distraction vs Academic Performance on Kaggle](https://www.kaggle.com/datasets/neurocipher/digital-distraction-vs-academic-performance), by neurocipher.
- **Analysis:** Data inspection, descriptive statistics, distributions, correlation analysis, and study/score profile comparisons.
- **Dashboard:** Five interactive filters covering gender, mental health, parent education, internet quality, and age.
- **Reported finding:** In the notebook, study hours have the strongest observed individual correlation with final exam score (approximately **r = 0.64**). This does not imply that changing study hours alone will cause the corresponding score change.

## Project structure

| File | Purpose |
| --- | --- |
| [`student_digital_life_analysis.ipynb`](student_digital_life_analysis.ipynb) | Exploratory analysis notebook and visualizations |
| [`dashboard.py`](dashboard.py) | Interactive Plotly Dash dashboard |
| [`student_digital_life.csv`](student_digital_life.csv) | Synthetic data supplied with the project |
| [`requirements.txt`](requirements.txt) | Python dependencies |
| [`scripts/check_dataset.py`](scripts/check_dataset.py) | Repeatable dataset integrity and correlation check |

## Get started

**Requirements:** Python 3.10+ and a terminal. Run all commands **from the repository root** (the folder containing `dashboard.py` and the CSV).

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/check_dataset.py
```

On Windows, activate the virtual environment with `.venv\Scripts\activate` instead.

### Open the notebook

```bash
jupyter notebook student_digital_life_analysis.ipynb
```

### Run the dashboard

```bash
python dashboard.py
```

Open **http://127.0.0.1:8050/**. Use the five filters to compare subgroups. The charts and summary values respond to the selected data.

`dashboard.py` reads `student_digital_life.csv` relative to your **current working directory**, so run it from the repository root. To use another CSV with the same schema, set the `CSV_PATH` environment variable:

```bash
CSV_PATH=/path/to/your.csv python dashboard.py
```

**No editing of a personal `/Users/.../Desktop` path is required.**

## Analysis approach

1. Inspect the structure and completeness of the student dataset.
2. Explore exam score, screen-time, attendance, sleep, and study-time distributions.
3. Compare correlations and grouped profiles using descriptive statistics and visualizations.
4. Build an interactive dashboard for viewing patterns by student characteristics.
5. Explain limitations before interpreting associations.

The project uses pre-existing synthetic observations, so the plots provide **exploratory evidence**, not validated causal conclusions or real-world treatment recommendations. Dashboard filters may yield small subgroups; interpret those cautiously.

## Reproducibility check

Run:

```bash
python scripts/check_dataset.py
```

The check confirms that the dataset is readable, contains the required 18 fields and 15,000 records, has no missing or duplicate rows, and reports the observed study-time/exam-score Pearson correlation. It does not train a predictive model.

## Data source and attribution

The dataset is credited to **neurocipher**, [Digital Distraction vs Academic Performance (Kaggle)](https://www.kaggle.com/datasets/neurocipher/digital-distraction-vs-academic-performance). It is described as **synthetic** in the project's notebook. Consult the source listing for the dataset's licensing and usage conditions; the code repository does not grant additional rights to the original dataset.

## Project status

This is a portfolio project focused on **EDA, interpretation, and interactive communication**. Future ML training/evaluation work, if added, should be documented separately with a reproducible train/test split and model metrics.
