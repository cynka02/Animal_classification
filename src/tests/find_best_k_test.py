import unittest
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from src.models.kNN import find_best_k


class TestFindBestK(unittest.TestCase):
    """
        Unit tests for the find_best_k function from the kNN model.
        The tests validate whether the function returns a valid k value.
    """

    def setUp(self):
        """
            Sets up a synthetic classification data for testing.
        """

        X, y = make_classification(n_samples=100, n_features=5, n_classes=2, random_state=42)
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    def test_find_best_k(self):
        """
            Test if find_best_k returns a valid k within the expected range.
        """

        best_k = find_best_k(self.x_train, self.x_test, self.y_train, self.y_test)
        self.assertTrue(1 <= best_k <= len(self.x_train))

    def test_is_best_k_integer(self):
        """
            Test if find_best_k returns an integer value.
        """

        best_k = find_best_k(self.x_train, self.x_test, self.y_train, self.y_test)
        # Check if best_k is an integer
        self.assertIsInstance(best_k, int)


if __name__ == "__main__":
    unittest.main()
