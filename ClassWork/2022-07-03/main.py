import utils.utils
import test1
print('test1 ending and main starting')
class Person1:
    def __init__(self,name,surname,yob):
        self._name = name
        self.__surname = surname
        self.yob = yob

ajaypersonobject = Person1('ajay','mani',1981)

try:
    print(ajaypersonobject._name)
    print(ajaypersonobject._Person1__surname)
except Exception as e:
    print(e)

print(test1.emp1.age(2022))
print(test1.emp1._age(2022))
print(test1.emp1._Person__age(2022))

emp2 = test1.Employee()

print(emp2.age(2000))
print(emp2._age(2000))
print(emp2._Person__age(2000))
print(emp2._Person__yob)
print(emp2._Employee__yob)
print(emp2._yob)
print(emp2._yob)

p1 = utils.utils.Person2('emil','joseph',1989)
print(p1.yob)

