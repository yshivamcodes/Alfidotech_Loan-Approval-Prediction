
import streamlit as st
import joblib
import numpy as np

# Load the trained model
with open('Loan Approval Prediction.pkl', 'rb') as file:

# Load the trained model
 model = joblib.load('Loan Approval Prediction.pkl')


# App title
st.title("Loan Approval Prediction App")

# User input form
st.header("Enter Applicant Details")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_amount_term = st.number_input("Loan Amount Term (in days)", min_value=0)
credit_history = st.selectbox("Credit History", ["Has History", "No History"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Encode categorical inputs manually as done during model training
def encode_inputs():
    gender_encoded = 1 if gender == "Male" else 0
    married_encoded = 1 if married == "Yes" else 0
    dependents_encoded = 3 if dependents == "3+" else int(dependents)
    education_encoded = 0 if education == "Graduate" else 1
    self_employed_encoded = 1 if self_employed == "Yes" else 0
    credit_history_encoded = 1.0 if credit_history == "Has History" else 0.0
    property_area_encoded = {"Urban": 2, "Semiurban": 1, "Rural": 0}[property_area]

    return np.array([
        [gender_encoded, married_encoded, dependents_encoded, education_encoded,
         self_employed_encoded, applicant_income, coapplicant_income,
         loan_amount, loan_amount_term, credit_history_encoded, property_area_encoded]
    ])

# Predict button
if st.button("Predict Loan Approval"):
    features = encode_inputs()
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("✅ Loan Approved!")
    else:
        st.error("❌ Loan Not Approved.")
