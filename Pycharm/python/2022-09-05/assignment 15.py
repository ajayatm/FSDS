def genprimes(num):
    primes = [2]
    yield 2
    for k in range(3, num, 2):
        flag = True
        for j in primes:
            if k % j == 0:
                flag = False
        if flag:
            primes.append(k)
            yield k


a = genprimes(100)

for i in range(30):
    print(next(a))
