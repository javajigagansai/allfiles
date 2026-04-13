import pandas as pd
iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print(iris.head())
print("Hello:\n",iris.head())
print("Describe:\n",iris.describe())
print("Info:\n")
iris.info()
print("shape:",iris.shape)
import matplotlib.pyplot as plt
import seaborn as sns
sns.scatterplot(data=iris,X='sepal_length',y='sepal_width',hue='species')
plt.title("scatter plot of seal dimensions")
plt.show()
sns.pairplot(iris,hue='species')
plt.show()
sns.boxplot(data=iris,orient='h')
plt.title("boxplot of features")
plt.show()