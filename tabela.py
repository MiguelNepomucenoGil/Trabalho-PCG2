import streamlit as st
import pandas as pd
import plotly.express as px

# Faz com que o gráfico ocupe a largura máxima
st.set_page_config(layout="wide")

# Lê os arquivos CSV, transformando em variáveis
df_euroleague = pd.read_csv("EUROLEAGUE.csv", sep=";", decimal=".")
df_nba = pd.read_csv("NBA.csv", sep=";", decimal='.')

# Separa colunas e remove vírgulas
df_euroleague = df_euroleague.applymap(lambda x: str(x).replace(',', ''))
df_nba = df_nba.applymap(lambda x: str(x).replace(',', ''))

# Converte colunas numéricas para float
for coluna in ['GP', 'MIN', '3PA', 'FTM', 'FTA', 'TOV', 'REB', 'AST', 'STL', 'BLK', 'PTS']:
    df_euroleague[coluna] = pd.to_numeric(df_euroleague[coluna], errors='coerce')
    df_nba[coluna] = pd.to_numeric(df_nba[coluna], errors='coerce')

# Renomeia as colunas
df_euroleague = df_euroleague.rename(columns={'League': 'Liga',
                                             'Season': 'Temporada',
                                             'Player': 'Jogador',
                                             'Team': 'Time'})

df_nba = df_nba.rename(columns={'League': 'Liga',
                                'Season': 'Temporada',
                                'Player': 'Jogador',
                                'Team': 'Time'})

# Define as categorias para a seleção
categorias = ['EuroLeague', 'NBA', 'Definições','Comparação']

# Adiciona um menu para a seleção da categoria
categoria_selecionada = st.sidebar.selectbox("Selecione a liga:", categorias)



# Exibe o dataframe da categoria selecionada
if categoria_selecionada == 'EuroLeague':
    st.header('EuroLeague')
    st.dataframe(df_euroleague)
elif categoria_selecionada == 'NBA':
    st.header('NBA')
    st.dataframe(df_nba)
elif categoria_selecionada == 'Definições':
    st.header('Definições das Abreviações')
    st.markdown("""
    **Abreviações Estatísticas:**
    
    * **GP:** Jogos Jogados
    * **MIN:** Minutos Jogados
    * **3PA:** Arremessos de Três Pontos Tentados
    * **FTM:** Lance Livre Convertido
    * **FTA:** Lance Livre Tentado
    * **TOV:** Turnover (Perda de Bola)
    * **REB:** Rebotes
    * **AST:** Assistências
    * **STL:** Roubos de Bola
    * **BLK:** Bloqueios
    * **PTS:** Pontos
    """)
elif categoria_selecionada == 'Comparação':
    st.header('Comparação EuroLeague e NBA')
    colunas_comparacao = ['GP', 'MIN', '3PA', 'FTM', 'FTA', 'TOV', 'REB', 'AST', 'STL', 'BLK', 'PTS']
    
    # Cria um menu para a seleção do tipo de gráfico
    tipo_grafico = st.selectbox("Selecione o tipo de gráfico:", ['Barras', 'Dispersão', 'Linhas', 'Caixa'])

    # Cria um menu para a seleção da coluna para comparação
    coluna_selecionada = st.selectbox("Selecione a coluna para comparação:", colunas_comparacao)

    # Cria os gráficos de acordo com o tipo selecionado
    if tipo_grafico == 'Barras':
        fig = px.histogram(df_euroleague, x=coluna_selecionada, title=f'Histograma - {coluna_selecionada} - EuroLeague')
        fig2 = px.histogram(df_nba, x=coluna_selecionada, title=f'Histograma - {coluna_selecionada} - NBA')
        st.plotly_chart(fig)
        st.plotly_chart(fig2)

    elif tipo_grafico == 'Dispersão':
        fig = px.scatter(df_euroleague, x='MIN', y=coluna_selecionada, title=f'Dispersão - {coluna_selecionada} vs MIN - EuroLeague')
        fig2 = px.scatter(df_nba, x='MIN', y=coluna_selecionada, title=f'Dispersão - {coluna_selecionada} vs MIN - NBA')
        st.plotly_chart(fig)
        st.plotly_chart(fig2)

    elif tipo_grafico == 'Linhas':
        fig = px.line(df_euroleague, x='Jogador', y=coluna_selecionada, title=f'{coluna_selecionada} por Jogador - EuroLeague')
        fig2 = px.line(df_nba, x='Jogador', y=coluna_selecionada, title=f'{coluna_selecionada} por Jogador - NBA')
        st.plotly_chart(fig)
        st.plotly_chart(fig2)

    elif tipo_grafico == 'Caixa':
        # Combine os dataframes para o gráfico de caixa
        df_comparacao = pd.concat([df_euroleague, df_nba])
        df_comparacao['Liga'] = df_comparacao['Liga'].fillna('EuroLeague')  # Preenche valores faltantes para a coluna 'Liga'
        fig = px.box(df_comparacao, x='Liga', y=coluna_selecionada, title=f'Caixa - {coluna_selecionada} - EuroLeague vs NBA')
        st.plotly_chart(fig)