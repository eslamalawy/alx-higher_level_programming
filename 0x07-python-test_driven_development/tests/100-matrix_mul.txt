The ``100-matrix_mul`` module
============================

Using ``matrix_mul``
---------------------

Import module:
    >>> matrix_mul = __import__('100-matrix_mul').matrix_mul

Test 2 bad matrices:
    >>> matrix_mul([[1, 2, 3], [3, 4, 5]], [[1, 2], [3, 4]])
    Traceback (most recent call last):
    ...
    ValueError: m_a and m_b can't be multiplied

Test 2 ok matrices:
    >>> matrix_mul([[1, 2], [3, 4], [3, 4]], [[5, 6, 1], [7, 8, 2]])
    [[19, 22, 5], [43, 50, 11], [43, 50, 11]]

Test singly empty matrix:
    >>> matrix_mul([], [[3]])
    Traceback (most recent call last):
    ...
    ValueError: m_a can't be empty

Test singly empty matrix:
    >>> matrix_mul([[]], [[3]])
    Traceback (most recent call last):
    ...
    ValueError: m_a can't be empty

Test singly empty matrix 2:
    >>> matrix_mul([[4]], [])
    Traceback (most recent call last):
    ...
    ValueError: m_b can't be empty

Test doubly empty matrix:
    >>> matrix_mul([[3]], [[]])
    Traceback (most recent call last):
    ...
    ValueError: m_b can't be empty

Test simple case:
    >>> matrix_mul([[3]], [[9]])
    [[27]]

Test string arg:
    >>> matrix_mul("foo", [[9]])
    Traceback (most recent call last):
    ...
    TypeError: m_a must be a list

Test string arg:
    >>> matrix_mul([[8]], "bar")
    Traceback (most recent call last):
    ...
    TypeError: m_b must be a list

Test int list:
    >>> matrix_mul([1, 3, 4], [[9]])
    Traceback (most recent call last):
    ...
    TypeError: m_a must be a list of lists

Test int list 2:
    >>> matrix_mul([[8]], [2, 4, 6])
    Traceback (most recent call last):
    ...
    TypeError: m_b must be a list of lists

Test notnum list:
    >>> matrix_mul([["foo"]], [[2, 4, 6]])
    Traceback (most recent call last):
    ...
    TypeError: m_a should contain only integers or floats

Test notnum list 2 :
    >>> matrix_mul([[2, 4, 6]], [["foo"]])
    Traceback (most recent call last):
    ...
    TypeError: m_b should contain only integers or floats

Test a bad rows:
    >>> matrix_mul([[1, 2], [3, 4, 5], [3, 4]], [[5, 6, 1], [7, 8, 2]])
    Traceback (most recent call last):
    ...
    TypeError: each row of m_a must should be of the same size

Test b bad rows:
    >>> matrix_mul([[1, 2], [3, 4], [3, 4]], [[5, 6, 1], [7, 2]])
    Traceback (most recent call last):
    ...
    TypeError: each row of m_b must should be of the same size

Test missing 1 arg:
    >>> matrix_mul([[3]])
    Traceback (most recent call last):
    ...
    TypeError: matrix_mul() missing 1 required positional argument: 'm_b'

Test missing 2 args:
    >>> matrix_mul()
    Traceback (most recent call last):
    ...
    TypeError: matrix_mul() missing 2 required positional arguments: 'm_a' and 'm_b'
