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
categorias = ['Dados','Comparação Liga','Comparação Jogadores']

# Adiciona um menu para a seleção da categoria
categoria_selecionada = st.sidebar.selectbox("Selecione a liga:", categorias)


# Exibe o dataframe da categoria selecionada
if categoria_selecionada == 'Dados':
    st.header('Dados')
    st.text('Euroleague')
    st.dataframe(df_euroleague)
    st.text('NBA')
    st.dataframe(df_nba)
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
    
elif categoria_selecionada == 'Comparação Liga':
    st.header('Comparação EuroLeague e NBA')
    colunas_comparacao_dict = {
        'Jogos Jogados': 'GP',
        'Minutos Jogados': 'MIN',
        'Arremessos de Três Pontos Tentados': '3PA',
        'Lance Livre Convertido': 'FTM',
        'Lance Livre Tentado': 'FTA',
        'Turnover (Perda de Bola)': 'TOV',
        'Rebotes': 'REB',
        'Assistências': 'AST',
        'Roubos de Bola': 'STL',
        'Bloqueios': 'BLK',
        'Pontos': 'PTS'
    }
    
    # Inverso do dicionário para mapeamento posterior
    colunas_comparacao_inv_dict = {v: k for k, v in colunas_comparacao_dict.items()}

    # Cria um menu para a seleção do tipo de gráfico
    tipo_grafico = st.selectbox("Selecione o tipo de gráfico:", ['Barras', 'Dispersão', 'Linhas', 'Caixa'])

    # Cria um menu para a seleção da coluna para comparação
    coluna_selecionada_renomeada = st.selectbox("Selecione a coluna para comparação:", list(colunas_comparacao_dict.keys()))

    # Obtém o nome original da coluna selecionada
    coluna_selecionada = colunas_comparacao_dict[coluna_selecionada_renomeada]
    
    # Cria os gráficos de acordo com o tipo selecionado
    if tipo_grafico == 'Barras':
        combined_df = pd.concat([df_euroleague, df_nba], ignore_index=True)
        # st.write("DataFrame Combinado:")
        # st.write(combined_df)

        # Agrupar por Liga e somar os valores da coluna selecionada
        summed_df = combined_df.groupby('Liga')[coluna_selecionada].sum().reset_index()
        
        # Mostra o DataFrame somado
        # st.write("DataFrame com Valores Somados:")
        # st.write(summed_df)

        # Cria o gráfico de barras
        fig = px.bar(summed_df, x='Liga', y=coluna_selecionada, title=f'Soma de {coluna_selecionada} por Liga')
        st.plotly_chart(fig)

    elif tipo_grafico == 'Dispersão':
        combined_df = pd.concat([df_euroleague, df_nba], ignore_index=True)
        # st.write("DataFrame Combinado:")
        # st.write(combined_df)

        # Agrupar por Liga e somar os valores da coluna selecionada
        summed_df = combined_df.groupby('Liga')[coluna_selecionada].sum().reset_index()
        
        # Mostra o DataFrame somado
        # st.write("DataFrame com Valores Somados:")
        # st.write(summed_df)

        # Cria o gráfico de Dispersão
        fig = px.scatter(summed_df, x='Liga', y=coluna_selecionada, title=f'Soma de {coluna_selecionada} por Jogador')
        st.plotly_chart(fig)

    elif tipo_grafico == 'Linhas':       
        combined_df = pd.concat([df_euroleague, df_nba], ignore_index=True)
        
        # Agrupar por Liga e somar os valores da coluna selecionada
        summed_df = combined_df.groupby('Liga')[coluna_selecionada].sum().reset_index()
        
        # Cria o gráfico de Linhas
        fig = px.line(summed_df, x='Liga', y=coluna_selecionada, title=f'Soma de {coluna_selecionada} por Jogador')
        st.plotly_chart(fig)

    elif tipo_grafico == 'Caixa':
        combined_df = pd.concat([df_euroleague, df_nba], ignore_index=True)
        
        # Agrupar por Liga e somar os valores da coluna selecionada
        summed_df = combined_df.groupby('Liga')[coluna_selecionada].sum().reset_index()
                
        # Cria o gráfico de Linhas
        fig = px.box(summed_df, x='Liga', y=coluna_selecionada, title=f'Soma de {coluna_selecionada} por Jogador')
        st.plotly_chart(fig)
    
