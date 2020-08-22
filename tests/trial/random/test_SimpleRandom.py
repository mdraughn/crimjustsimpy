from unittest import TestCase

from crimjustsimpy.rangen.RandomChoice import Choice
from crimjustsimpy.trial.random.SimpleRandomCase import SimpleRandomCase
from crimjustsimpy.trial.random.SimpleRandomCaseFactory import SimpleRandomCaseFactory
from crimjustsimpy.trial.trial import ICase, ICaseFactory


class TestSimpleRandomCase(TestCase):

    def test_interface(self):
        self.assertTrue(issubclass(SimpleRandomCase,ICase),"All case classes must implement ICase")
        case = SimpleRandomCase(1, prob_convict=0.5, sentence_range=(5,10))
        self.assertIsInstance(case,ICase,"All cases must implement ICase")

    def test_constructor(self):
        case = SimpleRandomCase(cid=1, prob_convict=0.5, sentence_range=(5,10))
        self.assertEqual(case.cid,1,"Case id not initialized correctly.")
        self.assertEqual(case.prob_convict,0.5,"Case prob_convict not initialized correctly.")
        self.assertEqual(case.sentence_min,5,"Case sentence_min not initialized correctly.")
        self.assertEqual(case.sentence_max,10,"Case sentence_max not initialized correctly.")

class TestSimpleRandomCaseFactory(TestCase):

    def test_interface(self):
        self.assertTrue(issubclass(SimpleRandomCaseFactory,ICaseFactory),
                        "Case factory classes must implement ICaseFactory")
        factory = SimpleRandomCaseFactory(convict_gen=Choice([0.123]))
        self.assertIsInstance(factory,ICaseFactory,"Case factories must implement ICaseFactory")

    def test_generator(self):
        factory = SimpleRandomCaseFactory(convict_gen=Choice([0.123]))
        case = factory.gen_case()
        self.assertIsNotNone(case)
        self.assertIsInstance(case,SimpleRandomCase)
        self.assertGreater(case.cid, 0)
        self.assertEqual(case.prob_convict,0.123,"Case probability not initialized correctly.")
