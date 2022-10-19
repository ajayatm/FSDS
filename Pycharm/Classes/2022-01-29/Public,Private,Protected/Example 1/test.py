from SubClass import Child
from MainClass import Main


x = Main(4, 5, 6)
x._a = 1
x._Main__b = 2
x.c = 7
print(x._a, x._Main__b, x.c)

y = Child(11, 12, 13)

y._a = 14
y._Main__b = 15
y.c = 18
print(y._a, y._Main__b, y.c)
