import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def plot_exchange_rate(currencies, df):
    min_date = df['Date'].min()
    max_date = df['Date'].max()

    num_dates = 3
    equal_spaced_dates = pd.date_range(start=min_date, end=max_date, periods=num_dates + 3)[1:-1]

    dates = [str(x).split()[0] for x in equal_spaced_dates]
    dates.append(str(min_date).split()[0])
    dates.append(str(max_date).split()[0])
    dates.sort()

    sns.set(style="darkgrid")

    fig, axs = plt.subplots(2, 3, figsize=(15, 10))
    for i, currency in enumerate(currencies):
        sns.lineplot(data=df, x='Date', y=currency, ax=axs[i // 3][i % 3])
        axs[i // 3][i % 3].set_xlabel('Date')
        axs[i // 3][i % 3].set_ylabel(f'Exchange rate ({currency}/PLN)')
        axs[i // 3][i % 3].set_title(f'Exchange rate of {currency} against PLN over the last year')
        axs[i // 3][i % 3].set_xticks(range(1, (len(dates)) * 50, 50))
        axs[i // 3][i % 3].set_xticklabels(dates, fontsize=8)

    plt.tight_layout()
    plt.savefig("./Src/Files/historical_exchange_rate.pdf")
    plt.show()


def matrix_correlaton(df):
    df.drop('Date', axis=1, inplace=True)
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title('Macierz korelacji')
    plt.savefig("./Src/Files/Correlation_matrix.pdf")
    plt.show()