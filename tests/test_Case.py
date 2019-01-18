from unittest import TestCase

from crimjustsim import Case


class TestClassCase(TestCase):

    def test_constructor_range(self):
        """
        Verify that the constructor does range checks on the probability.
        """
        self.assertRaises(AssertionError, lambda: Case(id=123,prob_convict=-0.1))
        self.assertIsNotNone(Case(id=123,prob_convict=0))
        self.assertIsNotNone(Case(id=123,prob_convict=1))
        self.assertRaises(AssertionError, lambda: Case(id=123,prob_convict=1.01))
