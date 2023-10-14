"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: slash
"""

# Import Libraries
import sys
sys.path.append('../')
import streamlit as st
from src.main_streamlit import search_items_API
from src.url_shortener import shorten_url
import pandas as pd
#from link_button import link_button

@st.cache
def convert_df_to_html(input_df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return input_df.to_html(escape=False, formatters=dict(Image=path_to_image_html,Link=path_to_url_html))


# Load external CSS for styling
with open('assets/style.css') as f:
    st.markdown(f"""
        <style>
        {f.read()}
        </style>
    """, unsafe_allow_html=True)

# Display Image
st.image("assets/slash.png")

st.write("Slash is a command line tool that scrapes the most popular e-commerce websites to get the best deals on the searched items across multiple websites")
product = st.text_input('Enter the product item name')
website = st.selectbox('Select the website',('Amazon', 'Walmart', 'Ebay', 'BestBuy', 'Target', 'Costco', 'All'))

website_dict = {
        'Amazon':'az',
        'Walmart':'wm',
        'Ebay':'eb',
        'BestBuy':'bb',
        'Target':'tg',
        'Costco':'cc',
        'All':'all'
        }
# Pass product and website to method
if st.button('Search') and product and website:
    results = search_items_API(website_dict[website], product)
    # Use st.columns based on return values
    description = []
    url = []
    price = []
    site = []
    if results:
        for result in results:
            if result!={} and result['price']!='':
                description.append(result['title'])
                url.append(result['link'])
                price.append(float(''.join(result['price'].split('$')[-1].strip('$').rstrip('0').split(','))))
                site.append(result['website'])
                
    if len(price):
        
        def highlight_row(dataframe):
            #copy df to new - original data are not changed
            df = dataframe.copy()
            minimumPrice = df['Price'].min()
            #set by condition
            mask = df['Price'] == minimumPrice
            df.loc[mask, :] = 'background-color: lightgreen'
            df.loc[~mask,:] = 'background-color: ""'
            return df
        
        dataframe = pd.DataFrame({'Description': description, 'Price':price, 'Link':url, 'Website':site})
        st.balloons()
        st.markdown("<h1 style='text-align: center; color: #1DC5A9;'>RESULT</h1>", unsafe_allow_html=True)

        html = "<div class='table-container'>"
        html += convert_df_to_html(dataframe)
        st.markdown(
            html,
            unsafe_allow_html=True
        )
        html += '</div>'

        csv = convert_df_to_csv(dataframe)
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='output.csv',
            mime='text/csv',
        )

        st.markdown("<h1 style='text-align: center; color: #1DC5A9;'>Visit the Website</h1>", unsafe_allow_html=True)

        min_value = min(price)
        min_idx = [i for i, x in enumerate(price) if x == min_value]
        for minimum_i in min_idx:
            link_button_url = shorten_url(url[minimum_i].split('\\')[-1])
            st.write("Cheapest Product [link]("+link_button_url+")")
            #link_button(site[minimum_i], link_button_url)
        
    else:
        st.error('Sorry!, there is no other website with same product')
        


# Footer
footer = """<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0%;
width: 100%;
background-color: #DFFFFA;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://github.com/sathiya06/slash-phase3" target="_blank">slash</a></p>
<p><a style='display: block; text-align: center;' href="https://github.com/anshulp2912/slash/blob/main/LICENSE" target="_blank">MIT License Copyright (c) 2021 Rohan Shah</a></p>
<p>Contributors: Aadithya, Dhiraj, Sathya, Sharat</p>
</div>
"""
# st.markdown(footer, unsafe_allow_html=True)


