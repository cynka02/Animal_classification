from sklearn.svm import SVC
from src.load_dataset import split_data


def get_model_SVC():
    x_train, x_test, y_train, y_test = split_data()
    model = SVC(probability=True)
    model.fit(x_train, y_train)
    return model


def main():
    get_model_SVC()


if __name__ == "__main__":
    main()
