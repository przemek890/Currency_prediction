import os
import pandas as pd
from Src.Data import get_data , create_dataframe_list_from_csv
from Src.Plot import matrix_correlaton, candle_chart
from Src.Settings import create_currencies_raport
from Src.Patterns import PatternDetector
""""""""""""""""""""""""""""""""""""""""""""""""""""""
if __name__ == '__main__':
    currencies = ['chfpln','eurpln','gbppln','jpypln','nokpln','usdpln']                       # Analizowane pary walut
    date_start = pd.to_datetime('2020-06-01')                                                  # Data startu -> default 100 dni temu
    date_end = pd.to_datetime('2020-08-01')                                                    # Data końca -> defaultowo dziś

    get_data(currencies)                                                                       # Pobierz aktualne dane dotyczące kursów walut i zapisz [raz na dzien -> dla danej daty]
    df_list = create_dataframe_list_from_csv(os.getcwd() + '/Exchange_rates',currencies)       # Utwórz listę dataframe'ów z plików csv /// zwracamy słownik postaci 'nokpln' : df

    matrix_correlaton(df_list)                                                                 # Korelacja par walut (kurs średni z otwarcia i zamkniecia)

    """Wyszukiwanie patternów w danym okresie czasowy"""
    dt = PatternDetector()
    dt.hangman(df_list)
    dt.hammer(df_list)

    create_currencies_raport(df_list)                                                          # Krótki raport o dataframe'ach
    dt.create_patterns_raport()                                                                # Krótki raport o patternach

    candle_chart(df_list,dt.get_patterns(),dt.get_colors())                                    # Wykresy świecowe w danym okresie czasu