elif categoria_selecionada == 'Comparação Jogadores':
    st.header('Comparação EuroLeague e NBA')
    colunas_comparacao_dict = {
        'Jogos Jogados': 'GP',
        'Minutos Jogados': 'MIN',
        'Arremessos de Três Pontos Tentados': '3PA',
        'Lance Livre Convertido': 'FTM',
        'Lance Livre Tentado': 'FTA',
        'Turnover (Perda de Bola)': 'TOV',
        'Rebotes': 'REB',
        'Assistências': 'AST',
        'Roubos de Bola': 'STL',
        'Bloqueios': 'BLK',
        'Pontos': 'PTS'
    }
    
    # Inverso do dicionário para mapeamento posterior
    colunas_comparacao_inv_dict = {v: k for k, v in colunas_comparacao_dict.items()}

    # Cria um menu para a seleção do tipo de gráfico
    tipo_grafico = st.selectbox("Selecione o tipo de gráfico:", ['Barras', 'Dispersão', 'Linhas', 'Caixa'])

    # Cria um menu para a seleção da coluna para comparação
    coluna_selecionada_renomeada = st.selectbox("Selecione a coluna para comparação:", list(colunas_comparacao_dict.keys()))

    # Obtém o nome original da coluna selecionada
    coluna_selecionada = colunas_comparacao_dict[coluna_selecionada_renomeada]
    
    # Adiciona uma seleção para a liga a ser exibida
    ligas_selecionadas = st.multiselect("Selecione as ligas para exibição:", ['NBA', 'Euroleague'], default=['NBA', 'Euroleague'])

    # Cria os gráficos de acordo com o tipo selecionado
    if tipo_grafico == 'Barras':
        combined_df = pd.concat([df_euroleague, df_nba], ignore_index=True)
        # st.write("DataFrame Combinado:")
        # st.write(combined_df)

        # Filtra os dados com base nas ligas selecionadas
        filtered_df = combined_df[combined_df['Liga'].isin(ligas_selecionadas)]

        # Agrupar por Liga e somar os valores da coluna selecionada
        summed_df = filtered_df.groupby('Jogador')[coluna_selecionada].sum().reset_index()
        
        # Ordenar do maior para o menor e selecionar os top 10
        summed_df = summed_df.sort_values(by=coluna_selecionada, ascending=False).head(10)

        # Mostra o DataFrame somado
        # st.write("DataFrame com Valores Somados:")
        # st.write(summed_df)

        # Cria o gráfico de barras
        fig = px.bar(summed_df, x='Jogador', y=coluna_selecionada, title=f'Soma de {coluna_selecionada} por Jogador')
        st.plotly_chart(fig)

    elif tipo_grafico == 'Dispersão':
        combined_df = pd.concat([df_euroleague, df_nba], ignore_index=True)
        # st.write("DataFrame Combinado:")
        # st.write(combined_df)

        # Filtra os dados com base nas ligas selecionadas
        filtered_df = combined_df[combined_df['Liga'].isin(ligas_selecionadas)]

        # Agrupar por Liga e somar os valores da coluna selecionada
        summed_df = filtered_df.groupby('Jogador')[coluna_selecionada].sum().reset_index()
        
        # Ordenar do maior para o menor e selecionar os top 10
        summed_df = summed_df.sort_values(by=coluna_selecionada, ascending=False).head(10)

        # Mostra o DataFrame somado
        # st.write("DataFrame com Valores Somados:")
        # st.write(summed_df)

        # Cria o gráfico de Dispersão
        fig = px.scatter(summed_df, x='Jogador', y=coluna_selecionada, title=f'Soma de {coluna_selecionada} por Jogador')
        st.plotly_chart(fig)

    elif tipo_grafico == 'Linhas':       
        combined_df = pd.concat([df_euroleague, df_nba], ignore_index=True)
        
        # Filtra os dados com base nas ligas selecionadas
        filtered_df = combined_df[combined_df['Liga'].isin(ligas_selecionadas)]

        # Agrupar por Liga e somar os valores da coluna selecionada
        summed_df = filtered_df.groupby('Jogador')[coluna_selecionada].sum().reset_index()
        
        # Ordenar do maior para o menor e selecionar os top 10
        summed_df = summed_df.sort_values(by=coluna_selecionada, ascending=False).head(10)

        # Cria o gráfico de Linhas
        fig = px.line(summed_df, x='Jogador', y=coluna_selecionada, title=f'Soma de {coluna_selecionada} por Jogador')
        st.plotly_chart(fig)

    elif tipo_grafico == 'Caixa':
        combined_df = pd.concat([df_euroleague, df_nba], ignore_index=True)
        
        # Filtra os dados com base nas ligas selecionadas
        filtered_df = combined_df[combined_df['Liga'].isin(ligas_selecionadas)]

        # Agrupar por Liga e somar os valores da coluna selecionada
        summed_df = filtered_df.groupby('Jogador')[coluna_selecionada].sum().reset_index()
        
        # Ordenar do maior para o menor e selecionar os top 10
        summed_df = summed_df.sort_values(by=coluna_selecionada, ascending=False).head(10)
        
        # Cria o gráfico de Linhas
        fig = px.box(summed_df, x='Jogador', y=coluna_selecionada, title=f'Soma de {coluna_selecionada} por Jogador')
        st.plotly_chart(fig)