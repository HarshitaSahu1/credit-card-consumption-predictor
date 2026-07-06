# 💳 Credit Card Consumption Predictor

An end-to-end **Machine Learning** project built with **Python** and **Streamlit** for predicting customer credit card consumption through interactive analytics and predictive modeling.

---

## 🌐 Live Application

🚀 **Try the App Here:**  
https://iph8aobmuhyyhyqdqrldcq.streamlit.app/

---

## 📌 Project Overview

The **Credit Card Consumption Predictor** is an interactive web application designed to analyze customer financial behavior and predict future credit card consumption using a Machine Learning model.

The application combines:

- Data Preprocessing
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Business Insights
- Machine Learning Prediction
- Interactive Streamlit Dashboard

---

## 🚀 Features

- 🔐 User Login Interface
- 📊 Interactive Business Dashboard
- 💳 Credit Card Consumption Analysis
- 💰 Debit Card Consumption Analysis
- 👥 Customer Demographic Analysis
- 📈 Investment Analysis
- 💡 Business Insights for Every Visualization
- 🤖 Credit Card Consumption Prediction
- 📁 Upload Customer Dataset (CSV)
- 📉 Actual vs Predicted Comparison

---

## 🤖 Machine Learning Model

### Model Information

| Feature | Details |
|---------|---------|
| **Algorithm** | Bagging Regressor |
| **Base Estimator** | Decision Tree Regressor |
| **Target Variable** | Credit Card Consumption |
| **Input** | Customer CSV File |
| **Output** | Predicted Credit Card Consumption |

### 📊 Model Performance

| Metric | Score |
|---------|-------:|
| **Training R² Score** | **0.8253** |
| **Training RMSE** | **2962.56** |

> **Interpretation:**  
> The Bagging Regressor explains approximately **82.5% of the variance** in customer credit card consumption on the training data, with an average prediction error (RMSE) of approximately **2963 consumption units**.

---

## 📂 Dataset

The application uses a processed dataset (`final_dataset.csv`) created by merging multiple customer-related datasets.

The preprocessing pipeline included:

- Data Merging
- Data Cleaning
- Handling Missing Values
- Feature Engineering
- Data Transformation

The final processed dataset is then used for both visualization and prediction.

---

## 📊 Dashboard Modules

### 💳 Customer Spending Analysis

- Monthly Credit Card Consumption
- Monthly Debit Card Consumption
- Transaction Count Analysis

### 👥 Customer Demographics

- Gender Distribution
- Age Group Distribution

### 💰 Investment Analysis

- Investment Type Distribution
- Investor Category Analysis

### 🤖 Prediction Module

Users can upload a CSV file containing customer information to generate predictions for future credit card consumption.

The prediction module provides:

- Predicted Credit Card Consumption
- Actual vs Predicted Comparison
- Interactive Visualizations

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib

---

## 📁 Project Structure

```text
credit-card-consumption-predictor/
│
├── app.py
├── train_model.py
├── final_dataset.csv
├── model_pipeline.pkl
├── Credit Consumption_image.png
├── requirements.txt
├── README.md
└── assets/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-github-username/credit-card-consumption-predictor.git
```

Navigate to the project folder

```bash
cd credit-card-consumption-predictor
```

Install the dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---


## 💼 Business Value

This project demonstrates how customer financial data can be transformed into meaningful business insights through interactive analytics and Machine Learning.

Potential business applications include:

- Customer Spending Analysis
- Customer Segmentation
- Financial Behavior Analysis
- Customer Consumption Forecasting
- Personalized Marketing Strategies
- Data-Driven Business Decisions

---

## 🔮 Future Enhancements

- Database Integration
- User Authentication with Database
- Cloud Database Support
- Advanced Ensemble Models
- Real-Time Prediction Pipeline
- Downloadable Prediction Reports

---

## 👩‍💻 Author

**Harshita Sahu**

**Aspiring Data Analyst**

**Skills:** Python • Machine Learning • Streamlit • Data Analysis • Data Visualization

---

⭐ **If you found this project helpful, please consider giving it a star!**
