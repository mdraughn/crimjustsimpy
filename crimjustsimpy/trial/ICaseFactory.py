import abc

from crimjustsimpy.trial import ICase


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