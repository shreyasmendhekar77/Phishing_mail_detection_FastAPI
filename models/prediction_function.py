
import re
import numpy as np
import pickle
from utils.common_functions import load_model

# Prediction function 

# import the ml model
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)


def prediction(data)->str:
    vector = np.array(data).reshape(1, -1)
    # print("Prediction function - shape of vector - ",vector.shape)
    prediction=model.predict(vector)
    print("prediction is ",prediction)
    if prediction==1.0:
        ans='Phishing mail'
    else:
        ans='Safe mail'
    
    return ans