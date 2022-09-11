
# Вопрос 2
def over_or_under_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'lab_09)")
    <BLANKLINE>
    >>> scm("(over-or-under 5 5)")
    0
    >>> scm("(over-or-under 5 4)")
    1
    >>> scm("(over-or-under 3 5)")
    -1
    """
    pass

# Вопрос 3
def filter_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'lab_09)")
    <BLANKLINE>
    >>> scm("(filter even? '(1 2 3 4))")
    (2 4)
    >>> scm("(filter odd? '(1 3 5))")
    (1 3 5)
    >>> scm("(filter odd? '(2 4 6 1))")
    (1)
    >>> scm("(filter even? '(3))")
    ()
    >>> scm("(filter odd? nil)")
    ()
    """
    pass

# Вопрос 4
def make_adder_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'lab_09)")
    <BLANKLINE>
    >>> scm("(define add-two (make-adder 2))")
    add-two
    >>> scm("(define add-three (make-adder 3))")
    add-three
    >>> scm("(add-two 2)")
    4
    >>> scm("(add-two 3)")
    5
    >>> scm("(add-three 3)")
    6
    >>> scm("(add-three 9)")
    12
    """
    pass

# Вопрос 5
def lst_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'lab_09)")
    <BLANKLINE>
    >>> scm("lst")
    ((1) 2 (3 . 4) 5)
    """
    pass

# Вопрос 6
def composed_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'lab_09)")
    <BLANKLINE>
    >>> scm("(define (add-one a) (+ a 1))")
    add-one
    >>> scm("(define (multiply-by-two a) (* a 2))")
    multiply-by-two
    >>> scm("((composed add-one add-one) 2)")
    4
    >>> scm("((composed multiply-by-two multiply-by-two) 2)")
    8
    >>> scm("((composed add-one multiply-by-two) 2)")
    5
    >>> scm("((composed multiply-by-two add-one) 2)")
    6
    >>> scm("((composed (composed add-one add-one) add-one) 2)")
    5
    >>> scm("((composed (composed add-one add-one) multiply-by-two) 2)")
    6
    >>> scm("((composed multiply-by-two (composed add-one add-one)) 2)")
    8
    """
    pass

# Вопрос 7
def remove_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'lab_09)")
    <BLANKLINE>
    >>> scm("(remove 3 nil)")
    ()
    >>> scm("(remove 2 '(1 3 2))")
    (1 3)
    >>> scm("(remove 1 '(1 3 2))")
    (3 2)
    >>> scm("(remove 42 '(1 3 2))")
    (1 3 2)
    >>> scm("(remove 3 '(1 3 3 7))")
    (1 7)
    """
    pass

# Вопрос 8
def no_repeats_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'lab_09)")
    <BLANKLINE>
    >>> scm("(no-repeats (list 5 4 2))")
    (5 4 2)
    >>> scm("(no-repeats (list 5 4 5 4 2 2))")
    (5 4 2)
    >>> scm("(no-repeats (list 5 5 5 5 5))")
    (5)
    >>> scm("(no-repeats ())")
    ()
    >>> scm("(no-repeats '(5 4 3 2 1))")
    (5 4 3 2 1)
    >>> scm("(no-repeats '(5 4 3 2 1 1))")
    (5 4 3 2 1)
    >>> scm("(no-repeats '(5 5 4 3 2 1))")
    (5 4 3 2 1)
    >>> scm("(no-repeats '(12))")
    (12)
    >>> scm("(no-repeats '(1 1 1 1 1 1))")
    (1)
    """
    pass

# Вопрос 9
def substitute_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'lab_09)")
    <BLANKLINE>
    >>> scm("(substitute '(c a t) 'c 'b)")
    (b a t)
    >>> scm("(substitute '(s u p e r) 's 'p)")
    (p u p e r)
    >>> scm("(substitute '(g (o) o (o)) 'o 'r)")
    (g (r) r (r))
    >>> scm("(substitute '((lead guitar) (bass guitar) (rhythm guitar) drums) 'guitar 'axe)")
    ((lead axe) (bass axe) (rhythm axe) drums)
    >>> scm("(substitute '(romeo romeo wherefore art thou romeo) 'romeo 'paris)")
    (paris paris wherefore art thou paris)
    >>> scm("(substitute '((to be) or not (to (be))) 'be 'eat)")
    ((to eat) or not (to (eat)))
    >>> scm("(substitute '(a b (c) d e) 'foo 'bar)")
    (a b (c) d e)
    """
    pass

# Вопрос 10
def sub_all_test():
    """
    >>> scm = scm_fixture()
    >>> scm("(load 'lab_09)")
    <BLANKLINE>
    >>> scm("(sub-all '(try ((not))) '(not try) '(do_not do_or))")
    (do_or ((do_not)))
    >>> scm("(sub-all '((4 calling birds) (3 french hens) (2 turtle doves)) '(1 2 3 4) '(one two three four))")
    ((four calling birds) (three french hens) (two turtle doves))
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