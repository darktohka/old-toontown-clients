# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\distributed\DistributedTestObject.py
from direct.distributed import DistributedObject

class DistributedTestObject(DistributedObject.DistributedObject):
    __module__ = __name__

    def setRequiredField(self, r):
        self.requiredField = r

    def setB(self, B):
        self.B = B

    def setBA(self, BA):
        self.BA = BA

    def setBO(self, BO):
        self.BO = BO

    def setBR(self, BR):
        self.BR = BR

    def setBRA(self, BRA):
        self.BRA = BRA

    def setBRO(self, BRO):
        self.BRO = BRO

    def setBROA(self, BROA):
        self.BROA = BROA

    def gotNonReqThatWasntSet(self):
        for field in ('B', 'BA', 'BO', 'BR', 'BRA', 'BRO', 'BROA'):
            if hasattr(self, field):
                return True

        return False