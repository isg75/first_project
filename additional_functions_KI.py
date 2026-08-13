def clear_data (dataf: pd.Series) -> pd.Series:
    dataf = dataf.str.strip().str.replace(',', '', regex=True)
    return dataf

def columns_formating(df: pd.Series) -> pd.Series:
    df.columns = [(column.lower()).replace(" ","_") for column in df.columns]  
    return df  