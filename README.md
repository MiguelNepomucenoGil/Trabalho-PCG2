# Comparação de Estatísticas de Basquete: EuroLeague vs NBA

Este projeto cria uma aplicação web interativa para comparar estatísticas de jogadores de basquete entre a EuroLeague e a NBA utilizando Streamlit e Plotly. A aplicação permite carregar dados de arquivos CSV, visualizar dados e gerar gráficos interativos.

## Funcionalidades

- **Visualização de Dados**: Exibição dos dados das ligas EuroLeague e NBA em tabelas interativas.
- **Definições de Abreviações**: Explicação das abreviações estatísticas usadas nos dados.
- **Comparação de Ligas**: Comparação visual das estatísticas selecionadas entre as ligas EuroLeague e NBA através de gráficos de barras, dispersão, linhas e caixas.
- **Personalização de Gráficos**: Seleção de tipos de gráficos e colunas para comparação com nomes amigáveis.

## Tecnologias Utilizadas

- [Streamlit](https://streamlit.io/): Framework para criar aplicações web interativas com Python.
- [Pandas](https://pandas.pydata.org/): Biblioteca para manipulação e análise de dados.
- [Plotly](https://plotly.com/python/): Biblioteca para criação de gráficos interativos.

## Estrutura do Projeto

project-root/
│
├── EUROLEAGUE.csv # Arquivo CSV com os dados da EuroLeague
├── NBA.csv # Arquivo CSV com os dados da NBA
├── tabela.py # Script principal da aplicação Streamlit
└── README.md # Este arquivo README


## Pré-requisitos

Certifique-se de ter o Python 3.7 ou superior instalado. 

## Uso

1. Coloque os arquivos `EUROLEAGUE.csv` e `NBA.csv` no diretório raiz do projeto. Certifique-se de que os arquivos estejam formatados corretamente com `;` como separador e `.` como separador decimal.

2. Execute a aplicação Streamlit:
    ```bash
    streamlit run tabela.py
    ```

3. Acesse a aplicação no navegador pelo endereço fornecido, geralmente `http://localhost:8501`.

## Estrutura do Código

O script `tabela.py` está dividido nas seguintes seções principais:

1. **Configuração Inicial**:
    - Leitura dos arquivos CSV.
    - Limpeza e preparação dos dados.
    - Renomeação das colunas para nomes mais amigáveis.

2. **Definição das Categorias**:
    - Menu de seleção de categoria (Dados, NBA, Definições, Comparação Liga).

3. **Exibição de Dados e Definições**:
    - Exibição dos dados das ligas em tabelas.
    - Exibição das definições das abreviações estatísticas.

4. **Comparação de Ligas**:
    - Seleção do tipo de gráfico (Barras, Dispersão, Linhas, Caixa).
    - Seleção da coluna para comparação utilizando nomes amigáveis.
    - Filtragem dos dados e criação de gráficos interativos.

Esperamos que este projeto seja útil para você! Aproveite para explorar e comparar as estatísticas das duas principais ligas de basquete do mundo.
