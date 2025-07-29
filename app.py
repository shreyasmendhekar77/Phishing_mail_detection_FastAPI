import fastapi 
from fastapi import FastAPI
import pickle
import numpy as np
from utils.common_functions import load_model
from utils.preprocessor import clean,get_email_vector
from models.prediction_function import prediction

app=FastAPI()
Model_version='1.0.0'


@app.get('/')
def home():
    return {
        'Welcome to the API for checking that mail is phishing or normal'
    }

@app.get('/health')
def health():
    return{
        'Status':'Ok',
        'Model version':Model_version,
    }


@app.post('/textdata')
def text_data(data:str)->str:
    ans=clean(data)
    vec_model=load_model('vector_embedding_model.pkl')
    vector=get_email_vector(ans,vec_model)
    output=prediction(vector)
    # print("The shape of the embedded vector is ",vector.shape)
    print("Output is ",output)
    return output

    

    