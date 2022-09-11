
def add_test():
    """
    >>> scm = scm_fixture()
    >>> scm("   (load 'hw_07)                  ")
    <BLANKLINE>
    >>> scm("   (define odds (list 3 5 7 9))   ")
    odds
    >>> scm("   (add odds 2)                   ")
    (2 3 5 7 9)
    >>> scm("   (add odds 5)                   ")
    (3 5 7 9)
    >>> scm("   (add odds 6)                   ")
    (3 5 6 7 9)
    >>> scm("   (add odds 10)                  ")
    (3 5 7 9 10)
    """
    pass

def cadr_caddr_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'hw_07)")
    <BLANKLINE>
    >>> scm("(cddr '(1 2 3 4))")
    (3 4)
    >>> scm("(cadr '(1 2 3 4))")
    2
    >>> scm("(caddr '(1 2 3 4))")
    3
    """
    pass

def contains_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'hw_07)")
    <BLANKLINE>
    >>> scm("(define odds (list 3 5 7 9))")
    odds
    >>> scm("(contains? odds 3)")
    #t
    >>> scm("(contains? odds 9)")
    #t
    >>> scm("(contains? odds 6)")
    #f
    """
    pass

def intersect_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'hw_07)")
    <BLANKLINE>
    >>> scm("(define odds (list 3 5 7 9))")
    odds
    >>> scm("(define eight (list 1 2 3 4 5 6 7 8))")
    eight
    >>> scm("(intersect odds (list 2 3 4 5))")
    (3 5)
    >>> scm("(intersect odds (list 2 4 6 8))")
    ()
    >>> scm("(intersect odds eight)")
    (3 5 7)
    """
    pass

def ordered_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'hw_07)")
    <BLANKLINE>
    >>> scm("(ordered? '(1 2 3 4 5))")
    #t
    >>> scm("(ordered? '(1 5 2 4 3))")
    #f
    >>> scm("(ordered? '(2 2))")
    #t
    >>> scm("(ordered? '(1 2 2 4 3))")
    #f
    """
    pass

def power_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'hw_07)")
    <BLANKLINE>
    >>> scm("(pow 2 5)")
    32
    >>> scm("(pow 10 3)")
    1000
    >>> scm("(pow 3 3)")
    27
    """
    pass

def sign_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'hw_07)")
    <BLANKLINE>
    >>> scm("(sign -42)")
    -1
    >>> scm("(sign 0)")
    0
    >>> scm("(sign 42)")
    1
    """
    pass

def union_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'hw_07)")
    <BLANKLINE>
    >>> scm("(define odds (list 3 5 7 9))")
    odds
    >>> scm("(define eight (list 1 2 3 4 5 6 7 8))")
    eight
    >>> scm("(union odds (list 2 3 4 5))")
    (2 3 4 5 7 9)
    >>> scm("(union odds (list 2 4 6 8))")
    (2 3 4 5 6 7 8 9)
    >>> scm("(union odds eight)")
    (1 2 3 4 5 6 7 8 9)
    """
    pass

import sys, os
import importlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))+'/scheme')
scheme = importlib.import_module('scheme')

def scm_fixture():
    _frame = scheme.create_global_frame()
    def eval_line(code_line):
        exp = scheme.read_line(code_line)
        result = scheme.scheme_eval(exp, _frame)
        if result==None: return
        if type(result) == bool:
            if result==True:
                print('#t')
            elif result==False:
                print('#f')
        else:
            print(result)
        return
    return eval_line






