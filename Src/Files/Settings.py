import os
def create_raport(df_list):
    with open(os.getcwd() + '/Src/Documents/report.txt', 'w') as report_file:
        for iter in df_list:  # Przechodzenie przez listę DataFrame'ów
            for currency, df in iter.items():  # Iteracja po słownikach zawierających DataFrame'y
                report_file.write("-------------------------------------\n")
                report_file.write("\n ---> Historical exchange rate " + currency + ':\n\n')

                df_str = str(df)
                report_file.write(df_str + '\n\n')

                df_desc = df.describe()
                report_file.write(str(df_desc) + '\n\n')

                report_file.write("-------------------------------------\n")