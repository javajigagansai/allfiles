import pandas as pd
import sklearn
titanic = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
titanic['Age'].fillna(titanic['Age'].median(), inplace=True)
titanic['Embarked'].fillna(titanic['Embarked'].mode()[0], inplace=True)
titanic = pd.get_dummies(titanic, columns=['Sex','Embarked'], drop_first=True)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
titanic[['Age', 'Fare']] = scaler.fit_transform(titanic[['Age', 'Fare']])
titanic.to_csv('cleaned_titanic.csv', index=False)
print("Cleaned dataset saved to 'cleaned_titanic.csv")

