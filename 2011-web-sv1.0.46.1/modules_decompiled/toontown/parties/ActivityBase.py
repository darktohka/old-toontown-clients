# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\parties\ActivityBase.py


class ActivityBase:
    __module__ = __name__

    def __init__(self, activityId, x, y, h):
        self.activityId = activityId
        self.x = x
        self.y = y
        self.h = h

    def __str__(self):
        string = '<ActivityBase activityId=%d, ' % self.activityId
        string += 'x=%d, y=%d, h=%d>' % (self.x, self.y, self.h)
        return string

    def __repr__(self):
        return self.__str__()