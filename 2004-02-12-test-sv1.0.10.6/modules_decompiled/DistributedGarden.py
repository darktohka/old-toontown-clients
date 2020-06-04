# File: D (Python 2.2)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
from DirectGui import *
from ClockDelta import *
import ToontownGlobals
import DistributedObject
import DirectNotifyGlobal
import FSM
import State
import AvatarDNA
import Toon
import RandomNumGen
import Localizer
import random
import whrandom
import cPickle
import DelayDelete
import PythonUtil
import Place
import Estate
import HouseGlobals

class DistributedGarden(DistributedObject.DistributedObject):
    notify = directNotify.newCategory('DistributedGarden')
    
    def __init__(self, cr):
        self.notify.debug('init')
        DistributedObject.DistributedObject.__init__(self, cr)
        self.lt = toonbase.localToon
        self.props = []
        self.pos = None
        self.radius = 0
        self.gridCells = 20
        self.propTable = [
            None] * self.gridCells
        for i in range(len(self.propTable)):
            self.propTable[i] = [
                None] * self.gridCells
        
        self.dx = 1.0 / self.gridCells
        self.occupied = []

    
    def generate(self):
        DistributedObject.DistributedObject.generate(self)

    
    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)

    
    def disable(self):
        pass

    
    def unload(self):
        pass

    
    def delete(self):
        for prop in self.props:
            prop[0].removeNode()
            del prop[0]
            del prop
        
        del self.props
        self.props = None
        self.unload()

    
    def sendNewProp(self, prop, x, y, z):
        self.notify.debug('sendNewProp')
        print 'new prop (%d) = %s,%s,%s' % (prop, x, y, z)
        if prop == HouseGlobals.PROP_ICECUBE:
            model = loader.loadModel('phase_8/models/props/icecube.bam')
        elif prop == HouseGlobals.PROP_FLOWER:
            model = loader.loadModel('phase_8/models/props/flower_treasure.bam')
        elif prop == HouseGlobals.PROP_SNOWFLAKE:
            model = loader.loadModel('phase_8/models/props/snowflake_treasure.bam')
        
        model.reparentTo(hidden)
        model.setPos(x, y, z)
        model.setScale(0.20000000000000001)
        model.setBillboardPointEye()
        model.reparentTo(render)
        self.props.append([
            model,
            x,
            y,
            z])

    
    def getPropPos(self, i, j):
        pos = [
            (self.pos[0] - self.radius) + 2 * self.radius * i,
            (self.pos[1] - self.radius) + 2 * self.radius * j,
            self.pos[2]]
        return pos

    
    def loadProp(self, prop, i, j):
        pos = self.getPropPos(i, j)
        if prop == HouseGlobals.PROP_ICECUBE:
            model = loader.loadModel('phase_8/models/props/icecube.bam')
        elif prop == HouseGlobals.PROP_FLOWER:
            model = loader.loadModel('phase_8/models/props/flower_treasure.bam')
        elif prop == HouseGlobals.PROP_SNOWFLAKE:
            model = loader.loadModel('phase_8/models/props/snowflake_treasure.bam')
        else:
            self.notify.error('cant find prop: %s' % prop)
        model.reparentTo(hidden)
        model.setPos(pos[0], pos[1], pos[2])
        model.setScale(0.20000000000000001)
        model.setBillboardPointEye()
        model.reparentTo(render)

    
    def setAddProp(self, prop, i, j):
        self.notify.debug('addProp')
        self.props.append([
            prop,
            i,
            j])
        self.loadProp(prop, i, j)
        self.b_setProps(self, props)

    
    def b_setProps(self, props):
        self.notify.debug('b_setProps')
        self.setProps(props)
        self.d_setProps(props)

    
    def d_setProps(self, props):
        self.notify.debug('d_setProps')
        aProps = []
        for prop in props:
            aProps = aProps + prop
        
        self.sendUpdate('setProps', [
            aProps])

    
    def setProps(self, props):
        self.notify.debug('setProps')
        self.props = props
        for prop in self.props:
            (pInd, i, j) = prop
            self.propTable[(i, j)] = pInd
        


