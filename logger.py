import logging 
import sys 

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('output.log')
logger.setLevel(10)
formatter_stream = logging.Formatter('[%(asctime)s] {%(levelname)s} - %(message)s')
formatter_file = logging.Formatter('[%(asctime)s] {%(levelname)s} %(name)s: #%(lineno)d - %(message)s')
file_handler.setFormatter(formatter_file)
stream_handler.setFormatter(formatter_stream)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)