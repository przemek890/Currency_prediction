import os
import pandas as pd
from Src.Data import get_data , create_dataframe_list_from_csv
from Src.Plot import matrix_correlaton, candle_chart
from Src.Settings import create_raport , list_patterns
from Src.Patterns import detect_head_and_shoulders, detect_hammer, detect_hangman
""""""""""""""""""""""""""""""""""""""""""""""""""""""
if __name__ == '__main__':
    currencies = ['chfpln','eurpln','gbppln','jpypln','nokpln','usdpln']            # Analizowane pary walut
    colors = {"Head and Shoulders": "red","Hammer": "blue","Hangman": "green"}      # Kolory strzałek wzorów
    date_start = pd.to_datetime('2023-05-01')                                       # Data startu -> default 100 dni temu
    date_end = pd.to_datetime('2023-08-01')                                         # Data końca -> defaultowo dziś
    patterns = []                                                                   # Znalezione patterny

    get_data(currencies)                                                            # Pobierz aktualne dane dotyczące kursów walut i zapisz [raz na dzien -> dla danej daty]
    df_list = create_dataframe_list_from_csv(os.getcwd() + '/Exchange_rates')       # Utwórz listę dataframe'ów z plików csv /// zwracamy słownik postaci 'nokpln' : df_1
    create_raport(df_list)                                                          # Krótki raport o dataframe'ach
    matrix_correlaton(df_list)                                                      # Korelacja par walut (kurs średni z otwarcia i zamkniecia)


   # detect_head_and_shoulders(df_list,period,patterns)                             # Wyszukiwanie patternów w danym okresie czasowy
   #  detect_hammer(df_list,patterns,pd.to_datetime('2023-05-01'))
   #  detect_hangman(df_list,patterns,pd.to_datetime('2023-05-01'))

    candle_chart(df_list,patterns,colors)                                           # Wykresy świecowe w danym okresie czasu
    list_patterns(patterns)                                                         # Raport o wykrytych patternach




