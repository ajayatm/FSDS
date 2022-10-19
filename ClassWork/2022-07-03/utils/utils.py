class Person2:
    def __init__(self,name,surname,yob):
        self._name = name
        self.__surname = surname
        self.yob = yob

ajaypersonobject = Person2('ajay','mani',1981)

try:
    print(ajaypersonobject._name)
    print(ajaypersonobject._Person2__surname)
except Exception as e:
    print(e)
