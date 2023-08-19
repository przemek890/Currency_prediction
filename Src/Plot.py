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
            time = datetime.now() - timedelta(days=period)
            filtered_df = df[df['Date'] >= time.strftime('%Y-%m-%d')]
            filtered_df = filtered_df.reset_index(drop=True)
            new_df[f'{currency}'] = (filtered_df['Open'] + filtered_df['Close']) / 2

    correlation_matrix = new_df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title(f'Exchange rate correlation {period} days')

    if not os.path.exists(os.getcwd() + f"/Documents/Charts/{period}-Days"):
        os.makedirs(os.getcwd() + f"/Documents/Charts/{period}-Days")

    plt.savefig(os.getcwd() + f"/Documents/Charts/{period}-Days/Correlation_matrix_{period}_days.pdf")

    plt.show()


def candle_chart(df_list,period,patterns,colors):

    for iter in df_list:
        for currency, df in iter.items():

            df['Date'] = pd.to_datetime(df['Date'])
            df.set_index('Date', inplace=True)
            time = df.index[-1] - pd.DateOffset(days=period)
            df_time = df[df.index >= time]

            fig, axes =  mpf.plot(df_time, type='candle', title=f'\n\nCandlestick Chart - {currency} - {period} days',returnfig=True)

            for pattern in patterns:
                pattern_date = pd.to_datetime(pattern['Date'])
                if pattern_date >= time:
                    pattern_index = df_time.index.get_loc(pattern_date)
                    candle_x = pattern_index # Środek świecy
                    candle_y = pattern['High']

                    avg = 0.5 * (df['High'].max() + df['Low'].min())

                    axes[0].annotate(f"{pattern['Name']}\n"
                                     f"{pattern['Low']}-{pattern['High']}\n"
                                     f"{pattern['Prediction']}\n"
                                     f"{pattern['Date']}",
                                     xy=(candle_x, candle_y),
                                     xytext=(candle_x, candle_y + 0.01 * avg),
                                     fontsize=5,
                                     ha="center",
                                     fontweight='bold',
                                     color=colors[pattern['Name']],
                                     arrowprops=dict(facecolor=colors[pattern['Name']], arrowstyle='fancy,tail_width=0.75')
                                     )
            if not os.path.exists(os.getcwd() + f"/Documents/Charts/{period}-Days"):
                os.makedirs(os.getcwd() + f"/Documents/Charts/{period}-Days")
            output_path = os.path.join(os.getcwd() + f"/Documents/Charts/{period}-Days/Candlestick_Chart_{currency}_{period}_days.pdf")
            plt.savefig(output_path)

            plt.grid()
            plt.show()

