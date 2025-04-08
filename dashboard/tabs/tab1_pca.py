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

    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-radius: 10px; border-left: 5px solid #179297; margin-bottom: 20px;">
    <ul>
    <li><strong>Variance Explained Proportion:</strong> Shows the proportion of variance explained by each principal component. It helps identify which components capture the most variability in the dataset.</li>
    <li><strong>Cumulative Variance Explained:</strong> Displays the cumulative variance explained by the principal components. It indicates how much of the total variance is captured as more components are added, helping to decide the optimal number of components to retain.</li>
    <li><strong>Eigenvalues (Keiser Method):</strong> Shows the eigenvalues associated with each principal component. Components with eigenvalues greater than 1 are considered significant according to the Keiser criterion.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

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
        eigenvectors = pca.components_
        fatores_x = [f'F{i}' for i in range(1, num_factors + 1)]
        cumulative_variance = np.cumsum(explained_variance_ratio)

        # ======== Plot com Plotly (3 Colunas) ========
        col1, col2, col3 = st.columns(3)

        # 1. Variância explicada
        with col1:
            fig1 = px.bar(
                x=fatores_x,
                y=explained_variance_ratio,
                labels={"x": "Factors", "y": "Variance explained proportion"},
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
                labels={"x": "Factors", "y": "Cumulative Variance Explained"},
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
                labels={"x": "Factors", "y": "Eigenvalues"},
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

        st.write("#")

        # ======== Scatterplot ========
        df_pca = pd.DataFrame(X_pca, columns=factor_options)
        df_pca['Date'] = dates.values

        col_scatter, col_eig = st.columns(2)

        with col_scatter:
            plt.figure(figsize=(4, 3))  

            sns.scatterplot(
                data=df_pca,
                x=x_factor,
                y=y_factor,
                color="#179297",  
                s=20,  
                edgecolor="black" 
            )

            st.markdown(
                f"""
                <h3 style='color: #179297;'>Principal Component Analysis: {x_factor} vs {y_factor}:</h3>
                """,
                unsafe_allow_html=True
            )

            # Obter a proporção de variância explicada para os fatores selecionados
            x_variance = explained_variance_ratio[factor_options.index(x_factor)]
            y_variance = explained_variance_ratio[factor_options.index(y_factor)]

            # Atualizar os rótulos dos eixos com a proporção de variância explicada
            plt.xlabel(f"{x_factor} ({x_variance:.2%} explained variance)", fontsize=7)
            plt.ylabel(f"{y_factor} ({y_variance:.2%} explained variance)", fontsize=7)

            for i in range(len(df_pca)):
                plt.text(
                df_pca[x_factor][i],
                df_pca[y_factor][i] +.05,
                str(df_pca['Date'][i].year),  
                fontsize=5,
                ha='center',
                va='bottom'
            )
            
            plt.xticks(fontsize=6)  
            plt.yticks(fontsize=6)

            plt.grid(True, linestyle='--', alpha=0.5)
            plt.tight_layout()

            st.pyplot(plt, clear_figure=True)

        with col_eig:
            st.markdown(
                """
                <h3 style='color: #179297;'>Eigenvectors matrix:</h3>
                """,
                unsafe_allow_html=True
            )
            st.dataframe(pd.DataFrame(eigenvectors, columns=df_for_pca.columns, index=fatores_x).T, use_container_width=True)
        
    except Exception as e:
        st.error("There is no enough data to perform PCA.")
