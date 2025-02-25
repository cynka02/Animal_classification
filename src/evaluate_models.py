from models.kNN import get_model_knn
from models.DecisionTree import get_model_decision_tree
from models.SVC import get_model_svc
from models.RandomForest import get_model_random_forest
from models.KMeans import get_model_kmeans
from models.GradientBoosting import get_model_gradient_boosting
from utils import split_data, get_repo_path
from sklearn.metrics import accuracy_score
from config import OUTPUT_FILE_PATH
import json


def evaluate_models():
    """
        Trains all available models and evaluate them to find the best fitted model.

        Returns:
            dict: Model names and accuracy.
    """

    _, x_test, _, y_test = split_data()

    knn = get_model_knn()
    decision_tree = get_model_decision_tree()
    svc = get_model_svc()
    random_forest = get_model_random_forest()
    kmeans = get_model_kmeans()
    gradient_boosting = get_model_gradient_boosting()

    models_evaluation = {'kNN': accuracy_score(y_test, knn.predict(x_test)),
                         'Decision Tree': accuracy_score(y_test, decision_tree.predict(x_test)),
                         'SVC': accuracy_score(y_test, svc.predict(x_test)),
                         'Random Forest': accuracy_score(y_test, random_forest.predict(x_test)),
                         'KMeans': accuracy_score(y_test, kmeans.predict(x_test)),
                         'Gradient Boosting': accuracy_score(y_test, gradient_boosting.predict(x_test))}

    return models_evaluation


def save_to_json(models_accuracy):
    """
        Saves models accuracy to .json file.
    """

    with open(get_repo_path() / OUTPUT_FILE_PATH, 'w') as f:
        json.dump(models_accuracy, f)


def main():
    models_accuracy = evaluate_models()
    save_to_json(models_accuracy)


if __name__ == '__main__':
    main()
