The ``5-text_indentation`` module
============================

Using ``text_indentation``
---------------------

Import module:
    >>> text_indentation = __import__('5-text_indentation').text_indentation

Test no delim:
    >>> text_indentation("Hello Holberton")
    Hello Holberton

Test string with spaces:
    >>> text_indentation("Holberton          ")
    Holberton

Test string with spaces 2:
    >>> text_indentation("        Holberton")
    Holberton
    
Test string with spaces 3:
    >>> text_indentation("        Holberton          ")
    Holberton
    
Test string with empty string:
    >>> text_indentation("")

Test string with empty string 2:
    >>> text_indentation("      ")

Test simple:
    >>> text_indentation("Hello: Holberton")
    Hello:
    <BLANKLINE>
    Holberton

Test delims with spaces:
    >>> text_indentation("      ?:  :  ")
    ?
    <BLANKLINE>
    :
    <BLANKLINE>
    :
    <BLANKLINE>

Test newline:
    >>> text_indentation("\n")
    <BLANKLINE>

Test newline 2:
    >>> text_indentation("\n\n")
    <BLANKLINE>
    <BLANKLINE>

Test newline 3:
    >>> text_indentation("Hello\n\n")
    Hello
    <BLANKLINE>

Test all delimeters:
    >>> text_indentation("Hello: Holberton? school. fooo")
    Hello:
    <BLANKLINE>
    Holberton?
    <BLANKLINE>
    school.
    <BLANKLINE>
    fooo

Test all delimeters with spaces:
    >>> text_indentation("Hello   :     Holberton    ?    school.    fooo")
    Hello:
    <BLANKLINE>
    Holberton?
    <BLANKLINE>
    school.
    <BLANKLINE>
    fooo

Test all delimeters with spaces at end:
    >>> text_indentation("Hello   :     Holberton    ?    school.    fooo     ")
    Hello:
    <BLANKLINE>
    Holberton?
    <BLANKLINE>
    school.
    <BLANKLINE>
    fooo

Test just delimeters:
    >>> text_indentation(".?:")
    .
    <BLANKLINE>
    ?
    <BLANKLINE>
    :
    <BLANKLINE>

Test just delimeters 2:
    >>> text_indentation("     ?   ")
    ?
    <BLANKLINE>

Test nonindent inside indent
    >>> text_indentation("?Hello.")
    ?
    <BLANKLINE>
    Hello.
    <BLANKLINE>

Test existing newlines:
    >>> text_indentation("?\n\n.\n\n:")
    ?
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    .
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    :
    <BLANKLINE>

Test none:
    >>> text_indentation(None)
    Traceback (most recent call last):
    ...
    TypeError: text must be a string

Test number:
    >>> text_indentation(33)
    Traceback (most recent call last):
    ...
    TypeError: text must be a string
