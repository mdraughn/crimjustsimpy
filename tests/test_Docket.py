from unittest import TestCase

from crimjustsimpy import Case,Docket


class TestClassDocket(TestCase):

    def test_constructor(self):
        docket = Docket()
        self.assertIsNotNone(docket.cases)
        self.assertEqual(len(docket.cases),0)

    def test_fill(self):
        docket = Docket()
        docket.fill(999,3,iter([Case(id=1,prob_convict=0.1),Case(id=2,prob_convict=0.2),
                           Case(id=3,prob_convict=0.3)]))
        self.assertEqual(len(docket.cases),3)
        self.assertEqual(docket.cases[0].docket,docket)
        self.assertEqual(docket.cases[0].id,1)
        self.assertEqual(docket.cases[0].prob_convict,0.1)
        self.assertEqual(docket.cases[1].docket,docket)
        self.assertEqual(docket.cases[1].id,2)
        self.assertEqual(docket.cases[1].prob_convict,0.2)
        self.assertEqual(docket.cases[2].docket,docket)
        self.assertEqual(docket.cases[2].id,3)
        self.assertEqual(docket.cases[2].prob_convict,0.3)

