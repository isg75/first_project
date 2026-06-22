# From notebooks, imports should work if you run from project root or add:
# import sys
# sys.path.append("..")


import matplotlib.pyplot as plt
import numpy as np
import polars as pl


def plot_fastest_aging_dumbbell(df: pl.DataFrame, highlight_country: str = "Japan") -> None:
    countries = df["country"].to_list()
    values_2010 = df["share_65plus_2010"].to_list()
    values_2018 = df["share_65plus_2018"].to_list()
    y = np.arange(len(countries))

    fig, ax = plt.subplots(figsize=(11.5, 6.5))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    for i, country in enumerate(countries):
        highlight = country == highlight_country

        line_color = "#d0d0d0" if not highlight else "#1f77b4"
        dot_2010_color = "#8c8c8c" if not highlight else "#1f77b4"
        dot_2018_color = "#222222" if not highlight else "#1f77b4"
        line_width = 2.8 if not highlight else 3.5
        dot_size = 55 if not highlight else 70

        ax.hlines(
            y=i,
            xmin=values_2010[i],
            xmax=values_2018[i],
            color=line_color,
            linewidth=line_width,
            zorder=1
        )

        ax.scatter(values_2010[i], i, color=dot_2010_color, s=dot_size, zorder=2)
        ax.scatter(values_2018[i], i, color=dot_2018_color, s=dot_size, zorder=3)

        ax.text(
            values_2010[i] - 0.75, i, f"{values_2010[i]:.1f}%",
            ha="right", va="center", fontsize=10, color="#666666"
        )
        ax.text(
            values_2018[i] + 0.75, i, f"{values_2018[i]:.1f}%",
            ha="left", va="center", fontsize=10.5, color="#222222"
        )

    ax.set_yticks(y)
    ax.set_yticklabels(countries, fontsize=11)

    xmin = min(values_2010) - 3.2
    xmax = max(values_2018) + 3.2
    ax.set_xlim(xmin, xmax)

    ax.set_title("Fastest Aging Societies, 2010–2018", fontsize=19, loc="left", pad=22)
    ax.text(
        0, 1.04,
        "Share of population aged 65+ increased fastest in selected economies.",
        transform=ax.transAxes,
        fontsize=11,
        color="#555555"
    )

    ax.set_xlabel("Population aged 65+ (%)", fontsize=12, labelpad=14)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#cccccc")

    ax.grid(axis="x", linestyle="--", linewidth=0.8, alpha=0.18)
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", colors="#666666")

    ax.text(
        0, -0.12,
        "Source: World Bank WDI, authors' calculations.",
        transform=ax.transAxes,
        fontsize=9.5,
        color="#777777"
    )

    plt.tight_layout()
    plt.show()


def plot_oldest_vs_youngest_dumbbell(df: pl.DataFrame, oldest_n: int = 5, youngest_n: int = 5) -> None:
    oldest = df.sort("share_65plus_2018", descending=True).head(oldest_n)
    youngest = df.sort("share_65plus_2018").head(youngest_n)

    comparison = pl.concat([oldest, youngest]).sort("share_65plus_2018")

    countries = comparison["country"].to_list()
    values_2010 = comparison["share_65plus_2010"].to_list()
    values_2018 = comparison["share_65plus_2018"].to_list()
    old_countries = oldest["country"].to_list()

    y = np.arange(len(countries))

    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    for i, country in enumerate(countries):
        is_old = country in old_countries

        if is_old:
            line_color = "#1f77b4"
            dot_2018_color = "#1f77b4"
        else:
            line_color = "#f2a65a"
            dot_2018_color = "#f2a65a"

        dot_2010_color = "#888888"

        ax.hlines(
            y=i,
            xmin=values_2010[i],
            xmax=values_2018[i],
            color=line_color,
            linewidth=3,
            zorder=1
        )

        ax.scatter(values_2010[i], i, color=dot_2010_color, s=60, zorder=2)
        ax.scatter(values_2018[i], i, color=dot_2018_color, s=70, zorder=3)

        ax.text(
            values_2010[i] - 0.7, i, f"{values_2010[i]:.1f}%",
            ha="right", va="center", fontsize=10, color="#666666"
        )
        ax.text(
            values_2018[i] + 0.7, i, f"{values_2018[i]:.1f}%",
            ha="left", va="center", fontsize=10, color="#222222"
        )

    ax.set_yticks(y)
    ax.set_yticklabels(countries, fontsize=11)

    xmin = min(values_2010) - 3.5
    xmax = max(values_2018) + 3.5
    ax.set_xlim(xmin, xmax)
    ax.set_xticks([])

    ax.set_title("Youngest vs Oldest Societies, 2010–2018", fontsize=20, loc="left", pad=24)
    ax.text(
        0, 1.04,
        "A widening demographic divide: older societies continue aging while the youngest remain extremely young.",
        transform=ax.transAxes,
        fontsize=11,
        color="#555555"
    )

    ax.set_xlabel("Population aged 65+ (%)", fontsize=12, labelpad=12)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    ax.tick_params(axis="y", length=0)

    ax.text(
        0, -0.12,
        "Source: World Bank World Development Indicators (WDI).",
        transform=ax.transAxes,
        fontsize=9.5,
        color="#777777"
    )

    plt.tight_layout()
    plt.show()


