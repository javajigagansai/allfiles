import pandas as pd

# Load the Excel files (replace filenames with your actual file paths)
df1 = pd.read_excel("locations.xlsx")  # First Excel file
df2 = pd.read_excel("Final ATP & SSS NMNF GPs' selection 07.04.25.xlsx")  # Second Excel file

# Create a set of tuples from the first Excel file's columns C (index 2) and D (index 3)
# Convert to strings to handle mixed data types consistently
matches = set((str(row[2]), str(row[3])) for index, row in df1.iterrows())

# Iterate through the second Excel file and update column K (index 10) where matches occur
for index, row in df2.iterrows():
    # Check if the pair (K, M) from the current row matches any pair from the first file
    if (str(row[10]), str(row[12])) in matches:
        df2.at[index, df2.columns[10]] = "NMNF"

# Save the modified second Excel file to a new file
df2.to_excel("modified_second_file.xlsx", index=False)

print("The second Excel file has been modified and saved as 'modified_second_file.xlsx'")