import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Import data
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')

    # 3. Line of best fit for all data
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope_all = res_all.slope
    intercept_all = res_all.intercept

    # Years for the prediction line (up to 2050)
    years_all = pd.Series(range(df['Year'].min(), 2051))
    line_all = intercept_all + slope_all * years_all
    ax.plot(years_all, line_all, 'r', label='Fit: All years')

    # 4. Line of best fit for 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    slope_recent = res_recent.slope
    intercept_recent = res_recent.intercept

    years_recent = pd.Series(range(2000, 2051))
    line_recent = intercept_recent + slope_recent * years_recent
    ax.plot(years_recent, line_recent, 'green', label='Fit: 2000 onwards')

    # 5. Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # 6. Save plot
    fig.savefig('sea_level_plot.png')

    return fig
