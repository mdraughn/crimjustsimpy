from unittest import TestCase

from crimjustsimpy.core import IdGenerator
from crimjustsimpy.trial import ICase, CaseBase, ICaseFactory, CaseFactoryBase


class TestCaseFactoryBase(TestCase):

    def test_default_constructor(self):
        self.assertTrue(issubclass(CaseFactoryBase,ICaseFactory),"CaseFactoryBase must implement ICaseFactory")
        factory = CaseFactoryBase(CaseBase)
        self.assertIsInstance(factory,ICaseFactory,"CaseFactoryBase instances must implement ICaseFactory")
        case = factory.gen_case()
        self.assertIsNotNone(case)
        self.assertIsInstance(case,ICase)
        self.assertGreater(case.cid, 0)

    def test_with_id_gen(self):
        self.assertTrue(issubclass(CaseFactoryBase,ICaseFactory),"CaseFactoryBase must implement ICaseFactory")
        factory = CaseFactoryBase(CaseBase, id_generator=IdGenerator())
        self.assertIsInstance(factory,ICaseFactory,"CaseFactoryBase instances must implement ICaseFactory")
        case = factory.gen_case()
        self.assertIsNotNone(case)
        self.assertIsInstance(case,ICase)
        self.assertGreater(case.cid, 0)