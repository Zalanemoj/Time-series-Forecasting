# 📈 Time Series Forecasting: LSTM & XGBoost

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-Latest-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

<img width="3168" height="1344" alt="Banner" src="https://github.com/user-attachments/assets/87ee53db-7c7f-441c-a19b-fed351bdac51" />


## 📖 Overview
This project focuses on **forecasting time-series data** (specifically electricity load/consumption) using machine learning and deep learning techniques. We compare the performance of gradient boosting models (**XGBoost**) against deep recurrent neural networks (**LSTM**) to predict future values based on historical patterns.

The project covers the full data science lifecycle:
1.  **Data Preprocessing:** Cleaning, scaling, and handling missing values.
2.  **Exploratory Data Analysis (EDA):** Visualizing trends, seasonality, and stationarity.
3.  **Model Development:** Training XGBoost and LSTM models.
4.  **Evaluation:** Comparing models using RMSE and MAE.

---

## 📂 Project Structure

```text
├── Scripts-Client/
│   ├── Preprocessing.ipynb   # Data cleaning, scaling, and formatting
│   ├── Eda.ipynb             # Exploratory Data Analysis & Visualization
│   ├── LSTM.ipynb            # Deep Learning Model (Long Short-Term Memory)
│   ├── Xgboost.ipynb         # Gradient Boosting Model
│   └── Splitting_data.py     # Helper script for train/test splits
├── Models/
│   ├── lstm_model.keras      # Saved LSTM model
│   ├── XGB_mode.pkl          # Saved XGBoost model
│   └── Sclar.pkl             # Saved Scaler object (for inverse transform)
└── README.md
