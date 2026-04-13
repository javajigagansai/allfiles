import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
data = pd.read_csv('IPL.csv')

# Set the style
sns.set(style="whitegrid")
# Plot 1: Number of Cups
plt.figure(figsize=(10, 6))
sns.barplot(y='no.of cups', x3='teams', data=data, palette='viridis')
plt.title('Number of IPL Cups by Team')
plt.xlabel('No. of Cups')
plt.ylabel('Teams')
plt.tight_layout()
plt.show()

# Plot 2: Orange Cups
plt.figure(figsize=(10, 6))
sns.barplot(x='teams',y='no.of orange cups', data=data, palette='autumn')
plt.title('Number of Orange Caps by Team')
plt.xlabel('No. of Orange Cups')
plt.ylabel('Teams')
plt.tight_layout()
plt.show()
