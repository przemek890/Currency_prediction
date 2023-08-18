import os
from Src.Data import get_data , create_dataframe_list_from_csv
from Src.Plot import matrix_correlaton, candle_chart
from Src.Settings import create_raport , list_patterns
from Src.Patterns import detect_head_and_shoulders
""""""""""""""""""""""""""""""""""""""""""""""""""""""
if __name__ == '__main__':
    currencies = ['chfpln','eurpln','gbppln','jpypln','nokpln','usdpln']            # Analizowane pary walut
    colors = {"Head and Shoulders": "red"}                                          # Kolory strzałek wzorów
    period = 100                                                                    # Ilość dni wstecz podlegająca analizie

    get_data(currencies)                                                            # Pobierz aktualne dane dotyczące kursów walut i zapisz pod ./Src/Exchange_rates

    df_list = create_dataframe_list_from_csv(os.getcwd() + '/Exchange_rates')       # Utwórz listę dataframe'ów z plików csv /// zwracamy słownik postaci 'nokpln' : df_1

    create_raport(df_list)                                                          # Krótki raport o dataframe'ach

    matrix_correlaton(df_list,period)                                               # Korelacja par walut (kurs średni z otwarcia i zamkniecia)

    """"""""""""""""""""""""""""""""""""

    patterns = detect_head_and_shoulders(df_list,period)                            # Wyszukiwanie patternów w danym okresie czasowy
    candle_chart(df_list,period,patterns,colors)                                    # Wykresy świecowe w danym okresie czasu

    list_patterns(patterns)                                                         # Raport o wykrytych patternach




