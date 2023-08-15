from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
""""""""
def matrix_correlaton(df_list):
    new_df = pd.DataFrame()

    for iter in df_list:
        for currency, df in iter.items():
            one_year_ago = datetime.now() - timedelta(days=365)
            filtered_df = df[df['Data'] >= one_year_ago.strftime('%Y-%m-%d')]
            filtered_df = filtered_df.reset_index(drop=True)
            new_df[f'{currency}'] = (filtered_df['Otwarcie'] + filtered_df['Zamkniecie']) / 2
    print(new_df)

    correlation_matrix = new_df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title('Exchange rate correlation')
    plt.savefig(f"{os.getcwd()}" + "/Src/Charts/Correlation_matrix.pdf")
    plt.show()