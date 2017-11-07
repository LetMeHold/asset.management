# -*- coding: UTF-8 -*-

import logging
from logging.handlers import RotatingFileHandler

def getLogger(loggerName, logfile):
    LOG = logging.getLogger(loggerName)
    LOG.setLevel(logging.DEBUG) # 这个级别是基础

    # 输出日志到控制台
    ch = logging.StreamHandler()
    #cfmt = logging.Formatter('%(asctime)s - %(name)s - %(threadName)s - %(levelname)s - %(message)s')
    cfmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(cfmt)
    ch.setLevel(logging.INFO)  # 设置级别如果低于LOG设置的级别则无效
    #LOG.addHandler(ch)  # 如果不需要打印到控制台，注释这行即可

    # 输出日志到文件,文件最大1M，最多保存两个
    fh = logging.handlers.RotatingFileHandler(logfile, maxBytes=1*1024*1024, backupCount=2)
    ffmt = logging.Formatter('%(asctime)s - %(name)s - %(threadName)s - %(levelname)s - %(message)s')
    fh.setFormatter(ffmt)
    fh.setLevel(logging.DEBUG)   # 设置级别如果低于LOG设置的级别则无效
    LOG.addHandler(fh)  # 如果不需要记录到文件，注释这行即可
    return LOG

