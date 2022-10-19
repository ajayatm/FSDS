"""d"""
class Ineuron:
    """d"""
    def students(self):
        """d"""
        print('print student details')


class ClassType:
    """d"""
    def students(self):
        """d"""
        print('print the class type of students')


def test(a, b):
    """d"""
    return a+b


print(test(3,4))
print(test('ajay','mani'))

def external(a):
    """d"""
    return a.students()

l = Ineuron()
external(l)
m = ClassType()
external(m)
