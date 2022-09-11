# Вопрос 1
def reverse_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'hw_08)")
    <BLANKLINE>
    >>> scm("(reverse '())")
    ()
    >>> scm("(reverse '(1))")
    (1)
    >>> scm("(reverse '(1 2 3))")
    (3 2 1)
    >>> scm("(reverse '(1 2 3 4 5))")
    (5 4 3 2 1)
    >>> scm("(reverse '(1 2 3 4 5 1 3 7))")
    (7 3 1 5 4 3 2 1)
    """
    pass

# Вопрос 2
def longest_increasing_subsequence_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'hw_08)")
    <BLANKLINE>
    >>> scm("(longest-increasing-subsequence '())")
    ()
    >>> scm("(longest-increasing-subsequence '(1))")
    (1)
    >>> scm("(longest-increasing-subsequence '(1 2 3))")
    (1 2 3)
    >>> scm("(longest-increasing-subsequence '(1 9 2 3))")
    (1 2 3)
    >>> scm("(longest-increasing-subsequence '(1 9 8 7 6 5 4 3 2 3))")
    (1 2 3)
    >>> scm("(longest-increasing-subsequence '(1 9 8 7 2 3 6 5 4 5))")
    (1 2 3 4 5)
    >>> scm("(longest-increasing-subsequence '(1 2 3 4 9 3 4 1 10 5))")
    (1 2 3 4 9 10)
    """
    pass

# Вопрос 3
def derive_sum_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'hw_08)")
    <BLANKLINE>
    >>> scm("(make-sum 1 3)")
    4
    >>> scm("(make-sum 'x 0)")
    x
    >>> scm("(make-sum 0 'x)")
    x
    >>> scm("(make-sum 'a 'x)")
    (+ a x)
    >>> scm("(make-sum 'a (make-sum 'x 1))")
    (+ a (+ x 1))
    >>> scm("(derive '(+ x 3) 'x)")
    1
    """
    pass

# Вопрос 4
def derive_product_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'hw_08)")
    <BLANKLINE>
    >>> scm("(make-product 2 3)")
    6
    >>> scm("(make-product 'x 0)")
    0
    >>> scm("(make-product 1 'x)")
    x
    >>> scm("(make-product 'a 'x)")
    (* a x)
    >>> scm("(derive '(* x y) 'x)")
    y
    >>> scm("(derive '(* (* x y) (+ x 3)) 'x)")
    (+ (* y (+ x 3)) (* x y))
    """
    pass

# Вопрос 5
def make_exp_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'hw_08)")
    <BLANKLINE>
    >>> scm("(make-exp 2 4)")
    16
    >>> scm("(make-exp 'x 1)")
    x
    >>> scm("(make-exp 'x 0)")
    1
    >>> scm("x^2")
    (^ x 2)
    >>> scm("(base x^2)")
    x
    >>> scm("(exponent x^2)")
    2
    >>> scm("(exp? x^2)") # True or False
    #t
    >>> scm("(exp? 1)")
    #f
    >>> scm("(exp? 'x)")
    #f
    """
    pass

# Вопрос 6
def derive_exp_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'hw_08)")
    <BLANKLINE>
    >>> scm("(derive x^2 'x)")
    (* 2 x)
    >>> scm("(derive x^3 'x)")
    (* 3 (^ x 2))
    >>> scm("(derive (make-sum x^3 x^2) 'x)")
    (+ (* 3 (^ x 2)) (* 2 x))
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