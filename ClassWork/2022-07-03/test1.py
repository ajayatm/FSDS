#import main
class Person:

    _name = 'ajay'
    __surname = 'mani'
    yob = 1981
    _yob = 1981
    __yob = 1981

    def age(self,currentyear):
        return currentyear - self.yob
    def _age(self,currentyear):
        return currentyear - self._yob
    def __age(self,currentyear):
        return currentyear - self.__yob
    
personobj = Person()
print(personobj.age(2022))
print(personobj._age(2022))
print(personobj._Person__age(2022))


class Employee(Person):
    _name = 'sagini'
    __surname = 'joy'
    yob = 1984
    _yob = 1984
    __yob = 1984

emp1 = Employee()

try:
    print(emp1.yob)
    print(emp1._name)
    print(emp1._Person__surname)
except Exception as e:
    print(e)

try:
    print(emp1.yob)
    print(emp1._name)
    print(emp1._Employee__surname)
except Exception as e:
    print(e)

print(emp1.age(2022))
print(emp1._age(2022))
print(emp1._Person__age(2022))


#new = main.Person1('michelle','thomas',2014)
#print(new.yob)
