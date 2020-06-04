# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\speedchat\TTSCSingingMenu.py
from direct.showbase import PythonUtil
from otp.speedchat.SCMenu import SCMenu
from otp.speedchat.SCMenuHolder import SCMenuHolder
from TTSCSingingTerminal import TTSCSingingTerminal
from otp.otpbase import OTPLocalizer
SingingMenuGuide = [
 (
  OTPLocalizer.SingingMenuSections[0], [{9000: 25}, {9001: 26}, {9002: 27}, {9003: 28}, {9004: 29}, {9005: 30}, {9006: 31}, {9007: 32}, {9008: 33}])]

class TTSCSingingMenu(SCMenu):
    __module__ = __name__

    def __init__(self):
        SCMenu.__init__(self)
        self.__singingMessagesChanged()

    def destroy(self):
        SCMenu.destroy(self)

    def clearMenu(self):
        SCMenu.clearMenu(self)

    def __singingMessagesChanged(self):
        self.clearMenu()
        try:
            lt = base.localAvatar
        except:
            return

        for count in xrange(len(SingingMenuGuide)):
            section = SingingMenuGuide[count]
            if section[0] == -1:
                for phrase in section[1]:
                    emote = None
                    if type(phrase) == type({}):
                        item = phrase.keys()[0]
                        emote = phrase[item]
                        phrase = item
                    if phrase not in OTPLocalizer.SpeedChatStaticText:
                        print 'warning: tried to link a singing phrase %s which does not seem to exist' % phrase
                        break
                    terminal = TTSCSingingTerminal(phrase)
                    if emote is not None:
                        terminal.setLinkedEmote(emote)
                    self.append(terminal)

        return