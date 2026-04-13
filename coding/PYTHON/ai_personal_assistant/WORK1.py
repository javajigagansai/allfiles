import pandas as pd
import numpy as np

# Load the Excel files
df1 = pd.read_excel("locations.xlsx")
df2 = pd.read_excel("Final ATP & SSS NMNF GPs' selection 07.04.25.xlsx")

# Create a mapping from the first file: (column C, column D) -> column K
# Using column positions: C is index 2, D is index 3, K is index 10 (0-based)
mapping = df1.set_index([df1.columns[2], df1.columns[3]])[df1.columns[10]].to_dict()

# For the second file, add a temporary column with matched values from the first file
# L is index 11, M is index 12
df2['K_from_df1'] = df2.apply(
    lambda row: mapping.get((row.iloc[11], row.iloc[12]), np.nan),
    axis=1
)

# Update column K (index 10) in the second file:
# If there’s a match (K_from_df1 is not NaN), use the matched value; otherwise, keep the original value
df2.iloc[:, 10] = np.where(
    df2['K_from_df1'].notna(),
    df2['K_from_df1'],
    df2.iloc[:, 10]
)

# Drop the temporary column
df2 = df2.drop(columns=['K_from_df1'])

# Save the modified second file to a new Excel file
df2.to_excel("modified_second_file.xlsx", index=False)

print("The second Excel file has been modified and saved as 'modified_second_file.xlsx'")