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

   st.info("We combined the pre-treatment and BRCA ER-positive single-cell RNA sequencing (scRNA-seq) datasets obtained from Wu et al. (PMID: 34493872) (n=14) and Bassez et al. (PMID: 33958794) (n=15) yielding 90,532 cells from 29 tumors. Our analysis highlighted the key players in the ER-positive TME, including tumor-associated macrophages (TAMs), epithelial cancer cells (ECCs), endothelial cells, and T cells.")
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

      a, b, c, d, e= st.columns([5, 10, 10, 10, 10], gap = "medium")
      a.markdown('##### No.')
      b.markdown('##### GEO/EGA_Accession')
      c.markdown('##### Number of total tumors')
      d.markdown('##### Number of ER+ tumors')
      e.markdown('##### Number of cells (ER+)')
    
      st.divider()

      st.markdown("""
      <style>
      [role=radiogroup]{
         gap: 1rem;
      }
      </style>
      """,unsafe_allow_html=True)


      

      genre = a.radio(label = "", label_visibility= 'collapsed', options = ['1', '2'])

     
      st.markdown('##### Quality Control by Paper')

      if genre == '1':
         st.write("• Cells expressing <200 genes or <250 unique molecular identifiers (UMIs) were removed.")
         st.write("• Normalisation, dimensionality reduction and clustering using default parameters.")     
         st.markdown('##### Reference')
         st.markdown(f'[{"A single-cell and spatially resolved atlas of human breast cancers"}](https://www.nature.com/articles/s41588-021-00911-1)') 
         st.write("Wu et al. Nat. Genetics 2021")
         st.markdown('##### Data Source')
         st.markdown('https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE176078')  

      else:
         st.write("• All cells expressing <200 or >6,000 genes were removed, as well as cells that contained <400 (UMIs) and >15% mitochondrial counts.") 
         st.write("• The default parameters of Seurat were used, unless mentioned otherwise.")
         st.markdown('##### Reference')    
         st.markdown(f'[{"A single-cell map of intratumoral changes during anti-PD1 treatment of patients with breast cancer"}](https://www.nature.com/articles/s41591-021-01323-8)') 
         st.write("Bassez et al. Nat. Med. 2021")
         st.markdown('##### Data Source')
         st.markdown('https://lambrechtslab.sites.vib.be/en/single-cell')    
      

      b.write("GSE176078")
      b.write("EGAD00001006608")


      c.write("26")
      c.write("31")

      d.write("14")
      d.write("15")

      e.write("53,255")
      e.write("41,120")  

   


     
     
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
      

