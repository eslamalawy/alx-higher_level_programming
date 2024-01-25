The ``4-print_square`` module
============================

Using ``print_square``
---------------------

Import module:
    >>> print_square = __import__('4-print_square').print_square

Test normal print 0:
    >>> print_square(0)

Test normal print 1:
    >>> print_square(1)
    #

Test normal print 2:
    >>> print_square(2)
    ##
    ##

Test normal print 3:
    >>> print_square(3)
    ###
    ###
    ###

Test normal print 10:
    >>> print_square(10)
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########

Test negative:
    >>> print_square(-10)
    Traceback (most recent call last):
    ...
    ValueError: size must be >= 0

Test float:
    >>> print_square(10.0)
    Traceback (most recent call last):
    ...
    TypeError: size must be an integer

Test str:
    >>> print_square("foo")
    Traceback (most recent call last):
    ...
    TypeError: size must be an integer

Test none:
    >>> print_square(None)
    Traceback (most recent call last):
    ...
    TypeError: size must be an integer

Test inf:
    >>> print_square(float('inf'))
    Traceback (most recent call last):
    ...
    TypeError: size must be an integer

Test nan:
    >>> print_square(float('nan'))
    Traceback (most recent call last):
    ...
    TypeError: size must be an integer

Missing one argument:
    >>> print_square()
    Traceback (most recent call last):
    ...
    TypeError: print_square() missing 1 required positional argument: 'size'
