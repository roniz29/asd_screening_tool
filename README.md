# 🧩 ASD Screening Support Tool

**Bachelor Thesis Artifact**
Ronizza Mangaya-ay | Noroff University College | 2025

---

## About

This interactive web application was developed as the practical artifact for the bachelor thesis:

**"Machine Learning and Deep Learning Approaches for Early Detection of Autism Spectrum Disorder"**

The tool implements a Decision Tree model trained on the UCI ASD Screening Dataset (5,021 records across children, adolescents, and adults).

---

## How to Use

1. Enter demographic information (age, gender, jaundice history, family ASD history)
2. Answer the 10 AQ-10 behavioural screening questions
3. Click **Calculate Screening Result**
4. View the model prediction and AQ-10 score

---

## Technical Details

| Component | Details |
|-----------|---------|
| Framework | Streamlit |
| Language | Python 3.13 |
| Model | Decision Tree (max_depth=10) |
| Input Features | 14 (10 AQ-10 + 4 demographic) |
| Dataset | UCI ASD Screening Dataset |
| Records | 5,021 across 3 age groups |

---

## Important Disclaimer

⚠️ This tool is for **research and educational purposes only**.
It does **not** constitute a clinical diagnosis.
A positive result should always be followed by evaluation from a trained specialist.

---

## Thesis Details

- **Author:** Ronizza Mangaya-ay
- **Supervisor:** Bertram Haskins
- **Institution:** Noroff University College, Norway
- **Year:** 2025
- **Best Model:** Decision Tree (PR-AUC: 0.3369, Nested CV F1: 0.2513)
