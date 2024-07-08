# Projeto Final - Pipeline ETL com API Brasil (IBGE e CPTEC)

## Descrição

Este projeto é uma implementação de um pipeline ETL (Extração, Transformação e Carga) usando as APIs Brasil, do IBGE e CPTEC. O objetivo do projeto é extrair dados de estados e municípios brasileiros da API do IBGE, e dados meteorológicos da API do CPTEC, transformar esses dados conforme necessário e carregá-los em um banco de dados SQLite para posterior consulta. Além disso, o projeto inclui um sistema de alerta para notificar falhas no processo de extração.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

At-Coderhouse/</br>
│ </br>
├── Projeto%20Final%20-%20Python/ </br>
│ ├── entrega_de_0607.ipynb </br>
│</br>
├── dados_ibge_cptec.db </br>
├── README.md </br>
├── requirements.txt </br>

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

Para executar o pipeline ETL, abra e execute todas as células do notebook `Projeto%20Final%20-%20Python/entrega_de_0607.ipynb` em um ambiente Jupyter Notebook.

## Estrutura do Notebook

1. Instalação das bibliotecas necessárias
2. Importação das bibliotecas
3. Definição da função de criação dos alertas
4. Definição para extrair dados da API e, se necessário, retornar mensagem de erro
5.1. Trazendo os dados e trabalhando a primeira tabela (estado)
5.2. Trazendo os dados e trabalhando a segunda tabela (Cidades do estado)
5.3. Trazendo os dados e trabalhando a terceira tabela (códigos CPTEC)
6. Relacionando tabelas (Previsão meteorológica)
7. Definição para carregamento de dados no banco de dados
8. Chamada da função para carregamento no db da tabela
9. Definição para visualizar dados usando queries
10. Chamada da função para carregamento no db da tabela
11. Exemplo para erro na extração da base
12. Hipóteses: Algumas cidades tendem a ter uma temperatura máxima consistentemente mais alta do que outras?
13. Testando o profiling

## Hipóteses e Análises

### Hipótese 12: Algumas cidades tendem a ter uma temperatura máxima consistentemente mais alta do que outras?

- Agrupamos os dados por cidade e calculamos a média das temperaturas máximas para cada cidade.
- Utilizamos um gráfico de barras para visualizar a temperatura máxima média por cidade.

```python
# Agrupar os dados por cidade e calcular a média das temperaturas máximas
df_temp_max = df_previsao_query.groupby('Cidade')['Maxima'].mean().reset_index()

# Plotando o gráfico de barras para a temperatura máxima média por cidade
plt.figure(figsize=(16, 6))
sns.barplot(data=df_temp_max, x='Cidade', y='Maxima')
plt.title('Temperatura Máxima Média por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Temperatura Máxima Média (°C)')
plt.xticks(rotation=90)
plt.show()
```
# Ainda da Hipótese 12: Análise de distribuição das temperaturas mínima e máxima
Utilizamos gráficos de distribuição (histogramas com Kernel Density Estimate - KDE) para analisar a distribuição das temperaturas mínima e máxima.

```python
# distribuição para a temperatura mínima
plt.figure(figsize=(16, 6))
sns.histplot(df_previsao_query['Minima'], bins=20, kde=True)
plt.title('Distribuição da Temperatura Mínima')
plt.xlabel('Temperatura Mínima (°C)')
plt.ylabel('Frequência')
plt.show()

# distribuição para a temperatura máxima
plt.figure(figsize=(16, 6))
sns.histplot(df_previsao_query['Maxima'], bins=20, kde=True)
plt.title('Distribuição da Temperatura Máxima')
plt.xlabel('Temperatura Máxima (°C)')
plt.ylabel('Frequência')
plt.show()
```

# Teste de Profiling
Utilizamos a biblioteca ydata-profiling para gerar um relatório de profiling dos dados extraídos e transformados.

```python
# Instalar a biblioteca ydata-profiling
%pip install ydata-profiling

# Adicionar o código para gerar o relatório de profiling
from ydata_profiling import ProfileReport

# Supondo que df_previsao_query seja o DataFrame que contém os dados de previsão
profile = ProfileReport(df_previsao_query, title="Profiling Report")

# Para exibir o relatório no Jupyter Notebook
profile.to_notebook_iframe()
```

# Dados da Previsão
Estado	    Cidade	    Codigo	Data	    Minima	Maxima
SP	        São Paulo	12345	01/01/2023	20    	30
SP	        Santos	    67890	01/01/2023	22	    29


# Consulta dos Dados
Para visualizar os dados armazenados no banco de dados, utilize a função executar_query:

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
```

# Contribuição
Se você quiser contribuir com este projeto, sinta-se à vontade para fazer um fork do repositório, criar uma branch para suas alterações e abrir um pull request.

# Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
