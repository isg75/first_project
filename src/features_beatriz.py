import polars as pl


def add_age_group(widef: pl.DataFrame) -> pl.DataFrame:
    """
    Create a broad AGE_GROUP category in WDI for working-age vs retirement-age populations.
    """
    return widef.with_columns(
        pl.when(pl.col("INDICATOR").str.contains(
            "SP_POP_2024|SP_POP_2529|SP_POP_3034|SP_POP_3539|SP_POP_4044|SP_POP_4549|SP_POP_5054|SP_POP_5559|SP_POP_6064"
        ))
        .then(pl.lit("working_age"))
        .when(pl.col("INDICATOR").str.contains(
            "SP_POP_65UP|SP_POP_6569|SP_POP_7074|SP_POP_7579|SP_POP_80UP"
        ))
        .then(pl.lit("retirement_age"))
        .otherwise(pl.lit("other"))
        .alias("AGE_GROUP")
    )


def filter_core_wdi_indicators(widef: pl.DataFrame) -> pl.DataFrame:
    """
    Keep only the WDI indicators relevant for this project.
    """
    keep_labels = [
        "GDP per capita (current US$)",
        "GDP per capita growth (annual %)",
        "Population ages 65 and above (% of total population)",
        "Population ages 65 and above, total",
        "Population, total",
    ]

    return widef.filter(
        pl.col("INDICATOR_LABEL").is_in(keep_labels) |
        pl.col("AGE_GROUP").is_in(["working_age", "retirement_age"])
    )


def filter_hci_index(hci: pl.DataFrame) -> pl.DataFrame:
    """
    Keep only the Human Capital Index rows if INDICATOR_LABEL exists.
    Otherwise return the table unchanged.
    """
    if "INDICATOR_LABEL" not in hci.columns:
        return hci

    labels = hci["INDICATOR_LABEL"].unique().to_list()

    # Common possible labels
    preferred_labels = [
        "Human Capital Index (scale 0-1)",
        "Human Capital Index",
    ]

    for label in preferred_labels:
        if label in labels:
            return hci.filter(pl.col("INDICATOR_LABEL") == label)

    return hci


def build_merged_dataset(
    widef: pl.DataFrame,
    hcp: pl.DataFrame,
    hci: pl.DataFrame
) -> pl.DataFrame:
    """
    Merge WDI, HCP, and HCI into one wide dataset.
    """
    # Keep only total-sex rows in HCI/HCP to reduce duplicate joins
    hcp_total = hcp.filter(pl.col("SEX_LABEL") == "Total")
    hci_total = hci.filter(pl.col("SEX_LABEL") == "Total") if "SEX_LABEL" in hci.columns else hci

    join_keys = ["REF_AREA", "REF_AREA_LABEL"]

    merged = widef.join(
        hcp_total,
        on=join_keys,
        how="left",
        suffix="_hcp"
    )

    merged = merged.join(
        hci_total,
        on=join_keys,
        how="left",
        suffix="_hci"
    )

    # Rename original WDI years so they are explicit
    if "2010" in merged.columns and "2018" in merged.columns:
        merged = merged.rename({
            "2010": "2010_hdi",
            "2018": "2018_hdi"
        })

    return merged


def build_aging_simple(merged: pl.DataFrame) -> pl.DataFrame:
    """
    Build a simple aging table from merged data using population ages 65+ (% of total population).
    """
    return (
        merged
        .filter(
            (pl.col("INDICATOR_LABEL") == "Population ages 65 and above (% of total population)") &
            (pl.col("SEX_LABEL") == "Total")
        )
        .select([
            "REF_AREA",
            "REF_AREA_LABEL",
            "2010_hdi",
            "2018_hdi"
        ])
        .unique()
        .sort("2018_hdi", descending=True)
        .with_row_index("rank_age", offset=1)
    )


def build_gdp_ranking(merged: pl.DataFrame, year_col: str = "2018_hdi") -> pl.DataFrame:
    """
    Rank countries by GDP per capita.
    """
    return (
        merged
        .filter(
            (pl.col("INDICATOR_LABEL") == "GDP per capita (current US$)") &
            (pl.col("SEX_LABEL") == "Total")
        )
        .select([
            "REF_AREA",
            "REF_AREA_LABEL",
            "2010_hdi",
            "2018_hdi",
            "2010_hcp",
            "2018_hcp",
            "2010_hci",
            "2018_hci",
        ])
        .unique()
        .sort(year_col, descending=True)
        .with_row_index("rank_gdp", offset=1)
    )


def build_hcp_ranking(merged: pl.DataFrame) -> pl.DataFrame:
    """
    Rank countries by labor-force participation (HCP indicator).
    """
    return (
        merged
        .filter(pl.col("SEX_LABEL") == "Total")
        .select([
            "REF_AREA",
            "REF_AREA_LABEL",
            "2010_hcp",
            "2018_hcp"
        ])
        .unique()
        .sort("2018_hcp", descending=True)
        .with_row_index("rank_hcp", offset=1)
    )


def filter_target_countries(df: pl.DataFrame, countries: list[str]) -> pl.DataFrame:
    """
    Keep only selected countries for comparison tables.
    """
    return df.filter(pl.col("REF_AREA_LABEL").is_in(countries))


def join_rank_tables(
    gdp_table: pl.DataFrame,
    hcp_table: pl.DataFrame,
    age_table: pl.DataFrame
) -> pl.DataFrame:
    """
    Join GDP, labor participation, and aging tables on REF_AREA.
    """
    result = gdp_table.join(
        hcp_table,
        on="REF_AREA",
        how="left",
        suffix="_hcp"
    )

    result = result.join(
        age_table,
        on="REF_AREA",
        how="left",
        suffix="_age"
    )

    return result