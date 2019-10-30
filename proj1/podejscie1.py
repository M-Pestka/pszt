import sys
import json
import os

def read_data():
    '''
    loads a json from standard input.
    JSON should contain:
    * N - number of semesters
    * m - number of days devoted to learning
    * k - number of points needed.
    * courses - dictionary of all courses where key is the
        courses name and value is a tuple(number of days needed, number of points)
    '''
    return json.load(os.stdin)



def get_k(semesters):
    '''
    calculate number of points gained in the semester
    :param semesters: list of semesters or semester where semester is a list of courses
    :returns: number of points gained
    '''
    if(len(semesters) == 0):
        return 0
        
    if(isinstance(semesters[0], list)):
        return sum([sum([c[2] for c in s]) for s in semesters])
    return sum([c[2] for c in semesters])


def get_m(semesters):
    '''
    returns number of days needed for studying during the semester
    :param semesters: list of semesters or semester where semester is a list of courses
    :returns: sum of days needed for studying
    '''
    if(len(semesters) == 0):
        return 0
        
    if(isinstance(semesters[0], list)):
        return sum([sum([c[1] for c in s]) for s in semesters])
    return sum([s[1] for s in semesters])


class Solver:
    '''
    Solver for the problem of multiple bin packing.
    '''
    def __init__(self, N, m, k, courses):
        '''
        constructor.
        :param N: number of semesters
        :param m: number of days of studying per semester
        :param k: number of points needed
        :param courses: list off all available courses
        :returns: None
        '''
        self.N = N

        # days 
        self.m = m * N
        self.days_per_sem = m

        # points
        self.k = k

        # best sum of days
        self.best_m = None
        self.courses = courses
        self.best_semesters = [[] for i in range(N)]

    def _solve(self, current_semesters, courses):
        if(get_m(current_semesters) > self.best_m):
            # if we already have worse solution
            return

        if(get_k(current_semesters) >= self.k):
            # found a better solution
            self.best_m = get_m(current_semesters)
            self.best_semesters = current_semesters
            return 

        if(len(courses) == 0): 
            # no more courses
            return 

        # iterate over courses
        for i in range(len(courses)):
            copy_courses = courses.copy()
            current_course = courses[i]
            current_semesters_copy = current_semesters.copy()
            # remebmer to add course to semester
            if(not self._add_course(semesters = current_semesters_copy, course = current_course)):
                # course was too large for any of the semesters
                continue

            del copy_courses[i]
            # solve for one course less
            self._solve(current_semesters_copy, copy_courses)

    def solve(self):

        if(self.best_m is None):
            self.best_m = sys.maxsize

        # solve for all semesters anf courses
        self._solve(self.best_semesters.copy(), self.courses.copy())

        # if the solutions has not improved
        if(self.best_m is sys.maxsize):
            raise ValueError('Cannot solve ;_;')

    def _add_course(self, semesters, course):
        '''
        adds course the the semesters
        :param semesters: list of semesters, list(list)
        :param course: single course (name, num_days, num_points)
        '''
        # iterate over semesters
        for s in semesters:
            # if a course fits, it sits
            if(get_m(s) + course[1] <= self.days_per_sem):
                s.append(course)
                return True
        return False

    def get_best_semesters(self):
        return self.best_semesters

    def get_min_num_days(self):
        return self.best_m




            

