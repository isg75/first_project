# duplicate.py
#================================================================
import pandas as pd

#================================================================

def remove_duplicate_rows(df, columns=None, keep="first"):   # here, we keep the first occurrence of each duplicate row
    """
    Remove duplicate rows from a pandas DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to clean.
    keep : {"first", "last", False}, optional
        - "first": keep the first occurrence (default)
        - "last": keep the last occurrence
        - False: drop all duplicates

    Returns
    -------
    pd.DataFrame
        A DataFrame without duplicate rows.
    """
    return df.drop_duplicates(subset=columns, keep=keep).reset_index(drop=True)
