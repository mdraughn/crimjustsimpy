import abc
from typing import Callable
from enum import Enum

from crimjustsimpy.trial import Verdict


class IResult(metaclass=abc.ABCMeta):
    """
    Represents the result of a case.
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'verdict') and
                hasattr(subclass, 'sentence')) or NotImplemented


