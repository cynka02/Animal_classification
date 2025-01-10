import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from models.RandomForest import get_model_random_forest
from src.load_dataset import split_data, load_data


data = load_data()


def distribution():
    """
        A count plot is generated to show the count of animals in each class type.
    """

    plt.figure(figsize=(8, 6))
    sns.countplot(x='class_type', data=data, color='plum')
    plt.title('Distribution of Animal Class Types')
    plt.xlabel('Class Type')
    plt.ylabel('Count')
    plt.savefig('plots/class_type_distribution.png')


def correlation():
    """
        Heatmap is generated to show the correlation heatmap of the animals' features.
    """

    corr = data.iloc[:, 1:-1].corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.savefig('plots/correlation_between_features.png')


def feature_importance():
    """
        The bar chart is generated to show the importance of animals' features based on the
        trained Random Forest model.
    """

    model = get_model_random_forest()
    x_train, _, _, _ = split_data()
    importance = pd.Series(model.feature_importances_, index=x_train.columns).sort_values(ascending=False)
    plt.figure(figsize=(16, 12))
    importance.plot(kind='bar', color='hotpink')
    plt.title('Feature Importance from Random Forest')
    plt.xlabel('Features')
    plt.ylabel('Importance')
    plt.savefig('plots/feature_importance.png')


def main():
    distribution()
    correlation()
    feature_importance()


if __name__ == '__main__':
    main()
