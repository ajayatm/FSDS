class Person:

    def __init__(self,name,surname,emailid,yob):
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.yob = yob

    def getage(ajay, currentyear):
        return currentyear - ajay.yob


anujvar = Person('anuj','bhandari','anuj@gmail.com',1987)
print(anujvar.name)
print(anujvar.surname)
print(anujvar.emailid)
print(anujvar.yob)
print(anujvar.getage(2022))