import os
import sys
import pandas as pd
from Src.Data import get_data , create_dataframe_list_from_csv
from Src.Plot import candle_chart
from Src.Settings import create_currencies_raport
from Src.Patterns import PatternDetector
""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""
if len(sys.argv) >= 4:
    currencies = []
    program_path = sys.argv[0]
    currency = ''.join(map(str, sys.argv[1]))
    currencies.append(currency)
    print(currencies)
    date_start = pd.to_datetime(sys.argv[2])
    date_end = pd.to_datetime(sys.argv[3])

    print("Program path:", program_path)
    print("Currency:", currencies)
    print("Date Start:", date_start)
    print("Date End:", date_end)
else:
    print("Brak wystarczającej liczby argumentów.")
    exit(0)
""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""

get_data(currencies)
df_list = create_dataframe_list_from_csv(os.getcwd() + "/Exchange_rates",currencies)
create_currencies_raport(df_list)

"""Wyszukiwanie patternów w danym okresie czasowy"""
dt = PatternDetector()
dt.hangman(df_list,date_start,date_end)
dt.hammer(df_list,date_start,date_end)
dt.create_patterns_raport()

candle_chart(df_list,dt.get_patterns(),dt.get_colors(),date_start,date_end)

currencies.clear()


