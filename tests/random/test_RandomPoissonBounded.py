from unittest import TestCase

from crimjustsimpy.random import RandomPoissonBounded


class TestRandomPoissonBounded(TestCase):

    def verify_range(self, sample, lower_limit, upper_limit):
        for s in sample:
            self.assertGreaterEqual(s, lower_limit)
            self.assertLessEqual(s, upper_limit)

    def test_generate_range_default(self):
        """
        Generate a bunch of numbers in the range 0.0 to 1.0
        """
        gen = RandomPoissonBounded()
        sample = [next(gen) for i in range(1000)]
        self.verify_range(sample, 0, 10) # Should mostly fit. Mostly.

    def test_generate_range(self):
        """
        Generate a bunch of numbers in the range 0.0 to 1.0
        """
        gen = RandomPoissonBounded(loc=5,mean=10)
        sample = [next(gen) for i in range(1000)]
        self.verify_range(sample, 5, 30) # Should mostly fit. Mostly.

    def test_missed_range(self):
        """
        Generate an error if too few numbers would be in range.
        """
        self.assertRaises(AssertionError, lambda: RandomPoissonBounded(mean=10.0, lower=0.0, upper=1.0))
