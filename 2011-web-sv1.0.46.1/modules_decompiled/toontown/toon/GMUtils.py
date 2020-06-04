# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\toon\GMUtils.py
from toontown.toonbase import TTLocalizer

def testGMIdentity(name=''):
    if name.find('$') != -1:
        return True
    else:
        return False


def handleGMName(name=''):
    if name.find('$000') != -1:
        prefix = TTLocalizer.GM_1
    elif name.find('$001') != -1:
        prefix = TTLocalizer.GM_2
    elif name.find('$002') != -1:
        prefix = TTLocalizer.GM_3
    elif name.find('$003') != -1:
        prefix = TTLocalizer.GM_4
    else:
        prefix = ''
    gmName = prefix + ' ' + name.lstrip('$0123456789')
    return gmName


def getGMType(name=''):
    if name.find('$000') != -1 or name.find(TTLocalizer.GM_1) == 0:
        return TTLocalizer.GM_1
    elif name.find('$001') != -1 or name.find(TTLocalizer.GM_2) == 0:
        return TTLocalizer.GM_2
    elif name.find('$002') != -1 or name.find(TTLocalizer.GM_3) == 0:
        return TTLocalizer.GM_3
    elif name.find('$003') != -1 or name.find(TTLocalizer.GM_4) == 0:
        return TTLocalizer.GM_4
    else:
        return ''