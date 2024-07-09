# login.py

import streamlit as st

# Dummy user database (replace with actual user database in a real application)
users = {
    "amir": {
        "name": "Amir",
        "password": "123"  # Replace with hashed password in a real application
    }
}

def authenticate(username, password):
    """ Function to authenticate user based on username and password. """
    if username in users:
        if password == users[username]["password"]:
            return True
    return False

def main():
    st.set_page_config(page_title='Login', layout='centered')

    st.title('User Login')

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        if authenticate(username, password):
            st.success(f'Logged in as {username}')
            st.rerun()  # Rerun to clear login form on successful login
            st.rerun()  
        else:
            st.error('Authentication failed. Please check your username and password.')

if __name__ == '__main__':
    main()
