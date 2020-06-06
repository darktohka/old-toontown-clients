# File: D (Python 2.2)

from ShowBaseGlobal import *
from PandaModules import NodePath
import DistributedObject
import Task

class DistributedNode(DistributedObject.DistributedObject, NodePath):
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedNode_initialized = 1
            DistributedObject.DistributedObject.__init__(self, cr)

        return None

    
    def disable(self):
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

    
    def __cmp__(self, other):
        if self is other:
            return 0
        else:
            return 1

    
    def b_setParent(self, parentToken):
        self.setParent(parentToken)
        self.d_setParent(parentToken)
        return None

    
    def d_setParent(self, parentToken):
        self.sendUpdate('setParent', [
            parentToken])
        return None

    
    def setParent(self, parentToken):
        return self.do_setParent(parentToken)

    
    def do_setParent(self, parentToken):
        if not self.isDisabled():
            parent = self.cr.token2nodePath[parentToken]
            self.wrtReparentTo(parent)
        
        return None

    
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


