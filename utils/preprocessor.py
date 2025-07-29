import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import re
import numpy as np

nltk.download('stopwords')

ps=PorterStemmer()

def clean(data):
    data = re.sub(r'[^a-zA-Z\s]', '', data)
    data = data.lower()
    stop_words = set(stopwords.words('english'))
    words = data.split()
    words = [word for word in words if word not in stop_words]
    words = [ps.stem(word) for word in words]
    return words  # returns a list of tokens
    
# Function to get average vector for an email
def get_email_vector(tokens, model):
    vectors = [model.wv[word] for word in tokens if word in model.wv]
    if vectors:
        return np.mean(vectors, axis=0)
    else:
        return np.zeros(model.vector_size)
