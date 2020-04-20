import sys
import logging
import traceback
import datetime
import test


class ExceptHookHandler(object):
    def __init__(self, logFile, mainFrame=None):
        self.__LogFile = logFile
        self.__MainFrame = mainFrame

        self.__Logger = self.__BuildLogger()
        sys.excepthook = self.__HandleException

    def __BuildLogger(self):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.addHandler(logging.FileHandler(self.__LogFile))
        return logger

    # excType: 异常类型
    # excValue: 异常对象
    # tb: 异常的trace back
    def __HandleException(self, excType, excValue, tb):
        # first logger
        try:
            currentTime = datetime.datetime.now()
            self.__Logger.info('Timestamp: %s' % (currentTime.strftime("%Y-%m-%d %H:%M:%S")))
            self.__Logger.error("Uncaught exception：", exc_info=(excType, excValue, tb))
            self.__Logger.info('\n')
        except:
            pass

        # sys.__excepthook__(excType, excValue, tb)

        err_msg = ':('.join(traceback.format_exception(excType, excValue, tb))
        err_msg += '\n Your App happen an exception, please contact administration.'

        print(err_msg)


if __name__ == '__main__':
    ExceptHookHandler('F:\比赛\作品赛\project\log\log.txt')
    a = 1
    test.Emmm()
