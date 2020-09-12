from typing import Callable
from ..core import IdGenerator
from . import ICaseFactory, ICase


class CaseFactoryBase(ICaseFactory):
    cls: Callable[[int],ICase]

    def __init__(self, cls, *, id_generator:Callable[[],int] = None):
        self.cls = cls
        self.gen = id_generator or IdGenerator()

    def gen_case(self) -> ICase:
        """Generate a new case"""
        return self.cls(self.gen())