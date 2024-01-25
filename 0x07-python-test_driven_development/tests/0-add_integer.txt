The ``0-add_integer`` module
============================

Using ``add_integer``
---------------------

Import function from module:

    >>> add_integer = __import__('0-add_integer').add_integer

Test one int argument:

    >>> add_integer(2)
    100

Test one int argument and check default second:

    >>> add_integer(0)
    98

Test one float:

    >>> add_integer(123.9)
    221

Test one negative float:

    >>> add_integer(-95.5)
    3

Test two integers:

    >>> add_integer(10, 5)
    15

Test two big integers:

    >>> add_integer(999999998, 999999999)
    1999999997

Test positive, negative integers:

    >>> add_integer(34263478, -89234582395)
    -89200318917

Test negative, positive integers:

    >>> add_integer(-13947692, 57234)
    -13890458

Test an integer and a float:

    >>> add_integer(123, 7.987)
    130

Test a float and an integer:

    >>> add_integer(234234.43545, 4352345)
    4586579

Test two floats:

    >>> add_integer(0.9, 0.9)
    0

Add infinity:

    >>> add_integer(float('inf'), float('-inf'))
    Traceback (most recent call last):
    ...
    OverflowError: cannot convert float infinity to integer

Add nan:

    >>> add_integer(0, float('nan'))
    Traceback (most recent call last):
    ...
    ValueError: cannot convert float NaN to integer

Test first arg invalid:

    >>> add_integer("foo", 0)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer

Test second arg invalid:

    >>> add_integer(123123, [])
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer

Test both args invalid:

    >>> add_integer(None, None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer

Test two strings:

    >>> add_integer("foo", "bar")
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer

Test float overflow:
    >>> add_integer(float('inf'), 0)
    Traceback (most recent call last):
    ...
    OverflowError: cannot convert float infinity to integer
    
