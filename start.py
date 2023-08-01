import streamlit as st
import hydralit_components as hc
from PIL import Image

from home import home_page
from datasets import datasets_page
from correlation import correlation_page
from correlation_2 import correlation_2_page
# from usage import usage_page
from contact import contact_page


st.set_page_config(
        page_title='Breast Cancer',
        page_icon= "./logos/breastcancer.png",
        initial_sidebar_state="expanded",
)

max_width_str = f"max-width: {85}%;"
st.markdown(f"""
        <style>
        .appview-container .main .block-container{{{max_width_str}}}
        </style>
        """,
        unsafe_allow_html=True,
    )

#Image.MAX_IMAGE_PIXELS = None

HOME = "Home"
DATASET = "Datasets"
CORRELATION = "Correlation With TAM Infiltration"
CORRELATION_2 = "Correlation with Pathway Activities"
#USAGE = "Usage"
CONTACT = "Contact Us"


tabs = [
    HOME,
    DATASET,
    CORRELATION,
    CORRELATION_2,
    #USAGE,
    CONTACT
]

option_data = [
   {'icon': "🏠", 'label':HOME},
   {'icon': "📊", 'label':DATASET},
   {'icon': "🔄", 'label':CORRELATION}, 
   {'icon': "🔃", 'label':CORRELATION_2}, 
  # {'icon': "📈", 'label':USAGE}, 
   {'icon': "☎️", 'label':CONTACT}
]

theme = {'txc_inactive': 'white','menu_background':'#ff94b6','txc_active':'black'}
chosen_tab = hc.nav_bar(menu_definition=option_data, override_theme = theme, use_animation= bool(True), hide_streamlit_markers= bool(True))

if chosen_tab ==HOME:
    home_page()

elif chosen_tab == DATASET:
    datasets_page()

elif chosen_tab == CORRELATION:
    correlation_page()

elif chosen_tab == CORRELATION_2:
    correlation_2_page()

# elif chosen_tab == USAGE:
#     usage_page()

elif chosen_tab == CONTACT:
    contact_page()

