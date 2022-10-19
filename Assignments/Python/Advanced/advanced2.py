class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self): # Behavior methods
        return self.name.split()[-1] # self is implied subject
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent)) # Must change here only
    def __repr__(self): # Added method
        return '[Person: %s, %s, %s]' % (self.name, self.pay, self.job) # String to print

class Manager(Person): # Inherit Person attrs
    def giveRaise(self, percent, bonus=.10): # Redefine to customize
        Person.giveRaise(self, percent+bonus)

if __name__ == '__main__': # When run for testing only
    # self-test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName()) # Use the new methods
    sue.giveRaise(.10) # instead of hardcoding
    print(sue)
    tom = Manager('Tom Jones', 'mgr', 50000) # Make a Manager
    tom.giveRaise(.10) # Runs custom version
    print(tom.lastName()) # Runs inherited method
    print(tom) # Runs inherited __repr__