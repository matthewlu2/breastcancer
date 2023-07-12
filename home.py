import streamlit as st
import hydralit_components as hc
from PIL import Image
import streamlit_analytics

def home_page():

    streamlit_analytics.start_tracking()
    streamlit_analytics.stop_tracking()
    
    img = "./data/Fig1_HomePage.png"

    st.markdown("<h2 style='text-align: center;  color: Black;'>Single-cell analysis reveals S100A11 recruits tumor-associated macrophages to epithelial cancer cells in the microenvironment of ER+ breast cancer</h1>", unsafe_allow_html=True)
    st.write("")
    st.image(img)
    st.markdown('➡️ Read our paper here: https://www.google.com')    
    st.write("The tumor microenvironment (TME) plays a critical role in tumor progression and includes heterogeneous cell types that can have pro-tumorigenic (e.g., immunosuppressive macrophages) and anti-tumorigenic cells (e.g. cytotoxic T cells). Among the most abundant cell types in the TME, an inflammatory cell population such as tumor-associated macrophage (TAM), is an influential component for tumor growth, metastasis, and immune-therapeutic response, which has potential to provide diagnostic and prognostic biomarkers. However, TAM-based biomarkers that predict tumor aggressiveness and the complex interaction network with cancer cells and other immune cells in breast TME remain unexplored. We characterized TAM infiltration and gene signatures associated with tumor characteristics using an integrative scRNA-seq analysis of ER-positive breast tumors (n=29) from two independent public datasets. We found that TAMs were enriched in the patients with high fraction of epithelial cancer cell (ECCs), but not in ones with low fraction of CD4+/CD8+ T-cells and B-cells, as well as a distinct transcriptomic landscape. Next analyses identified the associations between TAMs and cell type specific intracellular signaling transcripts or cancer cell derived factors. Especially, the expression S100A11, which is involved in cytoskeleton rearrangement, cell migration/invasion, and tumor progression, is positively associated with TAM infiltration in ECCs. We further validated that S100A11 promotes monocyte/macrophage recruitment in ER-positive BRCA cell lines and organoid models using 3D in vitro platform. This study reveals the cell-type specific relationship between TAMs and S100A11 expression in human breast tumor and elucidates the interactions with cancer cells or other immune cells.")