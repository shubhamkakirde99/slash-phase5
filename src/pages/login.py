"""
Copyright (c) 2023 Sharat Neppalli
This code is licensed under MIT license (see LICENSE.MD for details)

@author: Slash
"""

import requests
import streamlit as st

def render_login():

    # Display Image
    st.image("assets/slash.png")

    with open('assets/style.css') as f:
        st.markdown(f"""
            <style>
            {f.read()}
            </style>
        """, unsafe_allow_html=True)

    # variable to store the user id when logged in
    token = st.session_state.get('token', None)
    API_URL = "http://127.0.0.1:5050/auth"

    placeholder = st.empty()
    if not token:
        placeholder.empty()
        with placeholder.container():
            st.header("Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login = st.button("Login")
            if login:
                if username and password:
                    response = requests.post(
                        f"{API_URL}/token",
                        data={"username": username, "password": password}
                    )
                    if response.json().get("user"):
                        token = response.json().get("user")
                        cookie = response.cookies.get("access_token")
                        st.session_state.token = token
                        st.write(f"You are now logged in {token}")
                        st.experimental_rerun()
                    else:
                        st.error("Login failed. Please check your credentials.")
                else:
                    st.warning("Please enter both username and password.")
    # User is logged in
    if token:
        placeholder.empty()
        with placeholder.container():
            if st.button("View Wishlist"):
                # render_wishlist()
                pass
            if st.button("Logout"):
                response = requests.get(f"{API_URL}/logout")
                del st.session_state['token']
                token =None
                st.success("Logged out successfully.")
                st.experimental_rerun()

