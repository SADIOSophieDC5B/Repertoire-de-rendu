import pandas as pd

df = pd.read_csv("C:\\Users\\33789\\Desktop\\Python\\exo3\\fichier2_csv.csv")

df = df.dropna(subset=['Period', 'Data_value', 'Series_title_2'])


df = df[['Period', 'Data_value', 'Series_title_2']]

df = df[df['Series_title_2'].isin(['Credit', 'Debit', 'Services'])]


df = df.reset_index()


df['id'] = df.index + 1


df.to_csv('result.csv', index=False)



