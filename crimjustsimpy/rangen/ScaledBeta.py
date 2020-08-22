import random


def ScaledBetaProb(*, lower: float = 0.0, upper: float = 1.0, shape: float = 2.0, middle: float = None):
    """Create a probability generator using a Beta distribution.
        The ratio between traditional alpha and beta parameters to the Beta distribution
        will be calculated from the mean, with their absolute magnitude described by the scale.

        :param lower: Lowest probability that can be generated.
        :param middle: Mean probability.
        :param upper: Highest probability that can be generated.
        :param shape: A shaping factor controlling the shape of the curve.
    :return:
    """
    if middle is None:
        middle = (lower + upper) / 2

    assert lower <= middle <= upper
    assert shape > 0

    # Calculate derived values.
    width = upper - lower
    mu = (middle - lower) / width
    alpha = shape
    beta = shape * (1 - mu) / mu

    def rand():
        while True:
            # Get a random draw from the Beta distribution.
            p = random.betavariate(alpha, beta)

            # Scale it to the requested range.
            return p * width + lower

    return rand
