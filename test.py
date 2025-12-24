from Nbvista.logger import logger
from Nbvista.custom_exception import InvalidURLException
# logger.info("This is a test log message from test.py")

try:
    raise InvalidURLException()
except Exception as e:  
    logger.error(f"caught an exception: {e}")