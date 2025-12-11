# Add all the imports needed by the functions in the project here
#================================================================
#
#================================================================

# rename_columns.py

def rename_multiple_columns(df, column_mapping):
    """
	Renames multiple columns in a pandas DataFrame using a mapping dictionary.

    Args:
        df (pd.DataFrame): The DataFrame whose columns are to be renamed.
        column_mapping (dict): A dictionary where keys are the current column 
                               names (strings) and values are the new column 
                               names (strings).

    Returns:
        pd.DataFrame: The DataFrame with the renamed columns.
	"""
    # The 'columns' parameter takes the mapping dictionary
    # 'inplace=False' returns a new DataFrame (recommended practice)
    renamed_df = df.rename(columns=column_mapping, inplace=False)
    return renamed_df