"""
Copyright (c) 2023 Sathiya Narayanan Venkatesan
This code is licensed under MIT license (see LICENSE.MD for details)

@author: Slash
"""
import streamlit as st
import re
import json
import requests
import pandas as pd

def extract_and_format_numbers(input_string):
    # Use regular expressions to find all numbers in the input string
    numbers = re.findall(r'\d+\.\d+|\d+', input_string)

    if len(numbers) >= 2:
        # Take the first number and add a decimal point before the second number
        formatted_output = '$'+ numbers[0] + '.' + numbers[1]
        return formatted_output
    elif len(numbers) == 1:
        # If there's only one number, return it as is
        return '$'+ numbers[0]
    else:
        return "No valid numbers found in the input."



def ensure_https_link(link_text):
    if link_text.startswith("http://") or link_text.startswith("https://"):
        return link_text
    else:
        return "https://" + link_text

def path_to_image_html(path):
    return '<img src="' + path + '" width="60" >'

def path_to_url_html(path):
    return '<a href="'+ ensure_https_link(path) +'" target="_blank">Product Link</a>'

@st.cache
def convert_df_to_html(input_df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return input_df.to_html(escape=False, formatters=dict(Image=path_to_image_html,Link=path_to_url_html))

def render_wishlist():

    API_URL = "http://127.0.0.1:5050"

    # To get all the products wishlisted by the user
    response = requests.get(
        f"{API_URL}/wishlist"
    )

    response_json = response.json()  # This converts the response to a Python dictionary

    list = []

    # Add product_id as a 
    for key, value in response_json.items():
        product = json.loads(value)
        product['product_id'] = key
        list.append(product)

    description = []
    url = []
    price = []
    site = []
    image_url = []
    product_id = []

    for result in list:
        description.append(result['Description'])
        url.append(result['Link'])
        site.append(result['Website'])
        price.append(extract_and_format_numbers(result['Price']))
        image_url.append(result['Image'])
        product_id.append(result['product_id'])

    dataframe = pd.DataFrame({'product_id':product_id, 'Description': description, 'Price': price, 'Link': url, 'Website': site, 'Image':image_url})

    st.markdown("<h1 style='text-align: center; color: #1DC5A9;'>Wish List</h1>", unsafe_allow_html=True)

    html = "<div class='table-container'>"
    html += convert_df_to_html(dataframe)
    st.markdown(
        html,
        unsafe_allow_html=True
    )
    html += '</div>'
    

    product_index = st.text_input('Delete From Wish List')
    wishlist_button = st.button('Delete')
    if wishlist_button:
        print("request sent")
        response = requests.delete(
            f"{API_URL}/wishlist/{product_index}"
        )

        if response.status_code == 200:
            st.write("Removed successfully")
    
