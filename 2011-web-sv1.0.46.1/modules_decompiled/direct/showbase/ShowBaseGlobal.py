# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\showbase\ShowBaseGlobal.py
__all__ = []
from ShowBase import *
directNotify.setDconfigLevels()

def inspect(anObject):
    from direct.tkpanels import Inspector
    return Inspector.inspect(anObject)


import __builtin__
__builtin__.inspect = inspect
if not __debug__ and __dev__:
    notify = directNotify.newCategory('ShowBaseGlobal')
    notify.error("You must set 'want-dev' to false in non-debug mode.")