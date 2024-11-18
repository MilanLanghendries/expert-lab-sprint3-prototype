import pytest
import pandas as pd
from cleanpy_advanced.cleaning import clean_missing_values, normalize_column_names

def test_clean_missing_values_mean():
    df = pd.DataFrame({"A": [1, 2, None, 4], "B": [5, None, 7, 8]})
    result = clean_missing_values(df, strategy="mean")
    assert result["A"].isnull().sum() == 0
    assert result["B"].isnull().sum() == 0

def test_clean_missing_values_drop():
    df = pd.DataFrame({"A": [1, None, 3], "B": [None, 2, 3]})
    result = clean_missing_values(df, strategy="drop")
    assert result.shape[0] == 1

def test_normalize_column_names():
    df = pd.DataFrame({"Column A": [1, 2], "Column B": [3, 4]})
    result = normalize_column_names(df)
    assert "column_a" in result.columns
    assert "column_b" in result.columns
