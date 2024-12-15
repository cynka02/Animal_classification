import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


def accuracy_of_model(model, test):
    # test model
    # return percent of accuracy
    pass

def find_best_k(train, test, classes):
    for k in range(1, 10):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(train, classes)
        #
    # return k
    pass


def get_model_knn():
    data = pd.read_csv('../data/zoo.csv')
    classes = pd.read_csv('../data/class.csv')
    data = data.drop('animal_name', axis=1)
    classes = classes['Class_Number']

    train, test = train_test_split(data, test_size=0.2)

    k = find_best_k(train, test)

    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(train, classes)

    return knn


def main():

    get_model_knn()


if __name__ == "__main__":
    main()
