from unittest import TestCase
from crimjustsimpy.trial import ICase, CaseBase


class TestCaseBase(TestCase):

    def test_case_base(self):
        self.assertTrue(issubclass(CaseBase,ICase),"CaseBase must implement ICase")
        case = CaseBase(55)
        self.assertIsInstance(case,ICase,"CaseBase instances must implement ICase")
        self.assertEqual(case.cid, 55, "Case ID is passed in.")
