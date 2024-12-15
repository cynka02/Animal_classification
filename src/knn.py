import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


def find_best_k(train, test, classes):

    # create models for each k
    # return k
    pass


def get_model_knn():
    data = pd.read_csv('../data/zoo.csv')
    data = data.drop('animal_name', axis=1)

    train, test = train_test_split(data, test_size=0.2)

    k = find_best_k(train, test)

    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(train, data['class_type'])

    return knn


def main():

    get_model_knn()


if __name__ == "__main__":
    main()
