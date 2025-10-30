import joblib as jb
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

def data_transform(x):
    print("Data Transformation...")
    scaler.fit(x)
    t_data = scaler.transform(x)
    jb.dump(scaler,"models/scaler.pkl")
    return t_data