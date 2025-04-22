import pandas as pd
from functions import (
    standardize_column_names,
    fill_missing_values,
    convert_date_added,
    remove_duplicates,
    split_genres_column,
    clean_duration_column,
    extract_main_country,
    normalize_ratings
)

# 🧼 Apply all cleaning and transformation functions to the DataFrame
df = standardize_column_names(df)      # Normalize column names
df = fill_missing_values(df)           # Fill or drop missing values
df = convert_date_added(df)            # Convert 'date_added' to datetime
df = remove_duplicates(df)             # Remove duplicated titles
df = split_genres_column(df)           # Create 'genres' column from 'listed_in'
df = clean_duration_column(df)         # Split duration into int and type
df = extract_main_country(df)          # Create column for first country listed
df = normalize_ratings(df)             # Unify rating categories (e.g., 'UR', 'NR' → 'Unrated')


print("Dataset info:")
print(df.info())

print("Sample of cleaned data:")
print(df.head())  

print("Column names:")
print(df.columns.tolist()) 

print("Sample of 'duration_int' and 'duration_type':")
print(df[['duration_int', 'duration_type']].sample(5))

print("Top 10 most frequent countries (main_country):")
print(df['main_country'].value_counts().head(10))

print("Unique ratings after normalization:")
print(df['rating'].unique())
