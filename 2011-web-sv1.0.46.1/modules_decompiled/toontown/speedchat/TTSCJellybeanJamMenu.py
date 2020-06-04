# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\speedchat\TTSCJellybeanJamMenu.py
from direct.showbase import PythonUtil
from otp.speedchat.SCMenu import SCMenu
from otp.speedchat.SCMenuHolder import SCMenuHolder
from otp.speedchat.SCStaticTextTerminal import SCStaticTextTerminal
from otp.otpbase import OTPLocalizer
JellybeanJamMenu = [
 (
  OTPLocalizer.JellybeanJamMenuSections[0], [30180, 30181, 30182, 30183, 30184, 30185]), (OTPLocalizer.JellybeanJamMenuSections[1], [30186, 30187, 30188, 30189, 30190])]
JellybeanJamPhases = PythonUtil.Enum('TROLLEY, FISHING, PARTIES')
PhaseSpecifPhrases = [
 30180, 30181, 30182]

class TTSCJellybeanJamMenu(SCMenu):
    __module__ = __name__

    def __init__(self, phase):
        SCMenu.__init__(self)
        if phase in JellybeanJamPhases:
            self.__messagesChanged(phase)
        else:
            print 'warning: tried to add Jellybean Jam phase %s which does not seem to exist' % phase

    def destroy(self):
        SCMenu.destroy(self)

    def clearMenu(self):
        SCMenu.clearMenu(self)

    def __messagesChanged(self, phase):
        self.clearMenu()
        try:
            lt = base.localAvatar
        except:
            return

        for section in JellybeanJamMenu:
            if section[0] == -1:
                for phrase in section[1]:
                    if phrase not in OTPLocalizer.SpeedChatStaticText:
                        print 'warning: tried to link Jellybean Jam phrase %s which does not seem to exist' % phrase
                        break
                    self.append(SCStaticTextTerminal(phrase))

            else:
                menu = SCMenu()
                for phrase in section[1]:
                    if phrase not in OTPLocalizer.SpeedChatStaticText:
                        print 'warning: tried to link Jellybean Jam phrase %s which does not seem to exist' % phrase
                        break
                    menu.append(SCStaticTextTerminal(phrase))

                menuName = str(section[0])
                self.append(SCMenuHolder(menuName, menu))