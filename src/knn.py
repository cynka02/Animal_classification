import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


def accuracy_of_model(model, test, test_classes):
    prediction = model.predict(test)
    test_classes = test_classes.tolist()

    n = len(prediction)
    correct = 0
    for i in range(n):
        correct += test_classes[i] == prediction[i]
    return correct / n


def find_best_k(train, test, train_classes, test_classes):
    accuracy_list = []

    for k in range(1, len(train)):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(train, train_classes)
        accuracy_list.append(accuracy_of_model(knn, test, test_classes))

    return accuracy_list.index(max(accuracy_list)) + 1


def get_model_knn():
    data = pd.read_csv('../data/zoo.csv')
    data = data.drop('animal_name', axis=1)

    train, test = train_test_split(data, test_size=0.2)
    train_classes = train['class_type']
    train = train.drop('class_type', axis=1)
    test_classes = test['class_type']
    test = test.drop('class_type', axis=1)

    k = find_best_k(train, test, train_classes, test_classes)

    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(train, train_classes)

    return knn


def main():

    get_model_knn()


if __name__ == "__main__":
    main()
