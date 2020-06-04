# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\login\RemoteValueSet.py
from direct.directnotify import DirectNotifyGlobal
import TTAccount, HTTPUtil

class RemoteValueSet:
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('RemoteValueSet')

    def __init__(self, url, http, body='', expectedHeader=None, expectedFields=[], onUnexpectedResponse=None):
        if onUnexpectedResponse is None:
            onUnexpectedResponse = self.__onUnexpectedResponse
        response = HTTPUtil.getHTTPResponse(url, http, body)
        if expectedHeader is not None:
            if response[0] != expectedHeader:
                errMsg = 'unexpected response: %s' % response
                self.notify.warning(errMsg)
                onUnexpectedResponse(errMsg)
                return
            response = response[1:]
        self.dict = {}
        for line in response:
            if not len(line):
                continue
            try:
                (name, value) = line.split('=', 1)
            except ValueError, e:
                errMsg = 'unexpected response: %s' % response
                self.notify.warning(errMsg)
                onUnexpectedResponse(errMsg)
                return

            if len(expectedFields):
                if name not in expectedFields:
                    self.notify.warning("received field '%s' that is not in expected field list" % name)
            self.dict[name] = value

        for name in expectedFields:
            if not self.dict.has_key(name):
                errMsg = "missing expected field '%s'" % name
                self.notify.warning(errMsg)
                onUnexpectedResponse(errMsg)
                return

        return

    def __repr__(self):
        return 'RemoteValueSet:%s' % str(self.dict)

    def hasKey(self, key):
        return self.dict.has_key(key)

    def getBool(self, name, default=None):
        return self.__getValue(name, lambda x: int(x) != 0, default)

    def getInt(self, name, default=None):
        return self.__getValue(name, int, default)

    def getFloat(self, name, default=None):
        return self.__getValue(name, float, default)

    def getString(self, name, default=None):
        return self.__getValue(name, str, default)

    def __getValue(self, name, convOp, default):
        if default is None:
            return convOp(self.dict[name])
        else:
            return convOp(self.dict.get(name, default))
        return

    def __onUnexpectedResponse(self, errStr):
        raise HTTPUtil.UnexpectedResponse(errStr)