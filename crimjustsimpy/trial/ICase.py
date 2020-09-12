import abc


class ICase(metaclass=abc.ABCMeta):
    """
    Represents a case working its way through the justice system
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'cid'))

    @property
    def cid(self): raise NotImplementedError()
