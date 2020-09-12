import abc
from typing import Callable
from enum import Enum

from crimjustsimpy.trial import Verdict


class ResultBase():
    """
    Represents a case working its way through the justice system
    """
    __verdict:Verdict
    __sentence:float

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'verdict') and
                hasattr(subclass, 'sentence')) or NotImplemented

    @property
    def verdict(self): return self.__verdict

    @property
    def sentence(self): return self.__sentence
