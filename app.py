import streamlit as st
from PIL import Image
from diabetis_page import show_diabetis_page
from more_page import show_more_page

img = Image.open('Main.png')
hide_menu_style = """
        <style>
        #MainMenu {visibility: show; }
        footer {visibility: hidden; }
        </style>

"""

st.set_page_config(page_title='Diabetes Prediction System', page_icon=img)
#st.set_page_config(page_title='Disease Prediction System', page_icon=":shark:")
st.markdown(hide_menu_style, unsafe_allow_html=True)



page = st.sidebar.selectbox("Diabetes Or More", ("Diabetes", "More"))

if page == "Diabetes":
    show_diabetis_page()
else:
    show_more_page()




