Student Academic Performance Prediction

Project Overview

This project uses machine learning to predict whether a student is likely to pass or fail based on study-related features. It compares Logistic Regression and K-Nearest Neighbors (KNN) classifiers and provides a simple interactive interface using Streamlit.

Objectives

- Explore and analyse the dataset.
- Check for missing values and duplicate records.
- Visualise patterns in student performance.
- Train and compare two classification models.
- Evaluate models using accuracy, precision, recall, F1-score, and confusion matrices.
- Allow users to enter student information and view a prediction.

Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn
- Matplotlib and Seaborn
- Streamlit
- Joblib

Dataset

The dataset contains 20 records and six columns:

- "study_hours": Daily study hours
- "attendance": Attendance percentage
- "previous_score": Previous academic score
- "assignments_completed": Number of completed assignments
- "sleep_hours": Daily sleep hours
- "final_result": Pass or Fail

The dataset is small and should be treated as a demonstration dataset, not as representative of all students. Its source and whether the records are synthetic must be stated accurately.

Project Structure

student-performance-prediction/
├── data/
│   └── student_performance.csv
├── models/
│   ├── knn.pkl
│   └── logistic_regression.pkl
├── explore_data.py
├── visualize_data.py
├── train_model.py
├── app.py
├── README.md
└── requirements.txt

How to Run

1. Install Python 3.
2. Install dependencies:
   "pip install -r requirements.txt"
3. Run the data exploration script:
   "python explore_data.py"
4. Generate visualisations:
   "python visualize_data.py"
5. Train and save the models:
   "python train_model.py"
6. Launch the application:
   "streamlit run app.py"

Model Evaluation

Both Logistic Regression and KNN were trained using a train/test split and evaluated with classification metrics and confusion matrices.

The current dataset contains only 20 records, so the test set is very small. The resulting metrics can change significantly with a different split and should not be interpreted as reliable real-world performance.

Add the final measured results for both models after verifying the complete terminal output.

Limitations

- The dataset is very small.
- Predictions depend on the quality and representativeness of the data.
- The model may not generalise to students from different backgrounds or educational settings.
- A prediction is not a guarantee of academic performance and must not be used as the sole basis for real educational decisions.

AI Assistance Disclosure

AI assistance was used during development to help understand the task, structure the implementation, and troubleshoot code. The submitted code and results were reviewed and tested by the candidate.

Author

Akshay A Nair