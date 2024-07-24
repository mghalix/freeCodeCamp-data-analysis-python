import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(
    "./fcc-forum-pageviews.csv",
    index_col="date",
    parse_dates=True,
)

# Clean data
mask = (df["value"] > df["value"].quantile(0.025)) & (
    df["value"] < df["value"].quantile(0.975)
)

df = df[mask]


# Draw Line Plot
def draw_line_plot():
    fig, axes = plt.subplots(figsize=(16, 5))
    axes.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    axes.set_ylabel("Page Views")
    axes.set_xlabel("Date")
    axes.plot(
        df.index,
        df["value"],
        linestyle="solid",
        color="red",
        linewidth=1,
    )

    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    from calendar import month_name

    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()

    # Slice to skip the empty string in month_name at index 0
    months = list(month_name)[1:]
    # Convert month column to categorical using months as the available classes
    df_bar["month"] = pd.Categorical(df_bar["month"], categories=months)

    df_pivot_table = pd.pivot_table(
        data=df_bar,
        index="year",
        columns="month",
        values="value",
        aggfunc="mean",
        observed=False,
    )

    fig, ax = plt.subplots(figsize=(10, 8))
    df_pivot_table.plot(kind="bar", ax=ax)

    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months")

    fig.savefig("bar_plot.png")
    return fig

def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime("%b") for d in df_box.date]

    df_box["month_number"] = df_box["date"].apply(lambda x: x.month)
    df_box = df_box.sort_values("month_number")
    df_box.drop("month_number", axis=1, inplace=True)

    plot_objects = plt.subplots(nrows=1, ncols=2, figsize=(30, 12))
    fig, (ax1, ax2) = plot_objects
    ax1.set(title="Year-wise Box Plot (Trend)", xlabel="Year", ylabel="Page Views")
    sns.boxplot(
        x="year",
        y="value",
        data=df_box,
        ax=ax1,
        hue="year",
    )

    ax2.set(
        title="Month-wise Box Plot (Seasonality)", xlabel="Month", ylabel="Page Views"
    )
    sns.boxplot(
        x="month",
        y="value",
        data=df_box,
        ax=ax2,
        hue="month",
    )

    return fig


fig = draw_box_plot()