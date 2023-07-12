import streamlit as st
import hydralit_components as hc
import pandas as pd
from PIL import Image


option_data = [
   {'icon': "", 'label':i} for i in ['Metadata', 'Visualization']]

over_theme = {'txc_inactive': 'black','menu_background':'white','txc_active':'white','option_active':'#ff94b6'}
font_fmt = {'font-class':'h2','font-size':'50%'}

# BACKGROUND_COLOR = 'white'
# COLOR = 'black'


def datasets_page():

   st.info("Information Here...")
   page = hc.option_bar(
        option_definition=option_data,
        title='',
        override_theme=over_theme,
        horizontal_orientation=True,
        )
 
   if page == 'Metadata':

      st.info("Information Here...")
     
   elif page == 'Visualization':

      a, b, c, d, e = st.columns(5)

      img1 = "./data/dataset_figures/Fig2A_DatasetVisualization.png"
      img2 = "./data/dataset_figures/Fig2B_DatasetVisualization.png"
      img3 = "./data/dataset_figures/Fig2C_DatasetVisualization.png"
      img4 = "./data/dataset_figures/Fig2D_DatasetVisualization.png"
      img5 = "./data/dataset_figures/Fig2E_DatasetVisualization.png"

      a.image(img1)
      b.image(img2)
      c.image(img3)
      d.image(img4)
      e.image(img5)
      

