from sklearn.cluster import KMeans
from load_dataset import split_data
from config import SEED


def get_model_kmeans():
    """
        Trains a KMeans clustering model.

        Returns:
            KMeans: A trained KMeans clustering model.
    """

    x_train, x_test, y_train, y_test = split_data()
    model = KMeans(n_clusters=7, random_state=SEED)
    model.fit(x_train)
    return model


def main():
    get_model_kmeans()


if __name__ == '__main__':
    main()
