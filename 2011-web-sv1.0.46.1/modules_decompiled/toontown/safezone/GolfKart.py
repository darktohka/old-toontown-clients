# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\safezone\GolfKart.py
from pandac.PandaModules import *
from toontown.toonbase.ToonBaseGlobal import *
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.fsm import StateData
from toontown.toontowngui import TTDialog
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from direct.showbase import PythonUtil

class GolfKart(StateData.StateData):
    __module__ = __name__

    def __init__(self, safeZone, parentFSM, doneEvent, golfCourse):
        StateData.StateData.__init__(self, doneEvent)
        self.golfCourse = golfCourse
        self.fsm = ClassicFSM.ClassicFSM('GolfKart', [
         State.State('start', self.enterStart, self.exitStart, [
          'requestBoard', 'trolleyHFA', 'trolleyTFA']),
         State.State('trolleyHFA', self.enterTrolleyHFA, self.exitTrolleyHFA, [
          'final']),
         State.State('trolleyTFA', self.enterTrolleyTFA, self.exitTrolleyTFA, [
          'final']),
         State.State('requestBoard', self.enterRequestBoard, self.exitRequestBoard, [
          'boarding']),
         State.State('boarding', self.enterBoarding, self.exitBoarding, [
          'boarded']),
         State.State('boarded', self.enterBoarded, self.exitBoarded, [
          'requestExit', 'trolleyLeaving', 'final']),
         State.State('requestExit', self.enterRequestExit, self.exitRequestExit, [
          'exiting', 'trolleyLeaving']),
         State.State('trolleyLeaving', self.enterTrolleyLeaving, self.exitTrolleyLeaving, [
          'final']),
         State.State('exiting', self.enterExiting, self.exitExiting, [
          'final']),
         State.State('final', self.enterFinal, self.exitFinal, [
          'start'])], 'start', 'final')
        self.parentFSM = parentFSM
        return

    def load(self):
        self.parentFSM.getStateNamed('golfKartBlock').addChild(self.fsm)
        self.buttonModels = loader.loadModel('phase_3.5/models/gui/inventory_gui')
        self.upButton = self.buttonModels.find('**//InventoryButtonUp')
        self.downButton = self.buttonModels.find('**/InventoryButtonDown')
        self.rolloverButton = self.buttonModels.find('**/InventoryButtonRollover')

    def unload(self):
        self.parentFSM.getStateNamed('trolley').removeChild(self.fsm)
        del self.fsm
        del self.parentFSM
        self.buttonModels.removeNode()
        del self.buttonModels
        del self.upButton
        del self.downButton
        del self.rolloverButton

    def enter(self):
        self.fsm.enterInitialState()
        if base.localAvatar.hp > 0:
            messenger.send('enterGolfKartOK_%d' % self.golfCourse)
            self.fsm.request('requestBoard')
        else:
            self.fsm.request('trolleyHFA')
        return

    def exit(self):
        self.ignoreAll()
        return

    def enterStart(self):
        return

    def exitStart(self):
        return

    def enterTrolleyHFA(self):
        self.noTrolleyBox = TTDialog.TTGlobalDialog(message=TTLocalizer.TrolleyHFAMessage, doneEvent='noTrolleyAck', style=TTDialog.Acknowledge)
        self.noTrolleyBox.show()
        base.localAvatar.b_setAnimState('neutral', 1)
        self.accept('noTrolleyAck', self.__handleNoTrolleyAck)

    def exitTrolleyHFA(self):
        self.ignore('noTrolleyAck')
        self.noTrolleyBox.cleanup()
        del self.noTrolleyBox

    def enterTrolleyTFA(self):
        self.noTrolleyBox = TTDialog.TTGlobalDialog(message=TTLocalizer.TrolleyTFAMessage, doneEvent='noTrolleyAck', style=TTDialog.Acknowledge)
        self.noTrolleyBox.show()
        base.localAvatar.b_setAnimState('neutral', 1)
        self.accept('noTrolleyAck', self.__handleNoTrolleyAck)

    def exitTrolleyTFA(self):
        self.ignore('noTrolleyAck')
        self.noTrolleyBox.cleanup()
        del self.noTrolleyBox

    def __handleNoTrolleyAck(self):
        ntbDoneStatus = self.noTrolleyBox.doneStatus
        if ntbDoneStatus == 'ok':
            doneStatus = {}
            doneStatus['mode'] = 'reject'
            messenger.send(self.doneEvent, [doneStatus])
        else:
            self.notify.error('Unrecognized doneStatus: ' + str(ntbDoneStatus))

    def enterRequestBoard(self):
        return

    def handleRejectBoard(self):
        doneStatus = {}
        doneStatus['mode'] = 'reject'
        messenger.send(self.doneEvent, [doneStatus])

    def exitRequestBoard(self):
        return

    def enterBoarding(self, nodePath):
        camera.wrtReparentTo(nodePath)
        heading = PythonUtil.fitDestAngle2Src(camera.getH(nodePath), 180)
        self.cameraBoardTrack = LerpPosHprInterval(camera, 1.5, Point3(0, 18, 8), Point3(heading, -10, 0))
        self.cameraBoardTrack.start()
        return

    def exitBoarding(self):
        self.ignore('boardedTrolley')
        return

    def enterBoarded(self):
        self.enableExitButton()
        return

    def exitBoarded(self):
        self.cameraBoardTrack.finish()
        self.disableExitButton()
        return

    def enableExitButton(self):
        self.exitButton = DirectButton(relief=None, text=TTLocalizer.TrolleyHopOff, text_fg=(1,
                                                                                             1,
                                                                                             0.65,
                                                                                             1), text_pos=(0, -0.23), text_scale=0.8, image=(self.upButton, self.downButton, self.rolloverButton), image_color=(1,
                                                                                                                                                                                                                0,
                                                                                                                                                                                                                0,
                                                                                                                                                                                                                1), image_scale=(20,
                                                                                                                                                                                                                                 1,
                                                                                                                                                                                                                                 11), pos=(0,
                                                                                                                                                                                                                                           0,
                                                                                                                                                                                                                                           0.8), scale=0.15, command=lambda self=self: self.fsm.request('requestExit'))
        return

    def disableExitButton(self):
        self.exitButton.destroy()

    def enterRequestExit(self):
        messenger.send('trolleyExitButton')
        return

    def exitRequestExit(self):
        return

    def enterTrolleyLeaving(self):
        self.acceptOnce('playMinigame', self.handlePlayMinigame)
        self.acceptOnce('playGolf', self.handlePlayGolf)
        return

    def handlePlayMinigame(self, zoneId, minigameId):
        base.localAvatar.b_setParent(ToontownGlobals.SPHidden)
        doneStatus = {}
        doneStatus['mode'] = 'minigame'
        doneStatus['zoneId'] = zoneId
        doneStatus['minigameId'] = minigameId
        messenger.send(self.doneEvent, [doneStatus])

    def handlePlayGolf(self, zoneId, courseId):
        base.localAvatar.b_setParent(ToontownGlobals.SPHidden)
        doneStatus = {}
        doneStatus['mode'] = 'golfcourse'
        doneStatus['zoneId'] = zoneId
        doneStatus['courseId'] = courseId
        messenger.send(self.doneEvent, [doneStatus])

    def exitTrolleyLeaving(self):
        self.ignore('playMinigame')
        taskMgr.remove('leavingCamera')
        return

    def enterExiting(self):
        return

    def handleOffTrolley(self):
        doneStatus = {}
        doneStatus['mode'] = 'exit'
        messenger.send(self.doneEvent, [doneStatus])
        return

    def exitExiting(self):
        return

    def enterFinal(self):
        return

    def exitFinal(self):
        return