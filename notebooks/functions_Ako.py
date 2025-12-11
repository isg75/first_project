import pandas as pd


#reset index 
def index_reset(df: pd.DataFrame) -> pd.DataFrame: 
    """
    this function reset the hidden index into start from 1, not 0
    """
    df2 = df.copy()
    df2.reset_index(drop=True, inplace=True)

    df2.index = df2.index + 1
    df2.index.name = None

    return df2 
    

#cleaning datetime 

def date_time(df: pd.DataFrame, column_name: str) -> pd.DataFrame: 
    """
    this function convert Release Year columns from data type 'object' to date-time
    """

    df2 = df.copy()
    df2[column_name] = pd.to_datetime(df2[column_name],errors="coerce")
    
    return df2 
#df["Release Year"] = pd.to_numeric(df["Release Year"], errors='coerce')
#df["Release Year"] = df["Release Year"].astype("Int64")
