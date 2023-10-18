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
    token = None
    API_URL = "http://127.0.0.1:5050/auth"

    if not token:
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
                        st.write(f"You are now logged in {token}")
                    else:
                        st.error("Login failed. Please check your credentials.")
                else:
                    st.warning("Please enter both username and password.")

    if token:
        # User is logged in
        if st.button("View Wishlist"):
            # render_wishlist()
            pass
        if st.button("Logout"):
            response = requests.get(f"{API_URL}/logout")
            token = None
            st.success("Logged out successfully.")
            st.markdown("""
                        <script>
                        window.location.reload();
                        </script>
                        """,
                        unsafe_allow_html=True
                        )