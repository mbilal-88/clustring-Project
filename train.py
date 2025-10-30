import joblib as jb
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def model(t_data,x,n_clusters=5,random_state = 0):
    print("Model Training...")
    Means = KMeans(n_clusters = n_clusters,
                  random_state = random_state)
    Means.fit(t_data) 
    x_pred = Means.predict(t_data)

    jb.dump(Means, "models/model.pkl")

    Accuracy = silhouette_score(x,Means.labels_)
    print(f"Model Saved with accuracy: {Accuracy}")