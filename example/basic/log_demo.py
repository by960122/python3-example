import logging
import sys


class Logger(object):
    def __init__(self, log_file_name=None, log_level=logging.INFO, logger_name=None):
        # 创建一个logger
        self.__logger = logging.getLogger(logger_name)
        # 指定日志的最低输出级别
        self.__logger.setLevel(log_level)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s [%(filename)s:%(lineno)d] - [%(levelname)s] %(message)s')
        # 创建一个handler用于写入日志文件
        if log_file_name:
            file_handler = logging.FileHandler(log_file_name, mode="w", encoding='utf-8')
            file_handler.setFormatter(formatter)
            self.__logger.addHandler(file_handler)
        # 创建一个handler用于输出控制台
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.__logger.addHandler(console_handler)

    def get_log(self):
        return self.__logger


if __name__ == '__main__':
    log = Logger(log_file_name='log.txt', log_level=logging.INFO).get_log()
    log.info("测试")
