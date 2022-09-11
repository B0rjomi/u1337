# Вопрос 1
def reverse_test():
    """
    >>> scm = scm_fixture();\
        scm("(load 'hw_09)");\
        scm("(list-of x for x in '(1 2 3) if #t)")
    <BLANKLINE>
    (1 2 3)
    >>> scm("(list-of x for x in '(a 2 c) if (symbol? x))")
    (a c)
    >>> scm("(list-of (* x x) for x in '(3 4 5) if (odd? x))")
    (9 25)
    >>> scm("(list-of (* x x) for x in '(3 4 5) if (lambda (x) x))")
    (9 16 25)
    >>> scm("(list-of (* 2 x) for x in (list-of (* y y) for y in '(1 2 3 4 5) if (lambda (x) x)) if (odd? x))")
    (2 18 50)
    >>> scm("(list-of (* x x x) for x in '(9 10 11))")
    (729 1000 1331)
    >>> scm("(list-of 42 for x in '(q w e r t y))")
    (42 42 42 42 42 42)
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