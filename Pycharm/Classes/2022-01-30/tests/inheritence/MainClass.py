class Parent:
    def __init__(self, a):
        self.a = a

    def printa(self):
        print('Parent - ' + self.a)


class Child(Parent):
    pass

    def printa(self):
        print('Child - ' + self.a)


class GrandChild(Child):
    pass

    def printa(self):
        print('GrandChild - ' + self.a)


c = GrandChild("Ruby")
c.printa()

l = Parent('Ajay')
m = Child('Michelle')
n = GrandChild('Ruby')
l.printa()
m.printa()
n.printa()


class Father:
    def __init__(self, x):
        self.a = x

    def fathername(self):
        print(self.a)


class Mother:
    def __init__(self, x):
        self.b = x

    def mothername(self):
        print(self.b)


class Son(Father, Mother):
    def __init__(self, *args, **kwargs):
        Father.__init__(self, *args)
        Mother.__init__(self, **kwargs)

    def printson(self):
        print(self.a + ' ' + self.b)


f = Son('Ajay', x='Sagini')
f.printson()


class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addinput(self):
        if type(self.a) == int and type(self.b) == int:
            print('sum of numbers - ', self.a+self.b)
        else:
            r = str(self.a)
            s = str(self.b)
            print('string concatenation - ', r + s)


t = Add('3', 4)
t.addinput()
t = Add('a', 2)
t.addinput()


