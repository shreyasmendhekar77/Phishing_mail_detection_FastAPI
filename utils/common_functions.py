import pickle

def load_model(file):
    with open(file,'rb') as f:
        model=pickle.load(f)

    return model
