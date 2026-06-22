import polars as pl
from pathlib import Path


def ensure_directory(path: str | Path) -> Path:
    """
    Create directory if it does not exist and return it as a Path object.
    """
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def export_csv(df: pl.DataFrame, output_dir: str | Path, filename: str) -> Path:
    """
    Export a Polars DataFrame to CSV.
    """
    output_dir = ensure_directory(output_dir)
    output_path = output_dir / filename
    df.write_csv(output_path)
    return output_path


def export_multiple(dataframes: dict[str, pl.DataFrame], output_dir: str | Path) -> list[Path]:
    """
    Export multiple DataFrames to CSV.
    Example:
        export_multiple({
            "merged.csv": merged,
            "gdp_rank.csv": gdp_rank
        }, "../outputs")
    """
    output_dir = ensure_directory(output_dir)
    paths = []

    for filename, df in dataframes.items():
        output_path = output_dir / filename
        df.write_csv(output_path)
        paths.append(output_path)

    return paths