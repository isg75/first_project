from pathlib import Path
from typing import Optional, Tuple
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from typing import Dict, List  # if not already imported above
import yaml  # make sure this import is at the top with the others

# ----------------------------
# CONFIG HELPERS (YAML)
# ----------------------------
def load_config(path: str | Path = "../config.yaml") -> dict:
    """
    Load YAML configuration file.
    """
    p = Path(path)
    with p.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def read_csv_from_config(config: dict, key: str,
                         low_memory: bool = False,
                         **kwargs) -> pd.DataFrame:
    """
    Read a CSV file using path from config["input_data"][key].
    """
    if "input_data" not in config or key not in config["input_data"]:
        raise KeyError(f"Key '{key}' not found in config['input_data']")
    csv_path = Path(config["input_data"][key])
    return pd.read_csv(csv_path, low_memory=low_memory, **kwargs)


# ----------------------------
# 1) GENERAL UTILITIES
# ----------------------------
def print_shape(df: pd.DataFrame, name: str = "df") -> None:
    """Print DataFrame shape with label."""
    print(f"{name} shape: {df.shape}")

def listdicts_to_df(records: List[Dict]) -> pd.DataFrame:
    """Convert a list of dicts (like the ‘records’ in the photos) into a DataFrame with typed 'Year' if present."""
    df = pd.DataFrame(records).copy()
    if "Year" in df.columns:
        df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
    return df



# ----------------------------
# 2) CLEANING HELPERS
# ----------------------------
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Lowercase, strip, and replace spaces with underscores in column names."""
    df = df.copy()
    df.columns = (df.columns.str.strip()
                              .str.lower()
                              .str.replace(" ", "_")
                              .str.replace("-", "_"))
    return df

def drop_empty_columns(df: pd.DataFrame, thresh: float = 0.5) -> pd.DataFrame:
    """
    Drop columns with more than (1-thresh) fraction of missing values.
    Example: thresh=0.5 drops columns with >50% NaNs.
    """
    df = df.copy()
    limit = len(df) * thresh
    return df.dropna(axis=1, thresh=limit)

def fill_missing_with_unknown(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Fill missing values in specific columns with 'Unknown'."""
    df = df.copy()
    for col in columns:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown")
    return df

