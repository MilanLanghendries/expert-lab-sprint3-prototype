import pytest
import pandas as pd
from cleanpy_advanced.anomalies import detect_outliers

def test_detect_outliers():
    df = pd.DataFrame({"A": [1, 2, 3, 100], "B": [5, 6, 7, 8]})
    result = detect_outliers(df, ["A"])
    assert "outlier" in result.columns
    assert result["outlier"].sum() == 1  # 100 is an outlier

def test_no_outliers():
    df = pd.DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]})
    result = detect_outliers(df, ["A", "B"])
    assert result["outlier"].sum() == 0  # No outliers expected

def test_empty_dataframe():
    df = pd.DataFrame(columns=["A", "B"])
    result = detect_outliers(df, ["A"])
    assert result.empty

