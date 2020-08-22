from unittest import TestCase
import crimjustsimpy.rangen as rg


class TestRandomNormalBounded(TestCase):

    def verify_range(self, sample, lower_limit, upper_limit):
        for s in sample:
            self.assertGreaterEqual(s, lower_limit)
            self.assertLessEqual(s, upper_limit)

    def test_generate_range(self):
        """
        Generate a bunch of numbers in the range 0.0 to 1.0
        """
        rand = rg.NormalBounded()
        sample = [rand() for i in range(1000)]
        self.verify_range(sample, 0.0, 1.0)

    def test_generate_snap(self):
        """
        Generate a bunch of numbers in the range 0.0 to 1.0
        Snap out-of-range to range ends.
        """
        rand = rg.NormalBounded(snap_limit=True)
        sample = [rand() for i in range(1000)]
        self.verify_range(sample, 0.0, 1.0)
        zeroes = [1 for s in sample if s == 0.0]
        ones = [1 for s in sample if s == 1.0]
        self.assertGreater(len(zeroes), 400)
        self.assertGreater(len(ones), 120)

    def test_generate_negative_range(self):
        """
        Generate a bunch of numbers in the range -1.0 to 0.0
        """
        rand = rg.NormalBounded(lower=-1.0, upper=0.0)
        sample = [rand() for i in range(1000)]
        self.verify_range(sample,-1.0,0.0)

    def test_generate_negative_snap(self):
        """
        Generate a bunch of numbers in the range -1.0 to 0.0
        """
        rand = rg.NormalBounded(lower=-1.0, upper=0.0, snap_limit=True)
        sample = [rand() for i in range(1000)]
        self.verify_range(sample,-1.0,0.0)
        zeroes = [1 for s in sample if s == 0.0]
        ones = [1 for s in sample if s == -1.0]
        self.assertGreater(len(zeroes), 400)
        self.assertGreater(len(ones), 120)

    def test_missed_range(self):
        """
        Generate an error if too few numbers would be in range.
        """
        with self.assertRaises(ValueError):
            next(rg.NormalBounded(mean=10.0, std=1.0, lower=0.0, upper=1.0))

    def test_missed_range_snap(self):
        """
        Snaps all numbers when way out of range.
        """
        rand = rg.NormalBounded(mean=10.0, std=1.0, lower=0.0, upper=1.0, snap_limit=True)
        sample = [rand() for i in range(1000)]
        self.verify_range(sample, 0.0, 1.0)
        zeroes = [1 for s in sample if s == 0.0]
        ones = [1 for s in sample if s == 1.0]
        self.assertLess(len(zeroes), 1)
        self.assertGreater(len(ones), 999)
