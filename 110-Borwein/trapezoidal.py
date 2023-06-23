##
## EPITECH PROJECT, 2022
## 110-Borwein
## File description:
## trapezoidal_method.py
##

from function import f
from math import pi

def trapezoidal(n: int):
    temp = float()
    a = float()
    b = 0.5
    result = float()

    while b <= 5000:
        temp = f(a, n) + f(b, n)
        temp *= (b - a) / 2
        result += temp
        a += 0.5
        b += 0.5

    print("Trapezoidal:")
    print("I%i = %.10f" % (n, round(result, 10)))
    print("diff = %.10f" % abs((pi / 2) - result))
