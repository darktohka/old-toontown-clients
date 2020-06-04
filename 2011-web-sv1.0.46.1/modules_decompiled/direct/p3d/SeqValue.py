# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\p3d\SeqValue.py
import types

class SeqValue:
    __module__ = __name__

    def __init__(self, value=None):
        self.value = ()
        if value is not None:
            self.set(value)
        return

    def set(self, value):
        if isinstance(value, types.TupleType):
            self.setFromTuple(value)
        elif isinstance(value, types.StringTypes):
            self.setFromString(value)
        else:
            raise TypeError, 'Invalid sequence type: %s' % (value,)

    def setFromTuple(self, value):
        self.value = value

    def setFromString(self, value):
        self.value = ()
        if value:
            value = value.split('.')
            value = map(int, value)
            self.value = tuple(value)

    def loadXml(self, xelement, attribute='seq'):
        self.value = ()
        value = xelement.Attribute(attribute)
        if value:
            try:
                self.setFromString(value)
            except ValueError:
                return False
            else:
                return True
        return False

    def storeXml(self, xelement, attribute='seq'):
        if self.value:
            value = ('.').join(map(str, self.value))
            xelement.SetAttribute(attribute, value)

    def __add__(self, inc):
        if not self.value:
            value = (1, )
        else:
            value = self.value[:-1] + (self.value[(-1)] + inc,)
        return SeqValue(value)

    def __cmp__(self, other):
        return cmp(self.value, other.value)

    def __bool__(self):
        return bool(self.value)

    def __str__(self):
        return 'SeqValue%s' % repr(self.value)