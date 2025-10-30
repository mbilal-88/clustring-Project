# from src.dataEncoder import data_Encoder
import joblib as jb
import pandas as pd

OR = jb.load("models/encoder.pkl")
Scaler = jb.load("models/scaler.pkl")
model = jb.load("models/model.pkl")

def data_Encoder(df):
    print("Data Encoded")
    df["Genre"] = OR.transform(df[["Genre"]])
    return df

def data_scaler(df):
    print("Data Scaling") 
    numeric_cols = ["Age","Annual Income (k$)","Spending Score (1-100)"]
    df[numeric_cols] = Scaler.transform(df[numeric_cols])
    return df   


def prediction(data):
    data_dict = {
        "Genre": data[0],
        "Age": data[1],
        "Annual Income (k$)": data[2],
        "Spending Score (1-100)": data[3]
    }
    data = pd.DataFrame(data_dict, index=[0])
    df = data_Encoder(data)
    df = data_scaler(df)
    X = df[["Age", "Annual Income (k$)", "Spending Score (1-100)"]].values
    a = model.predict(X)
    # a = model.predict(df)
    return a
