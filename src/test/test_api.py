import pytest
import requests

# URL base da API
BASE_URL = "http://127.0.0.1:8000"

# Cliente fictício de teste
cliente_ficticio = {
    'Occupation': 'Scientist',
    'Payment_Behaviour': 'Low_spent_Small_value_payments',
    'Payment_of_Min_Amount': 'No',
    'Age': 30,
    'Year_credit_history': 20,
    'Month_credit_history': 2,
    'Delay_from_due_date': 2,
    'Num_of_Loan': 2,
    'Outstanding_Debt': 500.00,
    'Monthly_Inhand_Salary': 1500.00,
    'Monthly_Balance': 300.00,
    'Annual_Income': 25000.00
}

def test_api_online():
    """Testar se a API está online"""
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.json() == {'message': 'API Online'}

def test_prediction():
    """Testand a requisição predict"""
    response = requests.post(f"{BASE_URL}/predict", json=cliente_ficticio)
    assert response.status_code == 200
    prediction = response.json()
    assert 'prediction' in prediction
    assert isinstance(prediction['prediction'], list)
