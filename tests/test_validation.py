import pytest
import pandas as pd
from cleanpy_advanced.validation import validate_schema

def test_validate_correct_schema():
    df = pd.DataFrame({"A": [1, 2, 3], "B": ["x", "y", "z"]})
    schema = {"A": "int64", "B": "object"}
    assert validate_schema(df, schema) == True

def test_validate_missing_column():
    df = pd.DataFrame({"A": [1, 2, 3]})
    schema = {"A": "int64", "B": "object"}
    with pytest.raises(ValueError, match="Missing column: B"):
        validate_schema(df, schema)

def test_validate_incorrect_dtype():
    df = pd.DataFrame({"A": [1, 2, 3], "B": ["x", "y", "z"]})
    schema = {"A": "float64", "B": "object"}
    with pytest.raises(ValueError, match="Column A has incorrect data type."):
        validate_schema(df, schema)
