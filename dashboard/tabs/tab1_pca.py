import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import streamlit as st
from datetime import datetime
from config import *
#from viz import *


def plot_pca_results(df):

    current_year = datetime.now().year
    date2 = str(current_year - 1) + '-01-01'
    df = df[(df['Date'] >= '2008-01-01') & (df['Date'] <= date2)]
    
    # Add a selectbox for sector selection with a unique key
    sector = st.selectbox(
        "Select the business sector to analyze:",
        ldp_sectors, index=0, key="sector_selectbox_tab1"
    )
    
    if sector == 'All':
        df_filtered = df[medium_all_columns]
    else:
        df_filtered = df.filter(like=sector)
        if 'Date' not in df_filtered.columns:
            df_filtered['Date'] = df['Date']
            df_filtered = df_filtered[['Date'] + [col for col in df_filtered.columns if col != 'Date']]

    # Eliminar colunas com mais de 30% de valores nulos
    threshold = int(0.7 * df_filtered.shape[0])  # Pelo menos 70% de valores não nulos
    df_filtered = df_filtered.dropna(thresh=threshold, axis=1)

    # Eliminar linhas que ainda tiverem pelo menos um valor nulo
    df_filtered = df_filtered.dropna(axis=0)


    ###################################################

    dates = df_filtered['Date']
    df_for_pca = df_filtered[df_filtered.columns[1:]]  # remove 'Date'
    st.write("Shape dos dados para PCA:", df_for_pca.shape)

    try:
        # Escalar os dados
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(df_for_pca.values)

        max_factors = len(df_for_pca.columns)
        num_factors = st.slider(
            "Select the number of factors for PCA:",
            min_value=2,
            max_value=max_factors,
            value=min(2,5),  
            step=1
        )

        # Aplicar PCA com o número de fatores selecionado
        pca = PCA(n_components=num_factors)
        X_pca = pca.fit_transform(X_scaled)

        # Atualizar os fatores e variáveis relacionadas
        eigenvalues = pca.explained_variance_
        explained_variance_ratio = pca.explained_variance_ratio_
        fatores_x = [f'F{i}' for i in range(1, num_factors + 1)]
        cumulative_variance = np.cumsum(explained_variance_ratio)

        # ======== Plot com Plotly (3 Colunas) ========
        col1, col2, col3 = st.columns(3)

        # 1. Variância explicada
        with col1:
            fig1 = px.bar(
                x=fatores_x,
                y=explained_variance_ratio,
                labels={"x": "Fatores", "y": "Variance explained proportion"},
                title="Variance explained proportion",
                text=[f"{v:.2f}" for v in explained_variance_ratio]
            )
            fig1.update_traces(textposition="outside", marker_color="#179297")
            fig1.update_layout(height=400, margin=dict(l=20, r=20, t=40, b=20))
            st.plotly_chart(fig1, use_container_width=True)

        # 2. Variância acumulada
        with col2:
            fig2 = px.bar(
                x=fatores_x,
                y=cumulative_variance,
                labels={"x": "Fatores", "y": "Cumulative Variance Explained"},
                title="Cumulative Variance Explained",
                text=[f"{v:.2f}" for v in cumulative_variance]
            )
            fig2.update_traces(textposition="outside", marker_color="pink")
            fig2.update_layout(height=400, margin=dict(l=20, r=20, t=40, b=20))
            st.plotly_chart(fig2, use_container_width=True)

        # 3. Eigenvalues (Keiser)
        with col3:
            fig3 = px.bar(
                x=fatores_x,
                y=eigenvalues,
                labels={"x": "Fatores", "y": "Eigenvalues"},
                title="Keiser Method (Eigenvalues)",
                text=[f"{v:.2f}" for v in eigenvalues]
            )
            fig3.update_traces(textposition="outside", marker_color="#e8f5e9")
            fig3.update_layout(height=400, margin=dict(l=20, r=20, t=40, b=20))
            st.plotly_chart(fig3, use_container_width=True)

        # Adicionar opções para selecionar os fatores a serem representados no scatter plot
        factor_options = [f'F{i+1}' for i in range(num_factors)]

        col10, col11 = st.columns(2)
        with col10:
            x_factor = st.selectbox(
                "Select the factor for the X-axis:",
                options=factor_options,
                index=0,  # Default to the first factor
                key="scatter_x_factor"
            )
        with col11:
            y_factor = st.selectbox(
                "Select the factor for the Y-axis:",
                options=factor_options,
                index=1 if len(factor_options) > 1 else 0,  # Default to the second factor if available
                key="scatter_y_factor"
            )

        # ======== Scatterplot Interativo com Plotly ========
        df_pca = pd.DataFrame(X_pca, columns=factor_options)
        df_pca['Date'] = dates.values

        fig_scatter = px.scatter(
            df_pca, x=x_factor, y=y_factor,
            color='Date', text='Date',
            title=f'PCA: {x_factor }e {y_factor}',
            labels={'F1': 'Componente HUJOIPrincipal 1', 'F2': 'Componente Principal 2'}
        )
        fig_scatter.update_layout(
            height=600,  # Altura do gráfico
            width=400,   # Largura do gráfico
        )

        # Exibir o gráfico no Streamlit
        st.plotly_chart(fig_scatter, use_container_width=True)
        
    except Exception as e:
        st.error("Não há dados suficientes para plotar os gráficos.")
