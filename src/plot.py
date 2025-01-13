import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from models.RandomForest import get_model_random_forest
from src.load_dataset import split_data, load_data


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
    plt.savefig('plots/' + filename + '.png')


def correlation(title, filename):
    """
        Heatmap is generated to show the correlation heatmap of the animals' features.
    """

    corr = data.iloc[:, 1:-1].corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title(title)
    plt.savefig('plots/' + filename + '.png')


def feature_importance(title, x_label, y_label, filename):
    """
        The bar chart is generated to show the importance of animals' features based on the
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
    plt.savefig('plots/' + filename + '.png')


def main():
    distribution(title='Distribution of animal class types', x_label='Class type', y_label='Count',
                 filename='class_type_distribution')
    correlation(title='Correlation Heatmap', filename='correlation_between_features')
    feature_importance(title='Feature Importance from Random Forest', x_label='Features', y_label='Importance',
                       filename='feature_importance')


if __name__ == '__main__':
    main()
