# -*- coding:utf-8 -*-
__author__ = "leo"

import logging
import os
from datetime import datetime


class UserLog:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 控制台输出日志
        # console = logging.StreamHandler()
        # logger.addHandler(console)
        # 文件名
        base_dir = os.path.join(os.getcwd())
        log_dir = os.path.join(base_dir, "logs")
        log_file = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".log"
        log_name = log_dir + "\\" + log_file

        # 文件输出日志
        self.file_handle = logging.FileHandler(log_name, "a", encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s %(filename)s %(funcName)s %(levelno)s %(levelname)s %(message)s")
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

        self.logger.debug("test1234")

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)


if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.debug("test")
    user.close_handle()