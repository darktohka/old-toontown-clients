# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from pandac.PandaModules import NodePath
import DistributedObject
from direct.task import Task
import types

class DistributedNode(DistributedObject.DistributedObject, NodePath):
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedNode_initialized = 1
            self.gotStringParentToken = 0
            DistributedObject.DistributedObject.__init__(self, cr)

        return None

    
    def disable(self):
        if self.activeState != DistributedObject.ESDisabled:
            self.reparentTo(hidden)
            DistributedObject.DistributedObject.disable(self)
        

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedNode_deleted = 1
            if not self.isEmpty():
                self.removeNode()
            
            DistributedObject.DistributedObject.delete(self)


    
    def generate(self):
        DistributedObject.DistributedObject.generate(self)
        self.gotStringParentToken = 0

    
    def __cmp__(self, other):
        if self is other:
            return 0
        else:
            return 1

    
    def b_setParent(self, parentToken):
        if type(parentToken) == types.StringType:
            self.setParentStr(parentToken)
        else:
            self.setParent(parentToken)
        self.d_setParent(parentToken)

    
    def d_setParent(self, parentToken):
        if type(parentToken) == types.StringType:
            self.sendUpdate('setParentStr', [
                parentToken])
        else:
            self.sendUpdate('setParent', [
                parentToken])

    
    def setParentStr(self, parentTokenStr):
        self.do_setParent(parentTokenStr)
        if len(parentTokenStr) > 0:
            self.gotStringParentToken = 1
        

    
    def setParent(self, parentToken):
        if not self.isGenerated():
            pass
        justGotRequiredParentAsStr = self.gotStringParentToken
        if not justGotRequiredParentAsStr:
            self.do_setParent(parentToken)
        
        self.gotStringParentToken = 0

    
    def do_setParent(self, parentToken):
        if not self.isDisabled():
            self.cr.parentMgr.requestReparent(self, parentToken)
        

    
    def d_setX(self, x):
        self.sendUpdate('setX', [
            x])

    
    def d_setY(self, y):
        self.sendUpdate('setY', [
            y])

    
    def d_setZ(self, z):
        self.sendUpdate('setZ', [
            z])

    
    def d_setH(self, h):
        self.sendUpdate('setH', [
            h])

    
    def d_setP(self, p):
        self.sendUpdate('setP', [
            p])

    
    def d_setR(self, r):
        self.sendUpdate('setR', [
            r])

    
    def setXY(self, x, y):
        self.setX(x)
        self.setY(y)

    
    def d_setXY(self, x, y):
        self.sendUpdate('setXY', [
            x,
            y])

    
    def setXZ(self, x, z):
        self.setX(x)
        self.setZ(z)

    
    def d_setXZ(self, x, z):
        self.sendUpdate('setXZ', [
            x,
            z])

    
    def d_setPos(self, x, y, z):
        self.sendUpdate('setPos', [
            x,
            y,
            z])

    
    def d_setHpr(self, h, p, r):
        self.sendUpdate('setHpr', [
            h,
            p,
            r])

    
    def setXYH(self, x, y, h):
        self.setX(x)
        self.setY(y)
        self.setH(h)

    
    def d_setXYH(self, x, y, h):
        self.sendUpdate('setXYH', [
            x,
            y,
            h])

    
    def setXYZH(self, x, y, z, h):
        self.setPos(x, y, z)
        self.setH(h)

    
    def d_setXYZH(self, x, y, z, h):
        self.sendUpdate('setXYZH', [
            x,
            y,
            z,
            h])

    
    def d_setPosHpr(self, x, y, z, h, p, r):
        self.sendUpdate('setPosHpr', [
            x,
            y,
            z,
            h,
            p,
            r])


