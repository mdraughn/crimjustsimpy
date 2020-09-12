from . import ICase

class CaseBase(ICase):
    __cid: int

    def __init__(self, cid: int):
        assert 0 < cid
        self.__cid = cid

    @property
    def cid(self): return self.__cid

