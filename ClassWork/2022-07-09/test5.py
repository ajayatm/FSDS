"""d"""
class Ineuron:
    """d"""
    def __init__(self):
        self.students = "data science"

    def studentclass(self):
        """d"""
        print(self.students)

Iobject = Ineuron()
Iobject.studentclass()
Iobject.students = 'data analytics'
Iobject.studentclass()


class Ineuron1:
    """d"""
    def __init__(self):
        self.__students = "data science"
        self.age = 31

    def studentclass(self):
        """d"""
        print(self.__students)

    def getage(self):
        """d"""
        print(self.age)

    def studentchange(self,a):
        """d"""
        self.__students = a

Iobject1 = Ineuron1()
Iobject1.studentclass()
Iobject1.__students = 'data analytics'
Iobject1.studentclass()
Iobject1.studentchange('adasdads')
Iobject1.studentclass()
Iobject1.getage()
Iobject1.age = 32
Iobject1.getage()

print(Iobject1._Ineuron1__students)
