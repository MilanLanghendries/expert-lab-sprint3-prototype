import pandas as pd
import numpy as np

def clean_missing_values(df, strategy="mean", columns=None):
    """
    Handle missing values in the dataset.

    Parameters:
        df (pd.DataFrame): The DataFrame to clean.
        strategy (str): Strategy to fill missing values ('mean', 'median', 'drop').
        columns (list): Columns to process. Default is None (all columns).

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    if columns is None:
        columns = df.columns

    if strategy == "mean":
        for col in columns:
            if df[col].dtype in [np.float64, np.int64]:
                df[col].fillna(df[col].mean(), inplace=True)
    elif strategy == "median":
        for col in columns:
            if df[col].dtype in [np.float64, np.int64]:
                df[col].fillna(df[col].median(), inplace=True)
    elif strategy == "drop":
        df.dropna(subset=columns, inplace=True)
    else:
        raise ValueError("Invalid strategy. Choose 'mean', 'median', or 'drop'.")

    return df

def normalize_column_names(df):
    """
    Normalize column names (lowercase and replace spaces with underscores).

    Parameters:
        df (pd.DataFrame): The DataFrame to clean.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df
