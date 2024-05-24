import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")

# leitura dos arquivos CSV e transformando em variáveis 
df_dengue = pd.read_csv("dengue24_mes.csv", sep=";", decimal='.', encoding='ISO-8859-1')
df_chuvas = pd.read_csv("chuvas sao paulo mensal.csv", sep=";", decimal=".", encoding='ISO-8859-1')

# colocando caracteres de separação na tabela
df_dengue = df_dengue.applymap(lambda x: str(x).replace(',', ''))

# renomeando colunas do dataset. Nomes com ambiguidade
df_dengue = df_dengue.rename(columns={"Confirmados  autóctones ": "Confirmados autóctones Janeiro",
                                      "Confirmados  autóctones": "Confirmados autóctones Fevereiro",
                                      "Confirmados autoctones": "Confirmados autóctones Março",
                                      "Confirmados autóctones": "Confirmados autóctones Abril"})

# Alterando , por . nas colunas de valores do dataset
df_chuvas = df_chuvas.applymap(lambda x: str(x).replace(',', '.'))

#  Removendo a linha 4 (índice 3) do DataFrame df_chuvas 
df_chuvas = df_chuvas.drop(df_chuvas.index[4])

# Criando filtros interativos
st.sidebar.title("Categorias")
opcao = st.sidebar.radio("Selecione a categoria:", ("Dados", "Gráficos"))

if opcao == "Dados":
    st.title("Dados")
    
    # Exibindo as tabelas diretamente, sem checkboxes
    st.subheader("Dados de Dengue")
    st.dataframe(df_dengue) # Usando st.dataframe para uma tabela mais simples

    st.subheader("Dados de Chuvas")
    st.dataframe(df_chuvas) # Usando st.dataframe para uma tabela mais simples
    
    # Markdown de informação para auxiliar na interpretação dos datasets
    st.markdown("""
            #### **Legenda Dengue**
            
            **DRS:** Região de Saúde onde os casos foram registrados.
            
            **GVE:** Grupo de Vigilância Epidemiológica, se houver.
            
            **Município:** Município onde os casos foram registrados.
            
            **RS:** Regiões.
            
            **Confirmados Autóctones:** Casos contraídos pelo enfermo na zona de sua residência. 
            
            **Importados:** Casos contraídos fora da zona onde se fez o diagnóstico. 
            
            **Janeiro Notificados:** Casos notificados no mês de janeiro.
            
            **Fevereiro Notificados:** Casos notificados no mês de janeiro.
            
            **Março Notificados:** Casos notificados no mês de janeiro.
            
            **Abril Notificados:** Casos notificados no mês de janeiro.
                
            #### **Legenda Chuva**
            
            **Data:** Contém a data de obtenção do registro.

            **Hora UTC:** Indica o momento exato 

            **Precipitação Total, Horária (mm):** Quantidade de chuva acumulada durante a hora em questão, medida em milímetros. 

            **Pressão Atmosférica ao Nível da Estação, Horária (mB):** Força exercida pelo peso da atmosfera no local de medição, medida em milibares.

            **Radiação Global (Kj/m²):** Quantidade total de energia solar recebida por metro quadrado na hora da medição, expressa em quilojoules.

            **Temperatura do Ar - Bulbo Seco, Horária (°C):** Temperatura do ar ambiente, medida por um termômetro comum, expressa em graus Celsius.

            **Temperatura do Ponto de Orvalho (°C):** Temperatura na qual o ar precisa ser resfriado para que o vapor de água presente condense e forme orvalho.

            **Umidade Relativa do Ar, Horária (%):** Quantidade de vapor de água presente no ar em relação à quantidade máxima que o ar pode conter naquela temperatura, expressa em porcentagem.

            **Vento, Direção Horária (°):** Direção de onde o vento sopra, medida em graus em relação ao norte verdadeiro (0° = Norte, 90° = Leste, 180° = Sul, 270° = Oeste).

            **Vento, Velocidade Horária (m/s):** Velocidade média do vento durante a hora da medição, medida em metros por segundo.

            **Pressão Atmosférica Máxima na Hora Anterior (AUT) (mB):** Maior valor de pressão atmosférica registrado durante a hora anterior à medição.

            **Pressão Atmosférica Mínima na Hora Anterior (AUT) (mB):** Menor valor de pressão atmosférica registrado durante a hora anterior à medição.

            **Temperatura Máxima na Hora Anterior (AUT) (°C):** Temperatura mais alta registrada durante a hora anterior.

            **Temperatura do Ponto de Orvalho Mínima na Hora Anterior (AUT) (°C):** Menor valor da temperatura do ponto de orvalho na hora anterior.

            **Umidade Relativa Máxima na Hora Anterior (AUT) (%):** Maior porcentagem de umidade relativa registrada na hora anterior.

            **Umidade Relativa Mínima na Hora Anterior (AUT) (%):** Menor porcentagem de umidade relativa registrada na hora anterior.

            **Vento, Rajada Máxima (m/s):** Maior velocidade instantânea do vento registrada na hora anterior.

            """)

