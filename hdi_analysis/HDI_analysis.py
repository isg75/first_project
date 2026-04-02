import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import spearmanr
from matplotlib.ticker import PercentFormatter


# ======================================================
# CONFIGURATION
# ======================================================

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ======================================================
# RELIGION NORMALIZATION
# ======================================================

def normalize_religion_columns(df, religion_cols):
    """
    Normalize religion columns so that each row sums to 1.
    Then compute the dominant religion share.
    """

    df = df.copy()

    # Calculate total number of religious adherents per row
    df["religion_sum_before"] = df[religion_cols].sum(axis=1)

    # Remove rows where the total is zero to avoid division by zero
    df = df[df["religion_sum_before"] > 0]

    # Normalize each religion column
    df[religion_cols] = df[religion_cols].div(df["religion_sum_before"], axis=0)

    # Calculate the share of the largest religion
    df["dominant_share"] = df[religion_cols].max(axis=1)

    return df


# ======================================================
# DATA CLEANING
# ======================================================

def clean_data(df):

    df = df.copy()

    df["hdi"] = pd.to_numeric(df["hdi"], errors="coerce")
    df["dominant_share"] = pd.to_numeric(df["dominant_share"], errors="coerce")
    df["conflict_present"] = pd.to_numeric(df["conflict_present"], errors="coerce")

    df = df.replace([np.inf, -np.inf], np.nan)

    df = df.dropna(subset=["hdi", "dominant_share", "conflict_present"])

    return df


# ======================================================
# HDI vs DOMINANT RELIGION SHARE
# ======================================================

def compute_spearman(df):

    corr, p = spearmanr(df["hdi"], df["dominant_share"])

    print("\nSpearman correlation:", corr)
    print("p-value:", p)

    return corr, p


def run_ols_regression(df):

    X = sm.add_constant(df["hdi"])
    y = df["dominant_share"]

    model = sm.OLS(y, X).fit()

    print("\nOLS Regression Results")
    print(model.summary())

    return model


def plot_hdi_vs_religion(df):

    plt.figure(figsize=(8,6))

    sns.regplot(
        data=df,
        x="hdi",
        y="dominant_share",
        scatter_kws={"alpha":0.4}
    )

    plt.title("HDI vs Dominant Religion Share")
    plt.xlabel("Human Development Index")
    plt.ylabel("Share of Dominant Religion")

    plt.tight_layout()

    plt.savefig(
        os.path.join(OUTPUT_DIR,"hdi_vs_dominant_religion.png"),
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ======================================================
# HDI vs CONFLICT
# ======================================================

def run_logistic_regression(df):

    X = sm.add_constant(df["hdi"])
    y = df["conflict_present"]

    logit_model = sm.Logit(y, X).fit()

    print("\nLogit Regression Results")
    print(logit_model.summary())

    return logit_model


def plot_conflict_probability(df, logit_model):

    plot_df = df[["hdi","conflict_present"]].copy()

    hdi_range = np.linspace(plot_df["hdi"].min(), plot_df["hdi"].max(),100)

    X_pred = pd.DataFrame({"hdi":hdi_range})
    X_pred = sm.add_constant(X_pred)

    pred_prob = logit_model.predict(X_pred)

    plt.figure(figsize=(8,6))

    jitter = np.random.uniform(-0.02,0.02,len(plot_df))

    plt.scatter(
        plot_df["hdi"],
        plot_df["conflict_present"] + jitter,
        alpha=0.3
    )

    plt.plot(
        hdi_range,
        pred_prob,
        linewidth=3
    )

    plt.xlabel("HDI")
    plt.ylabel("Probability of Conflict")
    plt.title("Predicted Probability of Conflict vs HDI")

    plt.ylim(-0.05,1.05)

    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.yticks(np.linspace(0,1,11))

    plt.grid(alpha=0.2)

    plt.tight_layout()

    plt.savefig(
        os.path.join(OUTPUT_DIR,"conflict_probability_vs_hdi.png"),
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


def plot_conflict_boxplot(df):

    plot_df = df.copy()

    plot_df["conflict_label"] = plot_df["conflict_present"].map({
        0:"No Conflict",
        1:"Conflict"
    })

    plt.figure(figsize=(8,6))

    sns.boxplot(
        data=plot_df,
        x="conflict_label",
        y="hdi"
    )

    plt.title("HDI Distribution by Conflict Presence")
    plt.xlabel("Conflict Presence")
    plt.ylabel("Human Development Index")

    plt.tight_layout()

    plt.savefig(
        os.path.join(OUTPUT_DIR,"hdi_boxplot_conflict.png"),
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ======================================================
# MAIN PIPELINE
# ======================================================

def main():

    # Load dataset
    df = pd.read_csv("dataset.csv")


    # Example religion columns (adapt to your dataset)
    religion_cols = [
        "christianity_all",
        "islam_all",
        "buddhism_all",
        "hinduism_all",
        "judaism_all",
        "other_religions"
    ]


    # Normalize religion columns
    df = normalize_religion_columns(df, religion_cols)


    # Clean dataset
    df = clean_data(df)


    # ---------------------------------
    # HDI vs Dominant Religion Share
    # ---------------------------------

    compute_spearman(df)

    ols_model = run_ols_regression(df)

    plot_hdi_vs_religion(df)


    # ---------------------------------
    # HDI vs Conflict
    # ---------------------------------

    logit_model = run_logistic_regression(df)

    plot_conflict_boxplot(df)

    plot_conflict_probability(df, logit_model)


# ======================================================

if __name__ == "__main__":
    main()