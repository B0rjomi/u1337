### Лабораторная работа № 7: Связные списки, изменяемые деревья"""

##########################################
# Определение связных списков и деревьев #
##########################################

class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ', '
            self = self.rest
        return string + str(self.first) + '>'

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value

class Tree:
    """Дерево — это метка и список ветвей."""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches

###########
# Вопросы #
###########

# Вопрос 1.
def _q_01():
    """
    Часть 1
    >>> link = Link(1000)                                       # doctest: +SKIP
    >>> link.first                                              # doctest: +SKIP
    1000
    >>> link.rest is Link.empty                                 # doctest: +SKIP
    True
    >>> link = Link(1000, 2000)                                 # doctest: +SKIP
    Traceback (most recent call last):
      File "/usr/lib/python3.8/doctest.py", line 1329, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__._q_01[3]>", line 1, in <module>
        link = Link(1000, 2000)                                 # doctest: +SKIP
      File "lab_07.py", line 11, in __init__
        assert rest is Link.empty or isinstance(rest, Link)
    AssertionError
    >>> link = Link(1000, Link())                               # doctest: +SKIP
    Traceback (most recent call last):
      File "/usr/lib/python3.8/doctest.py", line 1329, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__._q_01[4]>", line 1, in <module>
        link = Link(1000, Link())                               # doctest: +SKIP
    TypeError: __init__() missing 1 required positional argument: 'first'

    Часть 2
    >>> link = Link(1, Link(2, Link(3)))                        # doctest: +SKIP
    >>> link.first                                              # doctest: +SKIP
    1
    >>> link.rest.first                                         # doctest: +SKIP
    2
    >>> link.rest.rest.rest is Link.empty                       # doctest: +SKIP
    True
    >>> link.first = 9001                                       # doctest: +SKIP
    >>> link.first                                              # doctest: +SKIP
    9001
    >>> link.rest = link.rest.rest                              # doctest: +SKIP
    >>> link.rest.first                                         # doctest: +SKIP
    3
    >>> link = Link(1)                                          # doctest: +SKIP
    >>> link.rest = link                                        # doctest: +SKIP
    >>> link.rest.rest.rest.rest.first                          # doctest: +SKIP
    1
    >>> link = Link(2, Link(3, Link(4)))                        # doctest: +SKIP
    >>> link2 = Link(1, link)                                   # doctest: +SKIP
    >>> link2.first                                             # doctest: +SKIP
    1
    >>> link2.rest.first                                        # doctest: +SKIP
    2

    Часть 3
    >>> link = Link(5, Link(6, Link(7)))                        # doctest: +SKIP
    >>> link.second                                             # doctest: +SKIP
    6
    >>> link.rest.second                                        # doctest: +SKIP
    7
    >>> link.second = 10                                        # doctest: +SKIP
    >>> link        # Посмотри на метод __repr__ класса Link    # doctest: +SKIP
    Link(5, Link(10, Link(7)))
    >>> link.second = Link(8, Link(9))                          # doctest: +SKIP
    >>> link.second.first                                       # doctest: +SKIP
    8
    >>> print(link)  # Посмотри на метод __str__ класса Link    # doctest: +SKIP
    <5, <8, 9>, 7>
    """
    return 0

# Вопрос 2.
def _q_02():
    """
    >>> t = Tree(1, Tree(2))                                    # doctest: +SKIP
    Traceback (most recent call last):
      File "/usr/lib/python3.8/doctest.py", line 1329, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__._q_02[0]>", line 1, in <module>
        t = Tree(1, Tree(2))                                    # doctest: +SKIP
      File "lab_07.py", line 41, in __init__
        for branch in branches:
    TypeError: 'Tree' object is not iterable
    >>> t = Tree(1, [Tree(2)])                                  # doctest: +SKIP
    >>> t.label                                                 # doctest: +SKIP
    1
    >>> t.branches[0]                                           # doctest: +SKIP
    Tree(2)
    >>> t.branches[0].label                                     # doctest: +SKIP
    2
    >>> t.label = t.branches[0].label                           # doctest: +SKIP
    >>> t                                                       # doctest: +SKIP
    Tree(2, [Tree(2)])
    >>> t.branches.append(Tree(4, [Tree(8)]))                   # doctest: +SKIP
    >>> len(t.branches)                                         # doctest: +SKIP
    2
    >>> t.branches[0]                                           # doctest: +SKIP
    Tree(2)
    >>> t.branches[1]                                           # doctest: +SKIP
    Tree(4, [Tree(8)])
    """
    return 0

# Вопрос 3.
def link_to_list_iter(link):
    """Принимает связный список и возвращает Python-список с теми же элементами.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list_iter(link)
    [1, 2, 3, 4]
    >>> link_to_list_iter(Link.empty)
    []
    """
    res = []
    if link is Link.empty:
        return []
    while link != Link.empty:
        res.append(link.first)
        link = link.rest
    return res

def link_to_list_rec(link):
    """Принимает связный список и возвращает Python-список с теми же элементами.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list_rec(link)
    [1, 2, 3, 4]
    >>> link_to_list_rec(Link.empty)
    []
    """
    if link is Link.empty:
        return []
    else:
        return [link.first] + link_to_list_rec(link.rest)

# Вопрос 4.
def store_digits(n):
    """Возвращает связный список цифр числа n.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    """
    link = Link.empty
    while n > 0:
        sub_n = n % 10
        link = Link(sub_n, link)
        n = n // 10
    return link

# Вопрос 5.
def cumulative_sum(t):
    """Изменяет t так, что значение в каждом узле
    становится суммой всех узловых значений в соответствующем
    поддереве c корнем в t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

# Вопрос 6.
def is_bst(t):
    """Возвращает True, если дерево t имеет структуру бинарного дерева поиска.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

# Вопрос 7.
def in_order_traversal(t):
    """
    Функция-генератор, которая совершает центрированный обход дерева,
    последовательно выдавая результаты. Считай, что каждый узел
    может содержать от 0 до 2 веток.

    Например, для такого дерева t:
            1
        2       3
    4     5
         6  7

    Последовательность центрированного обхода будет 4, 2, 6, 5, 7, 1, 3

    >>> t = Tree(1, [Tree(2, [Tree(4), Tree(5, [Tree(6), Tree(7)])]), Tree(3)])
    >>> list(in_order_traversal(t))
    [4, 2, 6, 5, 7, 1, 3]
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

# Вопрос 8.
def remove_all(link , value):
    """Удаляет все элементы связного списка link, содержащие значение value.
    Считай, что есть элементы для удаления и первый элемент никогда не удаляется.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0, 2, 2, 3, 1, 2, 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0, 3, 1, 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0, 1>
    """
    if link != Link.empty and link.rest != Link.empty:
        remove_all(link.rest, value)
        if link.rest.first == value:
            link.rest = link.rest.rest

# Вопрос 9.
def deep_map_mut(fn, link):
    """Изменяет все элементы связного списка link, применяя к их значениям
    функцию fn. Не создаёт новые объекты Link (то есть не использует конструктор Link)

    Не возвращает изменённый объект.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9, <16>, 25, 36>
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

# Вопрос 10.
def has_cycle(link):
    """Проверяет наличие цикла в связном списке.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

def has_cycle_constant(link):
    """Проверяет наличие цикла в связном списке.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

# Вопрос 11.
def reverse_other(t):
    """Изменяет дерево t так, что в узлах на нечётной
    глубине последовательность узловых значений разворачивается.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

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