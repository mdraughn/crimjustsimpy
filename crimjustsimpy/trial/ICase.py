import abc
from typing import Callable
from enum import Enum

class ICase(metaclass=abc.ABCMeta):
    """
    Represents a case working its way through the justice system
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'cid'))
