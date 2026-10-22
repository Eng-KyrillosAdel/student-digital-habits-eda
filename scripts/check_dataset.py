"""Check the included synthetic student dataset without modifying files.

Run from repository root: python scripts/check_dataset.py
Custom fixture: python scripts/check_dataset.py --csv file.csv --expected-rows 2
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys
import pandas as pd

REQUIRED_COLUMNS = [
    'student_id', 'age', 'gender', 'study_hours_per_day',
    'smartphone_usage_hours', 'social_media_hours', 'gaming_hours',
    'streaming_hours', 'sleep_hours', 'exercise_hours',
    'class_attendance_percent', 'assignment_completion_percent',
    'caffeine_intake_cups', 'mental_health_status',
    'parent_education_level', 'internet_quality', 'motivation_level',
    'final_exam_score',
]


def check(csv_path: Path, expected_rows: int) -> None:
    if not csv_path.is_file():
        raise ValueError(f'Dataset not found: {csv_path}')
    frame = pd.read_csv(csv_path)
    missing_columns = sorted(set(REQUIRED_COLUMNS) - set(frame.columns))
    extra_columns = sorted(set(frame.columns) - set(REQUIRED_COLUMNS))
    if missing_columns or extra_columns:
        raise ValueError(f'Unexpected dataset columns; missing={missing_columns}, extra={extra_columns}')
    if len(frame) != expected_rows:
        raise ValueError(f'Expected {expected_rows:,} records; got {len(frame):,}')
    nulls = int(frame.isna().sum().sum())
    if nulls:
        raise ValueError(f'Found {nulls} missing values')
    duplicates = int(frame.duplicated().sum())
    if duplicates:
        raise ValueError(f'Found {duplicates} duplicate records')
    corr = frame['study_hours_per_day'].corr(frame['final_exam_score'])
    print(f'PASS | rows={len(frame):,} | columns={len(frame.columns)} | missing=0 | duplicates=0')
    print(f'Study-hours vs exam-score Pearson r = {corr:.3f}')
    print('Note: correlation does not establish causation.')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--csv', default='student_digital_life.csv')
    parser.add_argument('--expected-rows', type=int, default=15000)
    args = parser.parse_args()
    try:
        check(Path(args.csv), args.expected_rows)
    except (ValueError, OSError, pd.errors.ParserError) as exc:
        print(f'FAIL | {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
