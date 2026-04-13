import pandas as pd

# Replace these with your actual file paths
file1_path = 'locations.xlsx'
file2_path = "Final ATP & SSS NMNF GPs' selection 07.04.25.xlsx"

# Load Excel files
file1 = pd.read_excel(file1_path)
file2 = pd.read_excel(file2_path)
for i in range(min(len(file1), len(file2))):
    val_c = file1.at[i, 'C']
    val_d = file1.at[i, 'D']
    val_l = file2.at[i, 'L']
    val_n = file2.at[i, 'N']

    # Check if both columns match in same row
    if val_c == val_l and val_d == val_n:
        # Copy text from File1 K to File2 K
        file2.at[i, 'K'] = file1.at[i, 'K']

file2.to_excel('file2_updated.xlsx', index=False)

print("File2 updated and saved as 'file2_updated.xlsx'")
