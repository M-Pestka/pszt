import unittest
from podejscie1 import get_k, get_m
from podejscie1 import Solver

class Test_utility_functions(unittest.TestCase):

    def test_add_course(self):
        s = Solver(3, 10, k = 30, courses = [])
        course_to_add = ('mat1', 5, 6)
        semesters = [[], [], []]
        self.assertTrue(s._add_course(semesters, course_to_add))
        self.assertEqual(semesters, [[('mat1', 5, 6)], [], []])
        self.assertFalse(s._add_course(semesters, ('pszt', 11, 2)))
        self.assertEqual(semesters, [[('mat1', 5, 6)], [], []])
        self.assertTrue(s._add_course(semesters, ('asd', 5, 5)))
        self.assertEqual(semesters, [[('mat1', 5, 6), ('asd', 5, 5)], [], []])
        self.assertTrue(s._add_course(semesters, ('ghj', 1, 2)))
        self.assertEqual(semesters, [[('mat1', 5, 6), ('asd', 5, 5)], [('ghj', 1, 2)], []])


    def test_get_k(self):
        semesters = [[('mat1', 4, 6), ('inf1', 3, 5)], [('mat2', 5, 2)], []]
        self.assertEqual(get_k(semesters), 13)
        self.assertEqual(get_k(semesters[0]), 11)
        self.assertEqual(get_k(semesters[-1]), 0)
        self.assertEqual(get_k([[] for i in range(10)]), 0)

    def test_get_m(self):
        semesters = [[('mat1', 4, 6), ('inf1', 3, 5)], [('mat2', 5, 2)], []]
        self.assertEqual(get_m(semesters), 12)
        self.assertEqual(get_m(semesters[1]), 5)
        self.assertEqual(get_m(semesters[-1]), 0)
        self.assertEqual(get_m([[] for i in range(5)]), 0)

class Test_safd(unittest.TestCase):


    def test_large_example(self):
        self.assertTrue(False)
        

    def test_simple_example(self):
        courses = [('mat1', 4, 6), ('inf1', 3, 5), ('mat2', 5, 2)]
        s = Solver(2, 4, 10, courses = courses)
        s.solve()
        self.assertEqual(s.get_min_num_days(), 7)
        sem = s.get_best_semesters()
        self.assertTrue([('mat1', 4, 6)] in sem)


    def test_impossible_example(self):
        self.assertTrue(False)
        

if(__name__ == '__main__'):
    unittest.main()