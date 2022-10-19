class Main:
    def __init__(self, f):
        self.f = f

    def readfile(self):
        try:
            a = open(self.f, 'r')
            return a.read()
            a.close()
        except Exception as e:
            return e

    def writefile(self, k):
        try:
            b = open(self.f, 'w')
            b.write(k)
            b.close()
            return None
        except Exception as e:
            return e
