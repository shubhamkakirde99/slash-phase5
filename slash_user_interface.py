from pyclbr import Function
from src.pages.search import render_search
from src.pages.wishlist import render_wishlist
import streamlit as st

st.set_page_config(page_title="Slash - Product Search", page_icon="🔍")

class UIManager:
    def __init__(self):
        self.pages = []

    def addPage(self, title, render_method):
        self.pages.append({"title": title, "function": render_method})

    def render(self):
        st.sidebar.markdown("## Main Menu")
        page = st.sidebar.selectbox(
            "Select Page", self.pages, format_func=lambda page: page["title"]
        )
        page["function"]()


uiManager = UIManager()

uiManager.addPage("Search", render_search)
uiManager.addPage("Wishlist", render_wishlist)
uiManager.render()
