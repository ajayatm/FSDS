from pkg1 import DictParser

d = DictParser.Dict_Parser({1:2})
print(d.check_dict())
print(d.dictkeys())
print(d.dictvalues())
print(d.insertion(3,4))
print(d.userinput())