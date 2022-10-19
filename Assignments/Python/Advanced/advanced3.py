def checkfunc():
    a = 10
    return a

class Checkfun:
    b = 20

    def __init__(self,c):
        print('b =', self.b)
        self.b = c
        print('b =', self.b)
        print('b =', Checkfun.b)

print('a =', checkfunc())
funct = Checkfun(30)
print('calling b from outside; b=',Checkfun.b)
print('calling a from outside; a=',checkfunc())