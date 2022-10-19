from collections import OrderedDict

letters = OrderedDict({("a", 1), ("b", 2), ("c", 3)})
print(letters)


d = {'d': 4, 'b': 2, 'c': 3}
print(d)

fancy = OrderedDict()
fancy['d'] = 4
fancy['b'] = 2
fancy['c'] = 3
print(fancy)

f = [1,2,3,4]
f.append('t')
print(f)

dict_of_lists = {'a':[1,2,3,4]}
dict_of_lists['a'].append('something for a')
print(dict_of_lists)
