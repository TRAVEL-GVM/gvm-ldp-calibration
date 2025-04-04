import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import sys
from pathlib import Path

# Add the parent directory to system path
sys.path.append(str(Path(__file__).parent.parent))
from config import *

def show_housing_types_sizes_tab():
    """

    """
    st.header("Macroeconomic data vs Risk drivers")
    
    # Start with a compelling problem statement
    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-radius: 10px; border-left: 5px solid #2e7d32; margin-bottom: 20px;">
    <h4 style="color: #2e7d32; margin-top: 0;">Overview</h4>
    <p>Esta análise revela insights importantes sobre .....</p>
    <ul>
      <li><strong>Tendências Principais:</strong> ....</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)