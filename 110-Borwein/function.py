##
## EPITECH PROJECT, 2022
## 110-Borwein
## File description:
## function.py
##

from math import sin

def f(x: float, n: float) -> float:
    result = float()
    result1 = float()
    result2 = float()
    iterator = float()

    if x == 0:
        return 1

    while iterator <= n:
        result1 = sin( x / ( (2 * iterator) + 1 ) )
        result2 = x / ( (2 * iterator) + 1 )

        if iterator != 0:
            result *= (result1 / result2)
        else:
            result = (result1 / result2)

        iterator += 1

    return result
