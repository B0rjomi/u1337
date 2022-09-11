### HW_02: Рекурсия

# Вопрос 1.

def g(n):
    """Возвращает значение G(n), вычисленное рекурсивно.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n > 3:
        return g(n-1) + 2*g(n-2) + 3*g(n-3)
    else:
        return n

def g_iter(n):
    """Возвращает значение G(n), вычисленное итеративно.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    if n <= 3:
        return n

    var1, var2, var3 = 1, 2, 3
    while n > 3:
        var1, var2, var3 = var2, var3, var3 + 2 * var2 + 3 * var1
        n -= 1
    return var3



# Вопрос 2.

def has_seven(k):
    """Проверка наличия цифры 7 в k
    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k < 10:
        if k == 7:
            return True
        else:
            return False
    else:
        return has_seven(k // 10) or has_seven(k % 10)

# Вопрос 3.

"1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6"

def pingpong(n):
    """Возвращает n-ый элемент последовательности «пинг-понг».

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

# Вопрос 4.

def ten_pairs(n):
    """Возвращает число пар цифр в положительном целом n, в сумме образующих 10.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    


# Вопрос 5.

def count_change(amount):
    """Возвращает количество способов размена amount киберденьгами.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    

# Вопрос 6.

from operator import sub, mul

def make_anonymous_factorial():
    """Возвращает выражение, вычисляющее факториал.

    >>> make_anonymous_factorial()(5)
    120
    """
    return ТВОЕ_ВЫРАЖЕНИЕ_ЗДЕСЬ