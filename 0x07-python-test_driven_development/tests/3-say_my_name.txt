The ``3-say_my_name`` module
============================

Using ``3-say_my_name``
---------------------

Import module:
    >>> say_my_name = __import__('3-say_my_name').say_my_name

Test basic:
	>>> say_my_name("hello", "there")
	My name is hello there

Test firstname:
	>>> say_my_name("hello")
	My name is hello 

Test lastname empty:
	>>> say_my_name("hello", "")
	My name is hello 

Test both names empty:
	>>> say_my_name("", "")
	My name is  

Test just spaces:
	>>> say_my_name("   ", "   ")
	My name is        

Test empty firstname:
	>>> say_my_name("", "hello")
	My name is  hello

Test not str arg1:
    >>> say_my_name(33, "hello")
    Traceback (most recent call last):
    ...
    TypeError: first_name must be a string

Test not str arg2:
    >>> say_my_name("hello", 98)
    Traceback (most recent call last):
    ...
    TypeError: last_name must be a string

Test not str arg1 arg2:
    >>> say_my_name(91, 98)
    Traceback (most recent call last):
    ...
    TypeError: first_name must be a string

Missing 2 args:
    >>> say_my_name()
    Traceback (most recent call last):
    ...
    TypeError: say_my_name() missing 1 required positional argument: 'first_name'
