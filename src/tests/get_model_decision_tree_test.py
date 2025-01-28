import unittest
from sklearn.tree import DecisionTreeClassifier
import repackage
repackage.up()
from models.DecisionTree import get_model_decision_tree


class TestDecisionTreeModel(unittest.TestCase):
    def test_return_type(self):
        """
            Test if get_model_decision_tree returns an instance of DecisionTreeClassifier.
        """
        model = get_model_decision_tree()
        self.assertIsInstance(model, DecisionTreeClassifier)


if __name__ == "__main__":
    unittest.main()
