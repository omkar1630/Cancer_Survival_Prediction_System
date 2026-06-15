# 🎗️ Cancer Survival Prediction System

## 📌 Overview

The Cancer Survival Prediction System is a Machine Learning-based web application that predicts whether a cancer patient is likely to be **Alive** or **Deceased** based on demographic and clinical information.

The application uses a **Decision Tree Classifier** trained on the India Cancer Patient Dataset (2022–2025) and provides real-time predictions through an interactive Streamlit interface.

---

## 🚀 Live Demo

🌐 https://cancer-survival-prediction-system.onrender.com/

---

## 🎯 Features

- Predict cancer patient survival status
- User-friendly Streamlit interface
- Real-time predictions
- Decision Tree Machine Learning model
- Fast and responsive design
- Easy deployment on Render

---

## 📊 Input Features

The model uses the following features:

- Age
- Gender
- State
- City
- Cancer Type
- Stage
- Treatment Type
- Survival Months

---

## 🧠 Machine Learning Model

**Algorithm Used:**

- Decision Tree Classifier

**Target Variable:**

- Survival Status

**Prediction Classes:**

- Alive
- Deceased

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Libraries
- Streamlit
- Scikit-learn
- Pandas
- NumPy

### Deployment
- Render

---

## 📂 Project Structure

```text
Cancer_Survival_Prediction_System/
│
├── app.py
├── decision_tree.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Cancer_Survival_Prediction_System.git
```

### Navigate to Project Folder

```bash
cd Cancer_Survival_Prediction_System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🌐 Render Deployment

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

---

## 📈 Dataset

**Dataset:** India Cancer Patient Dataset (2022–2025)

The dataset contains information about cancer patients, including demographic details, cancer type, treatment information, and survival-related attributes.

---

## 📷 Application Workflow

1. Enter patient information.
2. Click on **Predict Survival Status**.
3. The model processes the input data.
4. Prediction result is displayed instantly.
5. Output:
   - ✅ Alive
   - ⚠️ Deceased

---

## 🔮 Future Enhancements

- Survival probability score
- Interactive healthcare dashboard
- Explainable AI (XAI)
- Multiple ML model comparison
- Advanced analytics and visualizations

---

## 👨‍💻 Author

**Omkar Raut**

Aspiring Data Analyst | Machine Learning Enthusiast | Full Stack Developer

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub and share it with others.

---

## 📜 License

This project is developed for educational, research, and portfolio purposes.
