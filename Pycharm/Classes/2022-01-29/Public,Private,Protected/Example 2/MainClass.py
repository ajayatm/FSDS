class BonusCalculator:
    def __init__(self, empid, emprating):
        self.empid = empid
        self.emprating = emprating
        self.__bonusforratingA = '70%'
        self.__bonusforratingB = '60%'
        self.__bonusforratingC = '40%'

    def bonuscalculator(self):
        if self.emprating == 'A':
            bonus = self.__bonusforratingA
            return bonus
        elif self.emprating == 'B':
            bonus = self.__bonusforratingB
            return bonus
        elif self.emprating == 'C':
            bonus = self.__bonusforratingC
            return bonus
        else:
            return 'Invalid rating'

