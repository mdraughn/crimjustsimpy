from unittest import TestCase
from crimjustsimpy.trial import IResult, ResultBase, Verdict


class TestResultBase(TestCase):

    def test_result_base(self):
        self.assertTrue(issubclass(ResultBase,IResult),"ResultBase must implement IResult")
        rslt = ResultBase(Verdict.guilty, 3.14159)
        self.assertIsInstance(rslt,IResult,"ResultBase instances must implement IResult")
        self.assertEqual(rslt.verdict,Verdict.guilty,"Constructor must initialize verdict.")
        self.assertEqual(rslt.sentence,3.14159,"Constructor must initialize sentence.")
