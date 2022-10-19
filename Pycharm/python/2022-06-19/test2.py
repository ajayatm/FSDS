#q2 : try to print below by using while loop
"""
A
B H
C I N
D J O S
E K p T W
F L Q U X z
G M R V Y
"""
alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

i = 0
lines = 7
while i < lines:
    print(alphabets[i] + '   ',end='')
    j = 0
    column = i + lines - 1
    while j < i:
        if column < len(alphabets):
            print(alphabets[column] + '   ',end='')
            column = column + lines - j - 2
        else:
            j = i
        j+=1
    else:
        print('\n')
    i+=1