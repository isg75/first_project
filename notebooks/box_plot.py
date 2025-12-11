# box_plot.py
#================================================================
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#================================================================

def box_plot(df, column ="", title="Boxplot", ylabel=None, color="skyblue"):
    """
    Create a boxplot for a specific column in a pandas DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the data.
    column : str
        Column name to plot.
    title : str, optional
        Title of the plot (default: "Boxplot").
    ylabel : str, optional
        Label for the y-axis (default: column name).
    color : str, optional
        Color of the box (default: "skyblue").

    Returns
    -------
    None
        Displays the boxplot.
    """
    plt.figure(figsize=(6,4))
    plt.boxplot(df[column], patch_artist=True,
                boxprops=dict(facecolor=color, color="black"),
                medianprops=dict(color="red"))
    plt.title(title)
    plt.ylabel(ylabel if ylabel else column)
    plt.grid(True, axis="y", linestyle="--", alpha=0.7)
    plt.show()


