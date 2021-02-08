import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


def calculate_knn(data):
    data_test = pd.read_csv("data_files/UDP_DDoS_data.csv")
    data_features = data_test[["Data"]]
    data_target_bin = data_test["Attack"]

    x_test = data[["Data"]]

    x_train = data_features
    y_train = data_target_bin

    # X_train, X_test, y_train, y_test = train_test_split(X, y_bin, test_size=0.4, random_state=4)

    knn = KNeighborsClassifier(n_neighbors=2)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    data["knn"] = y_pred
    return "knn"
