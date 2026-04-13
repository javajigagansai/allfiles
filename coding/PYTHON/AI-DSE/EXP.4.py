import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
titanic_cleaned = pd.read_csv('cleaned_titanic.csv')
plt.figure(figsize=(10, 6))
sns.heatmap(titanic_cleaned.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()
print(titanic_cleaned.groupby('Pclass')['Survived'].mean())
print(titanic_cleaned.groupby('Sex_male')['Survived'].mean())
print(titanic_cleaned.groupby(pd.cut(titanic_cleaned['Age'], bins=[0, 12, 18, 60, 100]))['Survived'].mean())
from scipy.stats import chi2_contingency
gender_contingency = pd.crosstab(titanic_cleaned['Sex_male'], titanic_cleaned['Survived'])
chi2, p, dof, _ = chi2_contingency(gender_contingency)
print(f"Chi-Square Test: Chi2={chi2}, p-value={p}")