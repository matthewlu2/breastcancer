import streamlit as st
import hydralit_components as hc
import pandas as pd
from PIL import Image




def correlation_2_page():

    IMG_REPO1 = 'https://raw.githubusercontent.com/matthewlu2/bc_data/main/11a_OutgridLinedotplot_Correl_PathwayActivity_GeneExp_ColorTAMFract_Endo/'
    IMG_REPO2 = 'https://raw.githubusercontent.com/matthewlu2/bc_data/main/11e_OutgridLinedotplot_Correl_PathwayActivity_GeneExp_ColorTAMFract_EpiCan/'
    IMG_REPO3 = 'https://raw.githubusercontent.com/matthewlu2/bc_data/main/11f_OutgridLinedotplot_Correl_PathwayActivity_GeneExp_ColorTAMFract_CD8T/'
    IMG_REPO4 = 'https://raw.githubusercontent.com/matthewlu2/bc_data/main/11j_OutgridLinedotplot_Correl_PathwayActivity_GeneExp_ColorTAMFract_TAM/'


    
    option_data = [
    {'icon': "", 'label':i} for i in ['TAM', 'CCD8+T Cell', 'Endothelial Cell', 'Epithelial Cancer Cell']
        ]

    over_theme = {'txc_inactive': 'black','menu_background':'white','txc_active':'white','option_active':'#ff94b6'}
    font_fmt = {'font-class':'h2','font-size':'50%'}

    st.info("Correlation between pathway activities inferred by PROGENy and gene expressions in TAM, CD8+ T cells, Endothelial cells, and Epithelial Cancer cells. The mean of the gene expression and pathway activities were calculated in each patient and the color of each dot represents the TAM proportion in individual patients. The correlation coefficient was calculated by Spearman method.")

    legend = "./data/Legend_MacrophageInfiltrationColor.png"

    page = hc.option_bar(
        option_definition=option_data,
        title='',
        override_theme=over_theme,
        horizontal_orientation=True,
        )
    
    if page == 'Endothelial Cell':
      

        file = open('data/textfiles/long_list_a.txt', 'r')
        list = file.read().splitlines()

        option = st.selectbox(
        'Gene of Interest',
        (list)) 

        front = 'OutgridDotplot_Correl_'
        back = '_Exp_PathwayActivity_Endothelial'

        img = f'{IMG_REPO1}/{front}{option}{back}.png'
        a, b, c, d = st.columns([.2, .6, .1, .2])
        b.image(img)
        c.image(legend)


    elif page == 'Epithelial Cancer Cell':

        file = open('data/textfiles/long_list_e.txt', 'r')
        list = file.read().splitlines()

        option = st.selectbox(
        'Gene of Interest',
        (list)) 

        front = 'OutgridDotplot_Correl_'
        back = '_Exp_PathwayActivity_EpithelialCancer'

        img = f'{IMG_REPO2}/{front}{option}{back}.png'
        a, b, c, d = st.columns([.2, .6, .1, .2])
        b.image(img)
        c.image(legend)

    elif page == 'CCD8+T Cell':
        
        file = open('data/textfiles/long_list_f.txt', 'r')
        list = file.read().splitlines()

        option = st.selectbox(
        'Gene of Interest',
        (list)) 

        front = 'OutgridDotplot_Correl_'
        back = '_Exp_PathwayActivity_CD8Tcell'

        img = f'{IMG_REPO3}/{front}{option}{back}.png'
        a, b, c, d = st.columns([.2, .6, .1, .2])
        b.image(img)
        c.image(legend)

    elif page == 'TAM':

        file = open('data/textfiles/long_list_j.txt', 'r')
        list = file.read().splitlines()

        option = st.selectbox(
        'Gene of Interest',
        (list)) 

        front = 'OutgridDotplot_Correl_'
        back = '_Exp_PathwayActivity_Macrophage'

        img = f'{IMG_REPO4}/{front}{option}{back}.png'
        a, b, c, d = st.columns([.2, .6, .1, .2])
        b.image(img)
        c.image(legend)