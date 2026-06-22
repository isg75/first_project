# From notebooks, imports should work if you run from project root or add:
# import sys
# sys.path.append("..")


import polars as pl

EXCLUDED_TERRITORIES = [
    "Monaco",
    "San Marino",
    "Liechtenstein",
    "Andorra",
    "Nauru",
    "Palau",
    "Tuvalu",
    "Virgin Islands (U.S.)",
    "Puerto Rico",
    "St. Martin (French part)",
    "Sint Maarten (Dutch part)",
    "Bermuda",
    "Hong Kong SAR, China",
    "Aruba",
    "Isle of Man",
    "Guam",
]


def load_wdi(filepath: str) -> pl.DataFrame:
    """
    Load WDI dataset and keep only total-sex rows with numeric year columns.
    """
    return (
        pl.read_csv(filepath)
        .filter(pl.col("SEX_LABEL") == "Total")
        .with_columns([
            pl.col("2010").cast(pl.Float64),
            pl.col("2018").cast(pl.Float64),
        ])
    )


def build_aging_ranking(wdi: pl.DataFrame) -> pl.DataFrame:
    """
    Build a country-level aging table with:
    - total population
    - population aged 65+
    - share of population aged 65+ in 2010 and 2018
    - population values in millions
    """
    total_pop = (
        wdi
        .filter(pl.col("INDICATOR_LABEL") == "Population, total")
        .select([
            pl.col("REF_AREA_LABEL").alias("country"),
            pl.col("2010").alias("total_population_2010"),
            pl.col("2018").alias("total_population_2018"),
        ])
        .unique(subset=["country"])
    )

    pop65 = (
        wdi
        .filter(pl.col("INDICATOR_LABEL") == "Population ages 65 and above, total")
        .select([
            pl.col("REF_AREA_LABEL").alias("country"),
            pl.col("2010").alias("population_65plus_2010"),
            pl.col("2018").alias("population_65plus_2018"),
        ])
        .unique(subset=["country"])
    )

    ranking = (
        total_pop
        .join(pop65, on="country", how="inner")
        .with_columns([
            ((pl.col("population_65plus_2010") / pl.col("total_population_2010")) * 100)
            .round(3)
            .alias("share_65plus_2010"),
            ((pl.col("population_65plus_2018") / pl.col("total_population_2018")) * 100)
            .round(3)
            .alias("share_65plus_2018"),
            (pl.col("total_population_2010") / 1_000_000)
            .round(3)
            .alias("total_pop_2010_millions"),
            (pl.col("population_65plus_2010") / 1_000_000)
            .round(3)
            .alias("pop_65plus_2010_millions"),
            (pl.col("total_population_2018") / 1_000_000)
            .round(3)
            .alias("total_pop_2018_millions"),
            (pl.col("population_65plus_2018") / 1_000_000)
            .round(3)
            .alias("pop_65plus_2018_millions"),
        ])
        .sort("share_65plus_2018", descending=True)
        .with_row_index("rank_2018", offset=1)
    )

    return ranking


def exclude_microstates(df: pl.DataFrame) -> pl.DataFrame:
    """
    Remove microstates and small territories that distort demographic comparisons.
    """
    return df.filter(~pl.col("country").is_in(EXCLUDED_TERRITORIES))


def add_aging_speed(df: pl.DataFrame) -> pl.DataFrame:
    """
    Add aging speed as the increase in elderly share between 2010 and 2018.
    """
    return df.with_columns(
        (pl.col("share_65plus_2018") - pl.col("share_65plus_2010"))
        .round(2)
        .alias("aging_speed")
    )


def get_oldest(df: pl.DataFrame, n: int = 5) -> pl.DataFrame:
    return df.sort("share_65plus_2018", descending=True).head(n)


def get_youngest(df: pl.DataFrame, n: int = 5) -> pl.DataFrame:
    return df.sort("share_65plus_2018").head(n)


def get_middle(df: pl.DataFrame, n: int = 5) -> pl.DataFrame:
    start = len(df) // 2 - n // 2
    return df.sort("share_65plus_2018").slice(start, n)


def get_fastest_aging(df: pl.DataFrame, n: int = 6) -> pl.DataFrame:
    return df.sort("aging_speed", descending=True).head(n)


def prepare_hci_lfp(hci_path: str, lfp_path: str) -> pl.DataFrame:
    """
    Load, clean, and merge HCI with labor-force participation data for 2018.
    Assumes both files contain:
    - REF_AREA_LABEL
    - SEX_LABEL
    - 2018
    """
    hci = (
        pl.read_csv(hci_path)
        .select(["REF_AREA_LABEL", "SEX_LABEL", "2018"])
        .rename({
            "REF_AREA_LABEL": "country",
            "2018": "hci_2018",
        })
        .filter(pl.col("SEX_LABEL") == "Total")
        .drop("SEX_LABEL")
        .with_columns(pl.col("hci_2018").cast(pl.Float64))
    )

    lfp = (
        pl.read_csv(lfp_path)
        .select(["REF_AREA_LABEL", "SEX_LABEL", "2018"])
        .rename({
            "REF_AREA_LABEL": "country",
            "2018": "labor_participation_2018",
        })
        .filter(pl.col("SEX_LABEL") == "Total")
        .drop("SEX_LABEL")
        .with_columns(pl.col("labor_participation_2018").cast(pl.Float64))
    )

    return hci.join(lfp, on="country", how="inner").drop_nulls()