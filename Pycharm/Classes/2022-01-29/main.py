from ClassFile import xyz

p = xyz(1, 2, 3)

class xyz1(xyz):
    pass

q = xyz1(4,5,6)

class abc:
    a = 10
    def do_abc(self):
        return self.a

r = abc()

print(r.do_abc())

q.test1()