class Salary:
    def __init__(self):
        self.__SalaryA = 100000
        self.__SalaryB = 120000
        self.__SalaryC = 140000
        self.IdA = 101
        self.IdB = 102
        self.IdC = 103
        self._raiseA = 1.3
        self._raiseB = 1.2
        self._raiseC = 1.1
        self.ratingA = 'A'
        self.ratingB = 'B'
        self.ratingC = 'C'

    @staticmethod
    def purpose():
        print('the purpose of this class is to identify new salary')
