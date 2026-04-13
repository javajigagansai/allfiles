import pandas as pd 
df = pd.read_csv('IPL.CSV')
#Data Exploring
print("First 5 rows of the dataset:") 
print(df.head(),"\n")
print("Missing values in each column:") 
print(df.isnull().sum(),"\n")
