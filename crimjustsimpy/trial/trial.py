import abc
from typing import Callable
from enum import Enum

from ..core import IdGenerator

__trial_id_generator = IdGenerator()

def gen_id() -> int:
    return next(__trial_id_generator)

class ICase(abc.ABC):
    """
    Represents a case working its way through the justice system
    """
    cid:int

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'cid')) or NotImplemented

class CaseBase(ICase):

    def __init__(self, cid: int):
        assert 0 < cid
        self.cid = cid

class ICaseFactory(abc.ABC):
    """
    Creates cases on demand.
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'gen_case') and
            callable(subclass.gen_case)) or NotImplemented

    @abc.abstractmethod
    def gen_case(self) -> ICase:
        """Generate a new case"""
        raise NotImplementedError

class CaseFactoryBase(ICaseFactory):
    cls: Callable

    def __init__(self,cls):
        self.cls = cls

    def __iter__(self):
        return self

    def __next__(self):
        return self.gen_case()

    def gen_case(self) -> ICase:
        """Generate a new case"""
        return self.cls(gen_id())

class Verdict(Enum):
    guilty = 1
    not_guilty = 2
    mistrial = 3

class CaseOutcome:
    verdict: Verdict
    sentence: float

    def __init__(self, verdict: Verdict, sentence: float):
        self.verdict = verdict
        self.sentence = sentence

class ITrialEngine(abc.ABC):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'try_case') and
            callable(subclass.try_case)) or NotImplemented

    @abc.abstractmethod
    def try_case(self, case: ICase) -> CaseOutcome:
        """Report the case result."""
        assert isinstance(case,ICase)
        raise NotImplementedError

class TrialEngineBase(ITrialEngine):
    def _validate_case(self, case):
        assert isinstance(case,ICase)

    def try_case(self, case: ICase) -> CaseOutcome:
        """Report the case result."""
        self._validate_case(case)
        raise NotImplementedError

