import polars as pl
from typing import Tuple, Set


def load_raw_datasets(config: dict) -> Tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame]:
    """
    Load the three raw datasets referenced in config.yaml.
    """
    widef = pl.read_csv(config["input_data"]["file_bf1"])
    hci = pl.read_csv(config["input_data"]["file_bf2"])
    hcp = pl.read_csv(config["input_data"]["file_bf3"])
    return widef, hci, hcp


def select_widef_columns(widef: pl.DataFrame) -> pl.DataFrame:
    """
    Keep only the columns needed from WDI / WIDEF.
    """
    return widef.select([
        "REF_AREA",
        "REF_AREA_LABEL",
        "INDICATOR",
        "INDICATOR_LABEL",
        "SEX_LABEL",
        "AGE_LABEL",
        "2010",
        "2018",
    ])


def select_hci_columns(hci: pl.DataFrame) -> pl.DataFrame:
    """
    Keep only the columns needed from HCI.
    """
    keep = ["REF_AREA", "REF_AREA_LABEL", "SEX_LABEL", "2010", "2018"]
    if "INDICATOR_LABEL" in hci.columns:
        keep.insert(3, "INDICATOR_LABEL")
    return hci.select(keep)


def select_hcp_columns(hcp: pl.DataFrame) -> pl.DataFrame:
    """
    Keep only the columns needed from HCP.
    """
    return hcp.select([
        "REF_AREA",
        "REF_AREA_LABEL",
        "SEX_LABEL",
        "2010",
        "2018",
    ])


def standardize_country_names(df: pl.DataFrame) -> pl.DataFrame:
    """
    Harmonize country names across datasets.
    """
    return df.with_columns(
        pl.when(pl.col("REF_AREA_LABEL").str.contains("rkiye"))
        .then(pl.lit("Turkey"))
        .when(pl.col("REF_AREA_LABEL").str.contains("Ivoire"))
        .then(pl.lit("Cote d'Ivoire"))
        .when(pl.col("REF_AREA_LABEL").str.contains("Tome"))
        .then(pl.lit("Sao Tome and Principe"))
        .when(pl.col("REF_AREA_LABEL") == "Viet Nam")
        .then(pl.lit("Vietnam"))
        .when(pl.col("REF_AREA_LABEL") == "Federal Republic of Somalia")
        .then(pl.lit("Somalia"))
        .otherwise(pl.col("REF_AREA_LABEL"))
        .alias("REF_AREA_LABEL")
    )


def filter_valid_countries(df: pl.DataFrame, valid_countries: list[str]) -> pl.DataFrame:
    """
    Keep only rows whose country is in the approved country list.
    """
    return df.filter(pl.col("REF_AREA_LABEL").is_in(valid_countries))


def get_common_countries(
    widef: pl.DataFrame,
    hci: pl.DataFrame,
    hcp: pl.DataFrame
) -> Set[str]:
    """
    Return the set of countries present in all three datasets.
    """
    countries_widef = set(widef["REF_AREA_LABEL"].unique().to_list())
    countries_hci = set(hci["REF_AREA_LABEL"].unique().to_list())
    countries_hcp = set(hcp["REF_AREA_LABEL"].unique().to_list())
    return countries_widef & countries_hci & countries_hcp


def filter_common_countries(
    widef: pl.DataFrame,
    hci: pl.DataFrame,
    hcp: pl.DataFrame,
    common_countries: set[str]
) -> Tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame]:
    """
    Filter all three datasets to keep only shared countries.
    """
    return (
        widef.filter(pl.col("REF_AREA_LABEL").is_in(common_countries)),
        hci.filter(pl.col("REF_AREA_LABEL").is_in(common_countries)),
        hcp.filter(pl.col("REF_AREA_LABEL").is_in(common_countries)),
    )