from utils.preprocessor import train_word2vec_model



if __name__=='__main__':
    try:

        train_word2vec_model()
    
    except Exception as e:
        raise e