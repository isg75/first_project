from .functions import split_genres_column
import pandas as pd

def split_genres_column(df):
    """
    Splits the 'listed_in' column into a list of genres and stores it in a new 'genres' column.
    """
    df['genres'] = df['listed_in'].str.split(', ')
    return df

def clean_duration_column(df):
    """
    Cleans the 'duration' column into two new columns: 'duration_int' and 'duration_type'.
    Converts to numeric, handles nulls and standardizes naming.
    """
    df[['duration_int', 'duration_type']] = df['duration'].str.extract(r'(\d+)\s*(\w+)')
    df['duration_int'] = pd.to_numeric(df['duration_int'], errors='coerce')
    df['duration_type'] = df['duration_type'].replace('Seasons', 'Season')
    df = df[df['duration_int'].notna()]
    return df
