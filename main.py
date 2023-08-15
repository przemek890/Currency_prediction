import os
from Src.Data import get_data , create_dataframe_list_from_csv
from Src.Plot import matrix_correlaton
""""""""
if __name__ == '__main__':
    currencies = ['chfpln','eurpln','gbppln','jpypln','nokpln','usdpln']

    get_data(currencies)                                                            # Pobierz aktualne dane dotyczące kursów walut i zapisz pod ./Src/Exchange_rates

    df_list = create_dataframe_list_from_csv(os.getcwd() + '/Src/Exchange_rates')   # Utwórz listę dataframe'ów z plików csv /// zwracamy słownik postaci 'nokpln' : df_1

    for iter in df_list:                                                            # Krótko opisz dataframe'y
        for currency, df in iter.items():
            print("-------------------------------------")
            print("\n ---> Historical exchange rate",currency,':\n')
            print(df.info(),'\n')
            print(df,'\n')
            print(df.describe(),'\n')
            print("-------------------------------------")


    matrix_correlaton(df_list)                                                     # Korelacja par walut (kurs średni)










