import logging
logging.basicConfig(filename='log3.log',level=logging.INFO,format='%(levelname)s %(asctime)s %(message)s')

def div(a,b):
    logging.info('The numbers entered are %d and %d', a, b)
    return (a/b)
    
try:
    print(div(6,0))
except Exception as msg:
    logging.info(msg)

