import abc
from typing import Callable
from enum import Enum

class ITrialEngine(metaclass=abc.ABCMeta):
    """
    A mechanism of converting an ICase into an IVerdict
    """
    cid: int
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'cid'))
