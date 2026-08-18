#  Advertising Sales Prediction Using Linear Regression

##  Project Overview

This project demonstrates the implementation of a **Multiple Linear Regression** model to predict product sales based on advertising expenditure across different media platforms.

The model uses the following advertising channels as independent variables:

* TV
* Radio
* Newspaper

The target variable is:

* Sales

The project follows a complete machine learning workflow including data loading, preprocessing, data splitting, model training, prediction, and performance evaluation.

---

## Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn

---

## Dataset

The project uses the `Advertising.csv` dataset.

### Input Features

| Feature   | Description                          |
| --------- | ------------------------------------ |
| TV        | Advertising expenditure on TV        |
| Radio     | Advertising expenditure on Radio     |
| Newspaper | Advertising expenditure on Newspaper |

### Target Feature

| Feature | Description         |
| ------- | ------------------- |
| Sales   | Product sales value |

---

##  Project Workflow

```text
Advertising Dataset
        │
        ▼
Data Loading
        │
        ▼
Data Preprocessing
        │
        ▼
Exploratory Data Analysis
        │
        ├── Missing Value Analysis
        ├── Statistical Summary
        └── Correlation Analysis
        │
        ▼
Train-Test Split
        │
        ▼
Multiple Linear Regression Model
        │
        ▼
Prediction
        │
        ▼
Model Evaluation
        │
        ├── Mean Squared Error (MSE)
        ├── Root Mean Squared Error (RMSE)
        └── R² Score
        │
        ▼
Sales Prediction
```

---

## Machine Learning Algorithm

This project uses **Multiple Linear Regression**.

The model learns the relationship between advertising expenditure and product sales.

The mathematical representation is:

```text
Sales = β₀ + β₁(TV) + β₂(Radio) + β₃(Newspaper)
```

Where:

* `β₀` = Intercept
* `β₁`, `β₂`, `β₃` = Model coefficients
* `TV`, `Radio`, and `Newspaper` = Independent variables

---

## Model Evaluation Metrics

The performance of the model is evaluated using:

### Mean Squared Error (MSE)

Measures the average squared difference between actual and predicted values.

### Root Mean Squared Error (RMSE)

Shows the prediction error in the same unit as the target variable.

### R² Score

Measures how well the independent variables explain the variation in sales.

A higher R² score generally indicates a better fit of the model to the data.

---

##  Project Structure

```text
Advertising-Sales-Prediction-Linear-Regression/
│
├── Advertising.csv
├── LinearRegression.py
└── README.md
```

---

##  How to Run the Project

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd Advertising-Sales-Prediction-Linear-Regression
```

### 3. Install Required Libraries

```bash
pip install numpy pandas scikit-learn
```

### 4. Run the Program

```bash
python LinearRegression.py
```

---

## Workflow Implemented

The program is divided into the following steps:

1. **Load Dataset**
2. **Perform Data Preprocessing**
3. **Check Missing Values**
4. **Generate Statistical Summary**
5. **Perform Correlation Analysis**
6. **Split Data into Training and Testing Sets**
7. **Train the Linear Regression Model**
8. **Generate Predictions**
9. **Evaluate the Model using MSE, RMSE, and R² Score**

---

## Author

**Aarti Gorakshnath Wamane**

M.Tech Computer Engineering Student
Machine Learning and Python Enthusiast

---

⭐ If you found this project useful, consider giving it a star!

