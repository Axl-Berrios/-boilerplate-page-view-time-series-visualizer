import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)


df = df.dropna()

df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], color='red')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    

    
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['month'] = [d.month for d in df_bar.date]

    
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.barplot(x='year', y='value', data=df_bar, hue='month', palette='bright', ax=ax)
    
    labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September','October', 'November', 'December']
    for t, l in zip(ax.legend(loc='upper left', title='Months').texts, labels): t.set_text(l)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Average Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    

    
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,5))
    
    ax1 = ax[0]
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')

    
    ax2 = ax[1]
    sns.boxplot(x='month', y='value', data=df_box, ax=ax2)
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')
   
    ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec'])
    plt.tight_layout()
    

    
    fig.savefig('box_plot.png')
    return fig
