# 📧 Phishing Mail Detection using FastAPI & Machine Learning

![Python](https://img.shields.io/badge/Python-3.9-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![MLflow](https://img.shields.io/badge/MLflow-Experiment--Tracking-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A complete end-to-end pipeline to detect phishing emails using multiple machine learning models and serve predictions via a FastAPI endpoint.

---

## 🎯 Project Overview

This project focuses on detecting **phishing emails** using various **Machine Learning algorithms**, integrated into a **FastAPI**-based web service.

### 🗂️ Dataset

The dataset contains:
- `Email Text`: Raw text of the email
- `Email Type`: Label — **Phishing** or **Normal**

---

## 📊 Feature Engineering

- **Word2Vec Embeddings**:  
  A **Word2Vec model is trained from scratch** on the given email dataset to convert email text into numerical embeddings.

> This ensures domain-specific representation for better phishing detection.

---

## ⚙️ Getting Started

### 🔧 Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/phishing-mail-detector.git
    cd phishing-mail-detector
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download and preprocess dataset**:
    ```bash
    python -m Dataset_Preprocessor_download.download_dataset
    ```

   - This script:
     - Downloads the dataset
     - Trains the Word2Vec embedding model
     - Saves it locally for later use


- ✅ Ensure `download_dataset.py` is executed before API startup.
- ❗ Embedding model must exist for predictions to work.


4. **Run the FastAPI server**:
    ```bash
    uvicorn main:app --reload
    ```

---

## 🧠 Model Training

The following models were explored:
- **Basic Models**: KNN, Logistic Regression, Decision Tree, SVM
- **Ensemble Models**: Random Forest, XGBoost, LightGBM, CatBoost

> ✅ Hyperparameter tuning was applied on each model.  
> ✅ Best-performing model selected for deployment.

---

## 📈 Experiment Tracking

- All training and evaluation experiments are tracked using **MLflow**.
- Includes: model parameters, metrics, training time, and more.

---

## 🚀 FastAPI Endpoint

- **Method**: `POST`  
- **Route**: `/predict`
- **Input JSON**:
    ```json
    {
      "email": "Congratulations! You’ve won a free iPhone. Click here..."
    }
    ```
- **Output JSON**:
    ```json
    {
      "prediction": "Phishing",
      "confidence_scores": {
        "Phishing": 0.87,
        "Normal": 0.13
      }
    }
    ```

---

## 🐳 Docker Deployment

1. **Build Docker image**:
    ```bash
    docker build -t phishing-mail-api .
    ```

2. **Run the container**:
    ```bash
    docker run -d -p 8000:8000 phishing-mail-api
    ```

3. Visit the docs at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🌐 Demo

![demo](https://user-images.githubusercontent.com/demo-user/demo-gif.gif) <!-- Replace with your own hosted GIF URL -->

---

## 🧰 Tech Stack

- Python 3.9
- FastAPI
- Gensim (Word2Vec)
- Scikit-learn, LightGBM, CatBoost, XGBoost
- MLflow
- Docker

---

## 🚧 Future Work

- Add BERT-based embeddings (Hugging Face Transformers)
- Web UI for user interaction (Streamlit or React)
- Real-time alerts or email client plugin

---

## 📄 License

This project is licensed under the **MIT License**.
