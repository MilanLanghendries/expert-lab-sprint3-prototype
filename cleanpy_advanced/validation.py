def validate_schema(df, schema):
    """
    Validate the DataFrame against a given schema.

    Parameters:
        df (pd.DataFrame): The DataFrame to validate.
        schema (dict): Schema definition (column_name: data_type).

    Returns:
        bool: True if the schema matches, False otherwise.
    """
    for column, data_type in schema.items():
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")
        if not df[column].dtype == data_type:
            raise ValueError(f"Column {column} has incorrect data type.")
    return True
