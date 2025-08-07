import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import re
from pathlib import Path
import numpy as np
import pandas as pd
from gensim.models import Word2Vec
from utils.common_functions import save_model
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

def train_word2vec_model():
    dataset_path=Path('Dataset_Preprocessor_download/Phishing_Email.csv')
    if not dataset_path.exists():
        print(f"Dataset file not found at {dataset_path}. Please ensure the dataset is downloaded.")
        return
    else:
        data=pd.read_csv('Dataset_Preprocessor_download\Phishing_Email.csv')
        data['Email Text']=data['Email Text'].fillna('')
        data['tokens'] = data['Email Text'].apply(clean)
        w2v_model = Word2Vec(sentences=data['tokens'], vector_size=100, window=5, min_count=1, workers=4)
        save_model(w2v_model, Path('models\Embedding_model\\vector_embedding_model.pkl'))


# Function to get average vector for an email
def get_email_vector(tokens, model):
    vectors = [model.wv[word] for word in tokens if word in model.wv]
    if vectors:
        return np.mean(vectors, axis=0)
    else:
        return np.zeros(model.vector_size)
