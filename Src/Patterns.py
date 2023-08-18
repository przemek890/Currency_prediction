import pandas as pd

def detect_head_and_shoulders(df_list,period):
    patterns = []

    for iter in df_list:
        for currency, df in iter.items():
            df['Date'] = pd.to_datetime(df['Date'])
            df.set_index('Date', inplace=True)
            recent_data = df.tail(period)
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

    return patterns