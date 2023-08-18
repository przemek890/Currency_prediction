import os
from Src.Files.Data import get_data , create_dataframe_list_from_csv
from Src.Files.Plot import matrix_correlaton, candle_chart
from Src.Files.Settings import create_raport
""""""""
if __name__ == '__main__':
    currencies = ['chfpln','eurpln','gbppln','jpypln','nokpln','usdpln']
    period = 100

    get_data(currencies)                                                            # Pobierz aktualne dane dotyczące kursów walut i zapisz pod ./Src/Exchange_rates

    df_list = create_dataframe_list_from_csv(os.getcwd() + '/Src/Exchange_rates')   # Utwórz listę dataframe'ów z plików csv /// zwracamy słownik postaci 'nokpln' : df_1

    create_raport(df_list)                                                          # Krótki raport o dataframe'ach

    matrix_correlaton(df_list,period)                                                # Korelacja par walut (kurs średni z otwarcia i zamkniecia)
    candle_chart(df_list,period)