elif opcao == "Gráficos":
    st.title("Gráficos")
    
    # Filtrando o DataFrame de dengue pela DRS 'Capital'
    df_dengue_filtrado = df_dengue[df_dengue['GVE'] == 'CAPITAL']

    # Selectbox para escolher o tipo de gráfico
    tipo_grafico = st.selectbox("Selecione o tipo de gráfico:", ("Indices Meteorológicos", "Casos de Dengue", "Dengue-Chuva: Explorando Relações"))

    if tipo_grafico == "Indices Meteorológicos":
        fig = go.Figure()

        # Adicionando gráfico de barras para dados de precipitação
        fig.add_trace(go.Bar(
            x=df_chuvas['Data Medicao'],
            y=df_chuvas['PRECIPITACAO TOTAL, MENSAL(mm)'],
            name='Precipitação'
        ))

        # Adicionando gráfico de linha para dados de temperatura
        fig.add_trace(go.Scatter(
             x=df_chuvas['Data Medicao'],
             y=df_chuvas['TEMPERATURA MEDIA COMPENSADA, MENSAL(Â°C)'],
             name='Temperatura(°C)',
             mode='lines+markers',
             yaxis="y2" #  Colocando linha no segundo eixo do gráfico
        ))

        # Atualizando layout do gráfico
        fig.update_layout(
            title="Precipitação Mensal e Temperatura Média",
            xaxis_title="Data",
            yaxis_title="Valores",
            yaxis2={'title': 'Temperatura(°C)', 'overlaying': 'y', 'side': 'right'},
            barmode='group'
        )

        st.plotly_chart(fig)
        

    elif tipo_grafico == "Casos de Dengue":
        fig2 = go.Figure()

        # Adicionando gráfico de barras para dados de Janeiro a Abril de dengue
        fig2.add_trace(go.Bar(
            x=['Janeiro', 'Fevereiro', 'Março', 'Abril'],
            y=[df_dengue_filtrado['Janeiro Notificados'].astype(float).sum(),
               df_dengue_filtrado['Fevereiro Notificados'].astype(float).sum(),
               df_dengue_filtrado['Março Notificados'].astype(float).sum(),
               df_dengue_filtrado['Abril Notificados'].astype(float).sum()],
            name='Casos de Dengue'
        ))

        # Adicionando gráfico de linha para dados de casos residênciais confirmados
        fig2.add_trace(go.Scatter(
             x=['Janeiro', 'Fevereiro', 'Março', 'Abril'],
             y=[df_dengue_filtrado['Confirmados autóctones Janeiro'].astype(float).sum(),
                df_dengue_filtrado['Confirmados autóctones Fevereiro'].astype(float).sum(),
                df_dengue_filtrado['Confirmados autóctones Março'].astype(float).sum(),
                df_dengue_filtrado['Confirmados autóctones Abril'].astype(float).sum()],
             name='Casos Confirmados',
             mode='lines+markers'
        ))
        
        # Adicionando gráfico de linha para dados de casos importados (casos fora do município onde foi relatado)
        fig2.add_trace(go.Scatter(
             x=['Janeiro', 'Fevereiro', 'Março', 'Abril'],
             y=[df_dengue_filtrado[' importados '].astype(float).sum(),
                df_dengue_filtrado[' importados .1'].astype(float).sum(),
                df_dengue_filtrado[' importados .2'].astype(float).sum(),
                df_dengue_filtrado[' importados .3'].astype(float).sum()],
             name='Importados',
             mode='lines+markers'
        ))

        # Atualizando layout do gráfico
        fig2.update_layout(
            title="Casos de Dengue em Capital (Janeiro a Abril), Casos Confirmados e Importados",
            xaxis_title="Mês",
            yaxis_title="Valores",
            barmode='group'
        )

        st.plotly_chart(fig2)
        
    elif tipo_grafico == "Dengue-Chuva: Explorando Relações":
        fig3 = go.Figure()

        # Adicionando gráfico de barras para dados de Janeiro a Abril de dengue
        fig3.add_trace(go.Bar(
            x=['Janeiro', 'Fevereiro', 'Março', 'Abril'],
            y=[df_dengue_filtrado['Janeiro Notificados'].astype(float).mean(),
               df_dengue_filtrado['Fevereiro Notificados'].astype(float).mean(),
               df_dengue_filtrado['Março Notificados'].astype(float).mean(),
               df_dengue_filtrado['Abril Notificados'].astype(float).mean()],
            name='Casos de Dengue'
        ))

        # Adicionando gráfico de barra para dados de casos residênciais confirmados
        fig3.add_trace(go.Bar(
             x=['Janeiro', 'Fevereiro', 'Março', 'Abril'],
             y=[df_dengue_filtrado['Confirmados autóctones Janeiro'].astype(float).mean(),
                df_dengue_filtrado['Confirmados autóctones Fevereiro'].astype(float).mean(),
                df_dengue_filtrado['Confirmados autóctones Março'].astype(float).mean(),
                df_dengue_filtrado['Confirmados autóctones Abril'].astype(float).mean()],
             name='Casos Confirmados'
        ))
        
        # Adicionando gráfico de linha para dados de casos importados (casos fora do município onde foi relatado)
        fig3.add_trace(go.Bar(
             x=['Janeiro', 'Fevereiro', 'Março', 'Abril'],
             y=[df_dengue_filtrado[' importados '].astype(float).mean(),
                df_dengue_filtrado[' importados .1'].astype(float).mean(),
                df_dengue_filtrado[' importados .2'].astype(float).mean(),
                df_dengue_filtrado[' importados .3'].astype(float).mean()],
             name='Importados'
        ))
        
        # Adicionando gráfico de linha para dados de precipitação
        fig3.add_traces(go.Scatter(
             x=['Janeiro', 'Fevereiro', 'Março', 'Abril'],
             y=df_chuvas['PRECIPITACAO TOTAL, MENSAL(mm)'],
             name='Precipitação',
             mode='lines+markers',
             yaxis="y2" #  Colocando linha no segundo eixo do gráfico
        ))

        # Atualizando layout do gráfico
        fig3.update_layout(
            title="Dengue-Chuva (Precipitação(mm))",
            xaxis_title="Meses",
            yaxis_title="Casos",
            yaxis2={'title': 'Precipitação', 'overlaying': 'y', 'side': 'right'},
            barmode='group'
        )

        st.plotly_chart(fig3)
        
        
        fig4 = go.Figure()

        # Adicionando gráfico de barras para dados de janeiro e fevereiro de dengue
        fig4.add_trace(go.Bar(
            x=['Janeiro', 'Fevereiro', 'Março', 'Abril'],
            y=[df_dengue_filtrado['Janeiro Notificados'].astype(float).mean(),
               df_dengue_filtrado['Fevereiro Notificados'].astype(float).mean(),
               df_dengue_filtrado['Março Notificados'].astype(float).mean(),
               df_dengue_filtrado['Abril Notificados'].astype(float).mean()],
            name='Casos de Dengue'
        ))

        # Adicionando gráfico de barra para dados de casos residênciais confirmados
        fig4.add_trace(go.Bar(
             x=['Janeiro', 'Fevereiro', 'Março', 'Abril'],
             y=[df_dengue_filtrado['Confirmados autóctones Janeiro'].astype(float).mean(),
                df_dengue_filtrado['Confirmados autóctones Fevereiro'].astype(float).mean(),
                df_dengue_filtrado['Confirmados autóctones Março'].astype(float).mean(),
                df_dengue_filtrado['Confirmados autóctones Abril'].astype(float).mean()],
             name='Casos Confirmados'
        ))
        
        # Adicionando gráfico de linha para dados de casos importados (casos fora do município onde foi relatado)
        fig4.add_trace(go.Bar(
             x=['Janeiro', 'Fevereiro', 'Março', 'Abril'],
             y=[df_dengue_filtrado[' importados '].astype(float).mean(),
                df_dengue_filtrado[' importados .1'].astype(float).mean(),
                df_dengue_filtrado[' importados .2'].astype(float).mean(),
                df_dengue_filtrado[' importados .3'].astype(float).mean()],
             name='Importados'
        ))
        
        # Adicionando gráfico de linha para dados de temperatura
        fig4.add_traces(go.Scatter(
             x=['Janeiro', 'Fevereiro', 'Março', 'Abril'],
             y=df_chuvas['TEMPERATURA MEDIA COMPENSADA, MENSAL(Â°C)'],
             name='Temperatura Média(°C)',
             mode='lines+markers',
             yaxis="y2" #  Colocando linha no segundo eixo do gráfico
        ))

        # Atualizando layout do gráfico
        fig4.update_layout(
            title="Dengue-Chuva (Temperatura(°C))",
            xaxis_title="Meses",
            yaxis_title="Casos",
            yaxis2={'title': 'Temperatura(°C)', 'overlaying': 'y', 'side': 'right'},
            barmode='group'
        )

        st.plotly_chart(fig4)