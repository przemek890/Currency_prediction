import pandas as pd
from datetime import datetime, timedelta
import requests
""""""

def get_data(currencies):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)

    df = pd.DataFrame()

    for currency in currencies:
        url = f'http://api.nbp.pl/api/exchangerates/rates/A/{currency}/{start_date.strftime("%Y-%m-%d")}/{end_date.strftime("%Y-%m-%d")}/'
        response = requests.get(url)
        data = response.json()
        rates = data['rates']
        temp_df = pd.DataFrame(rates)
        temp_df['currency'] = currency
        df = pd.concat([df, temp_df])

    df = df.pivot(index='effectiveDate', columns='currency', values='mid')
    df.reset_index(inplace=True)
    df = df.drop(index=0)
    df.columns = ['Date',*currencies]

    return df
