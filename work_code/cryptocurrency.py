import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
import numpy as np

def load_data(file_path):
    data = pd.read_excel(file_path)
    return data

def prepare_data(data):
    data['Date'] = pd.to_datetime(data[['Year', 'Month', 'Day']])
    daily_data = data.groupby('Date').agg({'Rate': 'mean'}).reset_index()
    
    daily_data['Date_Ordinal'] = daily_data['Date'].apply(lambda x: x.toordinal())
    return daily_data[['Date_Ordinal', 'Rate']]

def train_model(data):
    X = data[['Date_Ordinal']].values
    y = data['Rate'].values
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_future_rate(model, future_date):
    future_date_ordinal = future_date.toordinal()
    predicted_rate = model.predict([[future_date_ordinal]])
    return predicted_rate[0]

def main():
    file_path = 'data.xlsx'
    data = load_data(file_path)
    prepared_data = prepare_data(data)
    model = train_model(prepared_data)
    
    future_date = datetime(2025, 1, 1)  
    predicted_rate = predict_future_rate(model, future_date)
    
    print(f"Predicted rate for {future_date.strftime('%Y-%m-%d')}: ${predicted_rate:.2f}")

if __name__ == "__main__":
    main()
