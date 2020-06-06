# File: P (Python 2.2)

from pandac.PandaModules import *
import Particles
import ForceGroup
from direct.directnotify import DirectNotifyGlobal

class ParticleEffect(NodePath):
    notify = DirectNotifyGlobal.directNotify.newCategory('ParticleEffect')
    pid = 1
    
    def __init__(self, name = None, particles = None):
        if name == None:
            name = 'particle-effect-%d' % ParticleEffect.pid
            ParticleEffect.pid += 1
        
        NodePath.__init__(self, name)
        self.name = name
        self.fEnabled = 0
        self.particlesDict = { }
        self.forceGroupDict = { }
        if particles != None:
            self.addParticles(particles)
        
        self.renderParent = None

    
    def start(self, parent = None, renderParent = None):
        self.renderParent = renderParent
        self.enable()
        if parent != None:
            self.reparentTo(parent)
        

    
    def cleanup(self):
        self.removeNode()
        self.disable()
        if hasattr(self, 'forceGroupDict'):
            for f in self.forceGroupDict.values():
                f.cleanup()
            
            del self.forceGroupDict
        
        if hasattr(self, 'particlesDict'):
            for p in self.particlesDict.values():
                p.cleanup()
            
            del self.particlesDict
        
        del self.renderParent

    
    def reset(self):
        self.removeAllForces()
        self.removeAllParticles()
        self.forceGroupDict = { }
        self.particlesDict = { }

    
    def enable(self):
        if hasattr(self, 'forceGroupDict') and hasattr(self, 'particlesDict'):
            if self.renderParent != None:
                for p in self.particlesDict.values():
                    p.setRenderParent(self.renderParent.node())
                
            
            for f in self.forceGroupDict.values():
                f.enable()
            
            for p in self.particlesDict.values():
                p.enable()
            
            self.fEnabled = 1
        

    
    def disable(self):
        self.detachNode()
        for p in self.particlesDict.values():
            p.setRenderParent(p.node)
        
        for f in self.forceGroupDict.values():
            f.disable()
        
        for p in self.particlesDict.values():
            p.disable()
        
        self.fEnabled = 0

    
    def isEnabled(self):
        return self.fEnabled

    
    def addForceGroup(self, forceGroup):
        forceGroup.nodePath.reparentTo(self)
        forceGroup.particleEffect = self
        self.forceGroupDict[forceGroup.getName()] = forceGroup
        for i in range(len(forceGroup)):
            self.addForce(forceGroup[i])
        

    
    def addForce(self, force):
        for p in self.particlesDict.values():
            p.addForce(force)
        

    
    def removeForceGroup(self, forceGroup):
        for i in range(len(forceGroup)):
            self.removeForce(forceGroup[i])
        
        forceGroup.nodePath.removeNode()
        forceGroup.particleEffect = None
        del self.forceGroupDict[forceGroup.getName()]

    
    def removeForce(self, force):
        for p in self.particlesDict.values():
            p.removeForce(force)
        

    
    def removeAllForces(self):
        for fg in self.forceGroupDict.values():
            self.removeForceGroup(fg)
        

    
    def addParticles(self, particles):
        particles.nodePath.reparentTo(self)
        self.particlesDict[particles.getName()] = particles
        for fg in self.forceGroupDict.values():
            for i in range(len(fg)):
                particles.addForce(fg[i])
            
        

    
    def removeParticles(self, particles):
        if particles == None:
            self.notify.warning('removeParticles() - particles == None!')
            return None
        
        particles.nodePath.detachNode()
        del self.particlesDict[particles.getName()]
        for fg in self.forceGroupDict.values():
            for f in fg.asList():
                particles.removeForce(f)
            
        

    
    def removeAllParticles(self):
        for p in self.particlesDict.values():
            self.removeParticles(p)
        

    
    def getParticlesList(self):
        return self.particlesDict.values()

    
    def getParticlesNamed(self, name):
        return self.particlesDict.get(name, None)

    
    def getParticlesDict(self):
        return self.particlesDict

    
    def getForceGroupList(self):
        return self.forceGroupDict.values()

    
    def getForceGroupNamed(self, name):
        return self.forceGroupDict.get(name, None)

    
    def getForceGroupDict(self):
        return self.forceGroupDict

    
    def saveConfig(self, filename):
        f = open(filename.toOsSpecific(), 'wb')
        f.write('\n')
        f.write('self.reset()\n')
        pos = self.getPos()
        hpr = self.getHpr()
        scale = self.getScale()
        f.write('self.setPos(%0.3f, %0.3f, %0.3f)\n' % (pos[0], pos[1], pos[2]))
        f.write('self.setHpr(%0.3f, %0.3f, %0.3f)\n' % (hpr[0], hpr[1], hpr[2]))
        f.write('self.setScale(%0.3f, %0.3f, %0.3f)\n' % (scale[0], scale[1], scale[2]))
        num = 0
        for p in self.particlesDict.values():
            target = 'p%d' % num
            num = num + 1
            f.write(target + " = Particles.Particles('%s')\n" % p.getName())
            p.printParams(f, target)
            f.write('self.addParticles(%s)\n' % target)
        
        num = 0
        for fg in self.forceGroupDict.values():
            target = 'f%d' % num
            num = num + 1
            f.write(target + " = ForceGroup.ForceGroup('%s')\n" % fg.getName())
            fg.printParams(f, target)
            f.write('self.addForceGroup(%s)\n' % target)
        
        f.close()

    
    def loadConfig(self, filename):
        
        try:
            if vfs:
                exec vfs.readFile(filename)
            else:
                execfile(filename.toOsSpecific())
        except:
            self.notify.error('loadConfig: failed to load particle file: ' + repr(filename))



