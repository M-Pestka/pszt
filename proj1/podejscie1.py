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
    calculate number of points

    '''
    if(len(semesters) == 0):
        return 0
        
    if(isinstance(semesters[0], list)):
        return sum([sum([c[2] for c in s]) for s in semesters])
    return sum([c[2] for c in semesters])


def get_m(semesters):
    '''
    returns number of days
    '''
    if(len(semesters) == 0):
        return 0
        
    if(isinstance(semesters[0], list)):
        return sum([sum([c[1] for c in s]) for s in semesters])
    return sum([s[1] for s in semesters])


class Solver:

    def __init__(self, N, m, k, courses):
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
            self.best_m = get_m(current_semesters)
            self.best_semesters = current_semesters
            return 

        if(len(courses) == 0): 
            if(get_k(current_semesters) < self.k):
                raise ValueError()

        for i in range(len(courses)):
            copy_courses = courses.copy()
            current_course = courses[i]
            # remebmer to add course to semester
            if(not self._add_course(semesters = current_semesters, course = current_course)):
                # course was too large for any of the semesters
                continue

            del copy_courses[i]
            days = self._solve(current_semesters.copy(), copy_courses)

    def solve(self):
        if(self.best_m is None):
            self.best_m = sys.maxsize
        self._solve(self.best_semesters.copy(), self.courses.copy())

    def _add_course(self, semesters, course):
        for s in semesters:
            if(get_m(s) + course[1] <= self.days_per_sem):
                s.append(course)
                return True
        return False

    def get_best_semesters(self):
        return self.best_semesters

    def get_min_num_days(self):
        return self.best_m




            

