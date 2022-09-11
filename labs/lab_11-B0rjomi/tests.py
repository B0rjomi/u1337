# Вопрос 3
def repeatedly_cube_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'lab_11)")
    <BLANKLINE>
    >>> scm("(repeatedly-cube 100 1)")
    1
    >>> scm("(repeatedly-cube 2 2)")
    512
    >>> scm("(repeatedly-cube 3 2)")
    134217728
    """
    pass

# Вопрос 4
def scheme_def_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'lab_11)")
    <BLANKLINE>
    >>> scm("(def f(x y) (+ x y))")
    f
    >>> scm("(f 2 3)")
    5
    >>> scm("(f 10 20)")
    30
    >>> scm("(def factorial(x) (if (zero? x) 1 (* x (factorial (- x 1)))))")
    factorial
    >>> scm("(factorial 4)")
    24
    """
    pass

# Вопрос 5
def switch_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'lab_11)")
    <BLANKLINE>
    >>> scm("(switch 1 ((1 (print 'a)) (2 (print 'b)) (3 (print 'c))))")
    a
    >>> scm("(switch (+ 1 1) ((1 (print 'a))  (2 (print 'b)) (3 (print 'c))))")
    b
    >>> scm("(define x 'b)")
    x
    >>> scm("(switch x ((a (print 1)) (b (print 2)) (c (print 3))))")
    2
    """
    pass

# Вопрос 6
def dragon_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'lab_11)")
    <BLANKLINE>
    >>> scm("(flatmap (lambda (x) (list (+ x 10) x)) nil)")
    ()
    >>> scm("(flatmap list '(1 2 3))")
    (1 2 3)
    >>> scm("(flatmap (lambda (x) (list (+ x 10) x)) '(1 2 3))")
    (11 1 12 2 13 3)
    >>> scm("(expand '(f))")
    (f)
    >>> scm("(expand '(x))")
    (x r y f r)
    >>> scm("(expand '(y))")
    (l f x l y)
    >>> scm("(expand '(f x y))")
    (f x r y f r l f x l y)
    >>> scm("(expand '(f r l f r l x x))")
    (f r l f r l x r y f r x r y f r)
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