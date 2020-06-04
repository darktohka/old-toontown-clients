# File: D (Python 2.2)

from pandac.PandaModules import *
from direct.distributed import DistributedNode
from direct.actor import DistributedActor
from otp.otpbase import OTPGlobals
import Avatar
import AvatarDNA
from otp.chat import ChatGarbler
from otp.chat import ChatManager
import string
from direct.task import Task
from otp.otpbase import OTPLocalizer
from otp.speedchat import SCDecoders
from direct.showbase import PythonUtil
import time

class DistributedAvatar(DistributedActor.DistributedActor, Avatar.Avatar):
    LaffNumberGenerator = TextNode('LaffNumberGenerator')
    LaffNumbersEnabled = 1
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedAvatar_initialized = 1
            Avatar.Avatar.__init__(self)
            DistributedActor.DistributedActor.__init__(self, cr)
            self.laffNumber = None
            self.hp = None
            self.maxHp = None


    
    def disable(self):
        self.reparentTo(hidden)
        self.removeActive()
        self.disableBodyCollisions()
        self.hideLaffNumber()
        self.hp = None
        DistributedActor.DistributedActor.disable(self)

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedAvatar_deleted = 1
            DistributedActor.DistributedActor.delete(self)
            Avatar.Avatar.delete(self)


    
    def generate(self):
        DistributedActor.DistributedActor.generate(self)
        if not self.isLocal():
            self.addActive()
            self.initializeBodyCollisions('distAvatarCollNode-' + str(self.doId))
            self.considerUnderstandable()
        
        self.setParent(OTPGlobals.SPHidden)
        self.setTag('avatarDoId', str(self.doId))

    
    def do_setParent(self, parentToken):
        if not self.isDisabled():
            if parentToken == OTPGlobals.SPHidden:
                self.nametag2dDist &= ~(Nametag.CName)
            else:
                self.nametag2dDist |= Nametag.CName
            self.nametag.getNametag2d().setContents(self.nametag2dContents & self.nametag2dDist)
            DistributedActor.DistributedActor.do_setParent(self, parentToken)
        

    
    def setHp(self, hitPoints, checkDied = 1):
        if self.hp != None:
            oldHp = max(self.hp, 0)
            newHp = max(hitPoints, 0)
            hpDisplayDelta = newHp - oldHp
            self.showLaffNumber(hpDisplayDelta)
        
        if hitPoints is not None and self.hp > 0:
            pass
        justRanOutOfHp = not hitPoints
        self.hp = hitPoints
        
        try:
            if self.hp != None and self.maxHp != None:
                messenger.send(self.uniqueName('hpChange'), [
                    self.hp,
                    self.maxHp])
            
            if oldHp <= 0 and newHp > 0:
                messenger.send(self.uniqueName('positiveHP'))
        except:
            pass

        if checkDied and justRanOutOfHp:
            self.died()
        

    
    def died(self):
        pass

    
    def getHp(self):
        return self.hp

    
    def setMaxHp(self, hitPoints):
        self.maxHp = hitPoints
        
        try:
            if self.hp != None and self.maxHp != None:
                messenger.send(self.uniqueName('hpChange'), [
                    self.hp,
                    self.maxHp])
        except AttributeError:
            pass

        if self.inventory:
            self.inventory.updateGUI()
        

    
    def getMaxHp(self):
        return self.maxHp

    
    def getName(self):
        return Avatar.Avatar.getName(self)

    
    def setName(self, name):
        
        try:
            self.node().setName('%s-%d' % (name, self.doId))
            self.gotName = 1
        except:
            pass

        return Avatar.Avatar.setName(self, name)

    
    def showLaffNumber(self, number, bonus = 0):
        if self.LaffNumbersEnabled and not (self.ghostMode):
            if number != 0:
                if self.laffNumber:
                    self.hideLaffNumber()
                
                self.LaffNumberGenerator.setFont(OTPGlobals.getSignFont())
                if number < 0:
                    self.LaffNumberGenerator.setText(str(number))
                else:
                    self.LaffNumberGenerator.setText('+' + str(number))
                self.LaffNumberGenerator.clearShadow()
                self.LaffNumberGenerator.setAlign(TextNode.ACenter)
                if bonus == 1:
                    r = 1.0
                    g = 1.0
                    b = 0
                    a = 1
                elif bonus == 2:
                    r = 1.0
                    g = 0.5
                    b = 0
                    a = 1
                elif number < 0:
                    r = 0.90000000000000002
                    g = 0
                    b = 0
                    a = 1
                else:
                    r = 0
                    g = 0.90000000000000002
                    b = 0
                    a = 1
                self.LaffNumberGenerator.setTextColor(r, g, b, a)
                self.laffNumberNode = self.LaffNumberGenerator.generate()
                self.laffNumber = self.attachNewNode(self.laffNumberNode)
                self.laffNumber.setBillboardPointEye()
                self.laffNumber.setBin('fixed', 100)
                self.laffNumber.setPos(0, 0, self.height / 2)
                seq = Task.sequence(self.laffNumber.lerpPos(Point3(0, 0, self.height + 1.5), 1.0, blendType = 'easeOut'), Task.pause(0.84999999999999998), self.laffNumber.lerpColor(Vec4(r, g, b, a), Vec4(r, g, b, 0), 0.10000000000000001), Task.Task(self.hideLaffNumberTask))
                taskMgr.add(seq, self.uniqueName('laffNumber'))
            
        

    
    def showLaffString(self, text, duration = 0.84999999999999998, scale = 0.69999999999999996):
        if self.LaffNumbersEnabled and not (self.ghostMode):
            if text != '':
                if self.laffNumber:
                    self.hideLaffNumber()
                
                self.LaffNumberGenerator.setFont(OTPGlobals.getSignFont())
                self.LaffNumberGenerator.setText(text)
                self.LaffNumberGenerator.clearShadow()
                self.LaffNumberGenerator.setAlign(TextNode.ACenter)
                r = 1.0
                a = 1.0
                g = 0.0
                b = 0.0
                self.LaffNumberGenerator.setTextColor(r, g, b, a)
                self.laffNumberNode = self.LaffNumberGenerator.generate()
                self.laffNumber = self.attachNewNode(self.laffNumberNode)
                self.laffNumber.setScale(scale)
                self.laffNumber.setBillboardAxis()
                self.laffNumber.setPos(0, 0, self.height / 2)
                seq = Task.sequence(self.laffNumber.lerpPos(Point3(0, 0, self.height + 1.5), 1.0, blendType = 'easeOut'), Task.pause(duration), self.laffNumber.lerpColor(Vec4(r, g, b, a), Vec4(r, g, b, 0), 0.10000000000000001), Task.Task(self.hideLaffNumberTask))
                taskMgr.add(seq, self.uniqueName('laffNumber'))
            
        

    
    def hideLaffNumberTask(self, task):
        self.hideLaffNumber()
        return Task.done

    
    def hideLaffNumber(self):
        if self.laffNumber:
            taskMgr.remove(self.uniqueName('laffNumber'))
            self.laffNumber.removeNode()
            self.laffNumber = None
        

    
    def getStareAtNodeAndOffset(self):
        return (self, Point3(0, 0, self.height))


