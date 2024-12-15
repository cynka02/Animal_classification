from knn import get_model_knn
from DecisionTree import get_model_DecisionTree
from svc import get_model_SVC
from RandomForest import get_model_RandomForest
from load_dataset import split_data
from sklearn.metrics import accuracy_score


def compute_accuracy(model, test, test_classes):
    return accuracy_score(test_classes, model.predict(test))


def evaluate_models():
    x_train, x_test, y_train, y_test = split_data()

    knn = get_model_knn()
    decision_tree = get_model_DecisionTree()
    svc = get_model_SVC()
    random_forest = get_model_RandomForest()

    models_evaulation = {'kNN': accuracy_score(y_test, knn.predict(x_test)),
                         'Decision Tree': accuracy_score(y_test, decision_tree.predict(x_test)),
                         'SVC': accuracy_score(y_test, svc.predict(x_test)),
                         'Random Forest': accuracy_score(y_test, random_forest.predict(x_test))}

    print(models_evaulation)


def main():

    evaluate_models()


if __name__ == "__main__":
    main()
