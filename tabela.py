import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# leitura dos arquivos CSV e transformando em variáveis 
df_dengue = pd.read_csv("dengue24_mes.csv", sep=";", decimal='.', encoding='ISO-8859-1')
df_chuvas = pd.read_csv("chuvas sao paulo mensal.csv", sep=";", decimal=".", encoding='ISO-8859-1')

# colocando caracteres de separação na tabela
df_dengue = df_dengue.applymap(lambda x: str(x).replace(',', ''))

# *** Removendo a linha 4 (índice 3) do DataFrame df_chuvas ***
df_chuvas = df_chuvas.drop(df_chuvas.index[4])


# Criando filtros interativos
st.sidebar.title("Filtros")
opcao = st.sidebar.radio("Selecione a categoria:", ("Dados", "Gráficos"))

if opcao == "Dados":
    st.title("Dados")
    
    # Exibindo as tabelas diretamente, sem checkboxes
    st.subheader("Dados de Dengue")
    st.dataframe(df_dengue) # Usando st.dataframe para uma tabela mais simples

    st.subheader("Dados de Chuvas")
    st.dataframe(df_chuvas) # Usando st.dataframe para uma tabela mais simples

elif opcao == "Gráficos":
    st.title("Gráficos")

    # Selectbox para escolher o tipo de gráfico
    tipo_grafico = st.selectbox("Selecione o tipo de gráfico:", ("Gráfico de Linhas", "Gráfico de Barras"))

    if tipo_grafico == "Gráfico de Linhas":
        fig = px.line(df_dengue, x="Ano", y="Casos", title="Casos de Dengue por Ano")
        st.plotly_chart(fig)

    elif tipo_grafico == "Gráfico de Barras":
        fig = px.bar(df_dengue, x="Ano", y="Casos", title="Casos de Dengue por Ano")
        st.plotly_chart(fig)