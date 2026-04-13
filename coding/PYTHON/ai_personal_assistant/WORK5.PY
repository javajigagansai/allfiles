import pandas as pd

# File paths (update with your actual file names or paths)
file2_path = 'locations.xlsx'
file1_path ="Final ATP & SSS NMNF GPs' selection 07.04.25.xlsx"

# Read both Excel files
file1 = pd.read_excel(file1_path)
file2 = pd.read_excel(file2_path)

# Loop through each row by index
for i in range(min(len(file1), len(file2))):
    val_file1_c = file1.at[i, 'C']
    val_file1_d = file1.at[i, 'D']
    val_file2_l = file2.at[i, 'L']
    val_file2_m = file2.at[i, 'M']

    # Check if values match
    if val_file1_c == val_file2_l and val_file1_d == val_file2_m:
        file2.at[i, 'K'] = file1.at[i, 'K']  # Copy K from file1 to file2

# Save the modified File2
file2.to_excel('file2_updated.xlsx', index=False)

print("✅ Done: file2_updated.xlsx created with matched K values.")
