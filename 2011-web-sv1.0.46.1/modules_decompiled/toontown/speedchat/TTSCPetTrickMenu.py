# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\speedchat\TTSCPetTrickMenu.py
from direct.directnotify import DirectNotifyGlobal
from otp.speedchat.SCMenu import SCMenu
from otp.speedchat import SCMenuHolder
from otp.speedchat.SCStaticTextTerminal import SCStaticTextTerminal
from otp.otpbase import OTPLocalizer
from toontown.pets import PetTricks

class TTSCPetTrickMenu(SCMenu):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('TTSCPetTrickMenu')

    def __init__(self):
        SCMenu.__init__(self)
        self.accept('petTrickPhrasesChanged', self.__phrasesChanged)
        self.__phrasesChanged()

    def destroy(self):
        self.ignore('petTrickPhrasesChanged')
        SCMenu.destroy(self)

    def __phrasesChanged(self, zoneId=0):
        self.clearMenu()
        try:
            lt = base.localAvatar
        except:
            return

        for trickId in lt.petTrickPhrases:
            if trickId not in PetTricks.TrickId2scIds:
                TTSCPetTrickMenu.notify.warning('unknown trick ID: %s' % trickId)
            else:
                for msg in PetTricks.TrickId2scIds[trickId]:
                    self.append(SCStaticTextTerminal(msg))