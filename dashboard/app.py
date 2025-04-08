import os
import numpy as np
import pandas as pd
import streamlit as st
from config import *
from get_data import *

from tabs.tab0_general_overview import *
from tabs.tab1_pca import * #show_geographic_analysis_tab
from tabs.tab2_macroeconomic_analysis import * #show_housing_distribution_tab
from tabs.tab3_bpstat_analysis import * #show_satisfaction_levels_tab
from tabs.tab4_concatdata_analysis import *

# Set page configuration
st.set_page_config(layout="wide", page_title="LDPs calibration dashboard")

start_date = '2006-01-01'

# Define function to load data
@st.cache_data
def load_data(ttl=3600*24):
    try:
        # macroeconomic data
        macro_ecb_data = process_ecb_indicators(MAP_CATEGORIES_ECB_INDICADORS_URLS, start_date=start_date) # annual data (number)
        
        df_unemployment = extract_data_from_ecb( # monthly data (start of period)
            MAP_OTHER_ECB_INDICATORS["Unemployment rate"]['url'].split("datasets/")[1].split('/')[1] ,
              start_date).rename(columns={''
              'TIME_PERIOD': 'Date',
              'OBS_VALUE': 'Unemployment rate'})                                                                                                                                            
        
        df_labour_prod = extract_data_from_ecb( # quarterly data (start of period)
            MAP_OTHER_ECB_INDICATORS["Labour Productivity (per persons)"]['url'].split("datasets/")[1].split('/')[1],
              start_date).rename(
                columns={'TIME_PERIOD': 'Date',
                         'OBS_VALUE': 'Labour Productivity (per persons)'})   
        
        df_inflation = extract_data_from_bank_pt( # monthly data (end of period)
            MAP_OTHER_BPSTAT_INDICATORS["CPI (Consumer Price Index) MA12"]['url'], None) 
         
        df_euribors = extract_euribors(start_date) # monthly data (start of period)

        # LDPs data (Small companies)  
        #df_small_ldp = get_ldp_data(SMALL_ENTREPRISE_MAP_INDICATORS_KEYS)
        
        # LDPs data (Medium companies)
        df_medium_ldp = get_ldp_data(MEDIUM_ENTREPRISE_MAP_INDICATORS_KEYS)
        # LDPs data (Large companies)
        #df_large_ldp = get_ldp_data(LARGE_ENTREPRISE_MAP_INDICATORS_KEYS)
        # LDPs data (All companies)
        #df_all_ldp= get_ldp_data(ALL_ENTREPRISE_MAP_INDICATORS_KEYS)

        return macro_ecb_data, df_unemployment, df_labour_prod, df_inflation, df_euribors, df_medium_ldp
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()  # Return empty dataframe if loading fails


# Load the data from the web
macro_ecb_data, df_unemployment, df_labour_prod, df_inflation, df_euribors, df_medium_ldp = load_data()

# Create dashboard title and introduction
st.image("design docs/travel.webp",width=250)

st.markdown(
    """
    <h3 style='color: #179297;'>Company type selection</h3>
    """,
    unsafe_allow_html=True
)

# Add a selectbox for company type selection
company_type = st.selectbox(
    "Select the type of companies to analyze:",
    ["Small", "Medium", "Large", "All"]
)

# Set file path based on company type
if company_type == "All":
    # fazer update para all
    df_ldp = df_medium_ldp.copy()

elif company_type == "Small":
    # fazer update para small
    df_ldp = df_medium_ldp.copy()

elif company_type == "Medium":

    df_ldp = df_medium_ldp.copy()

elif company_type == "Large":
    # fazer update para large
    df_ldp = df_medium_ldp.copy()


# Create tabs for different insights
tab0, tab1, tab2, tab3, tab4 = st.tabs([
    "General overview",
    "Principal Components Analysis", 
    "Macroeconomic data analysis", 
    "BPSTAT data analysis", 
    "Macroeconomic data vs Risk drivers"
])

with tab0:
    show_visao_geral_tab(df_unemployment, df_euribors, macro_ecb_data, df_labour_prod, df_inflation, df_ldp, company_type)

with tab1:
    plot_pca_results(df_medium_ldp)

with tab2:
    show_macrodata_tab(
        macro_ecb_data, df_unemployment, df_labour_prod, df_inflation, df_euribors
    )

with tab3:
    show_bpstat_tab(df_ldp)

with tab4:
    show_housing_types_sizes_tab()