# Add all the imports needed by the functions in the project here
#================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import re
#================================================================
#
# Library of custom preprocessing functions
#================================================================

# Renames all columns in the DataFrame to a consistent, standardized format—typically lowercase with underscores replacing spaces or special characters. 
# This process ensures uniform column naming, which minimizes errors and simplifies referencing columns throughout data cleaning and analysis workflows.
def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()
    return df

# Removes duplicate rows from a DataFrame, retaining the first occurrence. 
# Useful for ensuring data integrity and preventing double counting in analyses.
def drop_duplicates(df: pd.DataFrame, column) -> pd.DataFrame: 
    return df.drop_duplicates(subset=[column])

# Concatenates a list of DataFrames into a single DataFrame, stacking them vertically (row-wise). 
# Essential for merging datasets from similar sources or monthly data splits.
def concat_dataframes(left_df, right_df):
	return pd.concat([left_df,right_df], ignore_index = True)

# Removes all punctuation symbols from a given string. 
# Often used during text preprocessing to standardize and clean up textual data for analysis or NLP.
def remove_all_punctuation(df: pd.DataFrame, columns) -> pd.DataFrame:
    # Replace word/word and word-word with space between words
    pattern_slash = r'\b(\w+)(\-|\/)(\w+)\b'
    for col in columns:
        # Replace word/word and word-word
        df[col] = df[col].apply(lambda x: re.sub(pattern_slash, r'\1 \2', x) if isinstance(x, str) else x)
        # Lowercase, remove extra spaces
        df[col] = df[col].str.lower().str.strip().str.replace(r'\s+', ' ', regex=True)
    
    # Remove remaining punctuation (keep only letters, numbers, spaces) --> Outside the for loop
    df[columns] = df[columns].map(lambda x: re.sub(r'[^A-Za-z0-9 ]+', '', x) if isinstance(x, str) else x)
    return df

# Drops specified columns from a DataFrame, helping reduce dimensionality and focus on relevant variables for analysis
def drop_irrelevant_columns(df: pd.DataFrame, columns) -> pd.DataFrame:
    df_drop_cols = df.drop(columns=columns, axis=1, errors="ignore")
    return df_drop_cols

# Flters a DataFrame to keep only rows where the specified column contains a match to the provided regex pattern (case-insensitive).
# Returns a new DataFrame with matching rows, lowercasing the column before searching.
def filter_by_regex_pattern(df: pd.DataFrame, column, regex_pattern: str) -> pd.DataFrame:
    df[column] = df[column].str.lower()
    mask = df[column].str.contains(regex_pattern, flags=re.IGNORECASE, na=False, regex=True)
    return df[mask].copy().reset_index(drop=True)

# Converts specified columns to pandas `datetime` objects. 
# Facilitates time-series analysis, filtering, and date-based grouping.
def standardize_dates(df: pd.DataFrame, date_format_map: dict) -> pd.DataFrame:
    for col, fmt in date_format_map.items():
        # Try strict format first
        try:
            df[col] = pd.to_datetime(df[col], format=fmt, errors='coerce')
        except Exception:
            # Fallback: try default pandas parsing
            df[col] = pd.to_datetime(df[col], errors='coerce')
    return df


## def remove_all_punctuation(df: pd.DataFrame, columns) -> pd.DataFrame:
#    df[columns] = df[columns].map(lambda x: re.sub(r'[^A-Za-z0-9 ]+', '', x) if isinstance(x, str) else x)
#    # Lowercase All Categorical/Text Columns and Remove Extra Spaces
#    for col in columns:
#        df[col] = df[col].str.lower().str.strip().str.replace(r'\s+', ' ', regex=True)
#    return df

## def remove_all_punctuation(df: pd.DataFrame, columns) -> pd.DataFrame:
#     for col in columns:
#         df[col] = df[col].apply(
#             lambda x: re.sub(r'[^\w\s]', ' ', x) if isinstance(x, str) else x)  # Replace \ punctuation with space
#         df[col] = df[col].apply(lambda x: re.sub(r'\s+', ' ', x) if isinstance(x, str) else x)  # Remove extra spaces
#         df[col] = df[col].str.lower().str.strip()  # Lowercase & clean spaces
#     return df

# Converts specified columns to pandas `datetime` objects, handling various string date formats. 
# Facilitates time-series analysis, filtering, and date-based grouping.
## def standardize_dates(df: pd.DataFrame, column) -> pd.DataFrame:
#     df[column] = pd.to_datetime(df[column], format="%d-%b-%Y", errors='coerce') # Convert 'post_until' to datetime (with your format)
#     df[column] = df[column].dt.strftime('%d-%m-%Y') # Format 'post_until' as string in 'dd-mm-YYYY'
#     return df

# regex_pattern = r"(sql|tableau|bi|phyton|eda|llm|ai|ml|pandas|NumPy|Agile)"
# # Apply re.findall to each row in the 'Preferred_Skills' column
# keyword_matches = df_merged['Preferred_Skills'].apply(lambda x: re.findall(regex_pattern, x, flags=re.IGNORECASE) if isinstance(x, str) else [])
# # Filter rows where at least one keyword was found
# df_keywords = df_merged[keyword_matches.apply(lambda matches: len(matches) > 0)].copy().reset_index(drop=True)
