from unittest import TestCase

from crimjustsimpy.random import RandomScaledBetaProb


class TestRandomScaledBetaProb(TestCase):

    def verify_range(self, sample, lower_limit, upper_limit):
        for s in sample:
            self.assertGreaterEqual(s, lower_limit)
            self.assertLessEqual(s, upper_limit)

    def test_generate_range(self):
        """
        Generate a bunch of numbers in the range 0.0 to 1.0
        """
        rand = RandomScaledBetaProb()
        sample = [rand() for i in range(1000)]
        self.verify_range(sample, 0.0, 1.0)

    def verify_generate_shifted_range(self, lower, upper):
        rand = RandomScaledBetaProb(lower=lower, upper=upper)
        sample = [rand() for i in range(1000)]
        self.verify_range(sample,lower,upper)

    def test_generate_shifted_range(self):
        self.verify_generate_shifted_range(100.0,150.0)

    def test_generate_negative_range(self):
        self.verify_generate_shifted_range(-150.0,100.0)

    def test_generate_spanning_range(self):
        self.verify_generate_shifted_range(-100.0,100.0)

    def test_missed_range(self):
        self.assertRaises(AssertionError, lambda: RandomScaledBetaProb(lower=0.0, upper=1.0, middle=2.0))
