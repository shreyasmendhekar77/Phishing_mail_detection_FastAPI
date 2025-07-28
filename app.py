
import fastapi 
from fastapi import FastAPI
import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import pickle
import numpy as np

app=FastAPI()
Model_version='1.0.0'

ps=PorterStemmer()

def clean(data):
    data = re.sub(r'[^a-zA-Z\s]', '', data)
    data = data.lower()
    stop_words = set(stopwords.words('english'))
    words = data.split()
    words = [word for word in words if word not in stop_words]
    words = [ps.stem(word) for word in words]
    return words  # returns a list of tokens
    
def load_model(file):
    with open(file,'rb') as f:
        model=pickle.load(f)

    return model

# Function to get average vector for an email
def get_email_vector(tokens, model):
    vectors = [model.wv[word] for word in tokens if word in model.wv]
    if vectors:
        return np.mean(vectors, axis=0)
    else:
        return np.zeros(model.vector_size)

# Prediction function 

def prediction(data)->str:
    vector = np.array(data).reshape(1, -1)
    # print("Prediction function - shape of vector - ",vector.shape)
    model=load_model('Final_model\model.pkl')
    prediction=model.predict(vector)
    print("prediction is ",prediction)
    if prediction==1.0:
        ans='Phishing mail'
    else:
        ans='Safe mail'
    
    return ans

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

    

    