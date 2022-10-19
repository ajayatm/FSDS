"""docstring"""
class Ineuron:
    """docstring"""
    def student(self):
        """docstring"""
        print("print the details of all students")

    def achievers(self):
        """docstring"""
        print("print the details of all achievers")

    def hall_of_fame(self):
        """docstring"""
        print("print all of hall of fame")


class IneuronVision(Ineuron):
    """docstring"""
    def student(self):
        print("print the details of all vision students")


IVobject = IneuronVision()
IVobject.student()
