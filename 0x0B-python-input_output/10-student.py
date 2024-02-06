#!/usr/bin/python3
'''task 10 module'''


class Student:
    '''student class'''
    def __init__(self, first_name, last_name, age):
        '''Initialization of the student object'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''return a dictionary representation of a Student instance
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        '''
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict
