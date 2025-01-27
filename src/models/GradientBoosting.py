from sklearn.ensemble import GradientBoostingClassifier
from src.load_dataset import split_data
from src.config import SEED


def get_model_gradient_boosting():
    """
        Trains a Gradient Boosting Classifier model.

        Returns:
            GradientBoostingClassifier: A trained Gradient Boosting Classifier model.
    """

    x_train, x_test, y_train, y_test = split_data()
    model = GradientBoostingClassifier(random_state=SEED)
    model.fit(x_train, y_train)
    return model


def main():
    get_model_gradient_boosting()


if __name__ == '__main__':
    main()
