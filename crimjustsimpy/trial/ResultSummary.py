from crimjustsimpy.trial import Verdict, IResult


class ResultSummary():
    guilty_count: int
    not_guilty_count: int
    mistrial_count: int
    count: int
    sentence_sum: int

    def __init__(self):
        self.guilty_count = 0
        self.not_guilty_count = 0
        self.mistrial_count = 0
        self.count = 0
        self.sentence_sum = 0

