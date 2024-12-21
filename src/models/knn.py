from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from src.load_dataset import split_data


def find_best_k(x_train, x_test, y_train, y_test):
    accuracy_list = []

    for k in range(1, len(x_train)):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(x_train, y_train)
        prediction = knn.predict(x_test)
        accuracy_list.append(accuracy_score(y_test, prediction))

    return accuracy_list.index(max(accuracy_list)) + 1


def get_model_knn():
    x_train, x_test, y_train, y_test = split_data()

    best_k = find_best_k(x_train, x_test, y_train, y_test)

    model = KNeighborsClassifier(n_neighbors=best_k)
    model.fit(x_train, y_train)

    return model


def main():

    get_model_knn()


if __name__ == "__main__":
    main()
