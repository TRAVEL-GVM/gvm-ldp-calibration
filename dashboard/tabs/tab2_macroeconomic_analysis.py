import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import sys
from pathlib import Path

# Add the parent directory to system path
sys.path.append(str(Path(__file__).parent.parent))
from config import *

def show_macrodata_tab(macro_ecb_df, unemployment_df, labour_prod_df, inflation_df, euribors_df):
    """

    """
    st.header("Macroeconomic data")
    
    # Start with a compelling problem statement
    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-radius: 10px; border-left: 5px solid #179297; margin-bottom: 20px;">
    <h4 style="color: #179297; margin-top: 0;">Overview</h4>
    <p>Esta análise revela insights importantes.</p>
    <ul>
      <li><strong>Tendências Principais:</strong>...</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.dataframe(macro_ecb_df, use_container_width=True)

    st.dataframe(unemployment_df, use_container_width=True)

    st.dataframe(labour_prod_df, use_container_width=True)

    st.dataframe(inflation_df, use_container_width=True)

    st.dataframe(euribors_df, use_container_width=True)