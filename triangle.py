import unittest

def area(a, h):
    '''Принимает числа a и h, возвращает ah/2 - площадь треугольника
    При вызове функции print(area(25, 6,72)) выведет 84 - площадь треугольника со стороной основания a=25 и высотой, опущенной на эту сторону, h=6,72'''
    if (a>0) and (h>0):
        return a * h / 2
    else:
        return "error"

def perimeter(a, b, c):
    '''Принимает числа a, b и c, возвращает a + b + c - периметр треугольника
    При вызове функции print(perimeter(25, 24, 7)) выведет 56 - периметр треугольника со сторонами a=25, b=24 и c=7'''
    if (a>0) and (b>0) and (c>0):
        return a + b + c
    else:
        return "error"

