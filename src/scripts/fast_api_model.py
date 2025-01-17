from fastapi import FastAPI
import pandas as pd
import joblib
import pickle

app = FastAPI()

model_path = r'C:\Users\GabGalani\Documents\Data Projects\Analise_credito\src\model\model.pkl'
columns_model = r'C:\Users\GabGalani\Documents\Data Projects\Analise_credito\src\model\columns.joblib'


with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)
columns_do_modelo = joblib.load(columns_model)


@app.get("/")
def read_root():
    return {'message': 'API Online'}


@app.get("/predict/v1={Occupation}&v2={Payment_Behaviour}&v3={Payment_of_Min_Amount}&v4={Age}&v5={Year_credit_history}&v6={Month_credit_history}&v7={Delay_from_due_date}&v8={Num_of_Loan}&v9={Outstanding_Debt}&v10={Monthly_Inhand_Salary}&v11={Monthly_Balance}&v12={Annual_Income}")
def predict(Occupation, Payment_Behaviour, Payment_of_Min_Amount, Age, Year_credit_history, Month_credit_history, Delay_from_due_date, 
            Num_of_Loan, Outstanding_Debt, Monthly_Inhand_Salary, Monthly_Balance, Annual_Income):


    data = {
        "Occupation": [str(Occupation)],
        "Payment_Behaviour": [str(Payment_Behaviour)],
        "Payment_of_Min_Amount": [str(Payment_of_Min_Amount)],
        "Age": [int(Age)],
        "Year_credit_history": [int(Year_credit_history)],
        "Month_credit_history": [int(Month_credit_history)],
        "Delay_from_due_date": [int(Delay_from_due_date)],
        "Num_of_Loan": [int(Num_of_Loan)],
        "Outstanding_Debt": [float(Outstanding_Debt)],
        "Monthly_Inhand_Salary": [float(Monthly_Inhand_Salary)],
        "Monthly_Balance": [float(Monthly_Balance)],
        "Annual_Income": [float(Annual_Income)]        
    }

    cliente_df = pd.DataFrame(data)

    cliente_df['Credit_History_Age'] = (
        cliente_df['Year_credit_history'] * 12 + cliente_df['Month_credit_history']
    )

    selecao_colunas = [
        'Occupation', 
        'Payment_Behaviour', 
        'Payment_of_Min_Amount', 
        'Age', 
        'Credit_History_Age', 
        'Delay_from_due_date', 
        'Num_of_Loan',
        'Outstanding_Debt',
        'Monthly_Inhand_Salary',
        'Monthly_Balance',
        'Annual_Income'
    ]

    cliente_df = cliente_df[selecao_colunas]


    cliente_ficticio_encoded = pd.get_dummies(cliente_df, columns=['Occupation', 'Payment_Behaviour'], drop_first=True)
    cliente_ficticio_encoded = pd.get_dummies(cliente_ficticio_encoded, columns=['Payment_of_Min_Amount'], drop_first=False)


    cliente_ficticio_adjusted = cliente_ficticio_encoded.reindex(columns=columns_do_modelo, fill_value=0)

    prediction = model.predict(cliente_ficticio_adjusted)

    return {'prediction': prediction.tolist()[0]}