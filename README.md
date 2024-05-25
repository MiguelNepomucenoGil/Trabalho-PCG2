Leitura e Manipulação de Dados de Dengue e Chuvas em Python
Este código Python utiliza as bibliotecas Streamlit, Pandas e Plotly para carregar, analisar e visualizar dados de dengue e chuva em São Paulo.
Requisitos:
Python 3.7 ou superior
Bibliotecas: streamlit, pandas, plotly (instale com pip install streamlit pandas plotly)
Arquivos de dados: dengue24_mes.csv e chuvas sao paulo mensal.csv
Passo a passo:
Importar Bibliotecas:
streamlit: para criar a interface web interativa
pandas: para manipulação e análise de dados
plotly.express: para criar gráficos interativos
plotly.graph_objects: para gráficos mais complexos
Carregar os Dados:
pd.read_csv(): carrega os dados dos arquivos CSV com separador ;, usando decimal='.' para tratar os valores decimais corretamente.
encoding='ISO-8859-1': define a codificação do arquivo.
Formatar os Dados:
df_dengue.applymap(lambda x: str(x).replace(',', '')): remove as vírgulas dos dados do DataFrame df_dengue para garantir que sejam tratados como números.
df_dengue.rename(columns={...}): renomeia as colunas do DataFrame df_dengue para facilitar a interpretação.
df_chuvas.applymap(lambda x: str(x).replace(',', '.')): substitui as vírgulas por pontos nos valores do DataFrame df_chuvas.
df_chuvas.drop(df_chuvas.index[4]): remove a linha 4 do DataFrame df_chuvas.
Criar a Interface do Streamlit:
st.set_page_config(layout="wide"): configura o layout da página como "wide" para gráficos maiores.
st.sidebar.title("Categorias"): cria um título na barra lateral.
st.sidebar.radio("Selecione a categoria:", ("Dados", "Gráficos")): cria um botão de rádio para escolher entre "Dados" e "Gráficos".
Exibir Dados:
st.title("Dados"): cria um título na página principal.
st.subheader("Dados de Dengue"): cria um subtítulo para os dados de dengue.
st.dataframe(df_dengue): exibe o DataFrame df_dengue como uma tabela interativa.
st.subheader("Dados de Chuvas"): cria um subtítulo para os dados de chuva.
st.dataframe(df_chuvas): exibe o DataFrame df_chuvas como uma tabela interativa.
st.markdown("""..."""): exibe uma descrição dos dados em Markdown.
Criar Gráficos:
st.title("Gráficos"): cria um título na página principal.
df_dengue_filtrado = df_dengue[df_dengue['GVE'] == 'CAPITAL']: filtra o DataFrame df_dengue para apenas os dados da "CAPITAL".
st.selectbox("Selecione o tipo de gráfico:", ("Indices Meteorológicos", "Casos de Dengue", "Dengue-Chuva: Explorando Relações")): cria uma caixa de seleção para escolher o tipo de gráfico.
Criar Gráficos Específicos:
Indices Meteorológicos:
fig = go.Figure(): cria um objeto Figure do Plotly.
fig.add_trace(go.Bar(...)): adiciona um gráfico de barras para a precipitação.
fig.add_trace(go.Scatter(...)): adiciona um gráfico de linha para a temperatura.
fig.update_layout(...): configura o layout do gráfico (títulos, eixos, etc.).
st.plotly_chart(fig): exibe o gráfico na página.
Casos de Dengue:
Cria um gráfico de barras para os casos de dengue por mês.
Cria gráficos de linha para casos confirmados e importados.
Configura o layout do gráfico.
Exibe o gráfico na página.
Dengue-Chuva: Explorando Relações:
Cria um gráfico de barras para os casos de dengue por mês.
Cria um gráfico de linha para a precipitação.
Configura o layout do gráfico.
Exibe o gráfico na página.
Executar o Script:
Execute o script Python com o comando streamlit run seu_script.py (substitua seu_script.py pelo nome do seu arquivo).
Abra o endereço URL fornecido pelo Streamlit no seu navegador.
