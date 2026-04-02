import pandas as pd
import numpy as np
import statsmodels.formula.api as smf


# =========================================================
# CONFIG
# =========================================================

# Column names expected in the source files
COL_JME_COUNTRY = "Country"
COL_HDI_COUNTRY = "country"
COL_JME_REGION = "UN Region"

# HDI columns originally available in worldhdi.xlsx
BASE_HDI_YEARS = [
    "hdi_1990",
    "hdi_2000",
    "hdi_2010",
    "hdi_2015",
    "hdi_2019",
    "hdi_2020",
    "hdi_2021",
    "hdi_2022"
]

# Extra HDR yearly files that were added later in the project
# Expected filenames: hdr-data_YYYY.xlsx
EXTRA_YEARS = [
    1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
    2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
    2011, 2012, 2013, 2014,
    2016, 2017, 2018
]

# Columns that are not needed in the cleaned base HDI dataset
COLS_TO_DROP = [
    "rank_change_2015_2022",
    "avg_growth_1990_2000",
    "avg_growth_2000_2010",
    "avg_growth_2010_2022",
    "tier_hdi",
    "iso3c"
]

# Country name harmonization map:
# these names appear in some HDR files and need to be aligned
# with the names already accepted in the cleaned HDI dataset
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

# Rows that are not countries and must be removed from HDI files
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
# HELPER FUNCTIONS
# =========================================================

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names by removing leading/trailing spaces.
    """
    df = df.copy()
    df.columns = df.columns.str.strip()
    return df


def standardize_text_column(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    Standardize a text column:
    - convert to string
    - strip spaces
    - replace textual 'nan' with real missing values
    """
    df = df.copy()
    df[col] = df[col].astype(str).str.strip()
    df[col] = df[col].replace("nan", pd.NA)
    return df


def drop_unwanted_hdi_columns(df_hdi: pd.DataFrame) -> pd.DataFrame:
    """
    Remove columns not needed for the final cleaned HDI dataset.
    """
    df_hdi = df_hdi.copy()
    existing_cols = [c for c in COLS_TO_DROP if c in df_hdi.columns]
    return df_hdi.drop(columns=existing_cols)


def harmonize_hdi_country_names(df_hdi: pd.DataFrame) -> pd.DataFrame:
    """
    Harmonize country names using the predefined replacement dictionary.
    """
    df_hdi = df_hdi.copy()
    df_hdi[COL_HDI_COUNTRY] = df_hdi[COL_HDI_COUNTRY].replace(COUNTRY_RENAME_MAP)
    return df_hdi


def remove_non_country_rows(df_hdi: pd.DataFrame) -> pd.DataFrame:
    """
    Remove aggregate rows such as 'World', 'High human development', etc.
    """
    df_hdi = df_hdi.copy()
    return df_hdi[~df_hdi[COL_HDI_COUNTRY].isin(NON_COUNTRY_VALUES)]


def filter_hdi_by_jme_countries(df_hdi: pd.DataFrame, df_jme: pd.DataFrame) -> pd.DataFrame:
    """
    Keep only countries present in the JME dataset.
    JME is used as the reference list of valid countries.
    """
    df_hdi = df_hdi.copy()
    countries_ref = set(df_jme[COL_JME_COUNTRY].dropna())
    return df_hdi[df_hdi[COL_HDI_COUNTRY].isin(countries_ref)]


def add_un_region(df_hdi: pd.DataFrame, df_jme: pd.DataFrame) -> pd.DataFrame:
    """
    Add the UN region from JME to the HDI dataset and rename it to 'un_region'.
    """
    df_hdi = df_hdi.copy()

    df_hdi = df_hdi.merge(
        df_jme[[COL_JME_COUNTRY, COL_JME_REGION]],
        left_on=COL_HDI_COUNTRY,
        right_on=COL_JME_COUNTRY,
        how="left"
    )

    df_hdi = df_hdi.drop(columns=[COL_JME_COUNTRY])
    df_hdi = df_hdi.rename(columns={COL_JME_REGION: "un_region"})

    return df_hdi


