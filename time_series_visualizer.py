import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Import data
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data
df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df.index, df["value"], color="red", linewidth=1)

    # Formatting
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Prepare data for bar plot
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    df_bar = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    # Draw bar plot
    fig = df_bar.plot(kind="bar", figsize=(10, 6)).figure

    # Formatting
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=[
        "January", "February", "March", "April", "May", "June", "July", "August",
        "September", "October", "November", "December"
    ])

    # Save image
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box["year"] = df_box.index.year
    df_box["month"] = df_box.index.strftime("%b")  # Use short month names

    # Sort months in correct order
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Year-wise box plot
    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise box plot
    sns.boxplot(x="month", y="value", data=df_box, order=month_order, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save image
    fig.savefig('box_plot.png')
    return fig
