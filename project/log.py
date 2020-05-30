# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/03/26
# @Author  : 陈志鹏
# @File    : xxx.py

import os
import sys
import time
import logging

class Log(object):
    """
    封装后的logging
    """

    def __init__(self, logger=None, log_cate='search', log_path=os.getcwd()):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        """

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        self.log_time = time.strftime("%Y_%m_%d")
        # if log_path == None:
        #     file_dir = os.path.join(os.getcwd(), "log")
        # else:

        file_dir = os.path.join(log_path, "log")
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)
            # print(file_dir)
        # self.log_path = file_dir
        self.log_name = file_dir + "/" + log_cate + "." + self.log_time + '.log'
        # print(self.log_name)

        # fh = logging.FileHandler(self.log_name, 'a')  # 追加模式  这个是python2的
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s:%(lineno)d [%(levelname)1.1s] %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        #  添加下面一句，在记录日志之后移除句柄
        # self.logger.removeHandler(ch)
        # self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()
        ch.close()

    def getlog(self):
        return self.logger

    def test(self):
        self.logger.critical("test")
        self.logger.error("test")
        self.logger.warning("test")
        self.logger.info("test")
        self.logger.debug("test")


if __name__ == '__main__':
    log = Log(__name__)
    logger = log.getlog()
    log.test()
