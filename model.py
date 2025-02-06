import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.preprocessing import OneHotEncoder

def fun():
    df = pd.read_csv("product_data.csv")
    x=df[['Comp_name', 'Comp_price', 'Comp_rating','seller_sales','seller_stock']]
    y=df['seller_price']
    model = XGBRegressor()
    model.fit(x,y)
    price=model.predict(x)
    print(price)
