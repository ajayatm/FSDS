import logging
import os
import mysqlfile
logging.basicConfig(filename='pandaslog.log',level=logging.INFO)
class Pandas:
    def __init__(self, input1, input2):
        logging.info('Getting file details')
        self.input1 = input1
        self.input2 = input2
        try:
            if not os.path.isfile(self.input1):
                logging.critical('First file does not exist!!!')
                raise Exception
            if not os.path.isfile(self.input2):
                logging.critical('Second file does not exist!!!')
                raise Exception
        except:
            logging.critical('Critical Exception initializing, stopping the process')
    
    def loadtables(self):
        try:
            mysqlfile.loadingtables(self.input1, self.input2)
        except:
            logging.critical('Critical Exception loading tables')

    def leftjointables(self):
        try:
            mysqlfile.leftjoin()
        except:
            logging.critical('Critical Exception joining tables')
    
    def getdresscount(self):
        try:
            mysqlfile.noofdress()
        except:
            logging.critical('Critical Exception getting dress count')
    
    def zerorecommend(self):
        try:
            mysqlfile.zerorecommendation()
        except:
            logging.critical('Critical Exception getting zero recommendation count')
    
    def salescount(self):
        try:
            mysqlfile.totalsales()
        except:
            logging.critical('Critical Exception getting sales count')

    def getthirdhighest(self):
        try:
            mysqlfile.thirdhighest()
        except:
            logging.critical('Critical Exception getting third highest selling dress')

    def pandasmongo(self):
        try:
            mysqlfile.pandasdf()
        except:
            logging.critical('Critical Exception getting dataframe')

f1 = 'D:\\Ajay\\Education\\iNeuron\\FSDS\\ClassWork\\2022-07-24\\class assignment\\Attribute DataSet.xlsx'
f2 = 'D:\\Ajay\\Education\\iNeuron\\FSDS\\ClassWork\\2022-07-24\\class assignment\\Dress Sales.xlsx'


PandasObject = Pandas(f1,f2)
PandasObject.loadtables()
PandasObject.leftjointables()
PandasObject.getdresscount()
PandasObject.zerorecommend()
PandasObject.salescount()
PandasObject.getthirdhighest()
PandasObject.pandasmongo()