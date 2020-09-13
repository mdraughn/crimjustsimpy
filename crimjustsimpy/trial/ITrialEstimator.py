import abc

from . import ICase, ResultSummary


class ITrialEstimator(metaclass=abc.ABCMeta):
    """
    Creates cases on demand.
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'estimate') and
                callable(subclass.estimate) and
                hasattr(subclass,'key')) or NotImplemented

    @abc.abstractmethod
    def estimate(self, case: ICase) -> ResultSummary:
        """Generate a new case"""
        raise NotImplementedError

    @property
    def key(self) -> str:
        """Generate a key for indexing."""
        raise NotImplementedError