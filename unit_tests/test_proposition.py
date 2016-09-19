import unittest
import sys
import ast
from itertools import count
from sympy import *
sys.path.insert(0, '..')
from retic.proposition import *

class TestProp(unittest.TestCase):

    t_map={}
    p1 = PrimP('x', int)
    p2 = PrimP('y', str)
    p3 = PrimP('x', int)

    x1, x2 = symbols('1 2')

    def test_and_1(self):
        res, t_map = self.p1.transform_and_reduce(self.t_map)

        self.assert_(res == self.x1)
        p_and1 = AndProp([AndProp([self.p1, self.p1]), self.p2])
        res, t_map = p_and1.transform_and_reduce(t_map)
        self.assert_(res.equals(And(self.x1, self.x2)))

    def test_or_1(self):
        p_or1 = OrProp([OrProp([self.p1, self.p2]), self.p2])
        res, t_map = p_or1.transform_and_reduce(self.t_map)
        self.assert_(res.equals(Or(self.x2, self.x1)))


    def test_all(self):
        p_all = NotProp(AndProp([self.p3, self.p1]))
        res, t_map = p_all.transform_and_reduce(self.t_map)
        assert len(t_map) == 1

    def test_trans_back(self):
        self.assert_(Proposition.transform_back(self.x1, self.t_map) == self.p1)

        self.assert_(Proposition.transform_back(And(self.x1, self.x2), self.t_map) ==
                     AndProp([self.p1, self.p2]))
        self.assert_(Proposition.transform_back(Not(self.x1), self.t_map) == NotProp(self.p1))
        self.assert_(Proposition.transform_back(Or(Not(self.x1), Not(self.x2)), self.t_map) ==
                     OrProp([NotProp(self.p1), NotProp(self.p2)]))

