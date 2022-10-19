from ClassFile import xyz


class xyz1(xyz):
    def test(self):
        return 'this is from test method inside inherited xyz1 class'


x = xyz1(7,8,9)


class lmn:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def test(self):
        return 'method test1 from lmn1'


class lmn1:
    def __init__(self,p,q):
        self.p = p
        self.q = q

    def test1(self):
        return 'variables are ' + str(self.p) + ',' + str(self.q)


class child(lmn1,lmn):
    def __init__(self,*args,**kwargs):
        lmn.__init__(self,**kwargs)
        lmn1.__init__(self,*args)


n = child(3,4,a=5,b=6,c=7)

print(n.p)
print(n.q)
print(n.a)
print(n.b)
print(n.c)
print(n.test())
print(n.test1())
