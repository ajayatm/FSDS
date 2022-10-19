class Main:
    def __init__(self, a, b, c):
        self._a = a
        self.__b = 9
        self.c = c
        print(self.__b)


x = Main(1, 2, 3)
x.__b = 10
print(x.__b)
