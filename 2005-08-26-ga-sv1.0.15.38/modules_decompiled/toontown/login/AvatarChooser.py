# File: A (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase import ToontownGlobals
from direct.showbase import PandaObject
import AvatarChoice
from direct.fsm import StateData
from direct.fsm import ClassicFSM
from direct.fsm import State
from toontown.launcher import DownloadForceAcknowledge
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer
from direct.directnotify import DirectNotifyGlobal
import whrandom
MAX_AVATARS = 6
POSITIONS = (Vec3(-0.81999999999999995, 0, 0.34999999999999998), Vec3(0, 0, 0.34999999999999998), Vec3(0.81999999999999995, 0, 0.34999999999999998), Vec3(-0.81999999999999995, 0, -0.46999999999999997), Vec3(0, 0, -0.46999999999999997), Vec3(0.81999999999999995, 0, -0.46999999999999997))
COLORS = (Vec4(0.91700000000000004, 0.16400000000000001, 0.16400000000000001, 1), Vec4(0.152, 0.75, 0.25800000000000001, 1), Vec4(0.59799999999999998, 0.40200000000000002, 0.875, 1), Vec4(0.13300000000000001, 0.58999999999999997, 0.97699999999999998, 1), Vec4(0.89500000000000002, 0.34799999999999998, 0.60199999999999998, 1), Vec4(0.97699999999999998, 0.81599999999999995, 0.13300000000000001, 1))
chooser_notify = DirectNotifyGlobal.directNotify.newCategory('AvatarChooser')

