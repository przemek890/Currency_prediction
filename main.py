from Src.Data import get_data
from Src.Charts import plot_exchange_rate
""""""""
if __name__ == '__main__':
    currencies = ['NOK', 'USD', 'EUR', 'CHF', 'GBP']
    df = get_data(currencies)
    print(df.describe(),"\n\n",df)
    plot_exchange_rate(currencies,df)



