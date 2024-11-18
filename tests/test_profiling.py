import pytest
import pandas as pd
from cleanpy_advanced.profiling import profile_data

def test_profile_data():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [None, 5, 6]})
    report = profile_data(df)
    assert report["row_count"] == 3
    assert report["column_count"] == 2
    assert report["missing_values"]["B"] == 1
    assert "basic_statistics" in report

def test_profile_empty_dataframe():
    df = pd.DataFrame()
    report = profile_data(df)
    assert report["row_count"] == 0
    assert report["column_count"] == 0
    assert report["missing_values"] == {}
