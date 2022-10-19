class test:
    a = 10

    def __init__(self):
        self.b = 20

    def getname(self):
        print("getting name")

test1 = test()



print(test.a)
print(test1.a)
print(test1.b)

print(type(test))
print(type(test1))

class Person():
    pass

print(type(Person))
print(test1.getname())
print(test.getname(test))
print(test.getname(test1))
print(test1.getname())

class test2(test):
    pass

test3 = test2()