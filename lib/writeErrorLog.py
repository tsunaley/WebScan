import logging
import sys, os
import datetime


class WriteLog(object):
    def __init__(self, excType, excValue, tb):
        self.__LogFile = os.path.join(sys.path[0], "log", "RunTimeError.txt")
        self.xcType = excType
        self.excValue = excValue
        self.tb = tb
        self.__Logger = self.__BuildLogger()
        self.__WriteLog()

    def __BuildLogger(self):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.addHandler(logging.FileHandler(self.__LogFile))
        return logger

    def __WriteLog(self):
        try:
            currentTime = datetime.datetime.now()
            self.__Logger.info('Timestamp: %s' % (currentTime.strftime("%Y-%m-%d %H:%M:%S")))
            self.__Logger.error("Uncaught exception：", exc_info=(self.xcType, self.excValue, self.tb))
            self.__Logger.info('\n')
        except:
            pass