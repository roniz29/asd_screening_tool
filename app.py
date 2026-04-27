import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(page_title="ASD Screening Tool", page_icon="🧩", layout="centered")

# --- LOAD MODEL ---
@st.cache_resource
def load_model():
    model = joblib.load('model.pkl')
    return model

model = load_model()

# --- TITLE ---
st.title("🧩 ASD Screening Support Tool")
st.markdown("**Bachelor Thesis Artifact** — Ronizza Mangaya-ay | Noroff University College 2025")

# --- DISCLAIMER ---
st.warning("""
⚠️ **Disclaimer:** This tool is for research and educational purposes only.
It does not constitute a clinical diagnosis.
A positive result should always be followed by evaluation from a trained specialist.
""")

st.divider()

# --- DEMOGRAPHIC QUESTIONS ---
st.subheader("👤 Step 1: Demographic Information")

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=4, max_value=100, value=25)
    jaundice = st.selectbox("Born with jaundice?", ["No", "Yes"])
with col2:
    gender = st.selectbox("Gender", ["Male", "Female"])
    family_asd = st.selectbox("Family member with ASD?", ["No", "Yes"])

st.divider()

# --- AQ-10 QUESTIONS ---
st.subheader("📋 Step 2: AQ-10 Screening Questions")
st.markdown("Select **1 = Yes / Sometimes** or **0 = No / Rarely** for each question.")

questions = [
    "A1 — I often notice small sounds when others do not",
    "A2 — I usually concentrate more on the whole picture rather than small details",
    "A3 — I find it easy to do more than one thing at once",
    "A4 — If there is an interruption, I can switch back very quickly",
    "A5 — I find it easy to read between the lines when someone is talking to me",
    "A6 — I know how to tell if someone listening to me is getting bored",
    "A7 — When reading a story, I find it difficult to work out characters' intentions",
    "A8 — I like to collect information about categories of things",
    "A9 — I find it easy to work out what someone is thinking or feeling",
    "A10 — I find it difficult to work out people's intentions",
]

scores = []
for i, q in enumerate(questions):
    score = st.radio(q, [0, 1], horizontal=True, key=f"q{i}")
    scores.append(score)

st.divider()

# --- CALCULATE BUTTON ---
if st.button("🔍 Calculate Screening Result", use_container_width=True):

    # --- PREPARE INPUT FOR MODEL ---
    gender_encoded = 1 if gender == "Male" else 0
    jaundice_encoded = 1 if jaundice == "Yes" else 0
    family_asd_encoded = 1 if family_asd == "Yes" else 0

    # Build feature array matching training data
    # 10 AQ scores + age + gender + jaundice + family history
    input_features = scores + [age, gender_encoded, jaundice_encoded, family_asd_encoded]
    input_array = np.array(input_features).reshape(1, -1)

    # --- GET PREDICTION ---
    prediction = model.predict(input_array)[0]
    prediction_proba = model.predict_proba(input_array)[0]

    # --- AQ SCORE ---
    aq_score = sum(scores)

    # --- SHOW SCORE ---
    st.subheader("📊 AQ-10 Score")
    st.metric("Total Score", f"{aq_score} / 10")
    st.progress(aq_score / 10)

    st.divider()

    # --- SHOW MODEL RESULT ---
    st.subheader("🤖 Model Prediction")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Model Result", "ASD Risk" if prediction == 1 else "Low Risk")
    with col2:
        confidence = prediction_proba[1] if prediction == 1 else prediction_proba[0]
        st.metric("Confidence", f"{confidence:.1%}")

    if prediction == 1:
        st.error("🔴 **Result: Elevated Risk Indicated**")
        st.markdown("""
        The Decision Tree model predicts **elevated ASD risk** based on your inputs.
        This does **not** mean a diagnosis. Please consult a trained specialist.
        """)
    else:
        st.success("🟢 **Result: Low Risk Indicated**")
        st.markdown("""
        The Decision Tree model predicts **low ASD risk** based on your inputs.
        This does **not** rule out ASD. If you have concerns, please consult a specialist.
        """)

    st.divider()

    # --- FEATURE SUMMARY TABLE ---
    st.subheader("📋 Your Input Summary")
    summary_data = {
        "Feature": ["Age", "Gender", "Jaundice", "Family ASD",
                    "A1", "A2", "A3", "A4", "A5",
                    "A6", "A7", "A8", "A9", "A10"],
        "Your Answer": [age, gender, jaundice, family_asd] + scores
    }
    df_summary = pd.DataFrame(summary_data)
    st.dataframe(df_summary, use_container_width=True, hide_index=True)

    st.divider()

    # --- MODEL EXPLANATION ---
    st.subheader("🌳 How This Tool Works")
    st.markdown("""
    This tool uses a **Decision Tree model** trained on the UCI ASD Screening Dataset
    (5,021 records across children, adolescents, and adults).

    The Decision Tree was selected as the best model because:
    - ✅ Highest **PR-AUC of 0.3369** for minority class detection
    - ✅ **89× faster** than the deep learning MLP model
    - ✅ **Transparent and interpretable** decision rules
    - ✅ Most **stable performance** across all age groups
    """)

    st.divider()

    # --- LIMITATIONS ---
    st.subheader("⚠️ Limitations")
    st.markdown("""
    - This tool uses **offline experimental data** and has not been clinically validated
    - The dataset has a **class imbalance** of approximately 4:1 (non-ASD to ASD)
    - Results may **not generalise** across all cultural or geographic populations
    - This tool is a **screening support tool only** — not a diagnostic instrument
    - A positive result must always be followed by **specialist evaluation**
    """)

st.divider()

# --- ABOUT SECTION ---
st.subheader("📚 About This Research")
st.markdown("""
**Thesis Title:** Machine Learning and Deep Learning Approaches for Early Detection of Autism Spectrum Disorder

**Author:** Ronizza Mangaya-ay

**Institution:** Noroff University College, Norway

**Supervisor:** Bertram Haskins

**Year:** 2025

**Dataset:** UCI ASD Screening Dataset — 5,021 records across 3 age groups

**Models Evaluated:** Logistic Regression, Decision Tree, SVM, Random Forest, XGBoost, MLP

**Best Model:** Decision Tree (PR-AUC: 0.3369, Nested CV F1: 0.2513)
""")

st.markdown("---")
st.caption("🔗 Source code: https://github.com/roniz29/asd-screening-tool")
st.caption("For research and educational purposes only. Not a clinical diagnostic tool.")