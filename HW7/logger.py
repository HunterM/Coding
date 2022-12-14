import logging
import os

path = "D:/Coding/Coding/HW7/"
logging.basicConfig(filename=os.path.join(path, 'logger.log'),level=logging.DEBUG)

logging.basicConfig(
    level=logging.INFO,
    filename='logger.log',
    format= "%(asctime)s - [%(levelname)s] - %(app)s - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    datefmt='%d.%m.%Y %H:%M',
                    )



# os.replace("logger.log", "D:/Coding/Coding/HW7/logger.log")
