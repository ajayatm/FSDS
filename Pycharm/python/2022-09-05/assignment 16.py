years_list = [1981, 1982, 1983, 1984, 1985, 1986]

things = ["mozzarella", "cinderella", "salmonella"]

surprise = ["Groucho," "Chico", "Harpo"]
e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}

f2e = {}
for k,v in e2f.items():
    f2e[v] = k

m = []
for i in e2f:
    m.append(i)
m = set(m)

life = {'animals':{'cats':{'Henri', 'Grumpy', 'Lucy'}, 'octopi':{}, 'emus':{}}, 'plants':{}, 'other':{}}
print(life)
for j in life:
    print(j)
for j in life['animals']:
    print(j)
for j in life['animals']['cats']:
    print(j)
