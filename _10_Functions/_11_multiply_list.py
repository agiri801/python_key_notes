import random


def multiply_l(l, n):
    new_l = []
    for iteam in l:
        k = iteam * n
        new_l.append(k)
    print('Multiplied list: ', new_l)


def multi_l(l):
    mul = 1
    for i in l:
        mul *= i
    return mul


l = [random.randint(1, 20) for i in range(5)]
n = int(input('Enter number to be multilpied: '))
print('list l:', l)
multiply_l(l, n)
print('Multiplied all the iteams in list l: ', multi_l(l))
