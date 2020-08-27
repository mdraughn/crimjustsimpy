import collections.abc as abc
import typing as typ
from typing import Iterator

from . import SimpleRandomCase
from crimjustsimpy.trial import trial


class SimpleRandomCaseFactory(trial.CaseFactoryBase):
    """
    Creates cases on demand, using the conviction probability generator.
    """
    _convict_gen: Iterator[float]

    def __init__(self, *, convict_gen: typ.Iterator[float]):
        super().__init__(self.__class__)
        assert isinstance(convict_gen, abc.Iterator)
        self._convict_gen = convict_gen


    def gen_case(self) -> SimpleRandomCase:
        cid = trial.gen_id()
        prob_convict = next(self._convict_gen)
        return SimpleRandomCase(cid=cid, prob_convict=prob_convict, sentence_range=(30, 60))

