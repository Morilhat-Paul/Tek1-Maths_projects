##
## EPITECH PROJECT, 2022
## 110-Borwein
## File description:
## simspon_method.py
##

from function import f
from math import pi

def simspon(n: int):
    temp = float()
    a = float()
    b = 0.5
    result = float()

    while b <= 5000:
        temp = f(a, n) + f(b, n)
        temp += 4 * f((a + b) / 2, n)
        temp *= (b - a) / 6
        result += temp
        a += 0.5
        b += 0.5

    print("Simpson:")
    print("I%i = %.10f" % (n, round(result, 10)))
    print("diff = %.10f" % abs((pi / 2) - result))
