def _q_01():
    """
    ============================================================================
    Часть 1
    ----------------------------------------------------------------------------
    >>> scm = scm_fixture()                                     # doctest: +SKIP
    >>> scm("+")
    #[+]

    >>> scm("list")                                             # doctest: +SKIP
    #[list]

    >>> scm("(define-macro (f x) (car x))")                     # doctest: +SKIP
    f

    >>> scm("(f (2 3 4))")                                      # doctest: +SKIP
    2

    >>> scm("(f (+ 2 3))")                                      # doctest: +SKIP
    #[+]

    >>> scm("(define x 2000)")                                  # doctest: +SKIP
    x

    >>> scm("(f (x y z))")                                      # doctest: +SKIP
    2000

    >>> scm("(f (list 2 3 4))")                                 # doctest: +SKIP
    #[list]

    >>> scm("(f (quote (2 3 4)))")                              # doctest: +SKIP
    Traceback (most recent call last):
      File "C:\Python\lib\doctest.py", line 1329, in __run
        compileflags, 1), test.globs)
      File "<doctest __main__._q_01[9]>", line 1, in <module>
        scm("(f (quote (2 3 4)))")                              # doctest: +SKIP
      File "psp.py", line 135, in eval_line
        result = scheme.scheme_eval(exp, _frame)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 1465, in s03G8
        Rk4_L_C_g = O6_7Jf__(v10a_nB, c030L_B)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 987, in p1sY
        Rk4_L_C_g = p1sY(v10a_nB, c030L_B)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 1465, in s03G8
        Rk4_L_C_g = O6_7Jf__(v10a_nB, c030L_B)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 969, in p1sY
        Rk4_L_C_g = c030L_B.uA_92(v10a_nB)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 1047, in uA_92
        raise M7TS11(((('u' + 'nk') + ('n' + 'o')) + (('wn' + ' i') + ('dentifier: {' + '0}'))).format(i0_5i_))
    interpreter.M7TS11: unknown identifier: quote

    >>> scm("(define quote 7000)")                              # doctest: +SKIP
    quote

    >>> scm("(f (quote (2 3 4)))")                              # doctest: +SKIP
    7000

    ============================================================================
    Часть 2
    ----------------------------------------------------------------------------
    >>> scm = scm_fixture()                                     # doctest: +SKIP
    >>> scm("(define-macro (g x) (+ x 2))")                     # doctest: +SKIP
    g

    >>> scm("(g 2)")                                            # doctest: +SKIP
    4

    >>> scm("(g (+ 2 3))")                                      # doctest: +SKIP
    Traceback (most recent call last):
      File "C:\Python\lib\doctest.py", line 1329, in __run
        compileflags, 1), test.globs)
      File "<doctest __main__._q_01[15]>", line 1, in <module>
        scm("(g (+ 2 3))")                                      # doctest: +SKIP
      File "psp.py", line 152, in eval_line
        result = scheme.scheme_eval(exp, _frame)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 1465, in s03G8
        Rk4_L_C_g = O6_7Jf__(v10a_nB, c030L_B)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 986, in p1sY
        v10a_nB = c_139x5q.f6m6K(R4_uy, c030L_B)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 1134, in f6m6K
        return V3pO(I7_F05, X5_5N_8p, c030L_B)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 1451, in V3pO
        return p1sY(jMs_9.v10a_nB, jMs_9.c030L_B)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 1465, in s03G8
        Rk4_L_C_g = O6_7Jf__(v10a_nB, c030L_B)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 990, in p1sY
        Rk4_L_C_g = e3mfC1l(c_139x5q, iM977M_94, c030L_B)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 1002, in e3mfC1l
        return c_139x5q.i67X3_(iM977M_94, c030L_B)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 1105, in i67X3_
        return I7_F05.b01450ef(*I8__5rnR)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 534, in kO3I5i0mt
        return Yi3Zt_(operator.add, int(((0.49751274827083747 + 0.1712882331483475) * 0)), b_8_6S268)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 524, in Yi3Zt_
        D1JC1G4Y(*b_8_6S268)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 520, in D1JC1G4Y
        raise M7TS11(K_Fo3.format(Wn_Sl1h, d7Y904))
    interpreter.M7TS11: operand 0 ((+ 2 3)) is not a number

    >>> scm("(define-macro (h x) (list '+ x 2))")               # doctest: +SKIP
    h

    >>> scm("(h (+ 2 3))")                                      # doctest: +SKIP
    7

    ============================================================================
    Часть 3
    ----------------------------------------------------------------------------
    >>> scm = scm_fixture()                                     # doctest: +SKIP
    >>> scm("(define-macro (if-else-5 condition consequent) `(if ,condition ,consequent 5))") # doctest: +SKIP
    if-else-5

    >>> scm("(if-else-5 #t 2)")                                 # doctest: +SKIP
    2

    >>> scm("(if-else-5 #f 3)")                                 # doctest: +SKIP
    5

    >>> scm("(if-else-5 #t (/ 1 0))")                           # doctest: +SKIP
    Traceback (most recent call last):
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 553, in de4r79
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 1465, in s03G8
        Rk4_L_C_g = O6_7Jf__(v10a_nB, c030L_B)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 990, in p1sY
        Rk4_L_C_g = e3mfC1l(c_139x5q, iM977M_94, c030L_B)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 1002, in e3mfC1l
        return c_139x5q.i67X3_(iM977M_94, c030L_B)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 1105, in i67X3_
        return I7_F05.b01450ef(*I8__5rnR)
      File "C:\u1337\lab_11-B0rjomi\scheme\interpreter.py", line 555, in de4r79
        raise M7TS11(wN791w)
    interpreter.M7TS11: division by zero

    >>> scm("(if-else-5 #f (/ 1 0))")                           # doctest: +SKIP
    5

    >>> scm("(if-else-5 (= 1 1) 2)")                            # doctest: +SKIP
    2
    """
    return 0

def _q_02():
    """
    >>> scm = scm_fixture()                                     # doctest: +SKIP
    >>> scm("'(1 x 3)")                                         # doctest: +SKIP
    (1 x 3)

    >>> scm("(define x 2)")                                     # doctest: +SKIP
    x

    >>> scm("`(1 x 3)")                                         # doctest: +SKIP
    (1 x 3)

    >>> scm("`(1 ,x 3)")                                        # doctest: +SKIP
    (1 2 3)

    >>> scm("'(1 ,x 3)")                                        # doctest: +SKIP
    (1 (unquote x) 3)

    >>> scm("`(,1 x 3)")                                        # doctest: +SKIP
    (1 x 3)

    >>> scm("`,(+ 1 x 3)")                                      # doctest: +SKIP
    6

    >>> scm("`(1 (,x) 3)")                                      # doctest: +SKIP
    (1 (2) 3)

    >>> scm("`(1 ,(+ x 2) 3)")                                  # doctest: +SKIP
    (1 4 3)

    >>> scm("(define y 3)")                                     # doctest: +SKIP
    y

    >>> scm("`(x ,(* y x) y)")                                  # doctest: +SKIP
    (x 6 y)

    >>> scm("`(1 ,(cons x (list y 4)) 5)")                      # doctest: +SKIP
    (1 (2 3 4) 5)
    """



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