def standardize_text_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Standardize text column: strip, lowercase, replace multiple spaces with single."""
    if column not in df.columns:
        return df
    df = df.copy()
    df[column] = (df[column].astype(str)
                              .str.strip()
                              .str.lower()
                              .str.replace(r"\s+", " ", regex=True))
    return df

# --- Winners raw → standardized (compatible with your existing functions) ---

# Raw columns seen in your teammate's notebook:
# "Date", "Men's winner", "Country", "Time[b]", "Women's winner", "Country.1", "Time[b].1"

_RAW_TO_STANDARD_WINNERS = {
    "Men's winner": "men_winner",
    "Country": "men_country",
    "Time[b]": "men_time",
    "Women's winner": "women_winner",
    "Country.1": "women_country",
    "Time[b].1": "women_time",
}

def winners_from_raw(df: pd.DataFrame, date_col: str = "Date") -> pd.DataFrame:
    """
    Convert the raw winners table (with 'Men's winner', 'Time[b]', etc.)
    to your standardized schema expected by your code:
      ['year','men_winner','men_country','men_time','women_winner','women_country','women_time'].
    """
    out = df.rename(columns=_RAW_TO_STANDARD_WINNERS).copy()

    if date_col not in out.columns:
        raise KeyError(f"Column '{date_col}' not found to extract year.")

    out["year"] = (
        out[date_col].astype(str).str.extract(r"(\d{4})", expand=False).astype("Int64")
    )

    cols = [
        "year",
        "men_winner", "men_country", "men_time",
        "women_winner", "women_country", "women_time",
    ]
    existing = [c for c in cols if c in out.columns]
    return out[existing].sort_values("year").reset_index(drop=True)

def to_timedelta_cols_safe(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """
    Convert string time columns to pandas Timedelta (coerce). Safe not to clash with existing names.
    """
    out = df.copy()
    for c in cols:
        if c in out.columns:
            out[c] = pd.to_timedelta(df[c], errors="coerce")
    return out

def time_to_hours(series: pd.Series) -> pd.Series:
    """Convert time strings/Timedelta to float hours."""
    td = pd.to_timedelta(series, errors="coerce")
    return td.dt.total_seconds() / 3600.0


# ----------------------------
# 3) WINNERS TRANSFORMATIONS
# ----------------------------
def winners_wide_to_long(winners_df: pd.DataFrame) -> pd.DataFrame:
    """Reshape winners dataset from wide to long format with [year, winner, country, time, gender]."""
    men = winners_df[["year", "men_winner", "men_country", "men_time"]].copy()
    men = men.rename(columns={
        "men_winner": "winner",
        "men_country": "country",
        "men_time": "time"
    })
    men["gender"] = "male"

    women = winners_df[["year", "women_winner", "women_country", "women_time"]].copy()
    women = women.rename(columns={
        "women_winner": "winner",
        "women_country": "country",
        "women_time": "time"
    })
    women["gender"] = "female"

    for df in (men, women):
        df["year"] = pd.to_numeric(df["year"], errors="coerce")

    return pd.concat([men, women], ignore_index=True)

def top_countries_by_wins(winners_long: pd.DataFrame) -> pd.DataFrame:
    """Count total wins by country. Returns [country, wins]."""
    return (winners_long["country"]
            .value_counts()
            .reset_index()
            .rename(columns={"index": "country", "country": "wins"}))

def winners_by_decade_and_country(winners_long: pd.DataFrame) -> pd.DataFrame:
    """Aggregate number of wins by decade and country. Returns [decade, country, wins]."""
    tmp = winners_long.copy()
    tmp["year"] = pd.to_numeric(tmp["year"], errors="coerce")
    tmp["decade"] = (tmp["year"] // 10) * 10
    return (tmp.groupby(["decade", "country"])
            .size()
            .reset_index(name="wins")
            .sort_values(["decade", "wins"], ascending=[True, False]))


# ----------------------------
# 4) PLOTTING HELPERS
# ----------------------------
def plot_top_countries_bar(df_top: pd.DataFrame,
                           country_col: str = "country",
                           wins_col: str = "wins",
                           title: str = "Top Countries by Wins",
                           figsize: Tuple[int, int] = (8, 5),
                           save_path: Optional[str | Path] = None) -> plt.Axes:
    """Plot horizontal bar chart of countries by wins."""
    fig, ax = plt.subplots(figsize=figsize)
    df_plot = df_top.sort_values(wins_col)
    ax.barh(df_plot[country_col], df_plot[wins_col])
    ax.set_xlabel("Wins")
    ax.set_ylabel("Country")
    ax.set_title(title)
    plt.tight_layout()
    if save_path:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=200, bbox_inches="tight")
    return ax

def plot_decade_country_stacked(df_decade: pd.DataFrame,
                                decade_col: str = "decade",
                                country_col: str = "country",
                                wins_col: str = "wins",
                                title: str = "Country Dominance by Decade (Top 5 per decade)",
                                figsize: Tuple[int, int] = (9, 5),
                                save_path: Optional[str | Path] = None) -> plt.Axes:
    """Plot stacked bar chart of wins per decade and country."""
    pivot = (df_decade
             .pivot_table(index=decade_col, columns=country_col,
                          values=wins_col, aggfunc="sum", fill_value=0)
             .sort_index())

    fig, ax = plt.subplots(figsize=figsize)
    bottom = np.zeros(len(pivot))
    for col in pivot.columns:
        ax.bar(pivot.index, pivot[col].values, bottom=bottom, label=col)
        bottom += pivot[col].values

    ax.set_xlabel("Decade")
    ax.set_ylabel("Wins")
    ax.set_title(title)
    ax.legend(loc="best", ncol=2, fontsize=8)
    plt.tight_layout()
    if save_path:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=200, bbox_inches="tight")
    return ax

def plot_winning_times_evolution(
    winners_df: pd.DataFrame,
    year_col: str = "year",
    men_time_col: str = "men_time",
    women_time_col: str = "women_time",
    highlights: Optional[pd.DataFrame] = None,  # columns: Year, Gender ('Men'/'Women'), Winner, optional Color
    title: str = "Evolution of Winning Times in the Berlin Marathon (1974–2024)",
    figsize: Tuple[int, int] = (12, 6),
) -> plt.Axes:
    """
    Line plot of winning times for men & women (in hours).
    Optional 'highlights' to mark specific years/winners (e.g., WR holders).
    """
    men_h = time_to_hours(winners_df[men_time_col])
    women_h = time_to_hours(winners_df[women_time_col])

    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(winners_df[year_col], men_h, marker="o", alpha=0.4, label="Men (all winners)")
    ax.plot(winners_df[year_col], women_h, marker="o", alpha=0.4, label="Women (all winners)")

    if highlights is not None and not highlights.empty:
        hl = highlights.copy()
        if "Color" not in hl.columns:
            palette = list(plt.cm.tab10.colors)
            hl["Color"] = [palette[i % len(palette)] for i in range(len(hl))]
        for _, row in hl.iterrows():
            yr = int(row["Year"])
            gender = row["Gender"]
            color = row["Color"]
            mask = winners_df[year_col].astype(int) == yr
            if mask.any():
                y = men_h[mask].values[0] if gender == "Men" else women_h[mask].values[0]
                ax.scatter([yr], [y], s=100, color=color, zorder=5,
                           label=f"{gender} WR: {row.get('Winner','')} ({yr})")

    ax.set_xlabel("Year")
    ax.set_ylabel("Winning Time (hours)")
    ax.set_title(title)
    ax.grid(True, linestyle="--", alpha=0.6)
    fig.tight_layout()
    ax.legend()
    return ax


def plot_world_records_by_city(
    wr_df: pd.DataFrame,
    year_col: str = "Year",
    gender_col: str = "Gender",
    city_col: str = "City",
    time_col: str = "Time",
    title: str = "Evolution of World Marathon Records (Men & Women, all cities)",
    figsize: Tuple[int, int] = (12, 6),
) -> plt.Axes:
    """
    Plot the evolution of marathon world records for Men/Women and color the points by city.
    Expects wr_df with columns: Year (int), Gender ('Men'/'Women'), City, Time (str or timedeltas).
    """
    df = wr_df.copy()
    df["Time_h"] = time_to_hours(df[time_col])

    cities = sorted(df[city_col].dropna().unique())
    city_colors = {c: plt.cm.tab10(i % 10) for i, c in enumerate(cities)}

    fig, ax = plt.subplots(figsize=figsize)

    men = df[df[gender_col] == "Men"].sort_values(year_col)
    ax.plot(men[year_col], men["Time_h"], lw=2, label="Men WRs")
    ax.scatter(men[year_col], men["Time_h"], c=men[city_col].map(city_colors),
               s=180, marker="o", edgecolors="white", zorder=5)

    women = df[df[gender_col] == "Women"].sort_values(year_col)
    ax.plot(women[year_col], women["Time_h"], lw=2, label="Women WRs")
    ax.scatter(women[year_col], women["Time_h"], c=women[city_col].map(city_colors),
               s=180, marker="o", edgecolors="white", zorder=5)

    from matplotlib.lines import Line2D
    city_handles = [Line2D([0], [0], marker="o", color="w",
                           markerfacecolor=color, markersize=12, label=city)
                    for city, color in city_colors.items()]
    legend1 = ax.legend(handles=city_handles, title="City",
                        bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=10)

    gender_handles = [
        Line2D([0], [0], color="orange", lw=2, label="Women"),
        Line2D([0], [0], color="black", lw=2, label="Men"),
    ]
    legend2 = ax.legend(handles=gender_handles, title="Gender",
                        bbox_to_anchor=(1.05, 0.7), loc="upper left", fontsize=10)
    ax.add_artist(legend1)

    ax.set_xlabel("Year")
    ax.set_ylabel("World Record Time (hours)")
    ax.set_title(title)
    ax.grid(True, linestyle="--", alpha=0.6)
    fig.tight_layout()
    return ax

# ----------------------------
# 5) COMPATIBILITY HELPERS
# ----------------------------

def load_csv(path: str, **kwargs) -> pd.DataFrame:
    """
    Wrapper for pd.read_csv so notebooks using load_csv keep working.
    """
    return pd.read_csv(path, **kwargs)

def save_csv(df: pd.DataFrame, path: str, index: bool = False, **kwargs) -> None:
    """
    Wrapper for df.to_csv so notebooks using save_csv keep working.
    Creates parent directories if needed.
    """
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=index, **kwargs)

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Alias for clean_column_names to keep notebooks compatible.
    """
    return clean_column_names(df)

def check_missing(df: pd.DataFrame, name: str = "df") -> None:
    """
    Simple missing values check.
    
Prints number of missing values per column.
    """
    missing = df.isnull().sum()
    print(f"Missing values in {name}:")
    print(missing[missing > 0])

def clean_runners_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """
    Placeholder cleaning pipeline for runners dataset.
    Currently just returns the DataFrame unchanged.
    Added for compatibility with notebooks that import it.
    """
    return df
