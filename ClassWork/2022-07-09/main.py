"""docstring"""
class Car:
    """docstring"""
    def __init__(self, body, engine, tyre):
        self.body = body
        self.engine = engine
        self.tyre = tyre

    def mileage(self):
        """docstring"""
        print("mileage of this car")


class Toyota(Car):
    """docstring"""


t = Toyota('sedan', 'v6', 'radial')

print(t.mileage())
