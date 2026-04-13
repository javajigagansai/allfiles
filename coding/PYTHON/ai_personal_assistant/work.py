import pandas as pd

# Step 1: Load the Excel files into dataframes
df1 = pd.read_excel("locations.xlsx")
df2 = pd.read_excel("Final ATP & SSS NMNF GPs' selection 07.04.25.xlsx")

# Step 2: Perform a left join on Mandal and Panchayat names
# Using 'MNAME' and 'PNAME' from df1, and 'Mandal_Name' and 'Panchayat_Name' from df2
merged_df = pd.merge(
    df1,
    df2,
    left_on=['MNAME', 'PNAME'],
    right_on=['Mandal_Name', 'Panchayat_Name'],
    how='left'
)

# Step 3: Save the merged dataframe to a new Excel file
merged_df.to_excel("merged_locations.xlsx", index=False)

print("Files have been merged successfully into 'merged_locations.xlsx'")