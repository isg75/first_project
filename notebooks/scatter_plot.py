# Add all the imports needed by the functions in the project here
#================================================================
import pandas as pd
import matplotlib.pyplot as plt
#================================================================


def scatter_plot(df, x_col, y_col, title="Scatter Plot", xlabel=None, ylabel=None, color="blue", marker="o"):
    """
    Create a scatter plot from a pandas DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the data.
    x_col : str
        Column name for the x-axis.
    y_col : str
        Column name for the y-axis.
    title : str, optional
        Title of the plot (default: "Scatter Plot").
    xlabel : str, optional
        Label for the x-axis (default: x_col).
    ylabel : str, optional
        Label for the y-axis (default: y_col).
    color : str, optional
        Color of the points (default: "blue").
    marker : str, optional
        Marker style (default: "o").

    Returns
    -------
    None
        Displays the scatter plot.
    """
    plt.figure(figsize=(6,4))
    plt.scatter(df[x_col], df[y_col], color=color, marker=marker)
    plt.title(title)
    plt.xlabel(xlabel if xlabel else x_col)
    plt.ylabel(ylabel if ylabel else y_col)
    plt.grid(True)
    plt.show()