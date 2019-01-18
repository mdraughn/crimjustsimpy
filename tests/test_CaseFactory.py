from unittest import TestCase

from crimjustsim import Case,CaseFactory


class TestCaseFactory(TestCase):

    def test_iteration(self):
        gg = [0.1,0.2,0.3]
        cf = CaseFactory(convict_gen=iter(gg))
        self.validate_new(cf, 0, 0.1)
        self.validate_new(cf, 1, 0.2)
        self.validate_new(cf, 2, 0.3)

    def validate_new(self, cf, id, pc):
        case = next(cf)
        self.assertIsInstance(case,Case)
        self.assertEqual(case.id, id)
        self.assertEqual(case.prob_convict, pc)
