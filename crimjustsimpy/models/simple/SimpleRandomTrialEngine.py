from scipy.stats import uniform

from . import SimpleRandomCase
from ...trial import IResult, ResultBase, Verdict


class SimpleRandomTrialEngine:

    def try_case(self, case: SimpleRandomCase) -> IResult:
        assert isinstance(case,SimpleRandomCase)

        draw = uniform.rvs()

        # Random trial outcome based on probability of a conviction.
        if draw < case.prob_convict:
            sentence_span = case.sentence_max - case.sentence_min
            sentence = case.sentence_min + (uniform.rvs() * sentence_span)
            result = ResultBase(Verdict.guilty, sentence)
        else:
            result = ResultBase(Verdict.not_guilty, 0)

        return result