# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\catalog\CatalogInvalidItem.py
import CatalogItem
from toontown.toonbase import TTLocalizer
from direct.showbase import PythonUtil
from toontown.toonbase import ToontownGlobals

class CatalogInvalidItem(CatalogItem.CatalogItem):
    __module__ = __name__

    def requestPurchase(self, phone, callback):
        self.notify.error('Attempt to purchase invalid item.')

    def acceptItem(self, mailbox, index, callback):
        self.notify.error('Attempt to accept invalid item.')

    def output(self, store=-1):
        return 'CatalogInvalidItem()'