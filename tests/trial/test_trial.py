from unittest import TestCase
from crimjustsimpy.trial.trial import ICase, CaseBase, ICaseFactory, CaseFactoryBase


class TestCaseFramework(TestCase):

    def test_case_base(self):
        self.assertTrue(issubclass(CaseBase,ICase),"CaseBase must implement ICase")
        case = CaseBase(55)
        self.assertIsInstance(case,ICase,"CaseBase instances must implement ICase")

    def test_case_factory_base(self):
        self.assertTrue(issubclass(CaseFactoryBase,ICaseFactory),"CaseFactoryBase must implement ICaseFactory")
        factory = CaseFactoryBase(CaseBase)
        self.assertIsInstance(factory,ICaseFactory,"CaseFactoryBase instances must implement ICaseFactory")
        case = factory.gen_case()
        self.assertIsNotNone(case)
        self.assertIsInstance(case,ICase)
        self.assertGreater(case.cid, 0)