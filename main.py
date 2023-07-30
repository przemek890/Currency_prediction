from Src.Data import get_data
from Src.Charts import plot_exchange_rate, matrix_correlaton
""""""""
if __name__ == '__main__':
    currencies = ['CHF','EUR','GBP','JPY','NOK','USD',]
    df = get_data(currencies)
    print(df.describe(),"\n\n",df)

    plot_exchange_rate(currencies,df)
    matrix_correlaton(df.copy())



