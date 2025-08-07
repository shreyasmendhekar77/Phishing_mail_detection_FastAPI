import pickle
from pathlib import Path
def load_model(file):
    with open(file,'rb') as f:
        model=pickle.load(f)

    return model

def save_model(model, file):
    file_path = Path(file)
    file_path.parent.mkdir(parents=True, exist_ok=True)  # Create parent directories if needed
    with open(file_path, 'wb+') as f:
        pickle.dump(model, f)
    print(f"Model saved to {file_path}")
