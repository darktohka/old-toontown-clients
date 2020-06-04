# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\char\DistributedChar.py
from otp.avatar import DistributedAvatar
import Char

class DistributedChar(DistributedAvatar.DistributedAvatar, Char.Char):
    __module__ = __name__

    def __init__(self, cr):
        try:
            self.DistributedChar_initialized
        except:
            self.DistributedChar_initialized = 1
            DistributedAvatar.DistributedAvatar.__init__(self, cr)
            Char.Char.__init__(self)

    def delete(self):
        try:
            self.DistributedChar_deleted
        except:
            self.DistributedChar_deleted = 1
            Char.Char.delete(self)
            DistributedAvatar.DistributedAvatar.delete(self)

    def setDNAString(self, dnaString):
        Char.Char.setDNAString(self, dnaString)

    def setDNA(self, dna):
        Char.Char.setDNA(self, dna)

    def playDialogue(self, *args):
        Char.Char.playDialogue(self, *args)

    def setHp(self, hp):
        self.hp = hp