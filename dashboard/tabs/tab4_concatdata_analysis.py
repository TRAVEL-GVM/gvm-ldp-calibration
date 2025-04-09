import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import sys
from pathlib import Path

# Add the parent directory to system path
sys.path.append(str(Path(__file__).parent.parent))
from config import *

def show_macro_vs_riskdrivers_tab(df):
    """

    """

    with st.expander("📊 Analysis Overview", expanded=True):
        st.markdown("""
        <div style="background-color: #e8f5e9; padding: 20px; border-radius: 10px; border-left: 5px solid #179297; margin-bottom: 20px;">
        <h4 style="color: #179297; margin-top: 0;">Macroeconomic data vs Risk drivers</h4>
        <p>This section provides tools to analyze macroeconomic data vs BPSTAT data and identify key trends and relationships. Use the following features to explore the data:</p>
        <ul>
        <li><strong>Data Preview:</strong> View the first few rows of the dataset for a quick overview.</li>
        <li><strong>Time Series Plots:</strong> Generate line plots for selected variables to observe trends over time.</li>
        <li><strong>Sector Analysis:</strong> Select specific sectors or variables to focus your analysis.</li>
        <li><strong>Correlation Matrix:</strong> Visualize relationships between variables using a triangular correlation heatmap.</li>
        </ul>
        <p>These tools are designed to help you uncover patterns and dependencies in the data, enabling better decision-making and insights into macroeconomic trends.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🔍 Data Preview (first 3 rows)", expanded=False):
        st.write("Preview of the dataset:")
        st.dataframe(df)

    with st.expander("📈 Time Series Plots", expanded=True):
        st.write("Select variables to plot:")
        pass

    with st.expander("📊 Correlation Matrix", expanded=True):
        st.write("Visualize relationships between variables:")
        pass

