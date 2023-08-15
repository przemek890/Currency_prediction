import pandas as pd
import requests
import os
""""""""
def get_data(currencies):
    for currency in currencies:
        csv_url = f"https://stooq.pl/q/d/l/?s={currency}&i=d"  # Adres URL do pobrania pliku CSV

        response = requests.get(csv_url)  # Wykonaj żądanie GET i pobierz zawartość pliku CSV
        csv_content = response.content

        file_path = os.path.join(os.getcwd(), f"Src/Exchange_rates/{currency}.csv")  # Zapisz zawartość pliku CSV w katalogu projektu
        with open(file_path, "wb") as csv_file:
            csv_file.write(csv_content)
        print(f"Plik CSV został pomyślnie pobrany i zapisany jako {currency}.csv")
def create_dataframe_list_from_csv(path):
    dataframe_list = []                             # zwracamy słownik postaci 'nokpln' : df itp...

    for filename in os.listdir(path):
        if filename.endswith(".csv"):
            file_path = os.path.join(path, filename)
            df = pd.read_csv(file_path)
            word = {os.path.splitext(filename)[0] : df}
            dataframe_list.append(word)

    return dataframe_list