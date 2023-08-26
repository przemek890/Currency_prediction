import os
import sys
import pandas as pd
from Src.Data import get_data , create_dataframe_list_from_csv
from Src.Plot import matrix_correlaton, candle_chart
from Src.Settings import create_currencies_raport
from Src.Patterns import PatternDetector
""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""
if len(sys.argv) >= 4:
    program_path = sys.argv[0]
    currencies = sys.argv[1].split('_')
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

"""Wyszukiwanie patternów w danym okresie czasowy"""
dt = PatternDetector()
dt.hangman(df_list,date_start,date_end)
dt.hammer(df_list,date_start,date_end)

create_currencies_raport(df_list,date_start,date_end)
dt.create_patterns_raport(date_start,date_end)

matrix_correlaton(df_list,date_start,date_end)
candle_chart(df_list,dt.get_patterns(),dt.get_colors(),date_start,date_end)



