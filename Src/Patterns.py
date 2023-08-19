import pandas as pd
import os
from datetime import datetime, timedelta
""""""""""""""""""""""""""""""""""""""""""
class PatternDetector:
    def __init__(self):
        self._patterns = []
        self._colors = {"Hammer": "blue",
                       "Hangman": "green",
                       "Three_white_soldiers": "red",
                       "Three_black_ravens": "gray"}  # Kolory strzałek wzorów

    def hammer(self,df_list,start=datetime.now() - timedelta(days=100),end=datetime.now()):
        for iter in df_list:
            for currency, df in iter.items():
                df = df.copy()
                df['Date'] = pd.to_datetime(df['Date'])
                df.set_index('Date', inplace=True)
                recent_data = df[(df.index >= start) & (df.index <= end)]

                for i in range(len(recent_data)):
                    total_range = recent_data['High'][i] - recent_data['Low'][i]
                    if (
                            recent_data['Close'][i] > recent_data['Open'][i] and
                            recent_data['Close'][i] -  recent_data['Open'][i] < 0.5 * (recent_data['Open'][i] -  recent_data['Low'][i]) and
                            recent_data['High'][i] - recent_data['Close'][i] < 0.05 * total_range

                    ):
                        timestamp = recent_data.index[i]
                        date = timestamp.strftime('%Y-%m-%d')

                        self._patterns.append({
                            'Name': 'Hammer',
                            'Currency': f'{currency}',
                            'Date': date,
                            'High': recent_data['High'][i],
                            'Low': recent_data['Low'][i],
                            'Prediction': 'Hossa'
                        })
    def hangman(self,df_list,start=datetime.now() - timedelta(days=100),end=datetime.now()):
        for iter in df_list:
            for currency, df in iter.items():
                df = df.copy()
                df['Date'] = pd.to_datetime(df['Date'])
                df.set_index('Date', inplace=True)
                recent_data = df[(df.index >= start) & (df.index <= end)]

                for i in range(len(recent_data)):
                    total_range = recent_data['High'][i] - recent_data['Low'][i]
                    if (
                            recent_data['Open'][i] > recent_data['Close'][i] and
                            recent_data['Open'][i] -  recent_data['Close'][i] < 0.75 * (recent_data['Open'][i] -  recent_data['Low'][i]) and
                            recent_data['High'][i] - recent_data['Close'][i] < 0.1 * total_range

                    ):
                        timestamp = recent_data.index[i]
                        date = timestamp.strftime('%Y-%m-%d')

                        self._patterns.append({
                            'Name': 'Hangman',
                            'Currency': f'{currency}',
                            'Date': date,
                            'High': recent_data['High'][i],
                            'Low': recent_data['Low'][i],
                            'Prediction': 'Bessa'
                        })

# TODO:
    def three_white_soldiers(self,df_list,start=datetime.now() - timedelta(days=100),end=datetime.now()):
        for iter in df_list:
            for currency, df in iter.items():
                df = df.copy()
                df['Date'] = pd.to_datetime(df['Date'])
                df.set_index('Date', inplace=True)
                recent_data = df[(df.index >= start) & (df.index <= end)]

                for i in range(2, len(recent_data) - 2):
                    if (
                            recent_data['Open'][i-2] <  recent_data['Close'][i-2] and
                            recent_data['Open'][i-1] < recent_data['Close'][i-1] and
                            recent_data['Open'][i] < recent_data['Close'][i] and

                            recent_data['Low'][i-1] > recent_data['Open'][i-2] and
                            recent_data['Low'][i] > recent_data['Open'][i-1] and
                            recent_data['High'][i-2] < recent_data['Close'][i-1] and
                            recent_data['High'][i-1] < recent_data['Close'][i]
                    ):
                        i = i + 3  # Przeskocz o 3 świece do przodu
                        timestamp = recent_data.index[i]
                        date = timestamp.strftime('%Y-%m-%d')

                        self._patterns.append({
                            'Name': 'Three_white_soldiers',
                            'Currency': f'{currency}',
                            'Date': date,
                            'High': recent_data['High'][i],
                            'Low': recent_data['Low'][i],
                            'Prediction': 'Hossa'
                        })
# TODO:
    def three_black_ravens(self,df_list,start=datetime.now() - timedelta(days=100),end=datetime.now()):
        for iter in df_list:
            for currency, df in iter.items():
                df = df.copy()
                df['Date'] = pd.to_datetime(df['Date'])
                df.set_index('Date', inplace=True)
                recent_data = df[(df.index >= start) & (df.index <= end)]

                for i in range(2, len(recent_data) - 2):
                    if (
                            recent_data['Open'][i-2] >  recent_data['Close'][i-2] and
                            recent_data['Open'][i-1] > recent_data['Close'][i-1] and
                            recent_data['Open'][i] > recent_data['Close'][i] and

                            recent_data['Low'][i-1] > recent_data['Close'][i] and
                            recent_data['Low'][i-2] > recent_data['Close'][i-1] and

                            recent_data['High'][i-1] < recent_data['Open'][i-2] and
                            recent_data['High'][i] < recent_data['Open'][i-1]
                    ):
                        i = i + 3 # Przeskocz o 3 świece do przodu
                        timestamp = recent_data.index[i]
                        date = timestamp.strftime('%Y-%m-%d')

                        self._patterns.append({
                            'Name': 'Three_black_ravens',
                            'Currency': f'{currency}',
                            'Date': date,
                            'High': recent_data['High'][i],
                            'Low': recent_data['Low'][i],
                            'Prediction': 'Bessa'
                        })

    def create_patterns_raport(self):
        with open(os.getcwd() + '/Documents/Raports/patterns.txt', 'w') as report_file:
            for iter in self._patterns:
                report_file.write("-------------------------------------\n")
                for key, value in iter.items():
                    report_file.write(str(value) + '\n')
                report_file.write("-------------------------------------\n")

    def get_patterns(self):
        return self._patterns
    def get_colors(self):
        return self._colors


    ######################

