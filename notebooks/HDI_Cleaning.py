import pandas as pd


# =========================================================
# CONFIG
# =========================================================

COL_JME_COUNTRY = "Country"
COL_HDI_COUNTRY = "country"

HDI_YEARS = [
    "hdi_1990",
    "hdi_2000",
    "hdi_2010",
    "hdi_2015",
    "hdi_2019",
    "hdi_2020",
    "hdi_2021",
    "hdi_2022"
]

COLS_TO_DROP = [
    "rank_change_2015_2022",
    "avg_growth_1990_2000",
    "avg_growth_2000_2010",
    "avg_growth_2010_2022",
    "tier_hdi",
    "iso3c"
]

# Mapping of HDI country names -> names used in JME
COUNTRY_RENAME_MAP = {
    "Türkiye": "Turkey",
    "Eswatini (Kingdom of)": "Swaziland",
    "Moldova (Republic of)": "Republic of Moldova",
    "Tanzania (United Republic of)": "United Republic of Tanzania",
    "Congo (Democratic Republic of the)": "Democratic Republic of the Congo",
    "Palestine, State of": "State of Palestine",
    "Korea (Republic of)": "Republic of Korea",
    "Korea (Democratic People's Rep. of)": "Democratic People's Republic of Korea",
    "North Macedonia": "The former Yugoslav Republic of Macedonia"
}

# Values in the HDI dataset that correspond to regions or aggregates rather than countries
NON_COUNTRY_VALUES = {
    "Very high human development",
    "High human development",
    "Medium human development",
    "Low human development",
    "World",
    "Developing countries",
    "Least developed countries",
    "Small island developing states",
    "Organisation for Economic Co-operation and Development",
    "Sub-Saharan Africa",
    "South Asia",
    "East Asia and the Pacific",
    "Europe and Central Asia",
    "Latin America and the Caribbean",
    "Arab States",
    "Hong Kong, China (SAR)"
}


# =========================================================
# HELPERS
# =========================================================

