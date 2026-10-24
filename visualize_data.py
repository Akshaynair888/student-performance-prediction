import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("data/student_performance.csv")

sns.set_theme(style="whitegrid")

# Chart 1: Count of Pass and Fail
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="final_result")
plt.title("Student Final Results")
plt.xlabel("Final Result")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("result_distribution.png")
plt.show()

# Chart 2: Study hours vs previous score
plt.figure(figsize=(6, 4))
sns.scatterplot(
    data=df,
    x="study_hours",
    y="previous_score",
    hue="final_result",
    s=100
)
plt.title("Study Hours vs Previous Score")
plt.tight_layout()
plt.savefig("study_vs_score.png")
plt.show()

# Chart 3: Attendance by final result
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x="final_result", y="attendance")
plt.title("Attendance by Final Result")
plt.tight_layout()
plt.savefig("attendance_by_result.png")
plt.show()

print("Charts saved successfully.")