import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("./epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(data=df, x="Year", y="CSIRO Adjusted Sea Level")

    # Create first line of best fit
    slope, intercept, *_ = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    X = np.arange(df["Year"].min(), 2050 + 1)
    Y = slope * X + intercept
    ax.plot(X, Y, "r")

    # Create second line of best fit
    df2 = df.loc[df["Year"] >= 2000]
    slope2, intercept2, *_ = linregress(
        x=df2["Year"], y=df2["CSIRO Adjusted Sea Level"]
    )
    X2 = np.arange(2000, 2050 + 1)
    Y2 = slope2 * X2 + intercept2
    ax.plot(X2, Y2)

    # Add labels and title
    ax.set(title="Rise in Sea Level", xlabel="Year", ylabel="Sea Level (inches)")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