def standardize_country_strings(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    Remove textual NaNs, extra spaces, and standardize string formatting.
    """
    df = df.copy()
    df[col] = df[col].astype("string").str.strip()
    return df


def drop_unwanted_hdi_columns(df_hdi: pd.DataFrame) -> pd.DataFrame:
    """
    Remove HDI columns that are not necessary for the analysis.
    """
    df_hdi = df_hdi.copy()
    existing_cols = [c for c in COLS_TO_DROP if c in df_hdi.columns]
    return df_hdi.drop(columns=existing_cols)


def harmonize_hdi_country_names(df_hdi: pd.DataFrame) -> pd.DataFrame:
    """
    Harmonize HDI country names to match the naming convention used in the JME dataset.
    """
    df_hdi = df_hdi.copy()
    df_hdi[COL_HDI_COUNTRY] = df_hdi[COL_HDI_COUNTRY].replace(COUNTRY_RENAME_MAP)
    return df_hdi


def remove_non_country_rows(df_hdi: pd.DataFrame) -> pd.DataFrame:
    """
    Remove aggregated regions or groups from the HDI dataset.
    """
    df_hdi = df_hdi.copy()
    return df_hdi[~df_hdi[COL_HDI_COUNTRY].isin(NON_COUNTRY_VALUES)]


def filter_hdi_by_jme_countries(df_hdi: pd.DataFrame, df_jme: pd.DataFrame) -> pd.DataFrame:
    """
    Keep only countries in the HDI dataset that exist in the JME dataset.
    """
    df_hdi = df_hdi.copy()
    countries_ref = set(df_jme[COL_JME_COUNTRY].dropna())
    return df_hdi[df_hdi[COL_HDI_COUNTRY].isin(countries_ref)]


def missing_summary(df: pd.DataFrame, columns: list[str] | None = None) -> pd.DataFrame:
    """
    Produce a summary table of missing values including counts and percentages.
    """
    if columns is None:
        columns = df.columns.tolist()

    miss = df[columns].isna().sum()
    pct = (miss / len(df)) * 100

    out = pd.DataFrame({
        "missing_values": miss,
        "percent": pct.round(2)
    }).sort_values(["percent", "missing_values"], ascending=False)

    return out


def countries_missing_for_year(df_hdi: pd.DataFrame, year: int) -> pd.DataFrame:
    """
    List countries with missing HDI values for a specific year.
    """
    col = f"hdi_{year}"
    if col not in df_hdi.columns:
        raise ValueError(f"Column '{col}' does not exist in the dataframe.")

    out = df_hdi[df_hdi[col].isna()][[COL_HDI_COUNTRY]].copy()
    out = out.rename(columns={COL_HDI_COUNTRY: "country_missing"})
    return out.sort_values("country_missing").reset_index(drop=True)


def compare_country_sets(df_jme: pd.DataFrame, df_hdi: pd.DataFrame) -> tuple[set, set]:
    """
    Compare the set of countries between JME and HDI datasets.
    """
    jme_countries = set(df_jme[COL_JME_COUNTRY].dropna())
    hdi_countries = set(df_hdi[COL_HDI_COUNTRY].dropna())

    in_jme_not_hdi = jme_countries - hdi_countries
    in_hdi_not_jme = hdi_countries - jme_countries

    return in_jme_not_hdi, in_hdi_not_jme


# =========================================================
# MAIN PIPELINE
# =========================================================

def clean_hdi_with_jme_reference(df_jme: pd.DataFrame, df_hdi: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """
    Main pipeline:
    1) remove unnecessary columns
    2) standardize country strings
    3) harmonize country names
    4) remove regional aggregates
    5) filter HDI dataset using JME countries as reference
    6) return cleaned dataframe + diagnostics
    """
    # defensive copies
    df_jme = df_jme.copy()
    df_hdi = df_hdi.copy()

    # clean country columns
    df_jme = standardize_country_strings(df_jme, COL_JME_COUNTRY)
    df_hdi = standardize_country_strings(df_hdi, COL_HDI_COUNTRY)

    # remove NaN values from reference dataset
    df_jme = df_jme.dropna(subset=[COL_JME_COUNTRY])

    # clean HDI dataset
    df_hdi = drop_unwanted_hdi_columns(df_hdi)
    df_hdi = harmonize_hdi_country_names(df_hdi)
    df_hdi = remove_non_country_rows(df_hdi)

    # diagnostics before filtering
    missing_before_filter = compare_country_sets(df_jme, df_hdi)

    # filter HDI dataset using JME reference countries
    df_hdi_clean = filter_hdi_by_jme_countries(df_hdi, df_jme)

    # diagnostics after filtering
    missing_after_filter = compare_country_sets(df_jme, df_hdi_clean)

    diagnostics = {
        "jme_shape": df_jme.shape,
        "hdi_shape_before_clean": df_hdi.shape,
        "hdi_shape_after_filter": df_hdi_clean.shape,
        "missing_summary": missing_summary(
            df_hdi_clean,
            columns=[c for c in HDI_YEARS if c in df_hdi_clean.columns] + ["hdi_rank", "avg_growth_1990_2022"]
        ),
        "countries_in_jme_not_in_hdi_before_filter": missing_before_filter[0],
        "countries_in_hdi_not_in_jme_before_filter": missing_before_filter[1],
        "countries_in_jme_not_in_hdi_after_filter": missing_after_filter[0],
        "countries_in_hdi_not_in_jme_after_filter": missing_after_filter[1],
        "missing_hdi_1990_countries": countries_missing_for_year(df_hdi_clean, 1990)
            if "hdi_1990" in df_hdi_clean.columns else pd.DataFrame(),
    }

    return df_hdi_clean.reset_index(drop=True), diagnostics




# =========================================================

# Load datasets
df_jme = pd.read_csv("jme.csv")
df_hdi = pd.read_csv("hdi.csv")

# Run cleaning pipeline
df_hdi_clean, diag = clean_hdi_with_jme_reference(df_jme, df_hdi)

# Save cleaned dataset
df_hdi_clean.to_csv("hdi_clean.csv", index=False)

# Basic diagnostics
print("Final shape:", df_hdi_clean.shape)

print("\nMissing values summary:")
print(diag["missing_summary"])

print("\nCountries present in JME but missing in HDI after filtering:")
print(diag["countries_in_jme_not_in_hdi_after_filter"])

print("\nCountries without HDI values in 1990:")
print(diag["missing_hdi_1990_countries"].head(20))


