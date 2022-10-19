import logging
logging.basicConfig(filename='log3.log',level=logging.INFO)

class Loops:
    def __init__(self,List):
        self.List = List
    
    #q1 :
    #ineruon 
    #ineruon ineruon 
    #ineruon ineruon ineruon
    #ineruon ineruon ineruon ineruon
    def getsteps(self):
        logging.info('Printing \'Ineuron\' as steps')
        for i in range(4):
            print('ineuron ' * (i+1))
    
    """q2 - 

            ineruon
        ineruon ineruon
    ineruon ineruon ineruon
        ineruon ineruon
            ineruon"""
    def getdiamond(self,n,s):
        logging.info('Printing \'%s\' as diamond',s)
        padding = int(len(s)/2)

        for i in range(int((n+1)/2)):
            k = s + ' ' * padding
            k = k * (i) + s
            print(k.center(len(s)*n, ' '))
        for i in range(int((n)/2),0,-1):
            k = s + ' ' * padding
            k = k * (i - 1) + s
            print(k.center(len(s)*n, ' '))

    #q3 : Try to extract all the list entity
    def extractlist(self):
        logging.info('Printing lists in master list')
        for i in self.List:
            if type(i) is list:
                print(i)

    #q4 : Try to extract all the dict enteties
    def extractdict(self):
        logging.info('Printing dicts in master list')
        for i in self.List:
            if type(i) == dict:
                print(i)

    #q5 : Try to extract all the tuples entities
    def gettuples(self):
        logging.info('trying to get tuples from list')
        for i in self.List:
            if type(i) is tuple:
                print(i)

    #q6 : Try to extract all the numerical data it may b a part of dict key and values
    def getnum(self):
        logging.info('trying to get numerical data from list')     
        for i in self.List:
            if type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    if type(j) == int:
                        print(type(i), j)
            elif type(i) == dict:
                for k, v in i.items():
                    if type(k) == int:
                        print(type(i), 'key', k)
                    if type(v) == int:
                        print(type(i), 'value', v)

    #q7 : Try to give summation of all the numeric data 
    def getsumnum(self):
        logging.info('trying to get sum of numerical data from list')     
        sum = 0
        for i in self.List:
            if type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    if type(j) == int:
                        sum+=j
            elif type(i) == dict:
                for k, v in i.items():
                    if type(k) == int:
                        sum+=k
                    if type(v) == int:
                        sum+=v
        print('sum = ', sum)
    
    #q8 : Try to filter out all the odd values out all numeric data which is a part of a list
    def getodd(self):
        logging.info('trying to get odd numerical data from list')
        odd = []
        for i in self.List:
            if type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    if type(j) == int and j%2 != 0:
                        odd.append(j)
            elif type(i) == dict:
                for k, v in i.items():
                    if type(k) == int and k%2 != 0:
                        odd.append(k)
                    if type(v) == int and v%2 != 0:
                        odd.append(v)
        print(odd)

    #q9 : Try to extract "ineruon" out of this data
    def getineuron(self):
        logging.info('trying to get \'Ineuron\' from list')        
        for i in self.List:
            if type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    if j == 'ineuron':
                        print(type(i), j)
            elif type(i) == dict:
                for k, v in i.items():
                    if k == 'ineuron':
                        print(type(i), 'key', k)
                    if v == 'ineuron':
                        print(type(i), 'value', v)

    #q10 :Try to find out a number of occurances of all the data
    def getalldata(self):
        logging.info('trying to get number of occurrences data from list')        
        flatlist = []
        for i in self.List:
            if type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    flatlist.append(j)
            elif type(i) == dict:
                for k, v in i.items():
                    flatlist.append(k)
                    flatlist.append(v)
        uniqueset = set(flatlist)

        for i in uniqueset:
            print(i, flatlist.count(i))

    #q11 : Try to find out number of keys in dict element
    def getkeys(self):
        logging.info('trying to get number of keys in dict element from list') 
        keycount = 0
        for i in self.List:
            if type(i) == dict:
                for j in i:
                    keycount+=1
        print(keycount)

    #q12 : Try to filter out all the string data
    def getstring(self):
        logging.info('trying to get all string data from list')
        strlist = []
        for i in self.List:
            if type(i) is list or type(i) is tuple or type(i) is set:
                for j in i:
                    if type(j) is str:
                        strlist.append(j)
            elif type(i) == dict:
                for k, v in i.items():
                    if type(k) is str:
                        strlist.append(k)
                    if type(v) is str:
                        strlist.append(v)
        print(strlist)

    #q13 : Try to Find  out alphanum in data
    def getalphanum(self):
        logging.info('trying to get alphanum data from list')
        alnumlist = []
        for i in self.List:
            if type(i) is list or type(i) is tuple or type(i) is set:
                for j in i:
                    if type(j) is str and j.isalnum():
                        alnumlist.append(j)
            elif type(i) == dict:
                for k, v in i.items():
                    if type(k) is str and k.isalnum():
                        alnumlist.append(k)
                    if type(v) is str and v.isalnum():
                        alnumlist.append(v)
        print(alnumlist)

    #q14 : Try to find out multiplication of all numeric value in  the individual collection inside dataset 
    def getproduct(self):
        logging.info('trying to get product of all numeric data from list')
        multi = 1
        for i in self.List:
            if type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    if type(j) == int:
                        multi*=j
            elif type(i) == dict:
                for k, v in i.items():
                    if type(k) == int:
                        multi*=k
                    if type(v) == int:
                        multi*=v
        print('multi = ', multi)

    #q15 : Try to unwrape all the collection inside collection and create a flat list 
    def unwrap(self):
        logging.info('trying to unwrap all collections in list')
        flatlist = []
        for i in self.List:
            if type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    flatlist.append(j)
            elif type(i) == dict:
                for k, v in i.items():
                    flatlist.append(k)
                    flatlist.append(v)

        print(flatlist)


try:
    l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]
    Loopsobject = Loops(l)
    logging.info('Object created')
    Loopsobject.getsteps()
    Loopsobject.getdiamond(10,'Ineuron')
    Loopsobject.extractlist()
    Loopsobject.extractdict()
    Loopsobject.gettuples()
    Loopsobject.getnum()
    Loopsobject.getsumnum()
    Loopsobject.getodd()
    Loopsobject.getineuron()
    Loopsobject.getalldata()
    Loopsobject.getkeys()
    Loopsobject.getstring()
    Loopsobject.getalphanum()
    Loopsobject.getproduct()
    Loopsobject.unwrap()
except Exception as e:
    logging.critical(e)

