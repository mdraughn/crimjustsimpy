import collections.abc as abc
from typing import Iterator, Callable

from . import SimpleRandomCase
from ...trial import CaseFactoryBase


class SimpleRandomCaseFactory(CaseFactoryBase):
    """
    Creates cases on demand, using the conviction probability generator.
    """
    _convict_gen: Callable[[], float]

    def __init__(self, *, convict_gen: Callable[[], float]):
        super().__init__(self.__class__)
        assert isinstance(convict_gen, abc.Callable)
        self._convict_gen = convict_gen

    def gen_case(self) -> SimpleRandomCase:
        cid = self.gen()
        prob_convict = self._convict_gen()
        return SimpleRandomCase(cid=cid, prob_convict=prob_convict, sentence_range=(30, 60))

