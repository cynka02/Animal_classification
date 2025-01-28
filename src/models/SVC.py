from sklearn.svm import SVC
from utils import split_data
from config import SEED


def get_model_svc():
    """
        Trains a Support Vector Classifier (SVC) model

        Returns:
            SVC: A trained Support Vector Classifier model.
    """

    x_train, x_test, y_train, y_test = split_data()
    model = SVC(probability=True, random_state=SEED)
    model.fit(x_train, y_train)
    return model


def main():
    get_model_svc()


if __name__ == '__main__':
    main()
