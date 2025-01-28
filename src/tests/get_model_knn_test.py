import unittest
from sklearn.neighbors import KNeighborsClassifier
import repackage
repackage.up()
from models.kNN import get_model_knn


class TestKNNModel(unittest.TestCase):
    def test_return_type(self):
        model = get_model_knn()
        self.assertIsInstance(model, KNeighborsClassifier)


if __name__ == "__main__":
    unittest.main()
