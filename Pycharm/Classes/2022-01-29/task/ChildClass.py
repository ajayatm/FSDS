import os
from MainClass import Main
print(os.getcwd())

class child(Main):

    def childread(self):
        try:
            a = Main.readfile(self)
            print(a)
        except Exception as e:
            return e

    def childwrite(self, k):
        try:
             Main.writefile(self, k)
        except Exception as e:
            return e

