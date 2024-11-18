def profile_data(df):
    """
    Generate a summary report of the DataFrame.

    Parameters:
        df (pd.DataFrame): The DataFrame to profile.

    Returns:
        dict: A dictionary containing profiling information.
    """
    # Check if the DataFrame is empty or has no columns
    if df.empty or df.columns.size == 0:
        return {
            "row_count": 0,
            "column_count": 0,
            "missing_values": {},
            "data_types": {},
            "basic_statistics": {}
        }
    
    # Proceed with normal profiling for non-empty DataFrame
    report = {
        "row_count": df.shape[0],
        "column_count": df.shape[1],
        "missing_values": df.isnull().sum().to_dict(),
        "data_types": df.dtypes.astype(str).to_dict(),
        "basic_statistics": df.describe(include="all").to_dict()
    }
    return report
