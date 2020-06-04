# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\hood\HoodUtil.py
from toontown.toonbase import ToontownGlobals

def calcPropType(node):
    propType = ToontownGlobals.AnimPropTypes.Unknown
    fullString = str(node)
    if 'hydrant' in fullString:
        propType = ToontownGlobals.AnimPropTypes.Hydrant
    elif 'trashcan' in fullString:
        propType = ToontownGlobals.AnimPropTypes.Trashcan
    elif 'mailbox' in fullString:
        propType = ToontownGlobals.AnimPropTypes.Mailbox
    return propType