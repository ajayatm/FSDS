from functools import reduce
l1 = ['123', '1231', '122342', '34534', '23424']
l2 = [1, 2, 3, 4, 5, 6]
l3 = [2]


def add5(incoming):
    return incoming+5


def even(numlist):
    if numlist % 2 == 0:
        return None


def typeint(incoming):
    return int(incoming)


def sumtwo(a, b, c):
    return a+b+c


print(list(map(add5, l2)))
print(list(map(typeint, l1)))
print(list(filter(even, l2)))
print(reduce(sumtwo, l3))
fun = reduce(lambda x, y: x + y, l2)
print(fun)
print(list(zip(l1, l2, l3)))
