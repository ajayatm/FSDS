import logging
import os
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
    
    def creatingtables(self):
        try:
            createtables(self.input1, self.input2)
        except:
            logging.critical('Critical Exception creating tables')

    def loadtables(self):
        try:
            loadingtables(self.input1, self.input2)
        except:
            logging.critical('Critical Exception loading tables')

    def gettingdf(self):
        try:
            readtodf(self.input1, self.input2)
        except:
            logging.critical('Critical Exception loading dataframe')

    def dftojson(self, df):
        try:
            loaddftojson(df)
        except:
            logging.critical('Critical Exception creating json')

    def jsontomongo(self, js):
        try:
            loadjsontomongo(js)
        except:
            logging.critical('Critical Exception loading mongo')
    
    def leftjointables(self):
        try:
            joiningtablesleft()
        except:
            logging.critical('Critical Exception joining tables')
    
    def leftjointables(self):
        try:
            joiningtablesleft()
        except:
            logging.critical('Critical Exception joining tables')
    
    def getunique(self):
        try:
            getuniquedresscount()
        except:
            logging.critical('Critical Exception getting dress counts')
    
    def zerorecommend(self):
        try:
            getzerorecommend()
        except:
            logging.critical('Critical Exception getting zero recommendation count')
    
    def salescount(self):
        try:
            getsalescount()
        except:
            logging.critical('Critical Exception getting sales count')

    def thirdhighest(self):
        try:
            getthirdhighest()
        except:
            logging.critical('Critical Exception getting third highest selling dress')