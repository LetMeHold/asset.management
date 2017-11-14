# -*- coding: UTF-8 -*-

import sys
import traceback

class Global:

    def __init__(self):
        self.LOG = None
        self.ERR = None

    def setErr(self, err):
        self.ERR = err
        self.LOG.error(err)

GL = Global()
