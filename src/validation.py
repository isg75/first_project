import polars as pl


def count_unique_countries(df: pl.DataFrame, country_col: str = "REF_AREA_LABEL") -> int:
    """
    Count unique countries in a dataset.
    """
    return df[country_col].n_unique()


def get_missing_summary(df: pl.DataFrame) -> pl.DataFrame:
    """
    Return a table with null counts per column.
    """
    return pl.DataFrame({
        "column": df.columns,
        "null_count": [df[col].null_count() for col in df.columns]
    }).sort("null_count", descending=True)


def get_duplicate_rows(df: pl.DataFrame) -> pl.DataFrame:
    """
    Return duplicated rows in a DataFrame.
    """
    return df.filter(df.is_duplicated())


def check_required_columns(df: pl.DataFrame, required_columns: list[str]) -> list[str]:
    """
    Return a list of required columns that are missing.
    """
    return [col for col in required_columns if col not in df.columns]


def summarize_dataset(
    df: pl.DataFrame,
    country_col: str = "REF_AREA_LABEL"
) -> dict:
    """
    Return a quick summary of dataset shape, columns, and unique countries.
    """
    return {
        "rows": df.height,
        "columns": df.width,
        "column_names": df.columns,
        "unique_countries": df[country_col].n_unique() if country_col in df.columns else None,
    }


def compare_country_sets(
    df1: pl.DataFrame,
    df2: pl.DataFrame,
    country_col: str = "REF_AREA_LABEL"
) -> dict:
    """
    Compare country coverage between two datasets.
    """
    countries_1 = set(df1[country_col].unique().to_list())
    countries_2 = set(df2[country_col].unique().to_list())

    return {
        "only_in_df1": sorted(countries_1 - countries_2),
        "only_in_df2": sorted(countries_2 - countries_1),
        "in_both": sorted(countries_1 & countries_2),
    }


def validate_no_missing_in_columns(df: pl.DataFrame, columns: list[str]) -> pl.DataFrame:
    """
    Return rows that contain nulls in any of the specified columns.
    Useful for debugging merge problems.
    """
    condition = None
    for col in columns:
        col_null = pl.col(col).is_null()
        condition = col_null if condition is None else (condition | col_null)

    return df.filter(condition)