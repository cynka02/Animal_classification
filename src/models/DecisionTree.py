from sklearn.tree import DecisionTreeClassifier
from src.load_dataset import split_data


def get_model_decision_tree():
    """
        Trains a Decision Tree Classifier model.

        Returns:
            DecisionTreeClassifier: A trained Decision Tree Classifier model.
    """
    x_train, x_test, y_train, y_test = split_data()
    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)
    return model


def main():
    get_model_decision_tree()


if __name__ == "__main__":
    main()
