import streamlit as st
import pandas as pd
import joblib

# Page setup
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="📘",
)

st.title("Student Academic Performance Prediction")
st.write(
    "Enter the details below to explore a Pass/Fail prediction "
    "from a simple machine-learning model."
)

st.warning(
    "Educational demo only. This project uses a tiny synthetic dataset "
    "and must not be used to make real decisions about students."
)

# Load saved models
logistic_model = joblib.load("models/logistic_regression.pkl")
knn_model = joblib.load("models/knn.pkl")

# Select model
model_choice = st.selectbox(
    "Choose a model",
    ["Logistic Regression", "KNN"],
)

# Collect inputs
st.subheader("Student Information")

study_hours = st.number_input(
    "Study hours per day", min_value=0.0, max_value=24.0, value=4.0
)
attendance = st.number_input(
    "Attendance (%)", min_value=0.0, max_value=100.0, value=75.0
)
previous_score = st.number_input(
    "Previous score (%)", min_value=0.0, max_value=100.0, value=60.0
)
assignments_completed = st.number_input(
    "Assignments completed", min_value=0, max_value=100, value=6
)
sleep_hours = st.number_input(
    "Sleep hours per day", min_value=0.0, max_value=24.0, value=7.0
)

if st.button("Predict Result"):
    # Put the inputs in the same order used during training
    student_data = pd.DataFrame([{
        "study_hours": study_hours,
        "attendance": attendance,
        "previous_score": previous_score,
        "assignments_completed": assignments_completed,
        "sleep_hours": sleep_hours,
    }])

    if model_choice == "Logistic Regression":
        selected_model = logistic_model
    else:
        selected_model = knn_model

    prediction = selected_model.predict(student_data)[0]

    st.subheader("Prediction")
    st.write(f"Predicted result: **{prediction}**")

    st.caption(
        "This is a model prediction, not a guarantee of academic performance."
    )