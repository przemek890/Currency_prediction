import pandas as pd
from datetime import datetime, timedelta

# TODO: Sprawdzić czy dobrze napisany if
def detect_head_and_shoulders(df_list,patterns,start=datetime.now() - timedelta(days=14),end=datetime.now()):
    for iter in df_list:
        for currency, df in iter.items():
            df = df.copy()
            df['Date'] = pd.to_datetime(df['Date'])
            df.set_index('Date', inplace=True)
            time = end - start
            recent_data = df[df.index >= time]

            for i in range(2, len(recent_data) - 2):
                if (
                        recent_data['High'][i] > recent_data['High'][i - 1] and
                        recent_data['High'][i] > recent_data['High'][i + 1] and
                        recent_data['Low'][i] > recent_data['Low'][i - 1] and
                        recent_data['Low'][i] > recent_data['Low'][i + 1] and
                        recent_data['Low'][i - 1] < recent_data['Low'][i - 2] and
                        recent_data['Low'][i + 1] < recent_data['Low'][i + 2]
                ):

                    timestamp = recent_data.index[i]
                    date = timestamp.strftime('%Y-%m-%d')

                    patterns.append({
                        'Name': 'Head and Shoulders',
                        'Currency': f'{currency}',
                        'Date': date,
                        'High': recent_data['High'][i],
                        'Low': recent_data['Low'][i],
                        'Prediction': 'Bessa'
                    })
def detect_hammer(df_list, patterns,start=datetime.now() - timedelta(days=14),end=datetime.now()):
    for iter in df_list:
        for currency, df in iter.items():
            df = df.copy()
            df['Date'] = pd.to_datetime(df['Date'])
            df.set_index('Date', inplace=True)
            time = end - start
            recent_data = df[df.index >= time]

            for i in range(2, len(recent_data) - 2):
                total_range = recent_data['High'][i] - recent_data['Low'][i]
                if (
                        recent_data['Close'][i] > recent_data['Open'][i] and
                        recent_data['Close'][i] -  recent_data['Open'][i] < 0.5 * (recent_data['Open'][i] -  recent_data['Low'][i]) and
                        recent_data['High'][i] - recent_data['Close'][i] < 0.05 * total_range

                ):
                    timestamp = recent_data.index[i]
                    date = timestamp.strftime('%Y-%m-%d')

                    patterns.append({
                        'Name': 'Hammer',
                        'Currency': f'{currency}',
                        'Date': date,
                        'High': recent_data['High'][i],
                        'Low': recent_data['Low'][i],
                        'Prediction': 'Hossa'
                    })
def detect_hangman(df_list, patterns,start=datetime.now() - timedelta(days=14),end=datetime.now()):
    for iter in df_list:
        for currency, df in iter.items():
            df = df.copy()
            df['Date'] = pd.to_datetime(df['Date'])
            df.set_index('Date', inplace=True)
            time = end - start
            recent_data = df[df.index >= time]

            for i in range(2, len(recent_data) - 2):
                total_range = recent_data['High'][i] - recent_data['Low'][i]
                if (
                        recent_data['Open'][i] > recent_data['Close'][i] and
                        recent_data['Open'][i] -  recent_data['Close'][i] < 0.5 * (recent_data['Open'][i] -  recent_data['Low'][i]) and
                        recent_data['High'][i] - recent_data['Close'][i] < 0.1 * total_range

                ):
                    timestamp = recent_data.index[i]
                    date = timestamp.strftime('%Y-%m-%d')

                    patterns.append({
                        'Name': 'Hangman',
                        'Currency': f'{currency}',
                        'Date': date,
                        'High': recent_data['High'][i],
                        'Low': recent_data['Low'][i],
                        'Prediction': 'Bessa'
                    })

