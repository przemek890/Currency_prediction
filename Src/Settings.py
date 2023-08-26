import os
import re
from datetime import datetime, timedelta
import pandas as pd
def create_currencies_raport(df_list,start=datetime.now() - timedelta(days=100),end=datetime.now()):
    if not os.path.exists(os.getcwd() + f"/Documents/Files/{start.date()}_{end.date()}"):
        os.makedirs(os.getcwd() + f"/Documents/Files/{start.date()}_{end.date()}")
    elif os.path.exists(os.getcwd() + f"/Documents/Files/{start.date()}_{end.date()}/currencies_description.txt"):
        os.remove(os.getcwd() + f"/Documents/Files/{start.date()}_{end.date()}/currencies_description.txt")

    for iter in df_list:
        with open(os.getcwd() + f'/Documents/Files/{start.date()}_{end.date()}/currencies_description.txt', 'a+') as report_file:
                for currency, df in iter.items():
                    df = df.copy()
                    df['Date'] = pd.to_datetime(df['Date'])
                    df.set_index('Date', inplace=True)
                    recent_data = df[(df.index >= start) & (df.index <= end)]

                    report_file.write("-------------------------------------\n")
                    report_file.write("\n ---> Historical exchange rate " + currency + ':\n\n')

                    df_str = str(recent_data)
                    report_file.write(df_str + '\n\n')

                    df_desc = recent_data.describe()
                    report_file.write(str(df_desc) + '\n\n')

                    report_file.write("-------------------------------------\n")

def remove_all_files(folder_path,pattern):
    files = os.listdir(folder_path)
    for file_name in files:
        if re.search(pattern, file_name):
            file_path = os.path.join(folder_path, file_name)
            try:
                os.remove(file_path)
                print(f"File deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")