# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\classicchars\DistributedDonaldDockAI.py
from otp.ai.AIBaseGlobal import *
import DistributedCCharBaseAI
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.task import Task
import random, CharStateDatasAI
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer

class DistributedDonaldDockAI(DistributedCCharBaseAI.DistributedCCharBaseAI):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedDonaldDockAI')

    def __init__(self, air):
        DistributedCCharBaseAI.DistributedCCharBaseAI.__init__(self, air, TTLocalizer.DonaldDock)
        self.fsm = ClassicFSM.ClassicFSM('DistributedDonaldDockAI', [
         State.State('Off', self.enterOff, self.exitOff, [
          'Lonely', 'TransitionToCostume']),
         State.State('Lonely', self.enterLonely, self.exitLonely, [
          'Chatty', 'TransitionToCostume']),
         State.State('Chatty', self.enterChatty, self.exitChatty, [
          'Lonely', 'TransitionToCostume']),
         State.State('TransitionToCostume', self.enterTransitionToCostume, self.exitTransitionToCostume, [
          'Off'])], 'Off', 'Off')
        self.fsm.enterInitialState()
        self.handleHolidays()

    def delete(self):
        self.fsm.requestFinalState()
        DistributedCCharBaseAI.DistributedCCharBaseAI.delete(self)
        self.lonelyDoneEvent = None
        self.lonely = None
        self.chattyDoneEvent = None
        self.chatty = None
        return

    def generate(self):
        DistributedCCharBaseAI.DistributedCCharBaseAI.generate(self)
        self.lonelyDoneEvent = self.taskName('DonaldDock-lonely-done')
        self.lonely = CharStateDatasAI.CharLonelyStateAI(self.lonelyDoneEvent, self)
        self.chattyDoneEvent = self.taskName('DonaldDock-chatty-done')
        self.chatty = CharStateDatasAI.CharChattyStateAI(self.chattyDoneEvent, self)

    def start(self):
        self.fsm.request('Lonely')

    def __decideNextState(self, doneStatus):
        if doneStatus['state'] == 'lonely' and doneStatus['status'] == 'done':
            if len(self.nearbyAvatars) > 0:
                self.fsm.request('Chatty')
            else:
                self.fsm.request('Lonely')
        elif doneStatus['state'] == 'chatty' and doneStatus['status'] == 'done':
            self.fsm.request('Lonely')

    def enterOff(self):
        pass

    def exitOff(self):
        DistributedCCharBaseAI.DistributedCCharBaseAI.exitOff(self)

    def enterLonely(self):
        self.notify.debug('Entering Lonely')
        self.lonely.enter()
        self.acceptOnce(self.lonelyDoneEvent, self.__decideNextState)

    def exitLonely(self):
        self.notify.debug('Exiting Lonely')
        self.ignore(self.lonelyDoneEvent)
        self.lonely.exit()

    def enterChatty(self):
        self.notify.debug('Entering Chatty')
        self.chatty.enter()
        self.acceptOnce(self.chattyDoneEvent, self.__decideNextState)

    def exitChatty(self):
        self.notify.debug('Exiting Chatty')
        self.ignore(self.chattyDoneEvent)
        self.chatty.exit()

    def avatarEnterNextState(self):
        if len(self.nearbyAvatars) == 1:
            self.fsm.request('Chatty')
        else:
            self.notify.debug('avatarEnterNextState: num avatars: ' + str(len(self.nearbyAvatars)))

    def avatarExitNextState(self):
        if len(self.nearbyAvatars) == 0:
            self.fsm.request('Lonely')

    def enterTransitionToCostume(self):
        pass

    def exitTransitionToCostume(self):
        pass