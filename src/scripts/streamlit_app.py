import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# lendo os dados tratados
csv_path = r"C:\Users\GabGalani\Documents\Data Projects\Analise_credito\dataset\gold\dashboard_age.txt"
profissao_path = r"C:\Users\GabGalani\Documents\Data Projects\Analise_credito\dataset\gold\dashboard_profissao.txt"
tempo_path = r"C:\Users\GabGalani\Documents\Data Projects\Analise_credito\dataset\gold\dashboard_tempo.txt"
dados_pagamento_path = r"C:\Users\GabGalani\Documents\Data Projects\Analise_credito\dataset\gold\dados_pagamento.txt"

data_age = pd.read_csv(csv_path, sep=';')
data_profissao = pd.read_csv(profissao_path, sep=';')
data_tempo = pd.read_csv(tempo_path, sep=';')
data_dados_pagamento = pd.read_csv(dados_pagamento_path, sep=';')


# Funções
def fazer_requisicao(oc, pay_beh, pay_min, age, year_cre, month_cre, delay, num_loan, out_dev, month_in_hand, month_balance, annual_in):
    url = "http://127.0.0.1:8000/predict/"
    query = "v1={Occupation}&v2={Payment_Behaviour}&v3={Payment_of_Min_Amount}&v4={Age}&v5={Year_credit_history}&v6={Month_credit_history}&v7={Delay_from_due_date}&v8={Num_of_Loan}&v9={Outstanding_Debt}&v10={Monthly_Inhand_Salary}&v11={Monthly_Balance}&v12={Annual_Income}"

    # Montando a URL
    url = url + query.format(
        Occupation=oc,
        Payment_Behaviour=pay_beh,
        Payment_of_Min_Amount=pay_min,
        Age=age,
        Year_credit_history=year_cre,
        Month_credit_history=month_cre,
        Delay_from_due_date=delay,
        Num_of_Loan=num_loan,
        Outstanding_Debt=out_dev,
        Monthly_Inhand_Salary=month_in_hand,
        Monthly_Balance=month_balance,
        Annual_Income=annual_in
    )

    # Fazendo e retornando a requisição
    response = requests.get(url)
    return response.json()


# Filtros de profissão
profissoes = data_profissao['Occupation'].unique()
tipos_de_comportamento = data_dados_pagamento['Payment_Behaviour'].unique()

# Adicionando um menu lateral
st.sidebar.title("Menu Lateral")
st.sidebar.markdown("Faça seu classificação de risco de crédito")

# Definindo valores padrões para os inputs
oc = st.sidebar.selectbox('Selecione uma profissão:', profissoes, index=0)
pay_beh = st.sidebar.selectbox('Selecione o comportamento de pagamento do cliente:', tipos_de_comportamento, index=0)
pay_min = st.sidebar.selectbox('O cliente realiza pagamento mínimo?:', ['Yes', 'No', 'NM'], index=0)
age = st.sidebar.text_input('Digite a idade do cliente', '30')
year_cre = st.sidebar.text_input('Anos de histórico de crédito', '5')
month_cre = st.sidebar.text_input('Meses de histórico de crédito', '11')
delay = st.sidebar.text_input('Média de atraso em fatura em dias', '5')
num_loan = st.sidebar.text_input('Número de empréstimos que o cliente possui', '2')
out_dev = st.sidebar.text_input('Valor da dívida pendente', '1000')
month_in_hand = st.sidebar.text_input('Salário líquido', '3000')
media_gastos_mes = st.sidebar.text_input('Média de gastos mensais', '1500')

# Cálculo do saldo mensal
month_balance = str(int(month_in_hand) - int(media_gastos_mes))
# Cálculo da renda anual
annual_in = str(int(month_balance) * 12)

# Botão para enviar a requisição
if st.sidebar.button('Enviar Requisição'):
    resultado = fazer_requisicao(
        oc, pay_beh, pay_min, age, year_cre, month_cre, delay,
        num_loan, out_dev, month_in_hand, media_gastos_mes, annual_in
    )
    
    # Exibindo o resultado como um popup
    prediction = resultado.get("prediction", "Sem previsão")
    
    if prediction == "Good":
        st.success(f"Previsão de crédito: {prediction}")
    else:
        st.warning(f"Previsão de crédito: {prediction}")


# Gráfico 1
fig1 = px.pie(data_age, names="Credit_Mix", values="Media", title="Distribuição de Credit Mix")

color_map = {"Good": "green", "Standard": "blue", "Bad": "red"}
fig1.update_traces(
    marker=dict(colors=[color_map[name] for name in data_age["Credit_Mix"]]),
    textinfo="label+value"
)

fig1.update_layout(
    title=dict(
        text="Média de idades x Credit Mix",
        font=dict(size=24),
        x=0.5,
        xanchor="center"
    ),
    legend_title_text="Credit Mix",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.2,
        xanchor="center",
        x=0.5
    ),
    title_font=dict(size=24),
    title_x=0.5
)

fig3 = px.bar(
    data_tempo,
    x="Month",
    y="Count",
    color="Credit_Mix",
    title="Contagem por Classificação de Crédito por Mês",
    labels={"Count": "Contagem", "Month": "Mês", "Credit_Mix": "Classificação de Crédito"},
    barmode="group",
    height=400,
    color_discrete_map={"Good": "green", "Standard": "blue", "Bad": "red"}
)

fig3.update_traces(
    texttemplate="%{y}",
    textposition="outside"
)

fig3.update_layout(
    title=dict(
        text="Contagem por Classificação de Crédito por Mês",
        x=0.5,
        xanchor="center"
    ),
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    margin=dict(t=50, b=50, l=50, r=50)
)

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig1, use_container_width=True, key="grafico1")

with col2:
    profissao_selecionada = st.selectbox('Selecione a profissão para o gráfico 2:', profissoes)
    profissao_filtrada = data_profissao[data_profissao['Occupation'] == profissao_selecionada]
    fig2 = px.bar(
        profissao_filtrada,
        x="Contagem",
        y="Credit_Mix",
        title="Contagem por Risco por Profissão",
        labels={"Contagem": "", "Credit_Mix": ""},
        orientation="h"
    )

    colors = {"Good": "green", "Standard": "blue", "Bad": "red"}
    fig2.update_traces(
        marker_color=profissao_filtrada["Credit_Mix"].map(colors),
        texttemplate="%{x}",
        textposition="inside"
    )

    fig2.update_layout(
        title=dict(
            text="Contagem de Risco por Profissão",
            x=0.5,
            xanchor="center"
        ),
        xaxis=dict(showgrid=False, title=None, showticklabels=False),
        yaxis=dict(showgrid=False),
        height=500,
        width=1200
        
    )
    st.plotly_chart(fig2, use_container_width=True, key="grafico2")

# Gráfico 3
st.plotly_chart(fig3, use_container_width=True)
