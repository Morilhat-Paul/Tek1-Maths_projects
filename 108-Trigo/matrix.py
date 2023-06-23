##
## EPITECH PROJECT, 2022
## 108-Trigo
## File description:
## matrix
##

from math import factorial

def get_identical_matrix(matrix):
    lenght = len(matrix[0])
    matrix_I = [[] for i in range(lenght)]
    row = 0
    line = 0
    i = 0

    while i < lenght**2:
        if row >= lenght:
            row = 0
            line += 1
        if row == line:
            matrix_I[line].append(1)
        else:
            matrix_I[line].append(0)
        i += 1
        row += 1

    return matrix_I


def matrix_addition(matrix_A, matrix_B):
    i = 0
    result = [[] for i in range(len(matrix_A[0]))]

    for line in matrix_A:
        for coef in range(len(line)):
            calcul = line[coef] + matrix_B[i][coef]
            result[i].append(calcul)
        i += 1

    return result


def matrix_soustraction(matrix_A, matrix_B):
    i = 0
    result = [[] for i in range(len(matrix_A[0]))]

    for line in matrix_A:
        for coef in range(len(line)):
            calcul = line[coef] - matrix_B[i][coef]
            result[i].append(calcul)
        i += 1

    return result


def matrix_multiplication(matrix_A, matrix_B):
    i = 0
    calcul = 0
    result = [[] for i in range(len(matrix_A[0]))]

    for line in matrix_A:
        for coef in range(len(line)):
            calcul = 0
            for value in range(len(line)):
                calcul += line[value] * matrix_B[value][coef]
            result[i].append(calcul)
        i += 1

    return result


def matrix_square(matrix, exponent):
    result = matrix
    i = 1

    while i < exponent:
        result = matrix_multiplication(result, matrix)
        i += 1

    return result


def matrix_scalaire(matrix, scalaire):
    for line in matrix:
        for i in range(len(line)):
            line[i] *= scalaire

    return matrix


def exp(matrix, matrix_I):
    k = 2
    result = matrix_addition(matrix_I, matrix)

    while 1:
        calcul = matrix_addition(result, matrix_scalaire(matrix_square(matrix, k), (1 / factorial(k))))
        if calcul == result:
            break
        result = calcul
        k += 1

    return result


def cos(matrix, matrix_I):
    k = 1
    result = matrix_I

    while 1:
        calcul = matrix_addition(result, matrix_scalaire(matrix_square(matrix, 2*k), ((-1)**k) / factorial(2*k)))
        if calcul == result:
            break
        result = calcul
        k += 1

    return result


def sin(matrix, matrix_I):
    k = 1
    result = matrix

    while 1:
        calcul = matrix_addition(result, matrix_scalaire(matrix_square(matrix, (2*k)+1), ((-1)**k) / factorial((2*k)+1)))
        if calcul == result:
            break
        result = calcul
        k += 1

    return result


def cosh(matrix, matrix_I):
    k = 1
    result = matrix_I

    while 1:
        calcul = matrix_addition(result, matrix_scalaire(matrix_square(matrix, 2*k), (1 / factorial(2*k))))
        if calcul == result:
            break
        result = calcul
        k += 1

    return result


def sinh(matrix, matrix_I):
    k = 1
    result = matrix

    while 1:
        calcul = matrix_addition(result, matrix_scalaire(matrix_square(matrix, (2*k)+1), (1 / factorial((2*k)+1))))
        if calcul == result:
            break
        result = calcul
        k += 1

    return result


def print_matrix(matrix):
    for line in matrix:
        print(*["%.2f" % i for i in line], sep='\t')
