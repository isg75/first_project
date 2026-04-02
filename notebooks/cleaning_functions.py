import pandas as pd
from pathlib import Path


def read_dataframe(file_path: str) -> pd.DataFrame:
    file_type = Path(file_path).suffix.lower()

    if file_type == ".csv":
        return pd.read_csv(file_path)
    elif file_type in [".xls", ".xlsx"]:
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file type")

#Standardises column names (lowercase and spaces replaced with underscores) and renames columns if needed

def format_columns(df: pd.DataFrame, rename_dict: dict = None) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[^\w\s]", "", regex=True)
        .str.replace(" ", "_"))

    if rename_dict:
        df = df.rename(columns=rename_dict)

    return df

#Replaces invalid values across multiple columns
def clean_invalid_values(df: pd.DataFrame, replacements: dict) -> pd.DataFrame:
    
    df = df.copy()

    for column, replace_dict in replacements.items():
        if column in df.columns:
            df[column] = df[column].replace(replace_dict)

    return df

#replacements example:
    #{"gender": {"M": "Male", "F": "Female"}, "status": {"A": "Active", "I": "Inactive"}



#Fill missing numeric values using median or mean (default).
#Automatically detects numeric columns if none are specified.
  
def numeric_fill_nan(df: pd.DataFrame, columns: list = None, method: str = "mean") -> pd.DataFrame:
    
    df = df.copy()

    if columns is None:
        columns = df.select_dtypes(include="number").columns

    for column in columns:

        if column not in df.columns:
            continue

# Convert percentage strings to numeric
        df[column] = (
            df[column]
            .astype(str)
            .str.replace("%", "", regex=False)
        )

        df[column] = pd.to_numeric(df[column], errors="coerce")

        if method == "median":
            value = df[column].median()
        elif method == "mean":
            value = df[column].mean()
        else:
            raise ValueError("Method must be 'median' or 'mean'")

        df[column] = df[column].fillna(value)

    return df



#Fill missing categorical values using the mode.
#Automatically detects categorical columns if none are specified.
  
def categorical_fill_na(df: pd.DataFrame, columns: list = None) -> pd.DataFrame:
    df = df.copy()

    if columns is None:
        columns = df.select_dtypes(include="object").columns

    for column in columns:

        if column not in df.columns:
            continue

        mode_value = df[column].mode(dropna=True)

        if not mode_value.empty:
            df[column] = df[column].fillna(mode_value[0])

    return df


#Removes duplicates, optionally sets an index, and optionally saves the file.

def handle_duplicates_and_index(
    df: pd.DataFrame,
    id_column: str = None,
    output_file: str = None
) -> pd.DataFrame:

    df = df.copy()

    df = df.drop_duplicates()

    if id_column and id_column in df.columns:
        df = df.dropna(subset=[id_column])
        df = df.set_index(id_column)

    if output_file:
        df.to_csv(output_file, index=True)

    return df


#Main cleaning pipeline.
#Modify the CONFIG dictionary for different datasets.

def main():
    CONFIG = {
        "file": "raw_data.csv",

        "id_column": "id",

        "numeric_columns": ["age"],

        "categorical_columns": ["city"],

        "replacements": {
            "gender": {"M": "Male", "F": "Female"}
        },

        "output_file": "cleaned_data.csv"}

    # 1 Read data
    df = read_dataframe(CONFIG["file"])

    # 2 Format columns
    df = format_columns(df)

    # 3 Clean invalid values
    df = clean_invalid_values(df, CONFIG["replacements"])

    # 4 Fill numeric NaNs
    df = numeric_fill_nan(df, CONFIG["numeric_columns"])

    # 5 Fill categorical NaNs
    df = categorical_fill_na(df, CONFIG["categorical_columns"])

    # 6 Handle duplicates and index
    df = handle_duplicates_and_index(
        df,
        CONFIG["id_column"],
        CONFIG["output_file"]
    )

    print("Data cleaning complete.")

    return df


if __name__ == "__main__":
    main()