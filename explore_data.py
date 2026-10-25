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

# Display the last five rows
print("\nLAST FIVE ROWS")
print(df.tail())

# Summary statistics for numerical columns
print("\nSUMMARY STATISTICS")
print(df.describe())

# Check for invalid values
print("\nINVALID VALUES")
print("Study hours outside 0-24:", (~df["study_hours"].between(0, 24)).sum())
print("Attendance outside 0-100:", (~df["attendance"].between(0, 100)).sum())
print("Previous score outside 0-100:", (~df["previous_score"].between(0, 100)).sum())
print("Negative assignments:", (df["assignments_completed"] < 0).sum())
print("Sleep hours outside 0-24:", (~df["sleep_hours"].between(0, 24)).sum())

# Check target labels
print("\nUNEXPECTED RESULT LABELS")
print((~df["final_result"].isin(["Pass", "Fail"])).sum())