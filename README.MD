# 🎓 Student Exam Performance Prediction

An end-to-end Machine Learning project that predicts a student's **Mathematics Score** based on demographic, socioeconomic, and academic-performance factors.

The project follows a modular Machine Learning architecture covering **data ingestion, data transformation, model training, model evaluation, prediction, and deployment**.

## 🚀 Live Demo

👉 **[Try the Student Exam Performance Predictor](https://mlproject-edtbc8sjszsvipe2sa9txc.streamlit.app/)**

Enter the student's details and get a predicted **Math Score** directly from the deployed application.

---

## 📌 Project Overview

The objective of this project is to build a Machine Learning regression model capable of predicting a student's **Math Score** using:

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch Type
* Test Preparation Course
* Reading Score
* Writing Score

The project demonstrates an end-to-end workflow, starting from raw data ingestion and preprocessing and ending with a deployed application for real-time predictions.

---

## 🎯 Problem Statement

Predict a student's **Mathematics Score** based on demographic, socioeconomic, and academic features.

### Target Variable

**Math Score**

### Problem Type

**Regression**

Since the target variable is a continuous numerical value, the problem is treated as a regression problem.

---

## 📊 Dataset

The project uses the **Students Performance in Exams** dataset.

The dataset contains information about students' demographic characteristics, parental education, lunch type, test preparation, and examination scores.

### Features

| Feature                       | Description                                |
| ----------------------------- | ------------------------------------------ |
| `gender`                      | Student's gender                           |
| `race_ethnicity`              | Student's race/ethnicity group             |
| `parental_level_of_education` | Parent's highest education level           |
| `lunch`                       | Student's lunch type                       |
| `test_preparation_course`     | Test preparation course status             |
| `reading_score`               | Reading examination score                  |
| `writing_score`               | Writing examination score                  |
| `math_score`                  | Mathematics examination score — **Target** |

---

## 🔄 Machine Learning Workflow

```text
                    Raw Dataset
                         │
                         ▼
                  Data Ingestion
                         │
                         ▼
                  Train/Test Split
                         │
                         ▼
                 Data Transformation
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       Numerical Features    Categorical Features
              │                     │
              ▼                     ▼
           Scaling               Encoding
              │                     │
              └──────────┬──────────┘
                         ▼
                   Model Training
                         │
                         ▼
                  Model Evaluation
                         │
                         ▼
                   Best Model
                         │
                         ▼
                 Model Serialization
                    │            │
                    ▼            ▼
               model.pkl   preprocessor.pkl
                    │            │
                    └──────┬─────┘
                           ▼
                  Prediction Pipeline
                           │
                           ▼
                    Streamlit App
                           │
                           ▼
                 🎯 Predicted Math Score
```

---

## 🧠 Machine Learning Models

The project evaluates multiple regression algorithms to identify the best-performing model.

Models include:

* Linear Regression
* Lasso Regression
* Ridge Regression
* K-Neighbors Regressor
* Decision Tree Regressor
* Random Forest Regressor
* AdaBoost Regressor
* XGBoost Regressor
* CatBoost Regressor

The best-performing model is selected and saved for use in the prediction pipeline.

---

## ⚙️ Data Preprocessing

The project uses different preprocessing strategies for numerical and categorical features.

### Numerical Features

* Reading Score
* Writing Score

Numerical features are scaled before being passed to the Machine Learning model.

### Categorical Features

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch
* Test Preparation Course

Categorical features are encoded before model training.

The fitted preprocessing pipeline is saved as:

```text
artifacts/preprocessor.pkl
```

The trained model is saved as:

```text
artifacts/model.pkl
```

---

## 📁 Project Structure

```text
ML_Project/
│
├── artifacts/
│   ├── data.csv
│   ├── train.csv
│   ├── test.csv
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── catboost_info/
│
├── notebook/
│   └── EDA and Model Experimentation
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   └── predict_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── app.py
├── streamlit_app.py
├── requirements.txt
├── setup.py
└── README.md
```

This structure matches the files currently visible in your GitHub repository, including `artifacts`, `catboost_info`, `notebook`, `src`, `templates`, `app.py`, `streamlit_app.py`, `requirements.txt`, and `setup.py`.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* XGBoost
* CatBoost

### Web Application

* Streamlit
* Flask

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/ArunPentaboyina8/ML_Project.git
```

### 2. Navigate to the project

```bash
cd ML_Project
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

### Streamlit Application

Run:

```bash
streamlit run streamlit_app.py
```

Then open the URL provided by Streamlit.

Usually:

```text
http://localhost:8501
```

### Flask Application

Run:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

---

## 🔮 Prediction Process

The application accepts:

```text
Gender
Race/Ethnicity
Parental Level of Education
Lunch Type
Test Preparation Course
Reading Score
Writing Score
```

The data is converted into a DataFrame and passed through the prediction pipeline.

```text
User Input
    ↓
CustomData
    ↓
DataFrame
    ↓
Preprocessor
    ↓
Transformed Features
    ↓
Trained Model
    ↓
Predicted Math Score
```

### Example

```text
Input:

Gender: male
Race/Ethnicity: group A
Parental Education: bachelor's degree
Lunch: standard
Test Preparation: completed
Reading Score: 68
Writing Score: 67

Output:

Predicted Math Score: XX.XX
```

---

## 🧩 Project Components

### 1. Data Ingestion

Responsible for:

* Reading the raw dataset
* Creating train/test datasets
* Saving datasets into the artifacts directory

### 2. Data Transformation

Responsible for:

* Handling numerical features
* Handling categorical features
* Scaling numerical variables
* Encoding categorical variables
* Saving the fitted preprocessor

### 3. Model Trainer

Responsible for:

* Training multiple regression models
* Comparing model performance
* Selecting the best-performing model
* Saving the trained model

### 4. Prediction Pipeline

Responsible for:

* Loading the trained model
* Loading the preprocessing object
* Transforming new user input
* Generating the predicted Math Score

### 5. Streamlit Application

Provides an interactive interface where users can enter student information and receive a predicted Mathematics Score.

---

## 📚 Key Learning Outcomes

Through this project, I gained practical experience with:

* End-to-end Machine Learning workflows
* Exploratory Data Analysis
* Data ingestion
* Data preprocessing
* Feature transformation
* Categorical encoding
* Feature scaling
* Regression algorithms
* Model evaluation
* Model selection
* Hyperparameter tuning
* Model serialization
* Prediction pipelines
* Custom exception handling
* Logging
* Modular Python project architecture
* Flask application development
* Streamlit application development
* Git and GitHub
* Machine Learning deployment

---

## 🔮 Future Improvements

* Improve model performance through additional feature engineering
* Perform advanced hyperparameter optimization
* Add model explainability
* Improve application UI/UX
* Add model performance metrics to the application
* Deploy the application with a production-grade architecture
* Add automated CI/CD
* Add model monitoring

---

## 🙏 Acknowledgement

This project was developed as a learning implementation inspired by the **End-to-End Machine Learning Project by Krish Naik**.

The project follows a modular approach with separate components for data ingestion, transformation, model training, and prediction.

---

## 👨‍💻 Author

### Arun

**GitHub:**
https://github.com/ArunPentaboyina8

**Project Repository:**
https://github.com/ArunPentaboyina8/ML_Project

**Live Application:**
https://mlproject-edtbc8sjszsvipe2sa9txc.streamlit.app/

---

⭐ If you found this project useful, feel free to star the repository!
