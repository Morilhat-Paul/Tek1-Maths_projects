##
## EPITECH PROJECT, 2022
## 110-Borwein
## File description:
## midpoint.py
##

from function import f
from math import pi

def midpoint(n: int):
    result1 = float()
    result = float()
    a = float()
    b = 0.5

    while b <= 5000:
        result1 = f((a + b) / 2, n)
        result1 *= b - a
        result += result1
        a += 0.5
        b += 0.5

    print("Midpoint:")
    print("I%i = %.10f" % (n, round(result, 10)))
    print("diff = %.10f" % abs((pi / 2) - result))
