import pytest
import pandas as pd
from cleanpy_advanced.pipeline import CleaningPipeline
from cleanpy_advanced.cleaning import clean_missing_values, normalize_column_names

def test_pipeline_execution():
    df = pd.DataFrame({"Column A": [1, None, 3], "Column B": [4, 5, None]})
    pipeline = CleaningPipeline()
    pipeline.add_step(normalize_column_names)
    pipeline.add_step(clean_missing_values, strategy="mean")
    result = pipeline.run(df)

    assert "column_a" in result.columns
    assert "column_b" in result.columns
    assert result.isnull().sum().sum() == 0

def test_empty_pipeline():
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    pipeline = CleaningPipeline()
    result = pipeline.run(df)
    assert result.equals(df)
