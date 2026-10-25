Student Academic Performance Prediction

Verveox Technologies — AI/ML Trainee Assessment

1. Objective

The objective of this project is to develop a basic machine learning system that predicts whether a student is likely to pass or fail based on study-related and academic indicators.

This is a demonstration project intended to explore a machine learning workflow. Its predictions should not be used as the sole basis for real educational decisions.

2. Dataset

The project uses a dataset containing 20 records and six columns:

- "study_hours"
- "attendance"
- "previous_score"
- "assignments_completed"
- "sleep_hours"
- "final_result"

The target variable is "final_result", with the classes Pass and Fail. The dataset contains 11 Pass records and 9 Fail records.

Dataset source: [Replace this line with the actual source of your dataset.] If the dataset was generated synthetically, state that explicitly and describe how the labels were generated.

3. Data Exploration and Preprocessing

Exploratory analysis was performed using Pandas. The dataset was inspected for its dimensions, column data types, missing values, duplicate records, summary statistics, invalid numeric values, and unexpected target labels.

The inspection found 20 records, no missing values, no duplicate rows, and no detected invalid values under the checks implemented in the analysis script.

The target variable was separated from the input features before model training. Feature scaling was used within the model pipelines, particularly for K-Nearest Neighbors.

4. Exploratory Data Analysis

Three visualizations were created:

1. Student final results: compares the number of Pass and Fail records.
2. Study hours versus previous score: illustrates the relationship between these two variables and the observed outcomes.
3. Attendance by final result: compares attendance distributions for the Pass and Fail groups.

In this small dataset, Pass records generally show higher attendance and previous scores. These patterns are descriptive observations and do not establish causation or guarantee future outcomes.

5. Models and Methodology

Two classification algorithms were implemented:

- Logistic Regression: a baseline classification algorithm that estimates class probabilities using a learned relationship between the input features and the target.
- K-Nearest Neighbors (KNN): predicts a class using the labels of nearby training examples. Feature scaling is important because the algorithm relies on distances between observations.

The dataset was divided into training and test subsets using a reproducible split. Both models were evaluated on the held-out test subset. Preprocessing was fitted through the training workflow to reduce the risk of data leakage.

6. Evaluation Results

The following results were recorded for the current train/test split.

| Metric | Logistic Regression | KNN |
| --- | ---: | ---: |
| Accuracy | 0.833 | 0.833 |
| Precision | 0.750 | 0.750 |
| Recall | 1.000 | 1.000 |
| F1-score | 0.857 | 0.857 |

Both models produced the same confusion matrix:

[[2, 1],
 [0, 3]]

The label order is Fail, Pass, with rows representing actual classes and columns representing predicted classes.

Of the six test records, five were classified correctly. One actual Fail case was incorrectly predicted as Pass.

The two models achieved identical results on this split. These results do not establish that either model is superior.

7. Model Selection

Based on this evaluation, neither model demonstrated a performance advantage over the other. A reliable selection would require more representative data and stronger validation rather than relying solely on this small test set.

8. Prediction Interface

A Streamlit interface was implemented in "app.py". It accepts the required input features and displays a Pass or Fail prediction using a saved model pipeline.

The interface was tested with two different inputs. The predictions are model estimates, not guarantees of actual student outcomes.

9. Limitations

- The dataset contains only 20 records, and the test set contains only six records.
- Evaluation metrics are highly sensitive to the particular train/test split.
- If the dataset is synthetic, its patterns may not reflect real student outcomes.
- The model may not generalize to students from different backgrounds or educational settings.
- No external validation on a larger, independent dataset was performed.
- Predictions should support further investigation rather than determine educational decisions on their own.

10. Future Improvements

- Evaluate on a larger, representative dataset with a clearly documented source.
- Use cross-validation on training data to assess model stability.
- Test generalization on an independent dataset.
- Investigate class-specific errors and appropriate evaluation measures.
- Improve input validation and provide clear guidance on responsible interpretation.

11. AI Assistance Disclosure

ChatGPT was used as a supporting tool to help understand the assessment requirements, structure the implementation, interpret evaluation results, and prepare documentation. The project was developed and tested in VS Code, and the implementation and results should be reviewed and explained by the candidate. Any external resources or code used should be acknowledged accurately.

12. Conclusion

This project demonstrates a basic end-to-end machine learning workflow, including dataset inspection, exploratory visualization, classification using Logistic Regression and KNN, model evaluation, and a Streamlit prediction interface.

Both models achieved an accuracy of 0.833 on the current test split. Because the dataset and test set are very small, these results should be treated as preliminary demonstration results rather than evidence of real-world predictive performance.