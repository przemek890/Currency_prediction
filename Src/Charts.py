import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

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
    for currency in currencies:
        sns.lineplot(data=df, x='Date', y=currency)
        plt.xlabel('Date')
        plt.ylabel(f'Exchange rate ({currency}/PLN)')
        plt.title(f'Exchange rate of {currency} against PLN over the last year')
        plt.xticks(range(1,(len(dates)) * 50,50),dates)
        plt.show()

