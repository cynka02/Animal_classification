from sklearn.ensemble import RandomForestClassifier
from utils import split_data
from config import SEED


def get_model_random_forest():
    """
        Trains a Random Forest Classifier model.

        Returns:
            RandomForestClassifier: A trained Random Forest Classifier model.
    """

    x_train, x_test, y_train, y_test = split_data()
    model = RandomForestClassifier(random_state=SEED)
    model.fit(x_train, y_train)

    return model


def main():
    get_model_random_forest()


if __name__ == '__main__':
    main()
