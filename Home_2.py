import pickle
from pathlib import Path

import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator

# --- USER AUTHENTICATION ---
names = ["Peter Parker", "Rebecca Miller"]
usernames = ["pparker", "rmiller"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "face-recognition-insightface", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    st.set_page_config(page_title='Attendance System',layout='wide')

    st.header('Attendance System using Face Recognition')

    with st.spinner("Loading Models and Conneting to Redis db ..."):
        import face_rec
        
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")    
    st.success('Model loaded sucesfully')
    st.success('Redis db sucessfully connected')