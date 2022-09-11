def my_email():
    """Возвращает строку с твоим e-mail адресом.

    >>> my_email() != 'someone@example.com'
    True
    """
    return 'valerkalifanov@gmail.com'

from operator import add, mul

def thirteen_thirty_seven():
    """Нужно придумать самое захватывающее выражение, которое приводит к результату 1337.
    Можно использовать только числа и функции add(. . .) и mul(. . .). Чем длиннее, тем лучше.

    >>> thirteen_thirty_seven()
    1337
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"
    return add(mul(mul(20,5),add(5,5)), add(mul(3,mul(5,add(4,17))), add(3,add(1,mul(3,add(1,5))))))
