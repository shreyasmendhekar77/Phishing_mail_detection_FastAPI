import pickle
import numpy as np
import streamlit as st
from utils.common_functions import load_model
from utils.preprocessor import clean, get_email_vector
from utils.prediction_function import prediction
from fastapi import FastAPI

app = FastAPI()
Model_version = '1.0.0'

@app.get('/')
def home():
    return {'Welcome': 'to the API for checking that mail is phishing or normal'}

@app.get('/health')
def health():
    return {
        'Status': 'Ok',
        'Model version': Model_version,
    }

@app.post('/textdata')
def text_data(data: str) -> dict:
    ans = clean(data)
    vec_model = load_model('models\Embedding_model\\vector_embedding_model.pkl')
    vector = get_email_vector(ans, vec_model)
    output = prediction(vector)
    print("Output is ", output)
    return output
