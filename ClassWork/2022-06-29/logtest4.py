import logging
logging.basicConfig(filename='logtest4.log',level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')

try:
    f = open('ajay1.txt','r')
    logging.info('File opened')
except Exception as e:
    logging.critical(e)
