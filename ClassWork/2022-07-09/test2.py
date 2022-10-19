"""docstring"""
from test1 import Bank1
print('starting test2.py file--------------------')


class HDFCBank:
    """docstring"""
    def hdfc_to_icici(self):
        """docstring"""
        print('this will show the transactions to ICICI through HDFC')


class ICICI(Bank1, HDFCBank):
    """docstring"""


print('from test2.py')


ICICIobj = ICICI()
ICICIobj.hdfc_to_icici()
ICICIobj.account_opening()
ICICIobj.deposit()
ICICIobj.transaction()
