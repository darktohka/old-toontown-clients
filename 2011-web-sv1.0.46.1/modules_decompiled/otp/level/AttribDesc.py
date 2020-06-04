# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\level\AttribDesc.py


class AttribDesc:
    __module__ = __name__

    def __init__(self, name, default, datatype='string', params={}):
        self.name = name
        self.default = default
        self.datatype = datatype
        self.params = params

    def getName(self):
        return self.name

    def getDefaultValue(self):
        return self.default

    def getDatatype(self):
        return self.datatype

    def getParams(self):
        return self.params

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'AttribDesc(%s, %s, %s, %s)' % (repr(self.name), repr(self.default), repr(self.datatype), repr(self.params))