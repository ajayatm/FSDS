class Test(Exception):
    def __init__(self, msg):
        self.msg = msg


try:
    a = input("Please input input divisor - ")
    if int(a) != 0:
        b = 5/int(a)
        print(b)
    else:
        try:
            raise(Test("Input integer equal to 0"))
        except Test as t:
            print(t)

except Exception as e:
    print("Exception is", e)
