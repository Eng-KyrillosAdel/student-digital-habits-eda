# Student Digital Life: Screen Time & Academic Performance

Exploratory data analysis of a 15,000-student dataset looking at how study
time, smartphone/social media/gaming/streaming usage, sleep, and other
lifestyle habits relate to final exam scores. Includes a static EDA notebook
and an interactive Plotly Dash dashboard.

## Contents

| File | Description |
|---|---|
| `student_digital_life_analysis.ipynb` | Main EDA notebook: distributions, correlations, and profile comparisons |
| `dashboard.py` | Interactive Plotly Dash app with filters (gender, mental health, parent education, internet quality, age) built on the same dataset |
| `student_digital_life.csv` | Dataset (15,000 rows, 18 columns) |
| `requirements.txt` | Python dependencies |

## Data source

Dataset from Kaggle: [Digital Distraction vs Academic Performance](https://www.kaggle.com/datasets/neurocipher/digital-distraction-vs-academic-performance) by neurocipher.

18 columns, 15,000 rows, no missing values, no duplicate rows. Columns cover:

- **Demographics:** `student_id`, `age`, `gender`
- **Daily time use (hours):** `study_hours_per_day`, `smartphone_usage_hours`, `social_media_hours`, `gaming_hours`, `streaming_hours`, `sleep_hours`, `exercise_hours`
- **Academics:** `class_attendance_percent`, `assignment_completion_percent`, `final_exam_score`
- **Other:** `caffeine_intake_cups`, `mental_health_status`, `parent_education_level`, `internet_quality`, `motivation_level`

## Key findings

- Study time is the strongest single correlate of final exam score
  (r ≈ 0.64) — clearly stronger than any of the screen-time variables.
- Among students who study the same amount, the *type* of digital activity
  they favor (social media vs. gaming vs. streaming) is associated with
  small differences in average exam score.
- Grouping students into four profiles (lower/higher study time ×
  lower/higher score) highlights how study time and outcome relate
  independent of screen time.

## Running the notebook

The notebook currently reads the CSV from a hardcoded path:
`/Users/Karo/Desktop/student_digital_life.csv`. Make sure the file is at
that location, or edit the `pd.read_csv(...)` line in the first code cell
to point elsewhere.

```bash
pip install -r requirements.txt
jupyter notebook student_digital_life_analysis.ipynb
```

## Running the dashboard

```bash
pip install -r requirements.txt
python dashboard.py
```

Then open http://127.0.0.1:8050 in your browser. `dashboard.py` also
defaults to `/Users/Karo/Desktop/student_digital_life.csv`; override it
with the `CSV_PATH` environment variable, e.g.:

```bash
CSV_PATH=/path/to/student_digital_life.csv python dashboard.py
```

## Notes

This is an educational/portfolio EDA project. Correlation here does not
imply causation — e.g., students who already study more may also differ in
other unmeasured ways.