def plot_aging_level_vs_speed(df: pl.DataFrame) -> None:
    countries = df["country"].to_list()
    aging_level = df["share_65plus_2018"].to_list()
    aging_speed = df["aging_speed"].to_list()

    oldest = df.sort("share_65plus_2018", descending=True).head(5)["country"].to_list()
    youngest = df.sort("share_65plus_2018").head(5)["country"].to_list()

    x_mid = df["share_65plus_2018"].median()
    y_mid = df["aging_speed"].median()

    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    for i, country in enumerate(countries):
        if country in oldest:
            color = "#1f77b4"
            size = 70
        elif country in youngest:
            color = "#f2a65a"
            size = 70
        else:
            color = "#bfbfbf"
            size = 30

        ax.scatter(
            aging_level[i],
            aging_speed[i],
            s=size,
            color=color,
            alpha=0.9,
            zorder=3
        )

        if country in oldest or country in youngest:
            ax.text(
                aging_level[i] + 0.2,
                aging_speed[i] + 0.02,
                country,
                fontsize=10,
                color="#333333"
            )

    ax.axvline(x=x_mid, color="#999999", linestyle="--", linewidth=1)
    ax.axhline(y=y_mid, color="#999999", linestyle="--", linewidth=1)

    ax.set_xlabel("Population aged 65+ in 2018 (%)", fontsize=12)
    ax.set_ylabel("Increase in population aged 65+ (2010–2018)", fontsize=12)

    ax.set_title("Aging Level vs Aging Speed", fontsize=20, loc="left", pad=24)
    ax.text(
        0, 1.04,
        "Old societies are highlighted in blue, while the youngest populations appear in orange.",
        transform=ax.transAxes,
        fontsize=11,
        color="#555555"
    )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#cccccc")
    ax.spines["bottom"].set_color("#cccccc")

    ax.grid(True, linestyle="--", linewidth=0.8, alpha=0.15)
    ax.tick_params(colors="#666666")

    ax.text(
        0, -0.12,
        "Source: World Bank World Development Indicators (WDI).",
        transform=ax.transAxes,
        fontsize=9.5,
        color="#777777"
    )

    plt.tight_layout()
    plt.show()


def plot_hci_vs_lfp(df: pl.DataFrame, highlights: list[str] | None = None) -> None:
    if highlights is None:
        highlights = ["Japan", "Germany", "United States", "Brazil", "Kenya"]

    countries = df["country"].to_list()
    hci_values = df["hci_2018"].to_list()
    lfp_values = df["labor_participation_2018"].to_list()

    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    for i, country in enumerate(countries):
        highlight = country in highlights
        color = "#1f77b4" if highlight else "#bfbfbf"
        size = 60 if highlight else 30

        ax.scatter(
            hci_values[i],
            lfp_values[i],
            color=color,
            s=size,
            alpha=0.85,
            zorder=3 if highlight else 2
        )

        if highlight:
            ax.text(
                hci_values[i] + 0.003,
                lfp_values[i] + 0.2,
                country,
                fontsize=9.5,
                color="#333333"
            )

    ax.set_xlabel("Human Capital Index (2018)", fontsize=12)
    ax.set_ylabel("Labor Force Participation (%)", fontsize=12)

    ax.set_title("Human Capital and Labor Participation", fontsize=20, loc="left", pad=24)
    ax.text(
        0, 1.04,
        "Countries with stronger human capital tend to show higher labor force participation.",
        transform=ax.transAxes,
        fontsize=11,
        color="#555555"
    )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#cccccc")
    ax.spines["bottom"].set_color("#cccccc")

    ax.grid(True, linestyle="--", linewidth=0.8, alpha=0.15)
    ax.tick_params(colors="#666666")

    ax.text(
        0, -0.12,
        "Source: World Bank HCI and labor-force participation data.",
        transform=ax.transAxes,
        fontsize=9.5,
        color="#777777"
    )

    plt.tight_layout()
    plt.show()