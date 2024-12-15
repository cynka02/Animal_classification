from knn import get_model_knn
from DecisionTree import get_model_DecisionTree
from svc import get_model_SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd


def compute_accuracy(model, test):
    test_classes = test['class_type']
    test = test.drop(columns=['class_type', 'animal_name'])

    return accuracy_score(test_classes, model.predict(test))


def evaluate_models(path_to_dataset):
    data = pd.read_csv(path_to_dataset)
    train, test = train_test_split(data, test_size=0.3, random_state=42)

    knn = get_model_knn(path_to_dataset)
    decision_tree = get_model_DecisionTree(path_to_dataset)
    svc = get_model_SVC(path_to_dataset)

    models_evaulation = {'kNN': compute_accuracy(knn, test),
                         'Decision Tree': compute_accuracy(decision_tree, test),
                         'SVC': compute_accuracy(svc, test)}

    print(models_evaulation)

def main():

    evaluate_models('../data/zoo.csv')


if __name__ == "__main__":
    main()
