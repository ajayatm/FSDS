alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

f = open('vocab.pubmed.txt', 'r', encoding='utf-8')
g = f.readlines()
count = 0
list1 = []
for word in g:
    k = word.split()
    switch = False
    phrase = ''
    for x in k:
        for letter in x:
            if letter in alphabets:
                phrase = phrase + letter
                switch = True
    if switch:
        list1.append(phrase)
    else:
        list1.append('None')
    count += 1
count = 0
countnull = 0
countgood = 0
for word in g:
    k = word.split()
    print(count, k[0], list1[count])
    if list1[count] == 'None':
        countnull += 1
    else:
        countgood += 1
    count += 1

print(countnull)
print(countgood)
print(list1[35])
print(phrase)
