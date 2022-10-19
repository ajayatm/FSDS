class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print('name:', self.name)
        print('symbol:', self.symbol)
        print('number:', self.number)


Hydrogen = Element('Hydrogen', 'H', 1)
hydrdict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(hydrdict['name'], hydrdict['symbol'], hydrdict['number'])
print(Hydrogen.name)
print(hydrogen.number)
hydro1 = Element(**hydrdict)
print(hydro1.name)

hydrogen.dump()
