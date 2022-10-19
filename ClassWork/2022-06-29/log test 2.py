import logging
logging.basicConfig(filename='log2.log', level=logging.WARNING, format='%(levelname)s %(asctime)s %(message)s')
logging.warning('this is a warning message with time')
