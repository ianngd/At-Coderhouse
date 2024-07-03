# Projeto Final - Pipeline ETL com IBGE e CPTEC

## Descrição

Este projeto é uma implementação de um pipeline ETL (Extração, Transformação e Carga) usando APIs do IBGE e CPTEC. O objetivo do projeto é extrair dados de estados e municípios brasileiros da API do IBGE, e dados meteorológicos da API do CPTEC, transformar esses dados conforme necessário e carregá-los em um banco de dados SQLite para posterior consulta. Além disso, o projeto inclui um sistema de alerta para notificar falhas no processo de extração.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

projeto_final_etl_ibge_cptec/
│
├── notebooks/
│ ├── etl_pipeline.ipynb
│
├── venv/ # Ambiente virtual para gerenciamento de dependências
│ ├── Include/
│ ├── Lib/
│ ├── Scripts/
│ ├── pyvenv.cfg
│
├── dados_ibge_cptec.db
├── README.md
├── requirements.txt


## Funcionalidades

- **Extração**: Os dados são extraídos de endpoints das APIs do IBGE (/uf/v1 e /municipios/v1) e da CPTEC (/cidade e /clima/previsao).
- **Transformação**: Os dados são transformados em DataFrames pandas.
- **Carga**: Os dados transformados são carregados em um banco de dados SQLite.
- **Alertas**: Um sistema de alerta notifica falhas no processo de extração utilizando a biblioteca plyer.

## Instalação

Para executar este projeto, siga as instruções abaixo:

1. Clone o repositório:
    ```bash
    git clone https://github.com/ianngd/At-Coderhouse.git
    cd At-Coderhouse/Projeto%20Final%20-%20Python
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para executar o pipeline ETL, abra e execute todas as células do notebook `notebooks/etl_pipeline.ipynb` em um ambiente Jupyter Notebook.

## Estrutura do Notebook

1. Instalação das bibliotecas necessárias
2. Importação das bibliotecas
3. Definição da função de alerta
4. Definição da função para extrair dados da API
5. Definição da função para carregar dados no banco de dados
6. Solicitação da sigla do estado pelo usuário
7. Execução da extração, transformação e carga dos dados
8. Visualização dos dados extraídos

## Exemplo de Saída

Abaixo estão as primeiras linhas do DataFrame `previsao` carregado no banco de dados:

### Dados da Previsão

| Estado | Cidade    | Codigo | Data       | Minima | Maxima |
|--------|-----------|--------|------------|--------|--------|
| SP     | São Paulo | 12345  | 01/01/2023 | 20     | 30     |
| SP     | Santos    | 67890  | 01/01/2023 | 22     | 29     |

## Consulta dos Dados

Para visualizar os dados armazenados no banco de dados, utilize a função `executar_query`:

```python
import sqlite3
import pandas as pd

def executar_query(query, db_name="dados_ibge_cptec.db"):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Exemplo de visualização dos dados da tabela previsão
query_previsao = "SELECT * FROM previsao"
df_previsao_query = executar_query(query_previsao)
print(df_previsao_query.head())


# Contribuição
Se você quiser contribuir com este projeto, sinta-se à vontade para fazer um fork do repositório, criar uma branch para suas alterações e abrir um pull request.

# Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

