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
 
   IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/bc_data/main/6_FeaturePlot_AllGene/'
   IMG_REPO2 = 'https://raw.githubusercontent.com/matthewlu2/bc_data/main/Violin_1/'
   IMG_REPO3 = 'https://raw.githubusercontent.com/matthewlu2/bc_data/main/Violin_2/'

   
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

      file = open('data/textfiles/long_list.txt', 'r')
      list = file.read().splitlines()
      print(len(list))

      option = st.selectbox(
      'Gene of Interest',
      (list)) 

      col1, col2 = st.columns(2, gap = "large")

      front = 'OutFeatureplot_GSE176EGA6608_MergeSCTHarmony_'
      front2 = 'OutVlnplot_GeneExpByCellType_'
      img4 = f'{IMG_REPO}/{front}{option}.png'

      if option[0] <= 'M':
         img5 = f'{IMG_REPO2}/{front2}{option}.png'

      else:
          img5 = f'{IMG_REPO3}/{front2}{option}.png'

     

      col1.image(img4, caption = 'Feature Plot')
      for i in range(2):
         col2.write("")
      col2.image(img5, caption = 'Violin Plot')
      

