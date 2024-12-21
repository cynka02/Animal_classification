from sklearn.ensemble import RandomForestClassifier
from src.load_dataset import split_data


def get_model_RandomForest():
    x_train, x_test, y_train, y_test = split_data()
    model = RandomForestClassifier()
    model.fit(x_train, y_train)

    return model


def main():
    get_model_RandomForest()


if __name__ == "__main__":
    main()
