import sys
from math import factorial
from pprint import pprint
from types import ModuleType
from typing import Dict, List, Any
from inspect import getmodule


# pprint(__builtins__)
# pprint(dir(__builtins__))

# def func(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)
#
#
# sys.setrecursionlimit(3000)
# sys.set_int_max_str_digits(10000)
# print(func(2000))

# class Introspection:
#
#     def __init__(self, attribute):
#         self.attribute = attribute

def introspection_info(obj):
    res: dict[str, list[str] | ModuleType | None | Any] = {'type': type(obj)}
    for attr in dir(obj):
        if not callable(attr):
            res['attributes'] = dir(getattr(obj, attr))
    for meth in dir(obj):
        if callable(meth):
            res['method'] = dir(getattr(obj, meth))
    res['module'] = getmodule(obj)

    return res


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school

    def info(self):
        print(f'Мое имя {self.name} я обучаюсь в университете {self.school}')


number_info1 = introspection_info(42)
print(number_info1)
number_info2 = introspection_info(Student('Вячеслав', 'Urban'))
print(number_info2)
