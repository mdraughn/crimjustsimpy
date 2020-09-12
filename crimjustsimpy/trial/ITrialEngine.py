import abc

from . import IResult, ICase


class ITrialEngine(metaclass=abc.ABCMeta):
    """
    A mechanism of converting an ICase into an IVerdict
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'try_case') and
            callable(subclass.try_case)) or NotImplemented

    def try_case(self, case: ICase) -> IResult:
        raise NotImplementedError()
