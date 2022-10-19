class Dict_Parser:
    def __init__(self, a):
        self.a = a

    def dictkeys(self):
        try:
            self.test()
        except Exception as e:
            return e
        else:
            return list(self.a.keys())

    def dictvalues(self):
        try:
            self.test()
        except Exception as e:
            return e
        else:
            return list(self.a.values())

    def check_dict(self):
        try:
            return self.test()
        except Exception as e:
            return e

    def test(self):
        if type(self.a) != dict:
            raise TypeError("Only dictionary is allowed as input")
        else:
            return 'dict is good'

    def userinput(self):
        try:
            self.a = eval(input("Please enter a dictionary - "))
            if type(self.a) == dict:
                return self.a, type(self.a), list(self.a.keys()), list(self.a.values())
            else:
                raise TypeError("Only dictionary is allowed as input")
        except Exception as e:
            return e


    def insertion(self,k,v):
        self.a[k] = v
        return self.a