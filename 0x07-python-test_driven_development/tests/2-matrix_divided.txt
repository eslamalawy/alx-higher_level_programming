The ``2-matrix_divided`` module
============================

Using ``matrix_divided``
---------------------

Import module:
    >>> matrix_divided = __import__('2-matrix_divided').matrix_divided

Test normal matrix:
    >>> matrix_divided([[2, 4, 8], [1, 2, 3]], 2)
    [[1.0, 2.0, 4.0], [0.5, 1.0, 1.5]]

Test one el:
    >>> matrix_divided([[2]], 2)
    [[1.0]]

Test unmodified matrix:
    >>> m = [[2, 4, 8], [1, 2, 3]]
    >>> matrix_divided(m, 2)
    [[1.0, 2.0, 4.0], [0.5, 1.0, 1.5]]
    >>> m[1][1]
    2

Test division by negative:
    >>> matrix_divided([[2, 4, 8], [1, 2, 3]], -3)
    [[-0.67, -1.33, -2.67], [-0.33, -0.67, -1.0]]

Test division by inf:
    >>> matrix_divided([[2, 4, 8], [1, 2, 3]], float('inf'))
    [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]

Test division by nan:
    >>> matrix_divided([[2, 4, 8], [1, 2, 3]], float('nan'))
    [[nan, nan, nan], [nan, nan, nan]]

Test division by zero:
    >>> matrix_divided([[2, 4, 8], [1, 2, 3]], 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero

Test 1st arg none:
    >>> matrix_divided(none, 1)
    Traceback (most recent call last):
    ...
    NameError: name 'none' is not defined

Test empty matrix:
    >>> matrix_divided([[]], 10)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Test matrix with non number
    >>> matrix_divided([[2, 4, 8], [1, "foo", 3]], 2)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Test matrix with different rows
    >>> matrix_divided([[2, 4, 8], [1, 3]], 2)
    Traceback (most recent call last):
    ...
    TypeError: Each row of the matrix must have the same size

Test empty matrix more:
    >>> matrix_divided([[], [], []], 10)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats


Test 1st arg str:
    >>> matrix_divided("foo", 1)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats


Test 1st arg empty list:
    >>> matrix_divided([], 1)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Test division by non num:
    >>> matrix_divided([[2]], "foo")
    Traceback (most recent call last):
    ...
    TypeError: div must be a number

Test missing 1 arg:
    >>> matrix_divided()
    Traceback (most recent call last):
    ...
    TypeError: matrix_divided() missing 2 required positional arguments: 'matrix' and 'div'

