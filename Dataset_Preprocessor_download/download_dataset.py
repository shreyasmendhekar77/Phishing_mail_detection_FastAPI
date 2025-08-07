import gdown
import zipfile
from pathlib import Path

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