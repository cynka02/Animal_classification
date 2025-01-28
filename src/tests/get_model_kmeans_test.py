import unittest
from sklearn.cluster import KMeans
import repackage
repackage.up()
from models.KMeans import get_model_kmeans


class TestKMeansModel(unittest.TestCase):
    def test_return_type(self):
        model = get_model_kmeans()
        self.assertIsInstance(model, KMeans)


if __name__ == "__main__":
    unittest.main()
