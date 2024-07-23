import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Import Data
df = pd.read_csv("./medical_examination.csv")


# 2. Add 'overweight' column
# assumes weight in kg and height in m
calc_bmi = lambda weight, height: weight / height**2
cm_to_m = lambda x: x / 100

BMI = calc_bmi(df["weight"], cm_to_m(df["height"]))
overweight_mask = BMI > 25

# 1 for overweight (True) and 0 otherwise (False)
df["overweight"] = overweight_mask.astype(int)

## 3 - Normalizing Data 0 (Always Good) 1 (Always Bad)
## If the value is 1 set to 0 - if gt 1 set to 1
df[["cholesterol", "gluc"]] = (df[["cholesterol", "gluc"]] > 1).astype(int)

## OR
# df.loc[df["cholesterol"] == 1, "cholesterol"] = 0
# df.loc[df["cholesterol"] > 1, "cholesterol"] = 1

# df.loc[df["gluc"] == 1, "gluc"] = 0
# df.loc[df["gluc"] > 1, "gluc"] = 1

## OR
# df['cholesterol'] = df['cholesterol'].replace([1, 2, 3], [0, 1, 1])
# df['gluc'] = df['gluc'].replace([1, 2, 3], [0, 1, 1])

## OR
# df[["cholesterol", "gluc"]] = df[["cholesterol", "gluc"]].replace([1, 2, 3], [0, 1, 1])



# 4. Draw Categorical Plot
def draw_cat_plot():
    # 5. Create DataFrame for cat plot using `pd.melt` using just the values
    # from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(
        id_vars=["cardio"],
        value_vars=[
            "cholesterol",
            "gluc",
            "smoke",
            "alco",
            "active",
            "overweight",
        ],
    )

    # 6. Group and reformat the data to split it by 'cardio'. Show the counts
    # of each feature. You will have to rename one of the collumns for the
    # catplot to work correctly.
    df_cat = (
        df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")
    )

    ## OR
    ## WRONGGG (why?)
    # df_cat = (
    #     df_cat[["cardio", "variable", "value"]].value_counts().reset_index(name="total")
    # )

    # 7. Draw the catplot with 'sns.catplot()'
    draw = sns.catplot(
        data=df_cat, x="variable", y="total", hue="value", col="cardio", kind="bar"
    )

    ## OR
    # fig = (
    #     sns.catplot(data=df_cat, kind="count", x="variable", hue="value", col="cardio")
    #     .set_ylabels("total")
    #     .fig
    # )

    # 8. Get the figure for the output
    fig = draw.fig

    # 9. Do not modify the next two lines
    fig.savefig("catplot.png")
    return fig

# 10. Draw Heat Map
def draw_heat_map():
    correct_data_mask = (
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    )
    # 11. Clean the data
    df_heat = df[correct_data_mask]

    # 12. Calculate the correlation matrix
    corr = df_heat.corr()

    # 13. Generate a mask for the upper triangle
    mask = np.triu(corr)
    ## OR
    # mask = np.zeros_like(corr)
    # mask[np.triu_indices_from(mask)] = True

    # 14. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15. Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(
        data=corr,
        mask=mask,
        annot=True,
        fmt="0.1f",
        square=True,
        cbar_kws={"shrink": 0.45, "format": "%.2f"},
    )

    # 16. Do not modify the next two lines
    fig.savefig("heatmap.png")
    return fig
