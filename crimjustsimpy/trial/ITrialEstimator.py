import abc

from . import ICase, ResultSummary


class ITrialEstimator(metaclass=abc.ABCMeta):
    """
    Creates cases on demand.
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'estimate') and
            callable(subclass.estimate)) or NotImplemented

    @abc.abstractmethod
    def estimate(self, case: ICase) -> ResultSummary:
        """Generate a new case"""
        raise NotImplementedError