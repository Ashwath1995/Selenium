import inspect

import pytest
import logging


@pytest.mark.usefixtures('setup')
class Utilityclass:

    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler("C:\\Users\\Ashwath\\PycharmProjects\\ZestMoney\\com\\logs\\logs.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger


