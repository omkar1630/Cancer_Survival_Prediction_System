import streamlit as st
import pickle
import numpy as np

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Cancer Survival Predictor",
    page_icon="🎗️",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #E63946;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555;
    margin-bottom: 30px;
}

.stButton>button {
    width: 100%;
    background: linear-gradient(90deg,#E63946,#FF6B6B);
    color: white;
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
}

.result-box {
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Load Model
# -----------------------------
with open("decision_tree.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------
# Header
# -----------------------------
st.markdown('<p class="title">🎗️ Cancer Survival Prediction System</p>',
            unsafe_allow_html=True)

st.markdown(
    '<p class="subtitle">Predict whether a cancer patient is likely to be Alive or Deceased based on medical information.</p>',
    unsafe_allow_html=True
)

# -----------------------------
# Input Section
# -----------------------------
st.subheader("📋 Enter Patient Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 100, 40)

    gender = st.number_input(
        "Gender (Encoded Value)",
        min_value=0,
        step=1
    )

    state = st.number_input(
        "State (Encoded Value)",
        min_value=0,
        step=1
    )

    city = st.number_input(
        "City (Encoded Value)",
        min_value=0,
        step=1
    )

with col2:
    cancer_type = st.number_input(
        "Cancer Type (Encoded Value)",
        min_value=0,
        step=1
    )

    stage = st.number_input(
        "Stage (Encoded Value)",
        min_value=0,
        step=1
    )

    treatment_type = st.number_input(
        "Treatment Type (Encoded Value)",
        min_value=0,
        step=1
    )

    survival_months = st.number_input(
        "Survival Months",
        min_value=0,
        step=1
    )

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔍 Predict Survival Status"):

    features = np.array([[
        age,
        gender,
        state,
        city,
        cancer_type,
        stage,
        treatment_type,
        survival_months
    ]])

    prediction = model.predict(features)[0]

    if prediction == "Alive":
        st.markdown(
            """
            <div class="result-box" style="background:#d4edda;color:#155724;">
            ✅ Prediction: ALIVE
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div class="result-box" style="background:#f8d7da;color:#721c24;">
            ⚠️ Prediction: DECEASED
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")

st.info("""
Important:
Use the same encoded numeric values that were used during model training.
If LabelEncoder was used, apply the same mappings before prediction.
""")
