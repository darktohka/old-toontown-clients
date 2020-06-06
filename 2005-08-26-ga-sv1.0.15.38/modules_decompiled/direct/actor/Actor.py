# File: A (Python 2.2)

from direct.showbase.PandaObject import *
from pandac import LODNode
import types

class Actor(PandaObject, NodePath):
    notify = directNotify.newCategory('Actor')
    partPrefix = '__Actor_'
    
    def __init__(self, models = None, anims = None, other = None):
        
        try:
            return None
        except:
            self.Actor_initialized = 1

        NodePath.__init__(self)
        self._Actor__partBundleDict = { }
        self._Actor__animControlDict = { }
        self._Actor__controlJoints = { }
        self._Actor__LODNode = None
        if other == None:
            self.gotName = 0
            root = ModelNode('actor')
            root.setPreserveTransform(1)
            self.assign(NodePath(root))
            self.setGeomNode(self.attachNewNode(ModelNode('actorGeom')))
            self._Actor__hasLOD = 0
            if models:
                if type(models) == type({ }):
                    if type(models[models.keys()[0]]) == type({ }):
                        self.setLODNode()
                        sortedKeys = models.keys()
                        sortedKeys.sort()
                        for lodName in sortedKeys:
                            self.addLOD(str(lodName))
                            for modelName in models[lodName].keys():
                                self.loadModel(models[lodName][modelName], modelName, lodName)
                            
                        
                    elif type(anims[anims.keys()[0]]) == type({ }):
                        for partName in models.keys():
                            self.loadModel(models[partName], partName)
                        
                    else:
                        self.setLODNode()
                        sortedKeys = models.keys()
                        sortedKeys.sort()
                        for lodName in sortedKeys:
                            self.addLOD(str(lodName))
                            self.loadModel(models[lodName], lodName = lodName)
                        
                else:
                    self.loadModel(models)
            
            if anims:
                if len(anims) >= 1:
                    if type(anims[anims.keys()[0]]) == type({ }):
                        if type(models) == type({ }):
                            if type(models[models.keys()[0]]) == type({ }):
                                sortedKeys = models.keys()
                                sortedKeys.sort()
                                for lodName in sortedKeys:
                                    for partName in anims.keys():
                                        self.loadAnims(anims[partName], partName, lodName)
                                    
                                
                            else:
                                for partName in anims.keys():
                                    self.loadAnims(anims[partName], partName)
                                
                        
                    elif type(models) == type({ }):
                        sortedKeys = models.keys()
                        sortedKeys.sort()
                        for lodName in sortedKeys:
                            self.loadAnims(anims, lodName = lodName)
                        
                    else:
                        self.loadAnims(anims)
                
            
        else:
            otherCopy = other.copyTo(hidden)
            otherCopy.detachNode()
            self.gotName = other.gotName
            self.assign(otherCopy)
            self.setGeomNode(otherCopy.getChild(0))
            self._Actor__copyPartBundles(other)
            self._Actor__copyAnimControls(other)
        self._Actor__geomNode.node().setFinal(1)

    
    def delete(self):
        
        try:
            return None
        except:
            self.Actor_deleted = 1
            self.cleanup()


    
    def __cmp__(self, other):
        if self is other:
            return 0
        else:
            return 1

    
    def __str__(self):
        return 'Actor: partBundleDict = %s,\n animControlDict = %s' % (self._Actor__partBundleDict, self._Actor__animControlDict)

    
    def getActorInfo(self):
        lodInfo = []
        for lodName in self._Actor__animControlDict.keys():
            partDict = self._Actor__animControlDict[lodName]
            partInfo = []
            for partName in partDict.keys():
                partBundle = self._Actor__partBundleDict[lodName][partName]
                animDict = partDict[partName]
                animInfo = []
                for animName in animDict.keys():
                    file = animDict[animName][0]
                    animControl = animDict[animName][1]
                    animInfo.append([
                        animName,
                        file,
                        animControl])
                
                partInfo.append([
                    partName,
                    partBundle,
                    animInfo])
            
            lodInfo.append([
                lodName,
                partInfo])
        
        return lodInfo

    
    def getAnimNames(self):
        animNames = []
        for (lodName, lodInfo) in self.getActorInfo():
            for (partName, bundle, animInfo) in lodInfo:
                for (animName, file, animControl) in animInfo:
                    if animName not in animNames:
                        animNames.append(animName)
                    
                
            
        
        return animNames

    
    def pprint(self):
        for (lodName, lodInfo) in self.getActorInfo():
            print 'LOD:', lodName
            for (partName, bundle, animInfo) in lodInfo:
                print '  Part:', partName
                print '  Bundle:', `bundle`
                for (animName, file, animControl) in animInfo:
                    print '    Anim:', animName
                    print '      File:', file
                    if animControl == None:
                        print ' (not loaded)'
                    else:
                        print '      NumFrames: %d PlayRate: %0.2f' % (animControl.getNumFrames(), animControl.getPlayRate())
                
            
        

    
    def cleanup(self):
        self.stop()
        self._Actor__partBundleDict = { }
        self._Actor__animControlDict = { }
        self._Actor__controlJoints = { }
        self._Actor__geomNode.removeNode()
        if self._Actor__LODNode:
            self._Actor__LODNode.removeNode()
            self._Actor__LODNode = None
        
        self._Actor__hasLOD = 0
        if not self.isEmpty():
            self.removeNode()
        

    
    def getAnimControlDict(self):
        return self._Actor__animControlDict

    
    def getPartBundleDict(self):
        return self._Actor__partBundleDict

    
    def getLODNames(self):
        lodNames = self._Actor__partBundleDict.keys()
        lodNames.sort(lambda x, y: cmp(int(y), int(x)))
        return lodNames

    
    def getPartNames(self):
        return self._Actor__partBundleDict.values()[0].keys()

    
    def getGeomNode(self):
        return self._Actor__geomNode

    
    def setGeomNode(self, node):
        self._Actor__geomNode = node

    
    def getLODNode(self):
        return self._Actor__LODNode.node()

    
    def setLODNode(self, node = None):
        if node == None:
            lod = LODNode.LODNode('lod')
            self._Actor__LODNode = self._Actor__geomNode.attachNewNode(lod)
        else:
            self._Actor__LODNode = self._Actor__geomNode.attachNewNode(node)
        self._Actor__hasLOD = 1
        self.switches = { }

    
    def useLOD(self, lodName):
        self.resetLOD()
        sortedKeys = self.switches.keys()
        sortedKeys.sort()
        for eachLod in sortedKeys:
            index = sortedKeys.index(eachLod)
            self._Actor__LODNode.node().setSwitch(index, 0, 10000)
        
        index = sortedKeys.index(lodName)
        self._Actor__LODNode.node().setSwitch(index, 10000, 0)

    
    def printLOD(self):
        sortedKeys = self.switches.keys()
        sortedKeys.sort()
        for eachLod in sortedKeys:
            print 'python switches for %s: in: %d, out %d' % (eachLod, self.switches[eachLod][0], self.switches[eachLod][1])
        
        switchNum = self._Actor__LODNode.node().getNumSwitches()
        for eachSwitch in range(0, switchNum):
            print 'c++ switches for %d: in: %d, out: %d' % (eachSwitch, self._Actor__LODNode.node().getIn(eachSwitch), self._Actor__LODNode.node().getOut(eachSwitch))
        

    
    def resetLOD(self):
        sortedKeys = self.switches.keys()
        sortedKeys.sort()
        for eachLod in sortedKeys:
            index = sortedKeys.index(eachLod)
            self._Actor__LODNode.node().setSwitch(index, self.switches[eachLod][0], self.switches[eachLod][1])
        

    
    def addLOD(self, lodName, inDist = 0, outDist = 0):
        self._Actor__LODNode.attachNewNode(str(lodName))
        self.switches[lodName] = [
            inDist,
            outDist]
        self._Actor__LODNode.node().addSwitch(inDist, outDist)

    
    def setLOD(self, lodName, inDist = 0, outDist = 0):
        self.switches[lodName] = [
            inDist,
            outDist]
        sortedKeys = self.switches.keys()
        sortedKeys.sort()
        index = sortedKeys.index(lodName)
        self._Actor__LODNode.node().setSwitch(index, inDist, outDist)

    
    def getLOD(self, lodName):
        lod = self._Actor__LODNode.find('**/' + str(lodName))
        if lod.isEmpty():
            return None
        else:
            return lod

    
    def hasLOD(self):
        return self._Actor__hasLOD

    
    def update(self, lod = 0):
        lodnames = self.getLODNames()
        if lod < len(lodnames):
            partBundles = self._Actor__partBundleDict[lodnames[lod]].values()
            for partBundle in partBundles:
                partBundle.node().updateToNow()
            
        else:
            self.notify.warning('update() - no lod: %d' % lod)

    
    def getFrameRate(self, animName = None, partName = None):
        lodName = self._Actor__animControlDict.keys()[0]
        controls = self.getAnimControls(animName, partName)
        if len(controls) == 0:
            return None
        
        return controls[0].getFrameRate()

    
    def getBaseFrameRate(self, animName = None, partName = None):
        lodName = self._Actor__animControlDict.keys()[0]
        controls = self.getAnimControls(animName, partName)
        if len(controls) == 0:
            return None
        
        return controls[0].getAnim().getBaseFrameRate()

    
    def getPlayRate(self, animName = None, partName = None):
        lodName = self._Actor__animControlDict.keys()[0]
        controls = self.getAnimControls(animName, partName)
        if len(controls) == 0:
            return None
        
        return controls[0].getPlayRate()

    
    def setPlayRate(self, rate, animName, partName = None):
        for control in self.getAnimControls(animName, partName):
            control.setPlayRate(rate)
        

    
    def getDuration(self, animName = None, partName = None):
        lodName = self._Actor__animControlDict.keys()[0]
        controls = self.getAnimControls(animName, partName)
        if len(controls) == 0:
            return None
        
        animControl = controls[0]
        return animControl.getNumFrames() / animControl.getFrameRate()

    
    def getNumFrames(self, animName = None, partName = None):
        lodName = self._Actor__animControlDict.keys()[0]
        controls = self.getAnimControls(animName, partName)
        if len(controls) == 0:
            return None
        
        return controls[0].getNumFrames()

    
    def getCurrentAnim(self, partName = None):
        (lodName, animControlDict) = self._Actor__animControlDict.items()[0]
        if partName == None:
            (partName, animDict) = animControlDict.items()[0]
        else:
            animDict = animControlDict.get(partName)
            if animDict == None:
                Actor.notify.warning("couldn't find part: %s" % partName)
                return None
            
        for (animName, anim) in animDict.items():
            if isinstance(anim[1], AnimControl) and anim[1].isPlaying():
                return animName
            
        
        return None

    
    def getCurrentFrame(self, animName = None, partName = None):
        (lodName, animControlDict) = self._Actor__animControlDict.items()[0]
        if partName == None:
            (partName, animDict) = animControlDict.items()[0]
        else:
            animDict = animControlDict.get(partName)
            if animDict == None:
                Actor.notify.warning("couldn't find part: %s" % partName)
                return None
            
        for (animName, anim) in animDict.items():
            if isinstance(anim[1], AnimControl) and anim[1].isPlaying():
                return anim[1].getFrame()
            
        
        return None

    
    def getPart(self, partName, lodName = 'lodRoot'):
        partBundleDict = self._Actor__partBundleDict.get(lodName)
        if not partBundleDict:
            Actor.notify.warning('no lod named: %s' % lodName)
            return None
        
        return partBundleDict.get(partName)

    
    def removePart(self, partName, lodName = 'lodRoot'):
        partBundleDict = self._Actor__partBundleDict.get(lodName)
        if not partBundleDict:
            Actor.notify.warning('no lod named: %s' % lodName)
            return None
        
        animControlDict = self._Actor__animControlDict.get(lodName)
        if not animControlDict:
            Actor.notify.warning('no lod named: %s' % lodName)
            return None
        
        if partBundleDict.has_key(partName):
            partBundleDict[partName].removeNode()
            del partBundleDict[partName]
        
        if animControlDict.has_key(partName):
            del animControlDict[partName]
        

    
    def hidePart(self, partName, lodName = 'lodRoot'):
        partBundleDict = self._Actor__partBundleDict.get(lodName)
        if not partBundleDict:
            Actor.notify.warning('no lod named: %s' % lodName)
            return None
        
        part = partBundleDict.get(partName)
        if part:
            part.hide()
        else:
            Actor.notify.warning('no part named %s!' % partName)

    
    def showPart(self, partName, lodName = 'lodRoot'):
        partBundleDict = self._Actor__partBundleDict.get(lodName)
        if not partBundleDict:
            Actor.notify.warning('no lod named: %s' % lodName)
            return None
        
        part = partBundleDict.get(partName)
        if part:
            part.show()
        else:
            Actor.notify.warning('no part named %s!' % partName)

    
    def showAllParts(self, partName, lodName = 'lodRoot'):
        partBundleDict = self._Actor__partBundleDict.get(lodName)
        if not partBundleDict:
            Actor.notify.warning('no lod named: %s' % lodName)
            return None
        
        part = partBundleDict.get(partName)
        if part:
            part.show()
            part.getChildren().show()
        else:
            Actor.notify.warning('no part named %s!' % partName)

    
    def exposeJoint(self, node, partName, jointName, lodName = 'lodRoot'):
        partBundleDict = self._Actor__partBundleDict.get(lodName)
        if not partBundleDict:
            Actor.notify.warning('no lod named: %s' % lodName)
            return None
        
        part = partBundleDict.get(partName)
        if part:
            bundle = part.node().getBundle()
        else:
            Actor.notify.warning('no part named %s!' % partName)
            return None
        joint = bundle.findChild(jointName)
        if node == None:
            node = self.attachNewNode(jointName)
        
        if joint:
            joint.addNetTransform(node.node())
        else:
            Actor.notify.warning('no joint named %s!' % jointName)
        return node

    
    def stopJoint(self, partName, jointName, lodName = 'lodRoot'):
        partBundleDict = self._Actor__partBundleDict.get(lodName)
        if not partBundleDict:
            Actor.notify.warning('no lod named: %s' % lodName)
            return None
        
        part = partBundleDict.get(partName)
        if part:
            bundle = part.node().getBundle()
        else:
            Actor.notify.warning('no part named %s!' % partName)
            return None
        joint = bundle.findChild(jointName)
        if joint:
            joint.clearNetTransforms()
            joint.clearLocalTransforms()
        else:
            Actor.notify.warning('no joint named %s!' % jointName)

    
    def controlJoint(self, node, partName, jointName, lodName = 'lodRoot'):
        partBundleDict = self._Actor__partBundleDict.get(lodName)
        if not partBundleDict:
            Actor.notify.warning('no lod named: %s' % lodName)
            return None
        
        part = partBundleDict.get(partName)
        if part:
            bundle = part.node().getBundle()
        else:
            Actor.notify.warning('no part named %s!' % partName)
            return None
        joint = bundle.findChild(jointName)
        if joint == None:
            Actor.notify.warning('no joint named %s!' % jointName)
            return None
        
        if node == None:
            node = self.attachNewNode(jointName)
        
        if self._Actor__controlJoints.has_key(bundle):
            self._Actor__controlJoints[bundle][jointName] = node
        else:
            self._Actor__controlJoints[bundle] = {
                jointName: node }
        return node

    
    def instance(self, path, partName, jointName, lodName = 'lodRoot'):
        partBundleDict = self._Actor__partBundleDict.get(lodName)
        if partBundleDict:
            part = partBundleDict.get(partName)
            if part:
                joint = part.find('**/' + jointName)
                if joint.isEmpty():
                    Actor.notify.warning('%s not found!' % jointName)
                else:
                    return path.instanceTo(joint)
            else:
                Actor.notify.warning('no part named %s!' % partName)
        else:
            Actor.notify.warning('no lod named %s!' % lodName)

    
    def attach(self, partName, anotherPartName, jointName, lodName = 'lodRoot'):
        partBundleDict = self._Actor__partBundleDict.get(lodName)
        if partBundleDict:
            part = partBundleDict.get(partName)
            if part:
                anotherPart = partBundleDict.get(anotherPartName)
                if anotherPart:
                    joint = anotherPart.find('**/' + jointName)
                    if joint.isEmpty():
                        Actor.notify.warning('%s not found!' % jointName)
                    else:
                        part.reparentTo(joint)
                else:
                    Actor.notify.warning('no part named %s!' % anotherPartName)
            else:
                Actor.notify.warning('no part named %s!' % partName)
        else:
            Actor.notify.warning('no lod named %s!' % lodName)

    
    def drawInFront(self, frontPartName, backPartName, mode, root = None, lodName = None):
        if lodName != None:
            lodRoot = self.find('**/' + str(lodName))
            if root == None:
                root = lodRoot
            else:
                root = lodRoot.find('**/' + root)
        elif root == None:
            root = self
        
        frontParts = root.findAllMatches('**/' + frontPartName)
        if mode > 0:
            numFrontParts = frontParts.getNumPaths()
            for partNum in range(0, numFrontParts):
                frontParts[partNum].setBin('fixed', mode)
            
            return None
        
        if mode == -2:
            numFrontParts = frontParts.getNumPaths()
            for partNum in range(0, numFrontParts):
                frontParts[partNum].setDepthWrite(0)
                frontParts[partNum].setDepthTest(0)
            
        
        backPart = root.find('**/' + backPartName)
        if backPart.isEmpty():
            Actor.notify.warning('no part named %s!' % backPartName)
            return None
        
        if mode == -3:
            backPart.node().setEffect(DecalEffect.make())
        else:
            backPart.reparentTo(backPart.getParent(), -1)
        frontParts.reparentTo(backPart)

    
    def fixBounds(self, part = None):
        if part == None:
            part = self
        
        charNodes = part.findAllMatches('**/+Character')
        numCharNodes = charNodes.getNumPaths()
        for charNum in range(0, numCharNodes):
            charNodes.getPath(charNum).node().update()
        
        geomNodes = part.findAllMatches('**/+GeomNode')
        numGeomNodes = geomNodes.getNumPaths()
        for nodeNum in range(0, numGeomNodes):
            thisGeomNode = geomNodes.getPath(nodeNum)
            numGeoms = thisGeomNode.node().getNumGeoms()
            for geomNum in range(0, numGeoms):
                thisGeom = thisGeomNode.node().getGeom(geomNum)
                thisGeom.markBoundStale()
                Actor.notify.debug('fixing bounds for node %s, geom %s' % (nodeNum, geomNum))
            
            thisGeomNode.node().markBoundStale()
        

    
    def showAllBounds(self):
        geomNodes = self._Actor__geomNode.findAllMatches('**/+GeomNode')
        numGeomNodes = geomNodes.getNumPaths()
        for nodeNum in range(0, numGeomNodes):
            geomNodes.getPath(nodeNum).showBounds()
        

    
    def hideAllBounds(self):
        geomNodes = self._Actor__geomNode.findAllMatches('**/+GeomNode')
        numGeomNodes = geomNodes.getNumPaths()
        for nodeNum in range(0, numGeomNodes):
            geomNodes.getPath(nodeNum).hideBounds()
        

    
    def animPanel(self):
        TkGlobal = TkGlobal
        import direct.showbase
        AnimPanel = AnimPanel
        import direct.tkpanels
        return AnimPanel.AnimPanel(self)

    
    def stop(self, animName = None, partName = None):
        for control in self.getAnimControls(animName, partName):
            control.stop()
        

    
    def play(self, animName, partName = None, fromFrame = None, toFrame = None):
        if fromFrame == None:
            for control in self.getAnimControls(animName, partName):
                control.play()
            
        else:
            for control in self.getAnimControls(animName, partName):
                if toFrame == None:
                    control.play(fromFrame, control.getNumFrames() - 1)
                else:
                    control.play(fromFrame, toFrame)
            

    
    def loop(self, animName, restart = 1, partName = None, fromFrame = None, toFrame = None):
        if fromFrame == None:
            for control in self.getAnimControls(animName, partName):
                control.loop(restart)
            
        else:
            for control in self.getAnimControls(animName, partName):
                if toFrame == None:
                    control.loop(restart, fromFrame, control.getNumFrames() - 1)
                else:
                    control.loop(restart, fromFrame, toFrame)
            

    
    def pingpong(self, animName, restart = 1, partName = None, fromFrame = None, toFrame = None):
        if fromFrame == None:
            fromFrame = 0
        
        for control in self.getAnimControls(animName, partName):
            if toFrame == None:
                control.pingpong(restart, fromFrame, control.getNumFrames() - 1)
            else:
                control.pingpong(restart, fromFrame, toFrame)
        

    
    def pose(self, animName, frame, partName = None, lodName = None):
        for control in self.getAnimControls(animName, partName, lodName):
            control.pose(frame)
        

    
    def enableBlend(self, blendType = PartBundle.BTNormalizedLinear, partName = None):
        for (lodName, bundleDict) in self._Actor__partBundleDict.items():
            if partName == None:
                for partBundle in bundleDict.values():
                    partBundle.node().getBundle().setBlendType(blendType)
                
            else:
                partBundle = bundleDict.get(partName)
                if partBundle != None:
                    partBundle.node().getBundle().setBlendType(blendType)
                else:
                    Actor.notify.warning("Couldn't find part: %s" % partName)
        

    
    def disableBlend(self, partName = None):
        self.enableBlend(PartBundle.BTSingle, partName)

    
    def setControlEffect(self, animName, effect, partName = None, lodName = None):
        for control in self.getAnimControls(animName, partName, lodName):
            control.getPart().setControlEffect(control, effect)
        

    
    def getAnimControl(self, animName, partName, lodName = 'lodRoot'):
        animControlDict = self._Actor__animControlDict.get(lodName)
        animDict = animControlDict.get(partName)
        if animDict == None:
            Actor.notify.warning("couldn't find part: %s" % partName)
        else:
            anim = animDict.get(animName)
            if anim == None:
                Actor.notify.warning("couldn't find anim: %s" % animName)
            elif not isinstance(anim[1], AnimControl):
                self._Actor__bindAnimToPart(animName, partName, lodName)
            
            return anim[1]
        return None

    
    def getAnimControls(self, animName = None, partName = None, lodName = None):
        controls = []
        if lodName == None:
            animControlDictItems = self._Actor__animControlDict.items()
        else:
            animControlDict = self._Actor__animControlDict.get(lodName)
            if animControlDict == None:
                Actor.notify.warning("couldn't find lod: %s" % lodName)
                animControlDictItems = []
            else:
                animControlDictItems = [
                    (lodName, animControlDict)]
        for (lodName, animControlDict) in animControlDictItems:
            if partName == None:
                animDictItems = animControlDict.items()
            elif isinstance(partName, types.StringType):
                partNameList = [
                    partName]
            else:
                partNameList = partName
            animDictItems = []
            for partName in partNameList:
                animDict = animControlDict.get(partName)
                if animDict == None:
                    Actor.notify.warning("couldn't find part: %s" % partName)
                else:
                    animDictItems.append((partName, animDict))
            
            if animName == None:
                for (thisPart, animDict) in animDictItems:
                    for anim in animDict.values():
                        if isinstance(anim[1], AnimControl) and anim[1].isPlaying():
                            controls.append(anim[1])
                        
                    
                
            else:
                for (thisPart, animDict) in animDictItems:
                    anim = animDict.get(animName)
                    if anim == None:
                        Actor.notify.warning("couldn't find anim: %s" % animName)
                    elif not isinstance(anim[1], AnimControl):
                        if self._Actor__bindAnimToPart(animName, thisPart, lodName):
                            controls.append(anim[1])
                        
                    else:
                        controls.append(anim[1])
                
        
        return controls

    
    def loadModel(self, modelPath, partName = 'modelRoot', lodName = 'lodRoot', copy = 1):
        Actor.notify.debug('in loadModel: %s , part: %s, lod: %s, copy: %s' % (modelPath, partName, lodName, copy))
        if isinstance(modelPath, NodePath):
            if copy:
                model = modelPath.copyTo(hidden)
            else:
                model = modelPath
        elif copy:
            model = loader.loadModelCopy(modelPath)
        else:
            model = loader.loadModelOnce(modelPath)
        if model == None:
            raise StandardError, 'Could not load Actor model %s' % modelPath
        
        bundle = model.find('**/+PartBundleNode')
        if bundle.isEmpty():
            Actor.notify.warning('%s is not a character!' % modelPath)
            model.reparentTo(self._Actor__geomNode)
        else:
            acc = AnimControlCollection()
            autoBind(model.node(), acc, -1)
            numAnims = acc.getNumAnims()
            self.prepareBundle(bundle, partName, lodName)
            if numAnims != 0:
                Actor.notify.info('model contains %s animations.' % numAnims)
                self._Actor__animControlDict.setdefault(lodName, { })
                self._Actor__animControlDict[lodName].setdefault(partName, { })
                for i in range(numAnims):
                    animControl = acc.getAnim(i)
                    animName = acc.getAnimName(i)
                    self._Actor__animControlDict[lodName][partName][animName] = [
                        None,
                        animControl]
                
            
            model.removeNode()

    
    def prepareBundle(self, bundle, partName = 'modelRoot', lodName = 'lodRoot'):
        if not (self.gotName):
            self.node().setName(bundle.node().getName())
            self.gotName = 1
        
        bundle.node().setName(Actor.partPrefix + partName)
        if self._Actor__partBundleDict.has_key(lodName) == 0:
            needsDict = 1
            bundleDict = { }
        else:
            needsDict = 0
        if lodName != 'lodRoot':
            bundle.reparentTo(self._Actor__LODNode.find('**/' + str(lodName)))
        else:
            bundle.reparentTo(self._Actor__geomNode)
        if needsDict:
            bundleDict[partName] = bundle
            self._Actor__partBundleDict[lodName] = bundleDict
        else:
            self._Actor__partBundleDict[lodName][partName] = bundle

    
    def loadAnims(self, anims, partName = 'modelRoot', lodName = 'lodRoot'):
        Actor.notify.debug('in loadAnims: %s, part: %s, lod: %s' % (anims, partName, lodName))
        for animName in anims.keys():
            self._Actor__animControlDict.setdefault(lodName, { })
            self._Actor__animControlDict[lodName].setdefault(partName, { })
            self._Actor__animControlDict[lodName][partName][animName] = [
                anims[animName],
                None]
        

    
    def unloadAnims(self, anims, partName = 'modelRoot', lodName = 'lodRoot'):
        Actor.notify.debug('in unloadAnims: %s, part: %s, lod: %s' % (anims, partName, lodName))
        if lodName == None:
            lodNames = self._Actor__animControlDict.keys()
        else:
            lodNames = [
                lodName]
        if partName == None:
            if len(lodNames) > 0:
                partNames = self._Actor__animControlDict[lodNames[0]].keys()
            else:
                partNames = []
        else:
            partNames = [
                partName]
        if anims == None:
            if len(lodNames) > 0 and len(partNames) > 0:
                anims = self._Actor__animControlDict[lodNames[0]][partNames[0]].keys()
            else:
                anims = []
        
        for lodName in lodNames:
            for partName in partNames:
                for animName in anims:
                    animControlPair = self._Actor__animControlDict[lodName][partName][animName]
                    if animControlPair[1] != None:
                        del animControlPair[1]
                        animControlPair.append(None)
                    
                
            
        

    
    def bindAnim(self, animName, partName = 'modelRoot', lodName = 'lodRoot'):
        if lodName == None:
            lodNames = self._Actor__animControl.keys()
        else:
            lodNames = [
                lodName]
        for thisLod in lodNames:
            if partName == None:
                partNames = animControlDict[lodName].keys()
            else:
                partNames = [
                    partName]
            for thisPart in partNames:
                ac = self._Actor__bindAnimToPart(animName, thisPart, thisLod)
            
        

    
    def _Actor__bindAnimToPart(self, animName, partName, lodName):
        if not self._Actor__animControlDict[lodName][partName].has_key(animName):
            Actor.notify.debug('actor has no animation %s', animName)
        
        if isinstance(self._Actor__animControlDict[lodName][partName][animName][1], AnimControl):
            return None
        
        animPath = self._Actor__animControlDict[lodName][partName][animName][0]
        anim = loader.loadModelOnce(animPath)
        if anim == None:
            return None
        
        animBundle = anim.find('**/+AnimBundleNode').node().getBundle()
        bundle = self._Actor__partBundleDict[lodName][partName].node().getBundle()
        controlDict = self._Actor__controlJoints.get(bundle, None)
        if controlDict:
            for (jointName, node) in controlDict.items():
                if node:
                    joint = animBundle.makeChildDynamic(jointName)
                    if joint:
                        joint.setValueNode(node.node())
                    
                
            
        
        animControl = bundle.bindAnim(animBundle, -1)
        if animControl == None:
            Actor.notify.error('Null AnimControl: %s' % animName)
        else:
            self._Actor__animControlDict[lodName][partName][animName][1] = animControl
            Actor.notify.debug('binding anim: %s to part: %s, lod: %s' % (animName, partName, lodName))
        return animControl

    
    def _Actor__copyPartBundles(self, other):
        for lodName in other._Actor__partBundleDict.keys():
            self._Actor__partBundleDict[lodName] = { }
            for partName in other._Actor__partBundleDict[lodName].keys():
                partBundle = self.find('**/' + Actor.partPrefix + partName)
                if partBundle != None:
                    self._Actor__partBundleDict[lodName][partName] = partBundle
                else:
                    Actor.notify.error('lod: %s has no matching part: %s' % (lodName, partName))
            
        

    
    def _Actor__copyAnimControls(self, other):
        for lodName in other._Actor__animControlDict.keys():
            self._Actor__animControlDict[lodName] = { }
            for partName in other._Actor__animControlDict[lodName].keys():
                self._Actor__animControlDict[lodName][partName] = { }
                for animName in other._Actor__animControlDict[lodName][partName].keys():
                    self._Actor__animControlDict[lodName][partName][animName] = [
                        other._Actor__animControlDict[lodName][partName][animName][0],
                        None]
                
            
        

    
    def actorInterval(self, *args, **kw):
        ActorInterval = ActorInterval
        import direct.interval
        return ActorInterval.ActorInterval(self, *args, **args)


