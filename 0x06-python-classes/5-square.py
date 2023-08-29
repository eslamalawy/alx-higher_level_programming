#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Length of a side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Property for the length of a side of this square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of this square.

        Returns:
            The size squared.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints this square."""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
