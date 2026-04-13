import pandas as pd
df = pd.read_csv('IPL.CSV')
print(df.head())
print(df.columns)
df.columns = ['Teams', 'jersey_colour', 'no_of_cups', 'no_of_orange_caps']
df['no_of_cups'] = pd.to_numeric(df['no_of_cups'])
df['no_of_orange_caps'] = pd.to_numeric(df['no_of_orange_caps'])
