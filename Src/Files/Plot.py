from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import mplfinance as mpf
import os
""""""""
def matrix_correlaton(df_list,period):
    new_df = pd.DataFrame()

    for iter in df_list:
        for currency, df in iter.items():
            one_year_ago = datetime.now() - timedelta(days=period)
            filtered_df = df[df['Date'] >= one_year_ago.strftime('%Y-%m-%d')]
            filtered_df = filtered_df.reset_index(drop=True)
            new_df[f'{currency}'] = (filtered_df['Open'] + filtered_df['Close']) / 2

    correlation_matrix = new_df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title(f'Exchange rate correlation {period} days')
    plt.savefig(os.getcwd() + f"/Src/Documents/Correlation_matrix_{period}_days.pdf")
    plt.show()

def candle_chart(df_list,period):
    for iter in df_list:
        for currency, df in iter.items():
            df['Date'] = pd.to_datetime(df['Date'])
            df.set_index('Date', inplace=True)

            one_year_ago = df.index[-1] - pd.DateOffset(days=period)
            df_one_year = df[df.index >= one_year_ago]

            mpf.plot(df_one_year, type='candle', title=f'\n\nCandlestick Chart - {currency} - {period} days ',
                     savefig= os.getcwd() + f"/Src/Documents/Candlestick_Chart_{currency}_{period}_days.pdf")
