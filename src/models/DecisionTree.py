from sklearn.tree import DecisionTreeClassifier
from utils import split_data
from config import SEED


def get_model_decision_tree():
    """
        Trains a Decision Tree Classifier model.

        Returns:
            DecisionTreeClassifier: A trained Decision Tree Classifier model.
    """

    x_train, x_test, y_train, y_test = split_data()
    model = DecisionTreeClassifier(random_state=SEED)
    model.fit(x_train, y_train)
    return model


def main():
    get_model_decision_tree()


if __name__ == '__main__':
    main()
