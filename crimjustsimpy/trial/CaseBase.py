import abc
from typing import Callable
from enum import Enum

from crimjustsimpy.trial import ICase

class CaseBase():
    __cid: int

    def __init__(self, cid: int):
        assert 0 < cid
        self.__cid = cid

    @property
    def cid(self): return self.__cid

