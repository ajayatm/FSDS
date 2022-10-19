from statistics import *
import logging
logging.basicConfig(filename='log5.log',level=logging.INFO)

class Functions:
    #q1 : Try to print a prime number in between 1 to 1000

    def getprime(self,start,end):
        logging.info('getting prime numbers between 1 and 1000')
        primelist = []
        for i in range(start,end+1):
            count = 0
            for j in range(start, int((end+2)/2)):
                if i > j:
                    if (i%j == 0):
                        count+=1
            if count == 1:
                primelist.append(i)
        return primelist

    #q2 : Try to write a function which  is equivalent  to print function in python

    def printfunction(self,*args):
        logging.info('Function equivalent to print')
        return args

    #q3 : Try to write a function which is a replica of list append , extend and pop function

    def listappend(self,l,a):
        logging.info('Function equivalent to append')
        l.insert(len(l),a)
        return l

    def listextend(self,l,k):
        logging.info('Function equivalent to extend')
        for i in k:
            l.insert(len(l),i)
        return l

    def listpop(self,l,a):
        logging.info('Function equivalent to pop')
        if a == len(l) - 1:    
            k = l[-1]
        elif a >= len(l):
            return "Invalid Index"
        else:
            for i in range(len(l)-1):
                if i >= a:
                    if i == a:
                        k = l[i]
                    l[i] = l[i+1]

        l = l[:-1]       
        return k,l

    #q4 : Try to write a lambda function which can return a concatination of all the string that we will pass
    logging.info('lambda concatenate')
    x = ['ajay', 'mani']
    sumstrings = lambda *x: [''.join(i for i in x)]
    print(sumstrings)

    #q5 : Try to write a lambda function which can return list of square of all the data between 1-100 
    logging.info('lambda squares')
    c = [(lambda x: x*x)(x) for x in range(1,101)]
    print(c)

    #q6 : Try to write a 10 Different different example of lambda function with a choice of your tasks
    logging.info('lambda examples')
    #1. Add two numbers
    a = lambda x,y:x+y

    #2. return sum of values from a dictionary
    b = lambda d: sum(v for k,v in d.items())

    #3. get the length of a list
    c = lambda l: max(i for i in l)

    #4. find greater between two numbers
    d = lambda x,y: x if x >= y else y

    #5. find average of medians from a list of lists
    e = lambda l: median(l)
    avgofmed = lambda k: mean([e(i) for i in k])

    #6. Find the cube of a number
    (lambda x:pow(x,3))(10)

    #7. filter even numbers from a list
    list(filter(lambda x: x%2 == 0,range(10)))

    #8. get squares for all numbers in a list
    list(map(lambda x:x*x,range(10)))

    #9. Multiple conditions
    (lambda x: 'Good' if x > 10 else ('Bad' if x < 5 else 'Okay'))(4)

    #10. sum of all numbers in a list
    from functools import reduce
    (reduce(lambda x,y:x+y, range(101) ))

    #q7 : Try to wwrite a funtion whihc can perform a read operation from .txt file

    def readtxtfile(self,f):
        f = open(f,'r')
        logging.info('reading from file')
        print(f.read())
        f.close()

try:
    functionobject = Functions()
    print(functionobject.getprime(1,345))
    print(functionobject.printfunction(1,2,3,4,5,56,6,7,8))
    print(functionobject.listappend([1,2,3,4,5],6))
    print(functionobject.listextend([1,2,3,4,5],[6]))
    print(functionobject.listpop([1,2,3,4,5],2))
except Exception as e:
    logging.critical(e)




