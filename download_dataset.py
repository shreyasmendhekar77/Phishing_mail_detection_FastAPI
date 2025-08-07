import gdown
import zipfile
from pathlib import Path
from utils.preprocessor import train_word2vec_model

dataset_url = 'https://drive.google.com/file/d/1RpSMHhd_AJHOHYZHeq_mskJwRLj4YbP3/view?usp=sharing'
zip_download_dir = Path('Dataset_Preprocessor_download/data.zip')
unzip_path=Path('Dataset_Preprocessor_download')


if __name__ == "__main__":
    try:
        
        file_id = dataset_url.split("/")[-2]
        prefix = 'https://drive.google.com/uc?/export=download&id='
        gdown.download(prefix+file_id,str(zip_download_dir))    
# # 
        # Extracting the zip file
        if zip_download_dir.exists():
            
            with zipfile.ZipFile(zip_download_dir, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)

        # Removing the zip file after extraction
        zip_download_dir.unlink()
        print("Dataset downloaded and extracted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Train the Embedding model for the dataset
    try:
        print("Training Word2Vec model...")
        train_word2vec_model()
        print("Word2Vec model trained and saved successfully.")
        
    except Exception as e:
        raise e