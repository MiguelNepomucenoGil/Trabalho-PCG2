import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide")

#leitura dos arquivos CSV e transformando em variavéis 


df_dengue = pd.read_csv("dengue24_mes.csv", sep=";", decimal='.', encoding='ISO-8859-1')
df_chuvas = pd.read_csv("chuvas sao paulo mensal.csv", sep=";", decimal=".", encoding='ISO-8859-1')


# colocando caracteres de separação na tabela
df_dengue = df_dengue.applymap(lambda x: str(x).replace(',', ''))




df_dengue
df_chuvas