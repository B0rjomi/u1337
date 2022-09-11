def _q_01():
    """
    ============================================================================
    Часть 1
    ----------------------------------------------------------------------------
    >>> scm = scm_fixture()                                     # doctest: +SKIP
    >>> scm("(cons 1 (cons 2 nil))")                            # doctest: +SKIP
    (1 2)
    >>> scm("(car (cons 1 (cons 2 nil)))")                      # doctest: +SKIP
    1
    >>> scm("(cdr (cons 1 (cons 2 nil)))")                      # doctest: +SKIP
    (2)
    >>> scm("(list 1 2 3)")                                     # doctest: +SKIP
    (1 2 3)
    >>> scm("'(1 2 3)")                                         # doctest: +SKIP
    (1 2 3)
    >>> scm("'(2 . 3)")                                         # doctest: +SKIP
    (2 . 3)
    >>> scm("'(2 . (3))")                                       # doctest: +SKIP
    (2 3)
    >>> scm("(cons 1 '(list 2 3))")                             # doctest: +SKIP
    (1 list 2 3)

    ============================================================================
    Часть 2
    ----------------------------------------------------------------------------
    >>> scm("(cons (list 2 (cons 3 4)) nil)")                   # doctest: +SKIP
    ((2 (3 . 4)))
    >>> scm("(car (cdr '(127 . ((131 . (137))))))")             # doctest: +SKIP
    (131 137)
    >>> scm("'(cons 4 (cons (cons 6 8) ()))")                   # doctest: +SKIP
    (cons 4 (cons (cons 6 8) ()))

    ============================================================================
    Часть 3
    ----------------------------------------------------------------------------
    >>> scm("(define a '(1))")                                  # doctest: +SKIP
    a
    >>> scm("a")                                                # doctest: +SKIP
    (1)
    >>> scm("(define b (cons 2 a))")                            # doctest: +SKIP
    b
    >>> scm("b")                                                # doctest: +SKIP
    (2 1)
    >>> scm("(define c (list 3 b))")                            # doctest: +SKIP
    c
    >>> scm("c")                                                # doctest: +SKIP
    (3 (2 1))
    >>> scm("(car c)")                                          # doctest: +SKIP
    3
    >>> scm("(cdr c)")                                          # doctest: +SKIP
    ((2 1))
    >>> scm("(car (car (cdr c)))")                              # doctest: +SKIP
    2
    >>> scm("(cdr (car (cdr c)))")                              # doctest: +SKIP
    (1)
    """
    return 0

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

if __name__ == '__main__':
    import doctest, sys
    finder = doctest.DocTestFinder()
    runner = doctest.DocTestRunner(doctest.OutputChecker(), optionflags=doctest.FAIL_FAST)
    doctest.OutputChecker.output_difference = lambda a, b, c, d: ""
    m = sys.modules.get('__main__')
    for test in finder.find(m, m.__name__):
        if test.name == '__main__': continue
        if test.name.split('.')[1][:2] != '_q': continue
        for example in test.examples: example.options[doctest.SKIP] = False
        if  runner.run(test).failed != 0: break