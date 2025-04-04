import json
import sys
from pathlib import Path

import folium
import plotly.express as px
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static

# Add the parent directory to system path
sys.path.append(str(Path(__file__).parent.parent))
from config import SATISFACTION_COLORS, HOUSING_COLORS, BACKGROUND_COLORS, TEXT_COLORS


def show_visao_geral_tab():
    """
    Display the Overview (Visão Geral) tab with key metrics, interactive map, and affordability simulator.

    Parameters:
    df (DataFrame): The processed housing data
    """

    # Header and Key Metrics Row with enhanced styling
    st.markdown(
        """
    <style>
    .metric-card {
        background-color: #e8f5e9;
        border-radius: 10px;
        padding: 15px;
        margin: 5px 0px 5px 0px;
        text-align: center;
        justify-content: center;
        height: 100%;
    }
    .metric-value {
        font-size: 32px;
        font-weight: bold;
        color: #179297;
        margin: 5px 0;
    }
    .metric-label {
        font-size: 16px;
        color: #179297;
        margin-bottom: 10px;
    }
    .metric-icon {
        font-size: 32px;
        color: #179297;
        margin-top: 5px;
    }
    .section-divider {
        height: 2px;
        background: linear-gradient(to right, #e8f5e9, #179297, #e8f5e9);
        margin: 30px 0 20px 0;
        border-radius: 2px;
    }    
    .section-divider-space{
        margin: 30px 0 20px 0;
    }
    .header-title {
        color: #179297;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .header-subtitle {
        color: #179297; 
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .info-card {
        background-color: #f1f8e9;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
    }
    .info-card-2 {
        background-color: #f1f8e9; 
        padding: 15px; 
        border-radius: 8px; 
        margin-bottom: 20px; 
        border-left: 4px solid #66bb6a;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    st.header("General overview")

    col1, col2, col3, col4, col5 = st.columns(5)


    with col1:
        st.markdown(
            f"""
        <div class="metric-card">
            <div class="metric-label">IPC TVH</div>
            <div class="metric-value">{5}</div>
            <div class="metric-icon">👥</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
        <div class="metric-card">
            <div class="metric-label">EURIBOR</div>
            <div class="metric-value">{5:.1f}%</div>
            <div class="metric-icon">🏠</div>
        </div>
        """,
            unsafe_allow_html=True,
            )

    with col3:
        st.markdown(
            f"""
        <div class="metric-card">
            <div class="metric-label">DESEMPREGO</div>
            <div class="metric-value">{5:.1f}%</div>
            <div class="metric-icon">🏢</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            f"""
        <div class="metric-card">
            <div class="metric-label">PIB</div>
            <div class="metric-value">{5:.1f}%</div>
            <div class="metric-icon">👪</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col5:
        st.markdown(
            f"""
        <div class="metric-card">
            <div class="metric-label">XYZ</div>
            <div class="metric-value">{5:.1f}/5</div>
            <div class="metric-icon">⭐</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # Add a styled divider and enhanced text
    st.markdown(
        """
    <div class="section-divider-space"></div>
    """,
        unsafe_allow_html=True,
    )