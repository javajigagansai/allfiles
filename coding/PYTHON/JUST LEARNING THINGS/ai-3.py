import pandas as pd
iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print(iris.head())
print("Head:\n", iris.head())
print("Describe:\n", iris.describe())
print("Info:\n")
iris.info()
print("Shape:", iris.shape)
import matplotlib.pyplot as plt
import seaborn as sns
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species')
plt.title("Scatter Plot of Sepal Dimensions")
plt.show()
sns.pairplot(iris, hue='species')
plt.show()
sns.boxplot(data=iris, orient='h')
plt.title("Boxplot of Features")
plt.show()