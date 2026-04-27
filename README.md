# 🧩 ASD Screening Support Tool

Interactive research artifact accompanying the bachelor thesis:

> **Machine Learning and Deep Learning Approaches for Early 
> Detection of Autism Spectrum Disorder**
> Ronizza Mangaya-ay | Noroff University College | 2025
> Supervisor: Bertram Haskins

This application implements the Decision Tree screening support 
model developed in the thesis and allows users to enter AQ-10 
questionnaire responses and demographic features to generate an 
ASD risk screening result.

---

## 🚀 Live Demo

🔗 https://ronizza-asd-screening.streamlit.app

---

## 💻 Run Locally

```bash
streamlit run app.py
```

## 📦 Install Requirements

```bash
pip install -r requirements.txt
```

---

## ⚠️ Research Use Disclaimer

This tool is provided for **research and educational purposes only.**

- It is a screening support prototype and does not constitute 
a clinical diagnostic instrument
- It must not be used as a substitute for professional medical 
assessment or diagnosis
- An elevated screening result should be followed by evaluation by a qualified specialist.

---

## 📁 Artifact Components

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit application |
| `model.pkl` | Serialised Decision Tree model |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

## 🔬 Research Details

| Item | Details |
|------|---------|
| Author | Ronizza Mangaya-ay |
| Institution | Noroff University College, Norway |
| Supervisor | Bertram Haskins |
| Year | 2025 |
| Dataset | UCI ASD Screening Dataset |
| Records | 5,021 across 3 age groups |
| Deployment Model | Decision Tree (PR-AUC: 0.3369) |

---

## 📚 Source Code

🔗 https://github.com/roniz29/asd_screening_tool
