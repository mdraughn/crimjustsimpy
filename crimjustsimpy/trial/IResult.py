import abc


class IResult(metaclass=abc.ABCMeta):
    """
    Represents the result of a case.
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'verdict') and
                hasattr(subclass, 'sentence')) or NotImplemented

    @property
    def verdict(self): raise NotImplementedError()

    @property
    def sentence(self): raise NotImplementedError()