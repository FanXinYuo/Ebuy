import time
import logging


class Logger(object):
    def __init__(self, logger):
        # 创建一个loggerLogger
        self.logger = logging.getLogger(logger)
        # 设置日志的等级
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入到日志文件
        rq = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        log_path = './Ebuy/Logs/'
        log_name = log_path+rq+'.log'
        file_handler = logging.FileHandler(log_name, 'w')
        file_handler.setLevel(logging.INFO)
        # 再创建一个handler,用于输出到控制台
        c_handler = logging.StreamHandler()
        c_handler.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s- %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        c_handler.setFormatter(formatter)
        # 给logger添加handler
        self.logger.addHandler(file_handler)
        self.logger.addHandler(c_handler)

    def get_log(self):
        return self.logger
