import requests
from urllib.parse import urlencode

url = "http://127.0.0.1:8000/predict/"
query = "v1={Occupation}&v2={Payment_Behaviour}&v3={Payment_of_Min_Amount}&v4={Age}&v5={Year_credit_history}&v6={Month_credit_history}&v7={Delay_from_due_date}&v8={Num_of_Loan}&v9={Outstanding_Debt}&v10={Monthly_Inhand_Salary}&v11={Monthly_Balance}&v12={Annual_Income}"

# Dados do cliente fictício
url = url + query.format(
    Occupation= "Scientist",
    Payment_Behaviour= "Low_spent_Small_value_payments",
    Payment_of_Min_Amount= "No",
    Age= "30",
    Year_credit_history= "20",
    Month_credit_history= "2",
    Delay_from_due_date= "2",
    Num_of_Loan= "2",
    Outstanding_Debt= "500.00",
    Monthly_Inhand_Salary= "1500.00",
    Monthly_Balance= "300.00",
    Annual_Income= "25000.00"
)

# # Agora, fazendo a requisição com a URL completa
response = requests.get(url)

# # Acesso ao retorno da API
print(response.json()['prediction'])