def missing_summary(df: pd.DataFrame, columns: list[str] | None = None) -> pd.DataFrame:
    """
    Produce a missing-values summary table with counts and percentages.
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


def compare_country_sets(df_jme: pd.DataFrame, df_hdi: pd.DataFrame) -> tuple[set, set]:
    """
    Compare country sets between JME and HDI.

    Returns:
    - countries present in JME but missing in HDI
    - countries present in HDI but missing in JME
    """
    jme_countries = set(df_jme[COL_JME_COUNTRY].dropna())
    hdi_countries = set(df_hdi[COL_HDI_COUNTRY].dropna())

    in_jme_not_hdi = jme_countries - hdi_countries
    in_hdi_not_jme = hdi_countries - jme_countries

    return in_jme_not_hdi, in_hdi_not_jme


def to_long_format(df_hdi_wide: pd.DataFrame) -> pd.DataFrame:
    """
    Convert a wide HDI dataset into long format.

    Output columns:
    - year
    - country
    - un_region
    - hdi
    """
    df_hdi_wide = df_hdi_wide.copy()

    hdi_cols = df_hdi_wide.filter(regex=r"^hdi_\d{4}$").columns.tolist()

    df_long = df_hdi_wide.melt(
        id_vars=["country", "un_region"],
        value_vars=hdi_cols,
        var_name="year",
        value_name="hdi"
    )

    df_long["year"] = df_long["year"].str.extract(r"(\d{4})").astype(int)

    df_long = df_long[["year", "country", "un_region", "hdi"]]
    df_long = df_long.sort_values(["year", "country"]).reset_index(drop=True)

    return df_long


# =========================================================
# BASE CLEANING PIPELINE
# =========================================================

def clean_hdi_with_jme_reference(df_jme: pd.DataFrame, df_hdi: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """
    Clean the original worldhdi.xlsx dataset and align it with JME.

    Steps:
    1) clean column names
    2) standardize country text columns
    3) remove rows with missing country names
    4) drop columns not needed
    5) harmonize country names
    6) remove non-country rows
    7) filter by JME reference countries
    8) add un_region from JME
    9) return cleaned dataset + diagnostics
    """
    df_jme = df_jme.copy()
    df_hdi = df_hdi.copy()

    # Clean column names in both datasets
    df_jme = clean_column_names(df_jme)
    df_hdi = clean_column_names(df_hdi)

    # Standardize the country columns
    df_jme = standardize_text_column(df_jme, COL_JME_COUNTRY)
    df_hdi = standardize_text_column(df_hdi, COL_HDI_COUNTRY)

    # Drop rows where country is missing
    df_jme = df_jme.dropna(subset=[COL_JME_COUNTRY])
    df_hdi = df_hdi.dropna(subset=[COL_HDI_COUNTRY])

    # Clean the HDI dataset
    df_hdi = drop_unwanted_hdi_columns(df_hdi)
    df_hdi = harmonize_hdi_country_names(df_hdi)
    df_hdi = remove_non_country_rows(df_hdi)

    # Diagnostics before country filtering
    missing_before_filter = compare_country_sets(df_jme, df_hdi)

    # Keep only countries valid in JME
    df_hdi_clean = filter_hdi_by_jme_countries(df_hdi, df_jme)

    # Add region information
    df_hdi_clean = add_un_region(df_hdi_clean, df_jme)

    # Reorder columns so country and region come first
    ordered_cols = ["country", "un_region"] + [
        c for c in df_hdi_clean.columns if c not in ["country", "un_region"]
    ]
    df_hdi_clean = df_hdi_clean[ordered_cols]

    # Diagnostics after country filtering
    missing_after_filter = compare_country_sets(df_jme, df_hdi_clean)

    diagnostic_cols = [c for c in BASE_HDI_YEARS if c in df_hdi_clean.columns]
    if "hdi_rank" in df_hdi_clean.columns:
        diagnostic_cols.append("hdi_rank")

    diagnostics = {
        "jme_shape": df_jme.shape,
        "hdi_shape_after_cleaning": df_hdi_clean.shape,
        "missing_summary": missing_summary(df_hdi_clean, columns=diagnostic_cols),
        "countries_in_jme_not_in_hdi_before_filter": missing_before_filter[0],
        "countries_in_hdi_not_in_jme_before_filter": missing_before_filter[1],
        "countries_in_jme_not_in_hdi_after_filter": missing_after_filter[0],
        "countries_in_hdi_not_in_jme_after_filter": missing_after_filter[1],
        "countries_without_region": df_hdi_clean[df_hdi_clean["un_region"].isna()][["country"]].drop_duplicates()
    }

    return df_hdi_clean.reset_index(drop=True), diagnostics


# =========================================================
# EXTRA HDR YEARS INTEGRATION PIPELINE
# =========================================================

def build_full_annual_long_dataset(df_hdi_clean: pd.DataFrame, extra_years: list[int]) -> pd.DataFrame:
    """
    Build a complete annual long-format HDI panel by combining:
    - the cleaned base HDI dataset (wide format)
    - the additional yearly HDR Excel files (long format after loading)

    Expected extra files:
    hdr-data_YYYY.xlsx

    Each extra HDR file is expected to contain:
    - country
    - value   (which will be renamed to hdi)
    """
    # Convert the cleaned base dataset to long format first
    df_base_long = to_long_format(df_hdi_clean)

    # Collect all additional yearly datasets
    extra_data = []

    for y in extra_years:
        file = f"hdr-data_{y}.xlsx"

        # Load the yearly Excel file
        df = pd.read_excel(file)

        # Standardize column names and country values
        df = clean_column_names(df)
        df["country"] = df["country"].astype(str).str.strip()

        # Harmonize country names to match the base dataset
        df["country"] = df["country"].replace(COUNTRY_RENAME_MAP)

        # Keep only the columns needed from the yearly file
        # The HDR yearly files use 'value' for HDI
        df = df[["country", "value"]].rename(columns={"value": "hdi"})

        # Add the year from the filename loop
        df["year"] = y

        extra_data.append(df)

    # Concatenate all extra yearly files into one dataframe
    df_extra = pd.concat(extra_data, ignore_index=True)

    # Combine base long HDI values with the yearly additional values
    df_all = pd.concat([
        df_base_long[["country", "year", "hdi"]],
        df_extra[["country", "year", "hdi"]]
    ], ignore_index=True)

    # Re-attach region information from the cleaned reference dataset
    df_all = df_all.merge(
        df_hdi_clean[["country", "un_region"]].drop_duplicates(),
        on="country",
        how="left"
    )

    # Use hdi_clean.csv countries as the final valid country reference
    countries_ref = set(df_hdi_clean["country"].dropna().unique())

    # Keep rows only for valid countries
    df_all = df_all[df_all["country"].isin(countries_ref)].copy()

    # Final column order
    df_all = df_all[["year", "country", "un_region", "hdi"]]

    # Sort for panel analysis
    df_all = df_all.sort_values(["year", "country"]).reset_index(drop=True)

    return df_all


# =========================================================
# IMPUTATION PIPELINE — LONG DATASET VERSION
# =========================================================

def impute_hdi_long(df_hdi_long: pd.DataFrame):
    """
    Hierarchical imputation pipeline for a long-format HDI dataset.

    Expected input columns:
    - year
    - country
    - un_region
    - hdi

    Methods:
    1) temporal interpolation / extrapolation by country
    2) panel regression
    3) regional-temporal smoothing
    4) regional mean fallback

    Returns:
    - df_hdi_imputed_wide: imputed dataset in wide format
    - df_long_imputed: imputed dataset in long format, with audit columns
    - imputation_audit: only rows where HDI was imputed
    """
    df_long = df_hdi_long.copy()

    # -----------------------------------------------------
    # 0. BASIC CLEANING
    # -----------------------------------------------------

    # Standardize column names
    df_long.columns = df_long.columns.str.strip()

    # Make sure the required columns are present
    required_cols = {"year", "country", "un_region", "hdi"}
    missing_cols = required_cols - set(df_long.columns)

    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    # Convert string columns to plain Python objects compatible with statsmodels
    df_long["country"] = df_long["country"].astype(str).str.strip()
    df_long["un_region"] = df_long["un_region"].astype(str).str.strip()

    # Convert numeric columns safely
    df_long["year"] = pd.to_numeric(df_long["year"], errors="coerce")
    df_long["hdi"] = pd.to_numeric(df_long["hdi"], errors="coerce")

    # Drop rows missing country or year
    df_long = df_long.dropna(subset=["country", "year"]).copy()
    df_long["year"] = df_long["year"].astype(int)

    # Remove duplicate country-year rows if any
    df_long = df_long.drop_duplicates(subset=["country", "year"], keep="first")

    # Sort by country and year for interpolation
    df_long = df_long.sort_values(["country", "year"]).reset_index(drop=True)

    # -----------------------------------------------------
    # 1. AUDIT FIELDS
    # -----------------------------------------------------

    # Keep the original HDI values to identify what was imputed later
    df_long["hdi_original"] = df_long["hdi"]
    df_long["imputed_flag"] = 0
    df_long["imputation_method"] = pd.NA

    # -----------------------------------------------------
    # 2. METHOD 1 — TEMPORAL INTERPOLATION / EXTRAPOLATION
    # -----------------------------------------------------

    # First try to fill gaps using each country's own time series
    df_long["hdi_temp"] = (
        df_long.groupby("country")["hdi"]
        .transform(lambda x: x.interpolate(limit_direction="both"))
    )

    mask_temp = df_long["hdi"].isna() & df_long["hdi_temp"].notna()

    df_long.loc[mask_temp, "hdi"] = df_long.loc[mask_temp, "hdi_temp"]
    df_long.loc[mask_temp, "imputed_flag"] = 1
    df_long.loc[mask_temp, "imputation_method"] = "temporal_interpolation"

    # -----------------------------------------------------
    # 3. METHOD 2 — PANEL REGRESSION
    # -----------------------------------------------------

    # Use the non-missing rows to fit a panel-style regression
    df_model = df_long.dropna(subset=["hdi"]).copy()

    # Countries with all original HDI values missing should not receive
    # a country-specific panel estimate
    all_missing_countries = (
        df_long.groupby("country")["hdi_original"]
        .apply(lambda x: x.isna().all())
    )

    all_missing_countries = set(all_missing_countries[all_missing_countries].index)

    # Ensure statsmodels-friendly dtypes
    df_model["country"] = df_model["country"].astype("object")
    df_model["un_region"] = df_model["un_region"].astype("object")
    df_model["year"] = pd.to_numeric(df_model["year"], errors="coerce")
    df_model["hdi"] = pd.to_numeric(df_model["hdi"], errors="coerce")

    # Fit the model
    model = smf.ols(
        "hdi ~ C(country) + C(un_region) + year",
        data=df_model
    ).fit()

    # Predict only rows still missing after temporal interpolation
    mask_panel = df_long["hdi"].isna() & ~df_long["country"].isin(all_missing_countries)

    if mask_panel.sum() > 0:
        pred_data = df_long.loc[mask_panel].copy()
        pred_data["country"] = pred_data["country"].astype("object")
        pred_data["un_region"] = pred_data["un_region"].astype("object")
        pred_data["year"] = pd.to_numeric(pred_data["year"], errors="coerce")

        df_long.loc[mask_panel, "hdi"] = model.predict(pred_data)
        df_long.loc[mask_panel, "imputed_flag"] = 1
        df_long.loc[mask_panel, "imputation_method"] = "panel_regression"

    # -----------------------------------------------------
    # 4. METHOD 3 — REGIONAL-TEMPORAL SMOOTHING
    # -----------------------------------------------------

    # Compute the mean HDI by region and year
    regional_mean = (
        df_long.groupby(["un_region", "year"])["hdi"]
        .mean()
        .rename("regional_mean")
    )

    tmp = df_long.merge(
        regional_mean.reset_index(),
        on=["un_region", "year"],
        how="left"
    )

    # Compute each country's average deviation from its regional mean
    tmp["offset"] = tmp["hdi"] - tmp["regional_mean"]

    country_offset = (
        tmp.groupby("country")["offset"]
        .mean()
        .rename("country_offset")
    )

    tmp = tmp.merge(
        country_offset.reset_index(),
        on="country",
        how="left"
    )

    # Fill remaining gaps using regional mean + country offset
    mask_rts = tmp["hdi"].isna()

    tmp.loc[mask_rts, "hdi_fill_rts"] = (
        tmp.loc[mask_rts, "regional_mean"] +
        tmp.loc[mask_rts, "country_offset"].fillna(0)
    )

    mask_rts_valid = tmp["hdi"].isna() & tmp["hdi_fill_rts"].notna()

    tmp.loc[mask_rts_valid, "hdi"] = tmp.loc[mask_rts_valid, "hdi_fill_rts"]
    tmp.loc[mask_rts_valid, "imputed_flag"] = 1
    tmp.loc[mask_rts_valid, "imputation_method"] = "regional_temporal_smoothing"

    df_long = tmp.copy()

    # -----------------------------------------------------
    # 5. METHOD 4 — REGIONAL MEAN FALLBACK
    # -----------------------------------------------------

    # If anything is still missing, use only the regional mean for that year
    regional_mean_fallback = (
        df_long.groupby(["un_region", "year"])["hdi"]
        .mean()
        .rename("regional_mean_fallback")
    )

    df_long = df_long.merge(
        regional_mean_fallback.reset_index(),
        on=["un_region", "year"],
        how="left"
    )

    mask_regional = df_long["hdi"].isna() & df_long["regional_mean_fallback"].notna()

    df_long.loc[mask_regional, "hdi"] = df_long.loc[mask_regional, "regional_mean_fallback"]
    df_long.loc[mask_regional, "imputed_flag"] = 1
    df_long.loc[mask_regional, "imputation_method"] = "regional_mean_fallback"

    # -----------------------------------------------------
    # 6. FINAL CLEANING
    # -----------------------------------------------------

    # Mark rows still missing after all methods
    mask_still_missing = df_long["hdi"].isna()
    df_long.loc[mask_still_missing, "imputation_method"] = "not_imputed"

    # Restrict HDI to the valid [0, 1] range
    df_long["hdi"] = df_long["hdi"].clip(lower=0, upper=1)

    # -----------------------------------------------------
    # 7. CREATE IMPUTATION AUDIT TABLE
    # -----------------------------------------------------

    # Keep only the rows where HDI was actually imputed
    imputation_audit = df_long.loc[df_long["imputed_flag"] == 1, [
        "country", "un_region", "year", "hdi_original", "hdi", "imputation_method"
    ]].copy()

    imputation_audit = imputation_audit.rename(columns={"hdi": "hdi_filled"})
    imputation_audit = imputation_audit.sort_values(["country", "year"]).reset_index(drop=True)

    # -----------------------------------------------------
    # 8. CONVERT TO WIDE FORMAT
    # -----------------------------------------------------

    # Convert the imputed long panel back into wide format
    df_hdi_imputed_wide = df_long.pivot(
        index=["country", "un_region"],
        columns="year",
        values="hdi"
    ).reset_index()

    df_hdi_imputed_wide.columns = [
        f"hdi_{c}" if isinstance(c, int) else c
        for c in df_hdi_imputed_wide.columns
    ]

    # Order year columns chronologically
    year_cols = sorted(
        [c for c in df_hdi_imputed_wide.columns if c.startswith("hdi_")],
        key=lambda x: int(x.split("_")[1])
    )

    df_hdi_imputed_wide = df_hdi_imputed_wide[
        ["country", "un_region"] + year_cols
    ]

    # -----------------------------------------------------
    # 9. FINAL ORDERING OF LONG DATASET
    # -----------------------------------------------------

    df_long = df_long.sort_values(["year", "country"]).reset_index(drop=True)

    return df_hdi_imputed_wide, df_long, imputation_audit


# =========================================================
# MAIN USAGE
# =========================================================

# Load the two original source files
df_jme = pd.read_excel("JME.xlsx")
df_hdi = pd.read_excel("worldhdi.xlsx")

# ---------------------------------------------
# STEP 1 — CLEAN THE ORIGINAL WIDE HDI DATASET
# ---------------------------------------------
df_hdi_clean, diag = clean_hdi_with_jme_reference(df_jme, df_hdi)

# Save the cleaned base HDI dataset
df_hdi_clean.to_csv("hdi_clean.csv", index=False)

# ---------------------------------------------
# STEP 2 — BUILD THE FULL ANNUAL LONG DATASET
# ---------------------------------------------
df_all = build_full_annual_long_dataset(df_hdi_clean, EXTRA_YEARS)

# Save the long dataset before imputation
df_all.to_csv("hdi_long_full_pre_imputation.csv", index=False)

# ---------------------------------------------
# STEP 3 — IMPUTE MISSING HDI VALUES
# ---------------------------------------------
df_hdi_imputed, df_long_imputed, imputation_audit = impute_hdi_long(df_all)


# ---------------------------------------------
# STEP 4 — CREATE FINAL ANALYSIS DATASET
# ---------------------------------------------

# Remove technical columns used only for auditing the imputation
df_long_final = df_long_imputed.drop(
    columns=["imputed_flag", "imputation_method"],
    errors="ignore"
).copy()

# Round HDI values to two decimal places for presentation and analysis
df_long_final["hdi"] = df_long_final["hdi"].round(2)

# Reorder columns for clarity
df_long_final = df_long_final[["year", "country", "un_region", "hdi"]]

# Save the final dataset used for analysis
df_long_final.to_csv("hdi_long_final.csv", index=False)
