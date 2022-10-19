class Person:

    def getage(ajay, currentyear, yob):
        return currentyear - yob

    def emailidinput(self,email):
        print("take email id from a person and print it", email)
    
    def askname(self):
        name = input('tell me your name: ')
        return name
    
    def askdob(self):
        dob = input('tell me your dob: ')
        return dob


anujvar = Person()
print(anujvar.getage(2022,1999))
print(anujvar.emailidinput('a@b.c'))
print(anujvar.askname())
print(anujvar.askdob())
