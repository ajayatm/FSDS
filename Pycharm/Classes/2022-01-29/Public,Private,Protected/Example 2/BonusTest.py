from MainClass import BonusCalculator

emp1 = BonusCalculator(101, 'A')
emp2 = BonusCalculator(102, 'A')
emp3 = BonusCalculator(103, 'A')

print(emp1.bonuscalculator())
emp1._BonusCalculator__bonusforratingA = '80%'
print(emp1.bonuscalculator())

print(emp2.bonuscalculator())
print(emp3.bonuscalculator())
