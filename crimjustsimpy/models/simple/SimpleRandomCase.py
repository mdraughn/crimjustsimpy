from typing import Tuple

from ...trial import CaseBase


class SimpleRandomCase(CaseBase):
    """
    Represents a case working its way through the justice system
    """
    prob_convict: float
    sentence_min: int
    sentence_max: int

    def __init__(self, cid: int, *, prob_convict: float, sentence_range: Tuple[float, float]):
        super().__init__(cid)

        assert 0 <= prob_convict <= 1
        assert 0 <= sentence_range[0] <= sentence_range[1]

        self.prob_convict = prob_convict
        self.sentence_min, self.sentence_max = sentence_range
