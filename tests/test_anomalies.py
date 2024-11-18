import pytest
import pandas as pd
from cleanpy_advanced.anomalies import detect_outliers

def test_no_outliers():
    """Test case where no outliers should be detected"""
    df = pd.DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]})

    # Call the detect_outliers function with contamination set to 0.1 to ensure no outliers are detected
    result = detect_outliers(df, ["A", "B"], contamination=0.1)

    # Print the result for debugging
    print(f"Result for no outliers: \n{result}")

    # Check that no outliers are detected (sum of outliers should be 0)
    assert result["outlier"].sum() == 0  # No outliers should be detected


def test_multiple_outliers():
    """Test case where multiple outliers should be detected"""
    # Create a DataFrame with outliers (100 and 200 are outliers)
    df = pd.DataFrame({
        "A": [1, 2, 3, 100, 200],
        "B": [5, 6, 7, 8, 9]
    })

    # Call the detect_outliers function with contamination set to 0.3 to detect outliers
    result = detect_outliers(df, ["A", "B"], contamination=0.3)

    # Print the result for debugging
    print(f"Result for multiple outliers: \n{result}")
    
    # Check how many outliers are detected by counting the instances where "outlier" is 1
    outliers = (result["outlier"] == 1).sum()  # Count how many outliers are detected
    
    # Assert that the number of outliers detected is 2, as we expect 100 and 200 to be outliers
    assert outliers == 2  # Expect two outliers: 100 and 200
