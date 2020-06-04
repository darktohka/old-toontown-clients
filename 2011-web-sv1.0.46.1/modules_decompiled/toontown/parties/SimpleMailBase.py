# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\parties\SimpleMailBase.py


class SimpleMailBase:
    __module__ = __name__

    def __init__(self, msgId, senderId, year, month, day, body):
        self.msgId = msgId
        self.senderId = senderId
        self.year = year
        self.month = month
        self.day = day
        self.body = body

    def __str__(self):
        string = 'msgId=%d ' % self.msgId
        string += 'senderId=%d ' % self.senderId
        string += 'sent=%s-%s-%s ' % (self.year, self.month, self.day)
        string += 'body=%s' % self.body
        return string