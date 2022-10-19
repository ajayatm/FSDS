from AccessModifier import Salary

class NewSalary(Salary):
    def getnewsalary(self, empid, rating):
        if rating == self.ratingA:
            if empid == self.IdA:
                return self._Salary__SalaryA * self._raiseA
            elif empid == self.IdB:
                return self._Salary__SalaryB * self._raiseA
            elif empid == self.IdC:
                return self._Salary__SalaryC * self._raiseA
        elif rating == self.ratingB:
            if empid == self.IdA:
                return self._Salary__SalaryA * self._raiseB
            elif empid == self.IdB:
                return self._Salary__SalaryB * self._raiseB
            elif empid == self.IdC:
                return self._Salary__SalaryC * self._raiseB
        elif rating == self.ratingC:
            if empid == self.IdA:
                return self._Salary__SalaryA * self._raiseC
            elif empid == self.IdB:
                return self._Salary__SalaryB * self._raiseC
            elif empid == self.IdC:
                return self._Salary__SalaryC * self._raiseC


a = Salary()
b = NewSalary()
print(b.getnewsalary(101, 'A'))
print(b._Salary__SalaryA)
print(b._raiseA)
print(a.purpose())
print(b.purpose())
