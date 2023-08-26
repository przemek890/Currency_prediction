from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import mplfinance as mpf
import os
import pyautogui
""""""""""""""
def matrix_correlaton(df_list,start=datetime.now() - timedelta(days=100),end=datetime.now()):   # okres od wskazanej daty

    if len(df_list) < 2: return # Bez sensu tworzyc macierz korelacji 1x1

    new_df = pd.DataFrame()
    for iter in df_list:
        for currency, df in iter.items():
            df = df.copy()
            df['Date'] = pd.to_datetime(df['Date'])
            df.set_index('Date', inplace=True)
            filtered_df = df[(df.index >= start) & (df.index <= end)]

            new_df[f'{currency}'] = (filtered_df['Open'] + filtered_df['Close']) / 2

    correlation_matrix = new_df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title(f'Exchange rate correlation from {start.date()} to {end.date()}')

    if not os.path.exists(os.getcwd() + f"/Documents/Files/{start.date()}_{end.date()}"):
        os.makedirs(os.getcwd() + f"/Documents/Files/{start.date()}_{end.date()}")

    plt.savefig(os.getcwd() + f"/Documents/Files/{start.date()}_{end.date()}/Correlation_matrix_{start.date()}_{end.date()}.pdf")

    plt.show()
    plt.close()
def candle_chart(df_list, patterns, colors, start=datetime.now() - timedelta(days=100), end=datetime.now()):
    for iter in df_list:
        for currency, df in iter.items():

            df = df.copy()
            df['Date'] = pd.to_datetime(df['Date'])
            df.set_index('Date', inplace=True)
            df_time = df[(df.index >= start) & (df.index <= end)]

            fig, axes = mpf.plot(df_time, type='candle', title=f'\n\nCandlestick Chart - {currency} -> {start.date()}_{end.date()}', returnfig=True, figscale=0.75)

            for pattern in patterns:
                pattern_date = pd.to_datetime(pattern['Date'])
                pattern_index = df_time.index.get_loc(pattern_date)
                candle_x = pattern_index
                candle_y = pattern['High']

                avg = 0.5 * (df['High'].max() + df['Low'].min())

                axes[0].annotate(f"{pattern['Name']}\n"
                                 f"{pattern['Low']}-{pattern['High']}\n"
                                 f"{pattern['Prediction']}\n"
                                 f"{pattern['Date']}",
                                 xy=(candle_x, candle_y),
                                 xytext=(candle_x, candle_y + 0.005 * avg),
                                 fontsize=5,
                                 ha="center",
                                 fontweight='bold',
                                 color=colors[pattern['Name']],
                                 arrowprops=dict(facecolor=colors[pattern['Name']], arrowstyle='fancy,tail_width=0.75'))

            if not os.path.exists(os.getcwd() + f"/Documents/Files/{start.date()}_{end.date()}"):
                os.makedirs(os.getcwd() + f"/Documents/Files/{start.date()}_{end.date()}")
            output_path = os.path.join(os.getcwd() + f"/Documents/Files/{start.date()}_{end.date()}/Candlestick_Chart_{currency}_{start.date()}_{end.date()}.pdf")
            plt.savefig(output_path)

            plt.grid()
            plt.show()
            plt.close()
