import joblib as jb

scaler = jb.load("models\scaler.pkl")
# scaler.fit("age")
# scaler.fit("Annual Income (k$)")
# scaler.fit("Spending Score (1-100)")