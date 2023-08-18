import os
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
