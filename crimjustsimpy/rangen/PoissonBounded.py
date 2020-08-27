from typing import Callable

import scipy.stats
from scipy.stats import poisson


def PoissonBounded(*, mean: float = 1, loc: int = 0, lower: float = 0, upper: float = 1000,
                 sanity: float = 0.01) -> Callable[[],float]:
    """Generates numbers from a Poisson distribution with range limits.

    :param mean: Mean of the poisson curve.
    :param loc: Offset location of the poisson curve.
    :param lower: Lower bound of value to generate.
    :param upper: Upper bound of values to generate.
    :param sanity: Reject parameters if less than this fraction of numbers would be accepted.
    :return:
    """

    # Range check.
    assert lower <= mean <= upper

    # Calculate the required mu parameter.
    mu = mean - loc

    # Check that this won't discard too many generated values.
    dist = scipy.stats.poisson(mu)
    if dist.cdf(upper) - dist.cdf(lower) < sanity:
        raise ValueError("Poisson curve overlaps acceptable range ({1},{2}) by less than {0}"
                         .format(sanity, lower, upper))

    # Helper to do a random draw.
    def raw_draw() -> int:
        return poisson.rvs(mu, loc=loc)

    # Return the generator.
    def rand():
        while True:
            n = raw_draw()
            while not (lower <= n <= upper):
                n = raw_draw()
            return n

    return rand
