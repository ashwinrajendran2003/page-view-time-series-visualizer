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
    """Draws a line plot for daily page views over time."""
    
    fig, ax = plt.subplots(figsize=(12, 5))
    
    # Plot the data
    ax.plot(df.index, df["value"], color="red", linewidth=1)
    
    # Set title and labels
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    
    # Save image and return fig
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    """Draws a bar plot for average monthly page views by year."""
    
    # Prepare data
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.strftime('%B')  # FULL month names

    # Group and compute monthly averages
    df_bar = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    # Define month order
    month_order = ["January", "February", "March", "April", "May", "June", 
                   "July", "August", "September", "October", "November", "December"]

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 6))
    df_bar = df_bar[month_order]  # Reorder months correctly
    df_bar.plot(kind="bar", ax=ax, colormap="tab10")

    # Formatting
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months", labels=month_order)

    # Save image and return fig
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    """Draws two box plots: Year-wise and Month-wise page views."""

    # Prepare data for box plots
    df_box = df.copy()
    df_box["year"] = df_box.index.year
    df_box["month"] = df_box.index.strftime('%B')  # FULL month names

    # Define month order
    month_order = ["January", "February", "March", "April", "May", "June", 
                   "July", "August", "September", "October", "November", "December"]
    
    # Create subplots
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Year-wise box plot
    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0], hue="year", legend=False)
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise box plot
    sns.boxplot(x="month", y="value", data=df_box, order=month_order, ax=axes[1], hue="month", legend=False)
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save image and return fig
    fig.savefig('box_plot.png')
    return fig
