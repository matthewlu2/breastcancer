import streamlit as st
import hydralit_components as hc
import pandas as pd
from PIL import Image

def correlation_page():

    option_data = [
   {'icon': "", 'label':i} for i in ['TF/Pathway Activity', 'Cytokine/Surface Receptor Genes', 'Contractome Genes', 'Cytoskeleton Genes']
    ]

    over_theme = {'txc_inactive': 'black','menu_background':'white','txc_active':'white','option_active':'#ff94b6'}
    font_fmt = {'font-class':'h2','font-size':'50%'}

    st.info("We combined the pre-treatment and BRCA ER-positive single-cell RNA sequencing (scRNA-seq) datasets obtained from Wu et al. (PMID: 34493872) (n=14) and Bassez et al. (PMID: 33958794) (n=15) yielding 90,532 cells from 29 tumors. Our analysis highlighted the key players in the ER-positive TME, including tumor-associated macrophages (TAMs), epithelial cancer cells (ECCs), endothelial cells, and T cells.")

    page = hc.option_bar(
        option_definition=option_data,
        title='',
        override_theme=over_theme,
        horizontal_orientation=True,
        )
    
    if page == 'TF/Pathway Activity':
        
        a, b, c = st.columns([.1, .8, .1])
        col1, col2, col3 = st.columns([.1, .8, .1])
        col4, col5, col6 = st.columns([.25, .6, .15])
        img1 = "./data/tam_data/Figure3A_1.png"
        img2 = "./data/tam_data/Figure3A_2.png"
        img3 = "./data/tam_data/SupplementaryFigure1E.png"

        b.image(img1)
        col2.image(img2)
        col5.image(img3)

    elif page == 'Cytokine/Surface Receptor Genes':

        a, b, c = st.columns([.1, .8, .1])
        col1, col2, col3 = st.columns([.1, .8, .1])
        img1 = "./data/tam_data/Figure3B_1.png"
        img2 = "./data/tam_data/Figure3B_2.png"
        b.image(img1)
        col2.image(img2)

    elif page == 'Contractome Genes':

        a, b, c = st.columns([.1, .8, .1])
        col1, col2, col3 = st.columns([.1, .8, .1])
        img1 = "./data/tam_data/Figure3C_1.png"
        img2 = "./data/tam_data/Figure3C_2.png"
        b.image(img1)
        col2.image(img2)

    elif page == 'Cytoskeleton Genes':
        
        a, b, c = st.columns([.1, .8, .1])
        col1, col2, col3 = st.columns([.1, .8, .1])

        img1 = "./data/tam_data/Figure3C_3.png"
        img2 = "./data/tam_data/Figure3C_4.png"
        b.image(img1)
        col2.image(img2)