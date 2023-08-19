import os
import re
def create_raport(df_list):
    with open(os.getcwd() + '/Documents/Raports/currencies.txt', 'w') as report_file:
        for iter in df_list:
            for currency, df in iter.items():
                report_file.write("-------------------------------------\n")
                report_file.write("\n ---> Historical exchange rate " + currency + ':\n\n')

                df_str = str(df)
                report_file.write(df_str + '\n\n')

                df_desc = df.describe()
                report_file.write(str(df_desc) + '\n\n')

                report_file.write("-------------------------------------\n")

def list_patterns(patterns):
    with open(os.getcwd() + '/Documents/Raports/patterns.txt', 'w') as report_file:
        for iter in patterns:
            report_file.write("-------------------------------------\n")
            for key,value in iter.items():
                report_file.write(str(value) + '\n')
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