class AvatarChooser(PandaObject.PandaObject, StateData.StateData):
    
    def __init__(self, avatarList, parentFSM, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.choice = None
        self.avatarList = avatarList
        self.fsm = ClassicFSM.ClassicFSM('AvatarChooser', [
            State.State('Choose', self.enterChoose, self.exitChoose, [
                'CheckDownload']),
            State.State('CheckDownload', self.enterCheckDownload, self.exitCheckDownload, [
                'Choose'])], 'Choose', 'Choose')
        self.fsm.enterInitialState()
        self.parentFSM = parentFSM
        self.parentFSM.getCurrentState().addChild(self.fsm)

    
    def enter(self):
        if self.isLoaded == 0:
            self.load()
        
        base.disableMouse()
        self.title.reparentTo(aspect2d)
        self.quitButton.show()
        if base.cr.loginInterface.supportsRelogin():
            self.logoutButton.show()
        
        self.pickAToonBG.reparentTo(base.camera)
        choice = base.config.GetInt('auto-avatar-choice', -1)
        for panel in self.panelList:
            panel.show()
            self.accept(panel.doneEvent, self._AvatarChooser__handlePanelDone)
            if panel.position == choice and panel.mode == AvatarChoice.AvatarChoice.MODE_CHOOSE:
                self._AvatarChooser__handlePanelDone('chose', panelChoice = choice)
            
        

    
    def exit(self):
        if self.isLoaded == 0:
            return None
        
        for panel in self.panelList:
            panel.hide()
        
        self.ignoreAll()
        self.title.reparentTo(hidden)
        self.quitButton.hide()
        self.logoutButton.hide()
        self.pickAToonBG.reparentTo(hidden)

    
    def load(self, isPaid):
        if self.isLoaded == 1:
            return None
        
        self.isPaid = isPaid
        gui = loader.loadModelOnce('phase_3/models/gui/pick_a_toon_gui')
        gui2 = loader.loadModelOnce('phase_3/models/gui/quit_button')
        self.pickAToonBG = gui.find('**/av-chooser_FnlBG')
        self.pickAToonBG.reparentTo(hidden)
        self.pickAToonBG.setPos(0.0, 2.73, 0.0)
        self.pickAToonBG.setScale(1, 1, 1)
        self.title = OnscreenText(TTLocalizer.AvatarChooserPickAToon, scale = 0.125, parent = hidden, font = ToontownGlobals.getSignFont(), fg = (1, 0.90000000000000002, 0.10000000000000001, 1), pos = (0.0, 0.81999999999999995))
        self.quitButton = DirectButton(image = (gui.find('**/QuitBtn_UP'), gui.find('**/QuitBtn_DN'), gui.find('**/QuitBtn_RLVR')), relief = None, text = TTLocalizer.AvatarChooserQuit, text_font = ToontownGlobals.getSignFont(), text0_fg = (0.152, 0.75, 0.25800000000000001, 1), text1_fg = (0.152, 0.75, 0.25800000000000001, 1), text2_fg = (0.97699999999999998, 0.81599999999999995, 0.13300000000000001, 1), text_pos = (0, -0.035000000000000003), text_scale = 0.10000000000000001, scale = 1.05, pos = (0, 0, -0.92400000000000004), command = self._AvatarChooser__handleQuit)
        self.logoutButton = DirectButton(relief = None, image = (gui2.find('**/QuitBtn_UP'), gui2.find('**/QuitBtn_DN'), gui2.find('**/QuitBtn_RLVR')), image_scale = 1.1499999999999999, text = TTLocalizer.OptionsPageLogout, text_font = ToontownGlobals.getSignFont(), text0_fg = (0.152, 0.75, 0.25800000000000001, 1), text1_fg = (0.152, 0.75, 0.25800000000000001, 1), text2_fg = (0.97699999999999998, 0.81599999999999995, 0.13300000000000001, 1), text_scale = 0.10000000000000001, text_pos = (0, -0.035000000000000003), pos = (1.105, 0, -0.92400000000000004), scale = 0.5, command = self._AvatarChooser__handleLogoutWithoutConfirm)
        self.logoutButton.hide()
        gui.removeNode()
        gui2.removeNode()
        self.panelList = []
        used_position_indexs = []
        if base.cr.isPaid():
            okToLockout = 0
        else:
            okToLockout = 1
            for avatar in self.avatarList:
                if avatar.position != AvatarChoice.AvatarChoice.TRIALER_OPEN_POS:
                    okToLockout = 0
                    break
                
            
        for av in self.avatarList:
            panel = AvatarChoice.AvatarChoice(av, position = av.position, paid = isPaid, okToLockout = okToLockout)
            panel.setPos(POSITIONS[av.position])
            panel['image_color'] = COLORS[av.position]
            used_position_indexs.append(av.position)
            self.panelList.append(panel)
        
        for panelNum in range(0, MAX_AVATARS):
            if panelNum not in used_position_indexs:
                panel = AvatarChoice.AvatarChoice(position = panelNum, okToLockout = okToLockout)
                panel.setPos(POSITIONS[panelNum])
                panel['image_color'] = COLORS[panelNum]
                self.panelList.append(panel)
            
        
        if len(self.avatarList) > 0:
            self.initLookAtInfo()
        
        self.isLoaded = 1

    
    def getLookAtPosition(self, toonHead, toonidx):
        lookAtChoice = whrandom.random()
        if len(self.used_panel_indexs) == 1:
            lookFwdPercent = 0.33000000000000002
            lookAtOthersPercent = 0
        else:
            lookFwdPercent = 0.20000000000000001
            if len(self.used_panel_indexs) == 2:
                lookAtOthersPercent = 0.40000000000000002
            else:
                lookAtOthersPercent = 0.65000000000000002
        lookRandomPercent = 1.0 - lookFwdPercent - lookAtOthersPercent
        if lookAtChoice < lookFwdPercent:
            self.IsLookingAt[toonidx] = 'f'
            return Vec3(0, 1.5, 0)
        elif lookAtChoice < lookRandomPercent + lookFwdPercent or len(self.used_panel_indexs) == 1:
            self.IsLookingAt[toonidx] = 'r'
            return toonHead.getRandomForwardLookAtPoint()
        else:
            other_toon_idxs = []
            for i in range(len(self.IsLookingAt)):
                if self.IsLookingAt[i] == toonidx:
                    other_toon_idxs.append(i)
                
            
            if len(other_toon_idxs) == 1:
                IgnoreStarersPercent = 0.40000000000000002
            else:
                IgnoreStarersPercent = 0.20000000000000001
            NoticeStarersPercent = 0.5
            bStareTargetTurnsToMe = 0
            if len(other_toon_idxs) == 0 or whrandom.random() < IgnoreStarersPercent:
                other_toon_idxs = []
                for i in self.used_panel_indexs:
                    if i != toonidx:
                        other_toon_idxs.append(i)
                    
                
                if whrandom.random() < NoticeStarersPercent:
                    bStareTargetTurnsToMe = 1
                
            
            if len(other_toon_idxs) == 0:
                return toonHead.getRandomForwardLookAtPoint()
            else:
                lookingAtIdx = whrandom.choice(other_toon_idxs)
            if bStareTargetTurnsToMe:
                self.IsLookingAt[lookingAtIdx] = toonidx
                otherToonHead = None
                for panel in self.panelList:
                    if panel.position == lookingAtIdx:
                        otherToonHead = panel.headModel
                    
                
                otherToonHead.doLookAroundToStareAt(otherToonHead, self.getLookAtToPosVec(lookingAtIdx, toonidx))
            
            self.IsLookingAt[toonidx] = lookingAtIdx
            return self.getLookAtToPosVec(toonidx, lookingAtIdx)

    
    def getLookAtToPosVec(self, fromIdx, toIdx):
        x = -(POSITIONS[toIdx][0] - POSITIONS[fromIdx][0])
        y = POSITIONS[toIdx][1] - POSITIONS[fromIdx][1]
        z = POSITIONS[toIdx][2] - POSITIONS[fromIdx][2]
        return Vec3(x, y, z)

    
    def initLookAtInfo(self):
        self.used_panel_indexs = []
        for panel in self.panelList:
            if panel.dna != None:
                self.used_panel_indexs.append(panel.position)
            
        
        if len(self.used_panel_indexs) == 0:
            return None
        
        self.IsLookingAt = []
        for i in range(MAX_AVATARS):
            self.IsLookingAt.append('f')
        
        for panel in self.panelList:
            if panel.dna != None:
                panel.headModel.setLookAtPositionCallbackArgs((self, panel.headModel, panel.position))
            
        

    
    def unload(self):
        if self.isLoaded == 0:
            return None
        
        cleanupDialog('globalDialog')
        for panel in self.panelList:
            panel.destroy()
        
        del self.panelList
        self.title.removeNode()
        del self.title
        self.quitButton.destroy()
        del self.quitButton
        self.logoutButton.destroy()
        del self.logoutButton
        self.pickAToonBG.removeNode()
        del self.pickAToonBG
        del self.avatarList
        self.parentFSM.getCurrentState().removeChild(self.fsm)
        del self.parentFSM
        del self.fsm
        self.ignoreAll()
        self.isLoaded = 0
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()

    
    def _AvatarChooser__handlePanelDone(self, panelDoneStatus, panelChoice = 0):
        self.doneStatus = { }
        self.doneStatus['mode'] = panelDoneStatus
        self.choice = panelChoice
        if panelDoneStatus == 'chose':
            self._AvatarChooser__handleChoice()
        elif panelDoneStatus == 'nameIt':
            self._AvatarChooser__handleCreate()
        elif panelDoneStatus == 'delete':
            self._AvatarChooser__handleDelete()
        elif panelDoneStatus == 'create':
            self._AvatarChooser__handleCreate()
        

    
    def getChoice(self):
        return self.choice

    
    def _AvatarChooser__handleChoice(self):
        self.fsm.request('CheckDownload')

    
    def _AvatarChooser__handleCreate(self):
        
        def sendDoneTask(task):
            messenger.send(task.doneEvent, [
                task.doneStatus])
            return Task.done

        sdt = Task.Task(sendDoneTask)
        sdt.doneEvent = self.doneEvent
        sdt.doneStatus = self.doneStatus
        base.transitions.fadeOutTask(sdt)

    
    def _AvatarChooser__handleDelete(self):
        messenger.send(self.doneEvent, [
            self.doneStatus])

    
    def _AvatarChooser__handleQuit(self):
        cleanupDialog('globalDialog')
        self.doneStatus = {
            'mode': 'exit' }
        messenger.send(self.doneEvent, [
            self.doneStatus])

    
    def enterChoose(self):
        pass

    
    def exitChoose(self):
        pass

    
    def enterCheckDownload(self):
        self.accept('downloadAck-response', self._AvatarChooser__handleDownloadAck)
        self.downloadAck = DownloadForceAcknowledge.DownloadForceAcknowledge('downloadAck-response')
        self.downloadAck.enter(4)

    
    def exitCheckDownload(self):
        self.downloadAck.exit()
        self.downloadAck = None
        self.ignore('downloadAck-response')

    
    def _AvatarChooser__handleDownloadAck(self, doneStatus):
        
        def sendDoneTask(task):
            messenger.send(task.doneEvent, [
                task.doneStatus])
            return Task.done

        if doneStatus['mode'] == 'complete':
            sdt = Task.Task(sendDoneTask)
            sdt.doneEvent = self.doneEvent
            sdt.doneStatus = self.doneStatus
            base.transitions.fadeOutTask(sdt)
        else:
            self.fsm.request('Choose')

    
    def _AvatarChooser__handleLogoutWithoutConfirm(self):
        base.cr.loginFSM.request('login')


