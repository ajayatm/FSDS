import logging
logging.basicConfig(filename='test.log', level = logging.DEBUG)
logging.info('this is my first output for logging')
l = [1,2,3,4,5,6,7]
for i in l:
    if i==2:
        logging.info(i)
logging.critical('This is a critical message!!!')
logging.error('This is an error message!!!')
logging.warning('This is a warning message!!!')
logging.info('This is an info message!!!')
logging.debug('This is a debug message!!!')

logging.shutdown()