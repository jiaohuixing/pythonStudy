import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')
try:
    raise Exception('i am exception')
except Exception as e:
    logging.info(e)
    print(e)
finally:
    logging.info('finally!')