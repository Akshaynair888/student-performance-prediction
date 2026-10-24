import pandas as pd

# Load the dataset
df = pd.read_csv("data/student_performance.csv")

# Display the first five rows
print("FIRST FIVE ROWS")
print(df.head())

# Check the number of rows and columns
print("\nDATASET SHAPE")
print(df.shape)

# Check column names, data types, and missing values
print("\nDATASET INFORMATION")
df.info()

# Count Pass and Fail outcomes
print("\nFINAL RESULT COUNTS")
print(df["final_result"].value_counts())

# Check for missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Check for duplicate rows
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())