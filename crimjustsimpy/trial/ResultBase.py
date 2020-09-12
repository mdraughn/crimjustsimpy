from . import Verdict, IResult


class ResultBase(IResult):
    """
    Represents a case working its way through the justice system
    """
    __verdict: Verdict
    __sentence: float

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'verdict') and
                hasattr(subclass, 'sentence')) or NotImplemented

    def __init__(self, verdict: Verdict, sentence: float):
        self.__verdict = verdict
        self.__sentence = sentence

    @property
    def verdict(self): return self.__verdict

    @property
    def sentence(self): return self.__sentence
