import pandas as pd
titanic = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
titanic['Age'].fillna(titanic['Age'].median(), inplace=True)
titanic['Embarked'].fillna(titanic['Embarked'].mode()[0], inplace=True)
# Encode categorical variables
titanic = pd.get_dummies(titanic, columns=['Sex', 'Embarked'], drop_first=True)
# Normalize numerical features
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
titanic[['Age', 'Fare']] = scaler.fit_transform(titanic[['Age', 'Fare']])
# Save cleaned dataset
titanic.to_csv('cleaned_titanic.csv', index=False)
print("Cleaned dataset saved to 'cleaned_titanic.csv'")
