def train_model(x):
    from sklearn.cluster import DBSCAN
    import joblib

    model = DBSCAN(eps=5, min_samples=4)

    labels = model.fit_predict(x)

    joblib.dump(model, "artifacts/model.pkl")

    print("Model save ho gaya")
    print("Clusters:", labels)

    return model, labels

model, labels = train_model(x)
