# rijwana
# Customer Churn Prediction Using Machine Learning

## Student Details

- **Name:** Rijwana Jamadar
- **BITS ID:** 2025AC05724
- **Email:** 2025ac5724@wilp.bits-pilani.ac.in
- **Course:** Machine Learning
- **Assignment:** ML Assignment 2

---

## Problem Statement

Customer churn prediction is a critical business application that helps organizations identify customers who are likely to discontinue services. Retaining existing customers is generally more cost-effective than acquiring new customers.

The objective of this project is to develop and compare multiple machine learning classification models for predicting customer churn using the Telco Customer Churn dataset. The models are evaluated using various performance metrics and deployed using Streamlit for interactive usage.

---

## Dataset Description

**Dataset Name:** Telco Customer Churn Dataset

### Dataset Characteristics

- Dataset Type: Binary Classification
- Number of Records: 7,043
- Number of Features: 21
- Target Variable: Churn
- Classes:
  - Yes (Customer Churned)
  - No (Customer Retained)

### Features Include

- Gender
- SeniorCitizen
- Partner
- Dependents
- Tenure
- PhoneService
- MultipleLines
- InternetService
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies
- Contract
- PaperlessBilling
- PaymentMethod
- MonthlyCharges
- TotalCharges

---

## Repository and Application Links

### GitHub Repository

https://github.com/2025ac05724-maker/rijwana

### Streamlit Application

https://rijwana-hvvqcbueccatqm2hrcmjkt.streamlit.app/

---

## Data Preprocessing

The following preprocessing steps were performed:

1. Removed Customer ID column.
2. Converted TotalCharges to numeric format.
3. Handled missing values using median imputation.
4. Converted target variable (Churn) into binary format.
5. Applied One-Hot Encoding on categorical variables.
6. Split data into training and testing sets.
7. Applied feature scaling using StandardScaler for applicable models.

---

## Machine Learning Models Implemented

The following six classification models were implemented:

1. Logistic Regression
2. Decision Tree Classifier
3. K-Nearest Neighbors (KNN)
4. Gaussian Naive Bayes
5. Random Forest Classifier
6. Support Vector Machine (SVM)

---

## Evaluation Metrics

The models were evaluated using the following metrics:

- Accuracy
- AUC Score
- Precision
- Recall
- F1 Score
- Matthews Correlation Coefficient (MCC)

---

## Model Comparison

| Model | Accuracy | AUC | Precision | Recall | F1 Score | MCC |
|---------|----------|----------|----------|----------|----------|----------|
| Logistic Regression | 0.8070 | 0.8416 | 0.6584 | 0.5668 | 0.6092 | 0.4843 |
| SVM | 0.7928 | 0.7961 | 0.6444 | 0.4893 | 0.5562 | 0.4312 |
| Random Forest | 0.7899 | 0.8265 | 0.6336 | 0.4947 | 0.5556 | 0.4263 |
| KNN | 0.7473 | 0.7718 | 0.5253 | 0.5000 | 0.5123 | 0.3422 |
| Decision Tree | 0.7417 | 0.6623 | 0.5139 | 0.4947 | 0.5041 | 0.3296 |
| Naive Bayes | 0.6558 | 0.8096 | 0.4269 | 0.8663 | 0.5719 | 0.3951 |

---

## Model Performance Analysis

Six machine learning classification models were evaluated for customer churn prediction.

Among all evaluated models, **Logistic Regression** achieved the best overall performance with:

- Accuracy = 80.70%
- AUC = 0.8416
- Precision = 0.6584
- Recall = 0.5668
- F1 Score = 0.6092
- MCC = 0.4843

The model provided the best balance between predictive performance and interpretability.

### Confusion Matrix Results

| Actual / Predicted | No Churn | Churn |
|-------------------|---------|---------|
| No Churn | 925 | 110 |
| Churn | 162 | 212 |

The model correctly classified:

- 925 non-churn customers
- 212 churn customers

The confusion matrix indicates good classification capability with relatively few incorrect predictions.

### ROC Analysis

The ROC Curve achieved an **AUC Score of 0.8416**, indicating strong discriminative capability between churned and retained customers.

---

## Feature Importance

The most influential factors affecting customer churn include:

- Tenure
- Monthly Charges
- Internet Service Type
- Contract Type
- Total Charges
- Online Security
- Tech Support
- Payment Method

Customers with long-term contracts generally exhibit lower churn probability, while customers using fiber-optic internet services tend to show a higher likelihood of churn.

---

## Streamlit Application Features

The deployed Streamlit application provides:

- Dataset loading
- Classification model selection
- Accuracy display
- AUC display
- Precision display
- Recall display
- F1 Score display
- MCC Score display
- Model comparison
- Customer churn analysis

---

## Project Structure

```text
rijwana/
│
├── app.py
├── requirements.txt
├── README.md
├── Telco-Customer-Churn.csv
└── Telco_Customer_Churn_Assignment.ipynb
```

## Required Libraries

```txt
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
```

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Run Locally

```bash
streamlit run app.py
```

### Open in Browser

```text
http://localhost:8501
```

---

## Conclusion

This project demonstrates the effectiveness of machine learning techniques in predicting customer churn using the Telco Customer Churn dataset.

Among all evaluated models, **Logistic Regression** delivered the best overall performance across Accuracy, AUC, Precision, Recall, F1 Score, and MCC Score. The analysis identified several key business factors associated with churn, providing actionable insights that can support customer retention strategies.

The project successfully fulfills the assignment requirements by implementing six classification algorithms, evaluating them using multiple performance metrics, and deploying the solution through Streamlit.

---

## Author

**Rijwana Jamadar**  
BITS Pilani WILP  
M.Tech in Artificial Intelligence & Machine Learning  
BITS ID: 2025AC05724
``
