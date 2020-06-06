# File: T (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase.ToontownBattleGlobals import *
from direct.directnotify import DirectNotifyGlobal
import string
from toontown.toon import LaffMeter
from toontown.battle import BattleBase
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer

class TownBattleToonPanel(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('TownBattleToonPanel')
    
    def __init__(self, id):
        gui = loader.loadModelOnce('phase_3.5/models/gui/battle_gui')
        DirectFrame.__init__(self, relief = None, image = gui.find('**/ToonBtl_Status_BG'), image_color = Vec4(0.5, 0.90000000000000002, 0.5, 0.69999999999999996))
        self.setScale(0.80000000000000004)
        self.initialiseoptions(TownBattleToonPanel)
        self.avatar = None
        self.sosText = DirectLabel(parent = self, relief = None, pos = (0.10000000000000001, 0, 0.014999999999999999), text = TTLocalizer.TownBattleToonSOS, text_scale = 0.059999999999999998)
        self.sosText.hide()
        self.undecidedText = DirectLabel(parent = self, relief = None, pos = (0.10000000000000001, 0, 0.014999999999999999), text = TTLocalizer.TownBattleUndecided, text_scale = 0.10000000000000001)
        self.healthText = DirectLabel(parent = self, text = '', pos = (-0.059999999999999998, 0, -0.074999999999999997), text_scale = 0.055)
        self.hpChangeEvent = None
        self.gagNode = self.attachNewNode('gag')
        self.gagNode.setPos(0.10000000000000001, 0, 0.029999999999999999)
        self.hasGag = 0
        self.laffMeter = None
        self.whichText = DirectLabel(parent = self, text = '', pos = (0.10000000000000001, 0, -0.080000000000000002), text_scale = 0.050000000000000003)
        self.hide()
        gui.removeNode()
        return None

    
    def setLaffMeter(self, avatar):
        self.notify.debug('setLaffMeter: new avatar %s' % avatar.doId)
        if self.avatar == avatar:
            messenger.send(self.avatar.uniqueName('hpChange'), [
                avatar.hp,
                avatar.maxHp,
                1])
            return None
        elif self.avatar:
            self.cleanupLaffMeter()
        
        self.avatar = avatar
        self.laffMeter = LaffMeter.LaffMeter(avatar.style, avatar.hp, avatar.maxHp)
        self.laffMeter.setAvatar(self.avatar)
        self.laffMeter.reparentTo(self)
        self.laffMeter.setPos(-0.059999999999999998, 0, 0.050000000000000003)
        self.laffMeter.setScale(0.044999999999999998)
        self.laffMeter.start()
        self.setHealthText(avatar.hp, avatar.maxHp)
        self.hpChangeEvent = self.avatar.uniqueName('hpChange')
        self.accept(self.hpChangeEvent, self.setHealthText)
        return None

    
    def setHealthText(self, hp, maxHp, quietly = 0):
        self.healthText['text'] = TTLocalizer.TownBattleHealthText % {
            'hitPoints': hp,
            'maxHit': maxHp }
        return None

    
    def show(self):
        DirectFrame.show(self)
        if self.laffMeter:
            self.laffMeter.start()
        
        return None

    
    def hide(self):
        DirectFrame.hide(self)
        if self.laffMeter:
            self.laffMeter.stop()
        
        return None

    
    def updateLaffMeter(self, hp):
        if self.laffMeter:
            self.laffMeter.adjustFace(hp, self.avatar.maxHp)
        
        self.setHealthText(hp, maxHp)
        return None

    
    def setValues(self, index, track, level = None, numTargets = None, targetIndex = None, localNum = None):
        self.notify.debug('Toon Panel setValues: index=%s track=%s level=%s numTargets=%s targetIndex=%s localNum=%s' % (index, track, level, numTargets, targetIndex, localNum))
        self.undecidedText.hide()
        self.sosText.hide()
        self.gagNode.hide()
        self.whichText.hide()
        if self.hasGag:
            self.gag.removeNode()
            self.hasGag = 0
        
        if track == BattleBase.NO_ATTACK or track == BattleBase.UN_ATTACK:
            self.undecidedText.show()
        elif track == BattleBase.SOS and track == BattleBase.NPCSOS or track == BattleBase.PETSOS:
            self.sosText.show()
        elif track >= MIN_TRACK_INDEX and track <= MAX_TRACK_INDEX:
            self.undecidedText.hide()
            self.gagNode.show()
            invButton = base.localAvatar.inventory.buttonLookup(track, level)
            self.gag = invButton.instanceUnderNode(self.gagNode, 'gag')
            self.gag.setScale(0.80000000000000004)
            self.gag.setPos(0, 0, 0.02)
            self.hasGag = 1
            if numTargets is not None and targetIndex is not None and localNum is not None:
                self.whichText.show()
                self.whichText['text'] = self.determineWhichText(numTargets, targetIndex, localNum, index)
            
        else:
            self.notify.error('Bad track value: %s' % track)
        return None

    
    def determineWhichText(self, numTargets, targetIndex, localNum, index):
        returnStr = ''
        targetList = range(numTargets)
        targetList.reverse()
        for i in targetList:
            if targetIndex == -1:
                returnStr += 'X'
            elif targetIndex == -2:
                if i == index:
                    returnStr += '-'
                else:
                    returnStr += 'X'
            elif targetIndex >= 0 and targetIndex <= 3:
                if i == targetIndex:
                    returnStr += 'X'
                else:
                    returnStr += '-'
            else:
                self.notify.error('Bad target index: %s' % targetIndex)
        
        return returnStr

    
    def cleanup(self):
        self.ignoreAll()
        self.cleanupLaffMeter()
        if self.hasGag:
            self.gag.removeNode()
            del self.gag
        
        self.gagNode.removeNode()
        del self.gagNode
        DirectFrame.destroy(self)

    
    def cleanupLaffMeter(self):
        self.notify.debug('Cleaning up laffmeter!')
        self.ignore(self.hpChangeEvent)
        if self.laffMeter:
            self.laffMeter.destroy()
            self.laffMeter = None
        
        return None


