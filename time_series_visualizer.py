import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Import data and set the index to the column 'date'
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# 2. Clean the data by removing the top and bottom 2.5% of page views
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

# 3. Create a function to draw the line plot
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df.index, df['value'], color='r', linewidth=1)

    # Set title and labels
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save and return the figure
    fig.savefig('line_plot.png')
    return fig

# 4. Create a function to draw the bar plot
def draw_bar_plot():
    # Prepare data for bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # Group the data by year and month and calculate the average page views
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Create the bar plot
    fig = df_bar.plot(kind='bar', figsize=(10, 6)).figure

    plt.title('Average Daily Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')

    plt.legend(title='Months', labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    # Save and return the figure
    fig.savefig('bar_plot.png')
    return fig

# 5. Create a function to draw the box plot
def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box['year'] = [d.year for d in df_box.index]
    df_box['month'] = [d.strftime('%b') for d in df_box.index]
    df_box['month_num'] = df_box.index.month
    df_box = df_box.sort_values('month_num')

    # Draw box plots using Seaborn
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df_box, ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Save and return the figure
    fig.savefig('box_plot.png')
    return fig
