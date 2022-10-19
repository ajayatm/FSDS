alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

f = open('vocab.kos.txt', 'r')
g = f.readlines()
count = 0
list1 = []
for word in g:
    position = 0
    switch = False
    for letter in word:
        if letter in alphabets:
            list1.append(word[position::])
            switch = True
            break
        else:
            position += 1
        if not switch:
            list1.append('Null')

count = 0
print(len(list1))
for word in g:
    print(count, word, list1[count])
    count += 1
    