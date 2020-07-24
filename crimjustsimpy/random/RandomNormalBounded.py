import random
import scipy.stats


def RandomNormalBounded(mean: float = 0.0, std: float = 1.0, *, lower: float = 0.0, upper: float = 1.0, snap_limit: bool = False,
                 sanity: float = 0.01):
    """Generates numbers from a normal distribution with range limits.

    :param mean: Mean of the normal curve.
    :param std:  Standard deviation of the normal curve.
    :param lower: Lower bound of value to generate.
    :param upper: Upper bound of values to generate.
    :param snap_limit: If True, snap out-of-bound values to the nearest limit.
    :param sanity: Reject parameters if less than this fraction of numbers would be accepted.
    :return:
    """

    """
    """
    # Range check.
    assert lower <= upper

    # Check that this won't discard too many generated values.
    if not snap_limit:
        dist = scipy.stats.norm(mean, std)
        if dist.cdf(upper) - dist.cdf(lower) < sanity:
            raise ValueError("Normal curve overlaps acceptable range ({1},{2}) by less than {0}"
                             .format(sanity, lower, upper))

    while True:
        p = lower - 1
        while not (lower <= p <= upper):
            p = random.normalvariate(mean, std)

            # Snap out-of-bounds values in bounds.
            if snap_limit:
                p = min(max(p, lower), upper)
        yield p
