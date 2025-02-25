import matplotlib.pyplot as plt
import seaborn as sns
import json
from models.RandomForest import get_model_random_forest
from models.DecisionTree import get_model_decision_tree
from sklearn.tree import plot_tree
from utils import *
from config import *


data = load_data()


def distribution(title, x_label, y_label, filename):
    """
        A count plot is generated to show the count of animals in each class type.
    """

    plt.figure(figsize=(8, 6))
    sns.countplot(x='class_type', data=data, color='plum')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(get_repo_path() / 'plots' / filename)


def correlation(title, filename):
    """
        Heatmap is generated to show the correlation heatmap of the animal features.
    """

    corr = data.iloc[:, 1:-1].corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title(title)
    plt.savefig(get_repo_path() / 'plots' / filename)


def feature_importance(title, x_label, y_label, filename):
    """
        The bar chart is generated to show the importance of animal features based on the
        trained Random Forest model.
    """

    model = get_model_random_forest()
    x_train, _, _, _ = split_data()
    importance = pd.Series(model.feature_importances_, index=x_train.columns).sort_values(ascending=False)

    plt.figure(figsize=(16, 12))
    importance.plot(kind='bar', color='hotpink')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(get_repo_path() / 'plots' / filename)


def plot_decision_tree(model, filename):
    """
        Plots the trained Decision Tree Classifier model.
    """

    feature_names = data.drop(columns=['animal_name', 'class_type']).columns.tolist()
    plt.figure(figsize=(18, 22))
    plot_tree(model, feature_names=feature_names, class_names=CLASS_NAMES, fontsize=12, impurity=False)
    plt.savefig(get_repo_path() / 'plots' / filename)


def plot_accuracy(title, filename):
    """
        Plots accuracy of models from file accuracy.json.
    """

    with open(get_repo_path() / OUTPUT_FILE_PATH) as f:
        models_accuracy = json.load(f)
    y, x = zip(*sorted(models_accuracy.items()))
    accuracy_list = pd.Series(x, y).sort_values(ascending=False)

    plt.figure(figsize=(18, 22))
    accuracy_list.plot(kind='bar', color='hotpink', fontsize=18)
    plt.title(title, fontsize=40)
    plt.savefig(get_repo_path() / 'plots' / filename)


def main():
    distribution(title='Distribution of animal class types', x_label='Class type', y_label='Count',
                 filename='class_type_distribution.png')
    correlation(title='Correlation Heatmap', filename='correlation_between_features.png')
    feature_importance(title='Feature Importance from Random Forest', x_label='Features', y_label='Importance',
                       filename='feature_importance.png')
    plot_decision_tree(model=get_model_decision_tree(), filename='decision_tree.png')
    plot_accuracy(title='Models accuracy', filename='accuracy_plot.png')


if __name__ == '__main__':
    main()
