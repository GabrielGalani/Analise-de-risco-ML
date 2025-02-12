# Análise de Risco de Crédito - Machine Learning

## Descrição

Este projeto utiliza um dataset de classificação de risco de crédito para treinar um modelo de Machine Learning que avalia a situação e classifica o risco de crédito de um cliente. A apresentação dos dados e resultados é feita através de uma interface Streamlit.

## Bibliotecas Utilizadas

- `Pandas`: Para manipulação de dados.
- `Numpy`: Para operações numéricas.
- `seaborn`: Para visualizações.
- `matplotlib`: Para gráficos.
- `pickle`: Para salvar e carregar modelos de Machine Learning.
- `sklearn`: Para construir e treinar o modelo de Machine Learning.
- `scipy`: Para operações científicas.
- `Streamlit`: Para criar a interface web interativa.
- `FastAPI`: Para a criação da API para o modelo de Machine Learning.
- `Requests`: Para fazer requisições HTTP.

## Modelo de Machine Learning

O modelo utilizado para a classificação de risco de crédito é o `RandomForestClassifier` do `sklearn`.

## Link do Dataset

Você pode acessar o dataset de classificação de risco de crédito no Kaggle através do seguinte link:

[Dataset Kaggle - Credit Score Classification](https://www.kaggle.com/datasets/parisrohan/credit-score-classification)

## Como Utilizar

### Passo a Passo:

1. Clone este repositório:
    ```bash
    git clone https://github.com/GabrielGalani/Analise-de-risco-ML.git
    ```

2. Crie um ambiente virtual:
    ```bash
    python -m venv .venv
    ```

3. Ative o ambiente virtual:
    - No Windows:
      ```bash
      .\.venv\Scripts\activate
      ```
    - No Linux/Mac:
      ```bash
      source .venv/bin/activate
      ```

4. Instale os requisitos:
    ```bash
    pip install -r requirements.txt
    ```

5. Execute o FastAPI:
    ```bash
    uvicorn src.scripts.fast_api_model:app --reload
    ```

6. Execute o Streamlit:
    ```bash
    streamlit run .\src\scripts\streamlit_app.py
    ```

### O que Você Vai Ver:

Após seguir os passos acima, você verá uma interface Streamlit apresentando os resultados da análise de risco de crédito. Além disso, a API FastAPI estará disponível para fornecer previsões baseadas no modelo de Machine Learning.

## Resultados Esperados

- Visualizações de gráficos e imagens dos dados.
- Resultados interativos no Streamlit.
- Respostas da API com classificações de risco de crédito.

### Imagens de Exemplo

![FastAPI](https://github.com/GabrielGalani/Analise-de-risco-ML/blob/main/image/requests/requests_api_inicio.png)
![Gift execução FastAPI e StremLit](https://github.com/GabrielGalani/Analise-de-risco-ML/blob/main/image/Streamlit_fastAPI.gif)


## Contribuições

Se você deseja contribuir com este projeto, fique à vontade para fazer um fork e enviar um pull request.
