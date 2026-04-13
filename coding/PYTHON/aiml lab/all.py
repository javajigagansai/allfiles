import pandas as pd
# to  load the data
ipl_df = pd.read_csv("IPL.csv")
print(ipl_df)
#to plot grapha
import matplotlib.pyplot as plt
plt.bar(ipl_df["Teams"], ipl_df["no.of cups"], color='Green')
plt.title("Number of IPL Cups by Team")
plt.ylabel("Cups Won")
plt.show()

