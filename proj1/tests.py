import unittest
import random 
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

class Test_solver(unittest.TestCase):

    def test_large_example(self):
        courses = [
            ('mat', 6, 7),
            ('ang', 3, 5),
            ('mat2', 4, 2),
            ('pszt', 12, 4),
            ('aal', 9, 5),
            ('algb', 5, 3),
            ('bd', 3, 4),
            ('iop', 31, 2)
        ]

        s = Solver(2, 12, 15, courses = courses)

        s.solve()
        # mniejsze lub równe bo tyle mi się udało wyliczyć.
        print(s.get_best_semesters())
        self.assertLessEqual(s.get_min_num_days(), 12)
       
    def test_constraints(self):

        courses = [('a'*i, int(random.random()*10), int(random.random()*10)) for i in range(100)]

        tests_done = 0
        for i in range(100):
            N = int(random.random()*6)
            m = int(random.random()*20)
            k = int(random.random()*100)
            s = Solver(N, m, k, courses)
            try:
                    s.solve()
            except Exception as e:
                continue 

            semesters = s.get_best_semesters()
            self.assertGreaterEqual(get_k(semesters), k)
            for s in semesters:
                self.assertLessEqual(get_m(s), m)
                  
            tests_done += 1
        self.assertGreater(tests_done, 20)


    def test_simple_example(self):
        courses = [('mat1', 4, 6), ('inf1', 3, 5), ('mat2', 5, 2)]
        s = Solver(2, 4, 10, courses = courses)
        s.solve()
        self.assertEqual(s.get_min_num_days(), 7)
        sem = s.get_best_semesters()
        self.assertTrue([('mat1', 4, 6)] in sem)


    def test_impossible_example(self):
        courses = [('mat1', 4, 6), ('inf1', 3, 5), ('mat2', 5, 2)]
        s = Solver(2, 4, 12, courses = courses)
        with self.assertRaises(Exception):
            s.solve()

class Test_data_loading(unittest.TestCase):

    def test_example(self):
        pass
        

if(__name__ == '__main__'):
    unittest.main()
