
import re
import numpy as np
import pickle
from utils.common_functions import load_model

# Prediction function 

# import the ml model
with open('models\Prediciton_model\model.pkl', 'rb') as f:
    model = pickle.load(f)


def prediction(data)->dict:
    vector = np.array(data).reshape(1, -1)
    # print("Prediction function - shape of vector - ",vector.shape)
    prediction=model.predict(vector)
    # Predict probabilities
    probs = model.predict_proba(vector)
    print("Model type:", type(model))
    print("Model parameters:", model.get_params())
    print("Prediction probabilities: ", probs)
    print("prediction is ",prediction)
    if prediction==1.0:
        ans='Phishing mail'
    else:
        ans='Safe mail'
    
    output = {
        'prediction': ans,
        'probabilities': {
            'phishing': probs[0][1].tolist(),  # Probability of phishing
            'normal': probs[0][0].tolist()  # Probability of normal
        }
        }  # Convert numpy array to list for JSON serialization
    
    
    return output