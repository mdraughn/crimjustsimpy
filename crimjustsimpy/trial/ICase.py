import abc


class ICase(metaclass=abc.ABCMeta):
    """
    Represents a case working its way through the justice system
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'cid') and
                hasattr(subclass, 'key'))

    @property
    def cid(self): raise NotImplementedError()

    @property
    def key(self) -> str:
        """Generate a key for indexing."""
        raise NotImplementedError