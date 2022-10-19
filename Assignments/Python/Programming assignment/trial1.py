# code
# Python code to merge dict using a single
# expression
def Merge(dict1, dict2):
	res = dict1 | dict2
	return res
	
# Driver code
dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
dict3 = Merge(dict1, dict2)
print(dict3)

# This code is contributed by virentanti16

a = {'1':2, '2':9, '4':5, '3':4, '6':7, '5':5, '7':8}
b = {1:3, 2:8, 4:5, 3:4, 6:7, 5:6, 7:8}
c = a | b
print(c)

dict4 = Merge(a, b)
print(dict4)
