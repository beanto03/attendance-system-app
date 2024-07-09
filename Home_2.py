# home.py

import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit_authenticator as stauth

# Dummy user database (replace with actual user database in a real application)
users = {
    "amir": {
        "name": "Amir",
        "password": "123"  # Replace with hashed password in a real application
    }
}

def main():
    st.set_page_config(page_title='Attendance System', layout='wide')
    st.info('This is a purely informational message', icon="ℹ️")

    username = st.sidebar.title(f"Welcome {users['name']}")
    st.header('Attendance System using Face Recognition')

    with st.spinner("Loading Models and Connecting to Redis db ..."):
        # Perform operations needed for homepage after successful login
        import face_rec
        st.success('Model loaded successfully')
        st.success('Redis db successfully connected')

if __name__ == '__main__':
    main()
