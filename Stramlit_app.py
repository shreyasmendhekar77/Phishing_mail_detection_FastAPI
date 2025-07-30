# ------------------- Imports -------------------
import pickle
import numpy as np
import streamlit as st
from utils.common_functions import load_model
from utils.preprocessor import clean, get_email_vector
from models.prediction_function import prediction
from fastapi import FastAPI

# ------------------- FastAPI Setup -------------------
app = FastAPI()
Model_version = '1.0.0'

@app.get('/')
def home():
    return {'Welcome': 'to the API for checking that mail is phishing or normal'}

@app.get('/health')
def health():
    return {
        'Status': 'Ok',
        'Model version': Model_version,
    }

@app.post('/textdata')
def text_data(data: str) -> str:
    ans = clean(data)
    vec_model = load_model('vector_embedding_model.pkl')
    vector = get_email_vector(ans, vec_model)
    output = prediction(vector)
    print("Output is ", output)
    return output

# ------------------- Streamlit UI -------------------

st.set_page_config(page_title="Phishing Detector", page_icon="📧", layout="centered")
st.title("📧 Phishing Mail Detection")
st.markdown("Enter the content of the email below to check whether it's **phishing** or **legitimate**.")

# Input area
with st.form("email_form"):
    data = st.text_area("✍️ Enter email content here", height=200)
    submitted = st.form_submit_button("🚀 Analyze")

    if submitted:
        if not data.strip():
            st.warning("Please enter some email content before submitting.")
        else:
            with st.spinner("Analyzing..."):
                try:
                    ans = clean(data)
                    vec_model = load_model('vector_embedding_model.pkl')
                    vector = get_email_vector(ans, vec_model)
                    out = prediction(vector)
                    
                    st.success("Analysis Complete!")
                    if out == "Phishing mail":
                        st.error("⚠️ This email is likely a **PHISHING** attempt.")
                    else:
                        st.info("✅ This email appears to be **normal**.")
                except Exception as e:
                    st.error(f"❌ Error during prediction: {e}")

# Optional: Footer
st.markdown("---")
st.caption("Model Version: `1.0.0` • Built with ❤️ using Streamlit & FastAPI")
