import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import sys
from pathlib import Path

# Add the parent directory to system path
sys.path.append(str(Path(__file__).parent.parent))
from config import *

def show_bpstat_tab(df):
    """

    """
    st.header("Risk drivers")
    
    # Start with a compelling problem statement
    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-radius: 10px; border-left: 5px solid #179297; margin-bottom: 20px;">
    <h4 style="color: #179297; margin-top: 0;">Overview</h4>
    <p>....</p>
    <ul>
      <li><strong>Tendências Principais:</strong> .....</li>

    </ul>
    </div>
    """, unsafe_allow_html=True)

    #st.dataframe(df, use_container_width=True)

    # Add a selectbox for sector selection
    sector = st.selectbox(
        "Select the business sector to analyze:",
        ldp_sectors, index=0)
    
    if sector == 'All':
        df_filtered = df[medium_all_columns]
    else:
        df_filtered = df.filter(like=sector)
    
    st.dataframe(df_filtered, use_container_width=True)

    
