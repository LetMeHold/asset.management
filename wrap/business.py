# -*- coding: utf-8 -*-

from gl import *

class Business:

    def connect(self):
        GL.LOG.info('建立连接')

    def disconnect(self):
        GL.LOG.info('断开连接')


