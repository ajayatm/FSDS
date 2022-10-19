import logging
logging.basicConfig(filename='log2.log',level=logging.INFO)

class List():
    def __init__(self,inlist):
        self.inlist = inlist

    #1 . Try to reverse a list
    def reversinglist(self):
        logging.info('Trying to reverse the list')
        return self.inlist[::-1]
    
    #2.  try to access 234 out of this list
    def get234(self):
        logging.info('Trying to get 234 from anywhere in the list')
        return self.inlist[7][0], self.inlist[8].keys()

    #3 . try to access 456
    def get456(self):
        logging.info('Trying to get 456 from anywhere in the list')
        return self.inlist[5][1]

    #4 . Try to extract only a list collection form list l
    def getlist(self):
        logging.info('Trying to get list from anywhere in the master list')
        return self.inlist[5:7]

    #5 . Try to extract "sudh"
    def getsudh(self):
        logging.info('Trying to get sudh from anywhere in the master list')
        return self.inlist[8]['key1']
    
    #6 . Try to list all the key in dict element avaible in list
    def getdictkeys(self):
        logging.info('Trying to get keys from dict in the master list')
        return self.inlist[8].keys()

    #7 . Try to extract all the value element form dict available in list
    def getdictvalues(self):
        logging.info('Trying to get keys from dict in the master list')
        return self.inlist[8].values()

try:
    inlist = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
    listobject = List(inlist)
    print(listobject.reversinglist())
    print(listobject.get234())
    print(listobject.get456())
    print(listobject.getlist())
    print(listobject.getsudh())
    print(listobject.getdictkeys())
    print(listobject.getdictvalues())

except Exception as e:
    logging.critical(e)