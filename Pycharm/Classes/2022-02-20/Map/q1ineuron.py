hand = open('vocab.pubmed.trial.txt', 'r', encoding='utf-8')
di = dict()
count = 0
for lin in hand:
    lin = lin.split()
    for x in lin:
        print(x)
        print(di)
        print(di.get(x))
        di[x] = di.get(x, 0) + 1
        print(di[x])
        print('-----------')
print(list(di.items()))
