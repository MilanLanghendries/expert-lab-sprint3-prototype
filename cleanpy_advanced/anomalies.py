from sklearn.ensemble import IsolationForest

def detect_outliers(df, columns):
    """
    Detect outliers in specified columns using Isolation Forest.

    Parameters:
        df (pd.DataFrame): The DataFrame to analyze.
        columns (list): Columns to check for outliers.

    Returns:
        pd.DataFrame: DataFrame with an added column "outlier" (1 if outlier, -1 otherwise).
    """
    if df.empty or not columns:
        df['outlier'] = 0  # No outliers in empty data
        return df

    model = IsolationForest(contamination=0.25, random_state=42)
    df['outlier'] = model.fit_predict(df[columns])
    # Convert to binary outlier labels: 1 for outlier, 0 for inlier
    df['outlier'] = df['outlier'].apply(lambda x: 1 if x == -1 else 0)
    return df
