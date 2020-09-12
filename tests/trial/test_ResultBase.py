from unittest import TestCase
from crimjustsimpy.trial import IResult, ResultBase


class TestResultBase(TestCase):

    def test_result_base(self):
        self.assertTrue(issubclass(ResultBase,IResult),"ResultBase must implement IResult")
        rslt = ResultBase()
        self.assertIsInstance(rslt,IResult,"ResultBase instances must implement IResult")
