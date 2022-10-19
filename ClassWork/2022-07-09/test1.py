"""docstring"""
class Bank:
    """docstring"""

    def transaction(self):
        """docstring"""
        print('total transaction value')

    def account_opening(self):
        """docstring"""
        print('account opening status')

    def deposit(self):
        """docstring"""
        print('show depoited value')


class Bank1:
    """docstring"""

    def transaction(self):
        """docstring"""
        print('total transaction value')

    def account_opening(self):
        """docstring"""
        print('account opening status')

    def deposit(self):
        """docstring"""
        print('show depoited value')

    def hdfc_to_icici(self):
        """docstring"""
        print('this will show the transactions happend to ICICI through HDFC')


class HDFCBank(Bank):
    """docstring"""

    def hdfc_to_icici(self):
        """docstring"""
        print('this will show the transactions happend to ICICI through HDFC')


class ICICI(HDFCBank):
    """docstring"""


if __name__ == '__main__':
    print('from test1.py')
    ICICIobj = ICICI()
    ICICIobj.hdfc_to_icici()
    ICICIobj.account_opening()
    ICICIobj.deposit()
    ICICIobj.transaction()
