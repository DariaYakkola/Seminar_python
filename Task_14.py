# Требуется вывести все целые степени двойки
# (т.е. числа вида 2^k), не превосходящие числа N
n = int(input('Введите число N: '))
degree = 1
while degree <= n:
    print(degree)
    degree *= 2
