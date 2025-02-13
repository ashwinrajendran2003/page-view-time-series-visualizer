import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Import data
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) & 
        (df["value"] <= df["value"].quantile(0.975))]

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df.index, df["value"], color='red', linewidth=1)

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    plt.xticks(rotation=30)
    plt.grid(True)

    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    df_bar = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    fig = df_bar.plot(kind="bar", figsize=(12, 6)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=['January', 'February', 'March', 'April', 'May', 'June', 
 'July', 'August', 'September', 'October', 'November', 'December'])
    
    plt.xticks(rotation=0)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    df_box = df.copy()
    df_box["year"] = df_box.index.year
    df_box['month'] = df_box.index.strftime('%B')  # Convert numbers to full month names


    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']

    sns.boxplot(x="month", y="value", data=df_box, order=month_order, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig('box_plot.png')
    return fig
