# File: h (Python 2.2)

from direct.directtools.DirectSelection import *
from direct.directtools.DirectUtil import ROUND_TO
from direct.directtools.DirectGeometry import LineNodePath
from direct.gui.DirectGui import *
from direct.showbase.PandaObject import *
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.task import Task
from toontown.catalog import CatalogFurnitureItem
from toontown.catalog import CatalogItemTypes
from direct.showbase import PythonUtil
from toontown.toontowngui import TTDialog
from toontown.toonbase import TTLocalizer
from otp.otpbase import OTPLocalizer
camPos50 = (Point3(0.0, -10.0, 50.0), Point3(0.0, -9.6600000000000001, 49.060000000000002), Point3(0.0, 1.5, 12.380000000000001), Point3(0.0, 1.5, -3.1000000000000001), 1)
camPos40 = (Point3(0.0, -15.0, 40.0), Point3(0.0, -14.5, 39.130000000000003), Point3(0.0, 1.5, 12.380000000000001), Point3(0.0, 1.5, -3.1000000000000001), 1)
camPos30 = (Point3(0.0, -20.0, 30.0), Point3(0.0, -19.289999999999999, 29.289999999999999), Point3(0.0, 1.5, 12.380000000000001), Point3(0.0, 1.5, -3.1000000000000001), 1)
camPos20 = (Point3(0.0, -20.0, 20.0), Point3(0.0, -19.129999999999999, 19.5), Point3(0.0, 1.5, 12.380000000000001), Point3(0.0, 1.5, -3.1000000000000001), 1)
camPosList = [
    camPos20,
    camPos30,
    camPos40,
    camPos50]
DEFAULT_CAM_INDEX = 2
NormalPickerPanelColor = (1, 0.90000000000000002, 0.745, 1)
DeletePickerPanelColor = (1, 0.40000000000000002, 0.40000000000000002, 1)

class FurnitureItemPanel(DirectButton):
    
    def __init__(self, item, itemId, command = None, deleteMode = 0, withinFunc = None, helpCategory = None):
        self.item = item
        self.itemId = itemId
        self.command = command
        self.origHelpCategory = helpCategory
        framePanelColor = NormalPickerPanelColor
        if deleteMode:
            framePanelColor = DeletePickerPanelColor
        
        DirectButton.__init__(self, relief = RAISED, frameSize = (-0.25, 0.25, -0.20000000000000001, 0.20000000000000001), frameColor = framePanelColor, borderWidth = (0.02, 0.02), command = self.clicked)
        if deleteMode:
            helpCategory = 'FurnitureItemPanelDelete'
        
        self.bindHelpText(helpCategory)
        if withinFunc:
            self.bind(WITHIN, lambda event: withinFunc(self.itemId))
        
        self.initialiseoptions(FurnitureItemPanel)
        self.load()

    
    def show(self):
        DirectFrame.show(self)
        if self.ival:
            self.ival.resume()
        

    
    def hide(self):
        DirectFrame.hide(self)
        if self.ival:
            self.ival.pause()
        

    
    def load(self):
        panelWidth = 7
        panelCenter = 0
        (self.picture, self.ival) = self.item.getPicture(base.localAvatar)
        if self.picture:
            self.picture.reparentTo(self)
            self.picture.setScale(0.14000000000000001)
            self.picture.setPos(0, 0, -0.02)
            text = self.item.getName()
            text_pos = (0, -0.10000000000000001, 0)
        else:
            text = self.item.getTypeName() + ': ' + self.item.getName()
            text_pos = (0, -0.29999999999999999, 0)
        if self.ival:
            self.ival.loop()
            self.ival.pause()
        
        self.nameLabel = DirectLabel(parent = self, relief = None, pos = (0, 0, 0.17000000000000001), scale = 0.45000000000000001, text = text, text_scale = 0.14999999999999999, text_fg = (0, 0, 0, 1), text_pos = text_pos, text_font = ToontownGlobals.getInterfaceFont(), text_wordwrap = panelWidth)

    
    def clicked(self):
        self.command(self.item, self.itemId)

    
    def unload(self):
        del self.item
        self.nameLabel.destroy()
        del self.nameLabel
        if self.ival:
            self.ival.finish()
        
        del self.ival
        del self.picture
        DirectFrame.destroy(self)

    
    def destroy(self):
        self.unload()

    
    def bindHelpText(self, category):
        self.unbind(ENTER)
        self.unbind(EXIT)
        if category is None:
            category = self.origHelpCategory
        
        self.bind(ENTER, base.cr.objectManager.showHelpText, extraArgs = [
            category,
            self.item.getName()])
        self.bind(EXIT, base.cr.objectManager.hideHelpText)



class MovableObject(NodePath, PandaObject):
    
    def __init__(self, dfitem, parent = render):
        NodePath.__init__(self)
        self.assign(dfitem)
        self.dfitem = dfitem
        dfitem.transmitRelativeTo = dfitem.getParent()
        self.reparentTo(parent)
        self.setTag('movableObject', '1')
        self.builtInCNodes = self.findAllMatches('**/+CollisionNode')
        self.numBuiltInNodes = self.builtInCNodes.getNumPaths()
        self.stashBuiltInCollisionNodes()
        shadows = self.findAllMatches('**/*shadow*')
        shadows.addPathsFrom(self.findAllMatches('**/*Shadow*'))
        shadows.stash()
        flags = self.dfitem.item.getFlags()
        if flags & CatalogFurnitureItem.FLPainting:
            self.setOnFloor(0)
            self.setOnWall(1)
        else:
            self.setOnFloor(1)
            self.setOnWall(0)
        if flags & CatalogFurnitureItem.FLOnTable:
            self.setOnTable(1)
        else:
            self.setOnTable(0)
        if flags & CatalogFurnitureItem.FLRug:
            self.setIsRug(1)
        else:
            self.setIsRug(0)
        if flags & CatalogFurnitureItem.FLIsTable:
            self.setIsTable(1)
        else:
            self.setIsTable(0)
        m = self.getTransform()
        self.iPosHpr()
        (bMin, bMax) = self.getTightBounds()
        self.bounds = self.getTightBounds()
        bMin -= Vec3(0.10000000000000001, 0.10000000000000001, 0)
        bMax += Vec3(0.10000000000000001, 0.10000000000000001, 0)
        self.c0 = Point3(bMin[0], bMin[1], 0.20000000000000001)
        self.c1 = Point3(bMax[0], bMin[1], 0.20000000000000001)
        self.c2 = Point3(bMax[0], bMax[1], 0.20000000000000001)
        self.c3 = Point3(bMin[0], bMax[1], 0.20000000000000001)
        self.center = (bMin + bMax) / 2.0
        if flags & CatalogFurnitureItem.FLPainting:
            self.dragPoint = Vec3(self.center[0], bMax[1], self.center[2])
        else:
            self.dragPoint = Vec3(self.center[0], self.center[1], bMin[2])
        delta = self.dragPoint - self.c0
        self.radius = min(delta[0], delta[1])
        if self.getOnWall():
            self.setWallOffset(0.10000000000000001)
        else:
            self.setWallOffset(self.radius + 0.10000000000000001)
        self.makeCollisionBox()
        self.setTransform(m)
        self.unstashBuiltInCollisionNodes()
        shadows.unstash()

    
    def resetMovableObject(self):
        self.unstashBuiltInCollisionNodes()
        self.collisionNodePath.removeNode()
        self.clearTag('movableObject')

    
    def setOnFloor(self, fOnFloor):
        self.fOnFloor = fOnFloor

    
    def getOnFloor(self):
        return self.fOnFloor

    
    def setOnWall(self, fOnWall):
        self.fOnWall = fOnWall

    
    def getOnWall(self):
        return self.fOnWall

    
    def setOnTable(self, fOnTable):
        self.fOnTable = fOnTable

    
    def getOnTable(self):
        return self.fOnTable

    
    def setIsRug(self, fIsRug):
        self.fIsRug = fIsRug

    
    def getIsRug(self):
        return self.fIsRug

    
    def setIsTable(self, fIsTable):
        self.fIsTable = fIsTable

    
    def getIsTable(self):
        return self.fIsTable

    
    def setWallOffset(self, offset):
        self.wallOffset = offset

    
    def getWallOffset(self):
        return self.wallOffset

    
    def destroy(self):
        self.removeNode()

    
    def stashBuiltInCollisionNodes(self):
        self.builtInCNodes.stash()

    
    def unstashBuiltInCollisionNodes(self):
        self.builtInCNodes.unstash()

    
    def getFloorBitmask(self):
        if self.getOnTable():
            return ToontownGlobals.FloorBitmask | ToontownGlobals.FurnitureTopBitmask
        else:
            return ToontownGlobals.FloorBitmask

    
    def getWallBitmask(self):
        if self.getIsRug() or self.getOnWall():
            return ToontownGlobals.WallBitmask
        else:
            return ToontownGlobals.WallBitmask | ToontownGlobals.FurnitureSideBitmask

    
    def makeCollisionBox(self):
        self.collisionNodePath = self.attachNewNode('furnitureCollisionNode')
        if self.getIsRug() or self.getOnWall():
            return None
        
        mx = self.bounds[0][0] - 0.01
        Mx = self.bounds[1][0] + 0.01
        my = self.bounds[0][1] - 0.01
        My = self.bounds[1][1] + 0.01
        mz = self.bounds[0][2]
        Mz = self.bounds[1][2]
        cn = CollisionNode('sideCollisionNode')
        cn.setIntoCollideMask(ToontownGlobals.FurnitureSideBitmask)
        self.collisionNodePath.attachNewNode(cn)
        cp = CollisionPolygon(Point3(mx, My, mz), Point3(mx, my, mz), Point3(mx, my, Mz), Point3(mx, My, Mz))
        cn.addSolid(cp)
        cp = CollisionPolygon(Point3(Mx, my, mz), Point3(Mx, My, mz), Point3(Mx, My, Mz), Point3(Mx, my, Mz))
        cn.addSolid(cp)
        cp = CollisionPolygon(Point3(mx, my, mz), Point3(Mx, my, mz), Point3(Mx, my, Mz), Point3(mx, my, Mz))
        cn.addSolid(cp)
        cp = CollisionPolygon(Point3(Mx, My, mz), Point3(mx, My, mz), Point3(mx, My, Mz), Point3(Mx, My, Mz))
        cn.addSolid(cp)
        if self.getIsTable():
            cn = CollisionNode('topCollisionNode')
            cn.setIntoCollideMask(ToontownGlobals.FurnitureTopBitmask)
            self.collisionNodePath.attachNewNode(cn)
            cp = CollisionPolygon(Point3(mx, my, Mz), Point3(Mx, my, Mz), Point3(Mx, My, Mz), Point3(mx, My, Mz))
            cn.addSolid(cp)
        



class ObjectManager(NodePath, PandaObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('ObjectManager')
    
    def __init__(self):
        NodePath.__init__(self)
        self.assign(render.attachNewNode('objectManager'))
        self.objectDict = { }
        self.selectedObject = None
        self.movingObject = 0
        self.deselectEvent = None
        self.startPose = render.attachNewNode('startPose')
        self.dragPointNP = self.attachNewNode('dragPoint')
        self.gridSnapNP = self.dragPointNP.attachNewNode('gridSnap')
        self.collisionOffsetNP = self.gridSnapNP.attachNewNode('collisionResponse')
        self.iRay = SelectionRay()
        self.iSegment = SelectionSegment(numSegments = 6)
        self.iSegment4 = SelectionSegment(numSegments = 4)
        self.iSphere = SelectionSphere()
        self.houseExtents = None
        self.doorBlocker = None
        cp = CollisionPolygon(Point3(-100, -100, 0), Point3(100, -100, 0), Point3(100, 100, 0), Point3(-100, 100, 0))
        cn = CollisionNode('dragCollisionNode')
        cn.addSolid(cp)
        cn.setIntoCollideMask(ToontownGlobals.FurnitureDragBitmask)
        self.collisionNP = NodePath(cn)
        self.lnp = LineNodePath()
        self.fRecenter = 0
        self.gridSpacing = None
        self.firstTime = 0
        guiModels = loader.loadModel('phase_5.5/models/gui/house_design_gui')
        self.createSelectedObjectPanel(guiModels)
        self.createMainControls(guiModels)
        self.furnitureManager = None
        self.atticPicker = None
        self.inRoomPicker = None
        self.inTrashPicker = None
        self.dialog = None
        self.disabledButton = None
        self.deleteMode = 0
        self.nonDeletableItem = None
        self.verifyFrame = None
        self.deleteItemText = None
        self.okButton = None
        self.cancelButton = None
        self.itemIval = None
        self.itemPanel = None
        self.guiInterval = None
        self.accept('enterFurnitureMode', self.enterFurnitureMode)
        self.accept('exitFurnitureMode', self.exitFurnitureMode)

    
    def enterFurnitureMode(self, furnitureManager, fDirector):
        if not fDirector:
            if self.furnitureManager:
                self.exitFurnitureMode(self.furnitureManager)
            
            return None
        
        if furnitureManager == self.furnitureManager:
            return None
        
        if self.furnitureManager != None:
            self.exitFurnitureMode(self.furnitureManager)
        
        self.notify.info('enterFurnitureMode, fDirector = %s' % fDirector)
        if base.cr.productName == 'DisneyOnline-US':
            if not base.cr.isPaid():
                base.localAvatar.chatMgr.obscure(1, 0)
            
        
        self.furnitureManager = furnitureManager
        self.furnitureManager.d_avatarEnter()
        house = furnitureManager.getInteriorObject()
        house.hideExteriorWindows()
        self.setTargetNodePath(house.interior)
        self.createAtticPicker()
        self.initializeDistributedFurnitureItems(furnitureManager.dfitems)
        self.setCamPosIndex(DEFAULT_CAM_INDEX)
        base.localAvatar.setGhostMode(1)
        taskMgr.remove('editModeTransition')
        self.orientCamH(base.localAvatar.getH(self.targetNodePath))
        self.accept('mouse1', self.moveObjectStart)
        self.accept('mouse1-up', self.moveObjectStop)
        self.furnitureGui.show()
        self.deleteMode = 0
        self._ObjectManager__updateDeleteButtons()
        self.showAtticPicker()
        base.localAvatar.laffMeter.stop()
        base.setCellsAvailable(base.leftCells + [
            base.bottomCells[0]], 0)
        if self.guiInterval:
            self.guiInterval.finish()
        
        self.guiInterval = self.furnitureGui.posHprScaleInterval(1.0, Point3(-1.1599999999999999, 1, -0.029999999999999999), Vec3(0), Vec3(0.059999999999999998), startPos = Point3(-1.1899999999999999, 1, 0.33000000000000002), startHpr = Vec3(0), startScale = Vec3(0.040000000000000001), blendType = 'easeInOut', name = 'lerpFurnitureButton')
        self.guiInterval.start()
        taskMgr.add(self.recenterButtonFrameTask, 'recenterButtonFrameTask', 10)
        messenger.send('wakeup')

    
    def exitFurnitureMode(self, furnitureManager):
        if furnitureManager != self.furnitureManager:
            return None
        
        self.notify.info('exitFurnitureMode')
        house = furnitureManager.getInteriorObject()
        if house:
            house.showExteriorWindows()
        
        self.furnitureManager.d_avatarExit()
        self.furnitureManager = None
        base.localAvatar.setCameraPositionByIndex(0)
        if base.cr.productName == 'DisneyOnline-US':
            if not base.cr.isPaid():
                base.localAvatar.chatMgr.obscure(0, 0)
                base.localAvatar.chatMgr.normalButton.show()
            
        
        self.exitDeleteMode()
        self.houseExtents.detachNode()
        self.doorBlocker.detachNode()
        self.deselectObject()
        self.ignore('mouse1')
        self.ignore('mouse1-up')
        if self.atticPicker:
            self.atticPicker.destroy()
            self.atticPicker = None
        
        if self.inRoomPicker:
            self.inRoomPicker.destroy()
            self.inRoomPicker = None
        
        if self.inTrashPicker:
            self.inTrashPicker.destroy()
            self.inTrashPicker = None
        
        self._ObjectManager__cleanupVerifyDelete()
        self.furnitureGui.hide()
        base.setCellsAvailable(base.leftCells + [
            base.bottomCells[0]], 1)
        base.localAvatar.laffMeter.start()
        taskMgr.remove('recenterButtonFrameTask')
        self.cleanupDialog()
        taskMgr.remove('showHelpTextDoLater')
        messenger.send('wakeup')

    
    def initializeDistributedFurnitureItems(self, dfitems):
        self.objectDict = { }
        for item in dfitems:
            mo = MovableObject(item, parent = self.targetNodePath)
            self.objectDict[mo.id()] = mo
        

    
    def setCamPosIndex(self, index):
        self.camPosIndex = index
        base.localAvatar.setCameraSettings(camPosList[index])

    
    def zoomCamIn(self):
        self.setCamPosIndex(max(0, self.camPosIndex - 1))
        messenger.send('wakeup')

    
    def zoomCamOut(self):
        self.setCamPosIndex(min(len(camPosList) - 1, self.camPosIndex + 1))
        messenger.send('wakeup')

    
    def rotateCamCW(self):
        self.orientCamH(base.localAvatar.getH(self.targetNodePath) - 90)
        messenger.send('wakeup')

    
    def rotateCamCCW(self):
        self.orientCamH(base.localAvatar.getH(self.targetNodePath) + 90)
        messenger.send('wakeup')

    
    def orientCamH(self, toonH):
        targetH = ROUND_TO(toonH, 90)
        base.localAvatar.hprInterval(duration = 1, hpr = Vec3(targetH, 0, 0), other = self.targetNodePath, blendType = 'easeInOut', name = 'editModeTransition').start()

    
    def setTargetNodePath(self, nodePath):
        self.targetNodePath = nodePath
        if self.houseExtents:
            self.houseExtents.removeNode()
        
        if self.doorBlocker:
            self.doorBlocker.removeNode()
        
        self.makeHouseExtentsBox()
        self.makeDoorBlocker()
        self.collisionNP.reparentTo(self.targetNodePath)

    
    def loadObject(self, filename):
        mo = MovableObject(filename, parent = self.targetNodePath)
        self.objectDict[mo.id()] = mo
        self.selectObject(mo)
        return mo

    
    def pickObject(self):
        self.iRay.setParentNP(base.cam)
        entry = self.iRay.pickGeom(targetNodePath = self.targetNodePath, skipFlags = SKIP_ALL)
        if entry:
            nodePath = entry.getIntoNodePath()
            if self.isMovableObject(nodePath):
                self.selectObject(self.findObject(nodePath))
                return None
            
        
        self.deselectObject()

    
    def pickInRoom(self, objectId):
        self.selectObject(self.objectDict.get(objectId))

    
    def selectObject(self, selectedObject):
        messenger.send('wakeup')
        if self.selectedObject:
            self.deselectObject()
        
        if selectedObject:
            self.selectedObject = selectedObject
            self.deselectEvent = self.selectedObject.dfitem.uniqueName('disable')
            self.acceptOnce(self.deselectEvent, self.deselectObject)
            self.lnp.reset()
            self.lnp.reparentTo(selectedObject)
            self.lnp.moveTo(selectedObject.c0)
            self.lnp.drawTo(selectedObject.c1)
            self.lnp.drawTo(selectedObject.c2)
            self.lnp.drawTo(selectedObject.c3)
            self.lnp.drawTo(selectedObject.c0)
            self.lnp.create()
            self.buttonFrame.show()
            self.enableButtonFrameTask()
            self.sendToAtticButton.show()
            self.atticRoof.hide()
        

    
    def deselectObject(self):
        self.moveObjectStop()
        if self.deselectEvent:
            self.ignore(self.deselectEvent)
            self.deselectEvent = None
        
        self.selectedObject = None
        self.lnp.detachNode()
        self.buttonFrame.hide()
        self.disableButtonFrameTask()
        self.sendToAtticButton.hide()
        self.atticRoof.show()

    
    def isMovableObject(self, nodePath):
        return nodePath.hasNetTag('movableObject')

    
    def findObject(self, nodePath):
        np = nodePath.findNetTag('movableObject')
        if np.isEmpty():
            return None
        else:
            return self.objectDict.get(np.id(), None)

    
    def moveObjectStop(self, *args):
        if self.movingObject:
            self.movingObject = 0
            taskMgr.remove('moveObjectTask')
            if self.selectedObject:
                self.selectedObject.wrtReparentTo(self.targetNodePath)
                self.selectedObject.collisionNodePath.unstash()
                self.selectedObject.dfitem.stopAdjustPosHpr()
            
            for object in self.objectDict.values():
                object.unstashBuiltInCollisionNodes()
            
            self.centerMarker['image'] = [
                self.grabUp,
                self.grabDown,
                self.grabRollover]
            self.centerMarker.configure(text = [
                '',
                TTLocalizer.HDMoveLabel], text_pos = (0, 1), text_scale = 0.69999999999999996, text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), image_scale = 0.29999999999999999)
        

    
    def moveObjectStart(self):
        self.moveObjectStop()
        self.pickObject()
        self.moveObjectContinue()

    
    def moveObjectContinue(self, *args):
        messenger.send('wakeup')
        if self.selectedObject:
            for object in self.objectDict.values():
                object.stashBuiltInCollisionNodes()
            
            self.selectedObject.collisionNodePath.stash()
            self.selectedObject.dfitem.startAdjustPosHpr()
            self.firstTime = 1
            self.iPosHpr()
            self.startPoseValid = 0
            self.centerMarker['image'] = self.grabDown
            self.centerMarker.configure(text = TTLocalizer.HDMoveLabel, text_pos = (0, 1), text_scale = 0.69999999999999996, text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), image_scale = 0.29999999999999999)
            taskMgr.add(self.moveObjectTask, 'moveObjectTask')
            self.movingObject = 1
        

    
    def setLnpColor(self, r, g, b):
        for i in range(5):
            self.lnp.lineSegs.setVertexColor(i, r, g, b)
        

    
    def markNewPosition(self, isValid):
        if not isValid:
            if self.startPoseValid:
                self.collisionOffsetNP.setPosHpr(self.startPose, self.selectedObject.dragPoint, Vec3(0))
            
            self.setLnpColor(1, 0, 0)
        else:
            self.startPoseValid = 1

    
    def moveObjectTask(self, state):
        so = self.selectedObject
        target = self.targetNodePath
        self.startPose.iPosHpr(so)
        self.setLnpColor(1, 1, 1)
        self.iRay.setParentNP(base.cam)
        entry = self.iRay.pickBitMask(bitMask = ToontownGlobals.FurnitureDragBitmask, targetNodePath = target, skipFlags = SKIP_BACKFACE | SKIP_CAMERA | SKIP_UNPICKABLE)
        if not entry:
            return Task.cont
        
        self.setPos(base.cam, entry.getSurfacePoint(base.cam))
        if self.firstTime:
            self.moveObjectInit()
            self.firstTime = 0
        else:
            self.gridSnapNP.iPos()
            self.collisionOffsetNP.iPosHpr()
        if self.gridSpacing:
            pos = self.dragPointNP.getPos(target)
            self.gridSnapNP.setPos(target, ROUND_TO(pos[0], self.gridSpacing), ROUND_TO(pos[1], self.gridSpacing), pos[2])
        
        self.iRay.setParentNP(base.cam)
        entry = self.iRay.pickBitMask3D(bitMask = so.getWallBitmask(), targetNodePath = target, dir = Vec3(self.getNearProjectionPoint(self.gridSnapNP)), skipFlags = SKIP_BACKFACE | SKIP_CAMERA | SKIP_UNPICKABLE)
        fWall = 0
        if not so.getOnTable():
            while entry:
                intoMask = entry.getIntoNodePath().node().getIntoCollideMask()
                fClosest = (intoMask & ToontownGlobals.WallBitmask).isZero()
                if self.alignObject(entry, target, fClosest = fClosest):
                    fWall = 1
                    break
                
                entry = self.iRay.findNextCollisionEntry(skipFlags = SKIP_BACKFACE | SKIP_CAMERA | SKIP_UNPICKABLE)
        
        if so.getOnWall():
            self.markNewPosition(fWall)
            return Task.cont
        
        self.iRay.setParentNP(target)
        entry = self.iRay.pickBitMask3D(bitMask = so.getFloorBitmask(), targetNodePath = target, origin = Point3(self.gridSnapNP.getPos(target) + Vec3(0, 0, 10)), dir = Vec3(0, 0, -1), skipFlags = SKIP_BACKFACE | SKIP_CAMERA | SKIP_UNPICKABLE)
        if not entry:
            self.markNewPosition(0)
            return Task.cont
        
        nodePath = entry.getIntoNodePath()
        if self.isMovableObject(nodePath):
            self.gridSnapNP.setPos(target, Point3(entry.getSurfacePoint(target)))
        else:
            self.gridSnapNP.setPos(target, Point3(entry.getSurfacePoint(target) + Vec3(0, 0, ToontownGlobals.FloorOffset)))
            if not fWall:
                self.iSphere.setParentNP(self.gridSnapNP)
                self.iSphere.setCenterRadius(0, Point3(0), so.radius * 1.25)
                entry = self.iSphere.pickBitMask(bitMask = so.getWallBitmask(), targetNodePath = target, skipFlags = SKIP_CAMERA | SKIP_UNPICKABLE)
                if entry:
                    self.alignObject(entry, target, fClosest = 1)
                
            
        isValid = self.collisionTest()
        self.markNewPosition(isValid)
        return Task.cont

    
    def collisionTest(self):
        so = self.selectedObject
        target = self.targetNodePath
        entry = self.segmentCollision()
        if not entry:
            return 1
        
        offsetDict = { }
        while entry:
            offset = self.computeSegmentOffset(entry)
            if offset:
                eid = entry.getInto()
                maxOffsetVec = offsetDict.get(eid, Vec3(0))
                if offset.length() > maxOffsetVec.length():
                    maxOffsetVec.assign(offset)
                
                offsetDict[eid] = maxOffsetVec
            
            entry = self.iSegment.findNextCollisionEntry(skipFlags = SKIP_CAMERA | SKIP_UNPICKABLE)
        if offsetDict:
            keys = offsetDict.keys()
            ortho1 = offsetDict[keys[0]]
            ortho2 = Vec3(0)
            v1 = Vec3(ortho1)
            v1.normalize()
            for key in keys[1:]:
                offset = offsetDict[key]
                v2 = Vec3(offset)
                v2.normalize()
                dp = v1.dot(v2)
                if abs(dp) > 0.94999999999999996:
                    if offset.length() > ortho1.length():
                        ortho1.assign(offset)
                    
                elif abs(dp) < 0.050000000000000003:
                    if offset.length() > ortho2.length():
                        ortho2.assign(offset)
                    
                else:
                    o1Len = ortho1.length()
                    parallelVec = Vec3(ortho1 * offset.dot(ortho1) / o1Len * o1Len)
                    perpVec = Vec3(offset - parallelVec)
                    if parallelVec.length() > o1Len:
                        ortho1.assign(parallelVec)
                    
                    if perpVec.length() > ortho2.length():
                        ortho2.assign(perpVec)
                    
            
            totalOffset = ortho1 + ortho2
            self.collisionOffsetNP.setPos(self.collisionOffsetNP, totalOffset)
            if not self.segmentCollision():
                return 1
            
        
        m = self.startPose.getMat(so)
        deltaMove = Vec3(m.getRow3(3))
        if deltaMove.length() == 0:
            return 1
        
        self.iSegment4.setParentNP(so)
        entry = self.iSegment4.pickBitMask(bitMask = so.getWallBitmask(), targetNodePath = target, endPointList = [
            (so.c0, Point3(m.xformPoint(so.c0))),
            (so.c1, Point3(m.xformPoint(so.c1))),
            (so.c2, Point3(m.xformPoint(so.c2))),
            (so.c3, Point3(m.xformPoint(so.c3)))], skipFlags = SKIP_CAMERA | SKIP_UNPICKABLE)
        maxLen = 0
        maxOffset = None
        while entry:
            offset = Vec3(entry.getSurfacePoint(entry.getFromNodePath()) - entry.getFrom().getPointA())
            offsetLen = Vec3(offset).length()
            if offsetLen > maxLen:
                maxLen = offsetLen
                maxOffset = offset
            
            entry = self.iSegment4.findNextCollisionEntry(skipFlags = SKIP_CAMERA | SKIP_UNPICKABLE)
        if maxOffset:
            self.collisionOffsetNP.setPos(self.collisionOffsetNP, maxOffset)
        
        if not self.segmentCollision():
            return 1
        
        return 0

    
    def segmentCollision(self):
        so = self.selectedObject
        self.iSegment.setParentNP(so)
        entry = self.iSegment.pickBitMask(bitMask = so.getWallBitmask(), targetNodePath = self.targetNodePath, endPointList = [
            (so.c0, so.c1),
            (so.c1, so.c2),
            (so.c2, so.c3),
            (so.c3, so.c0),
            (so.c0, so.c2),
            (so.c1, so.c3)], skipFlags = SKIP_CAMERA | SKIP_UNPICKABLE)
        return entry

    
    def computeSegmentOffset(self, entry):
        fromNodePath = entry.getFromNodePath()
        if entry.hasSurfaceNormal():
            normal = entry.getSurfaceNormal(fromNodePath)
        else:
            return None
        hitPoint = entry.getSurfacePoint(fromNodePath)
        m = self.selectedObject.getMat(self.startPose)
        hp = Point3(m.xformPoint(hitPoint))
        hpn = Vec3(m.xformVec(normal))
        hitPointVec = Vec3(hp - self.selectedObject.dragPoint)
        if hitPointVec.dot(hpn) > 0:
            return None
        
        nLen = normal.length()
        offsetVecA = hitPoint - entry.getFrom().getPointA()
        offsetA = normal * offsetVecA.dot(normal) / nLen * nLen
        if offsetA.dot(normal) > 0:
            return offsetA * 1.01
        else:
            offsetVecB = hitPoint - entry.getFrom().getPointB()
            offsetB = normal * offsetVecB.dot(normal) / nLen * nLen
            return offsetB * 1.01

    
    def alignObject(self, entry, target, fClosest = 0, wallOffset = None):
        if not entry.hasSurfaceNormal():
            return 0
        
        normal = entry.getSurfaceNormal(target)
        if abs(normal.dot(Vec3(0, 0, 1))) < 0.10000000000000001:
            tempNP = target.attachNewNode('temp')
            normal.setZ(0)
            normal.normalize()
            lookAtNormal = Point3(normal)
            lookAtNormal *= -1
            tempNP.lookAt(lookAtNormal)
            if fClosest:
                angle = ROUND_TO(self.gridSnapNP.getH(tempNP), 90.0)
            else:
                angle = 0
            self.gridSnapNP.setHpr(tempNP, angle, 0, 0)
            hitPoint = entry.getSurfacePoint(target)
            tempNP.setPos(hitPoint)
            if wallOffset == None:
                wallOffset = self.selectedObject.getWallOffset()
            
            self.gridSnapNP.setPos(tempNP, 0, -wallOffset, 0)
            tempNP.removeNode()
            return 1
        
        return 0

    
    def rotateLeft(self):
        if not (self.selectedObject):
            return None
        
        so = self.selectedObject
        so.dfitem.startAdjustPosHpr()
        self.iPosHpr(so)
        self.moveObjectInit()
        if so.getOnWall():
            startR = self.gridSnapNP.getR()
            newR = ROUND_TO(startR + 22.5, 22.5)
            self.gridSnapNP.setR(newR)
        else:
            startH = self.gridSnapNP.getH(self.targetNodePath)
            newH = ROUND_TO(startH - 22.5, 22.5)
            self.gridSnapNP.setHpr(self.targetNodePath, newH, 0, 0)
            self.collisionTest()
        so.wrtReparentTo(self.targetNodePath)
        self.disableButtonFrameTask()
        so.dfitem.stopAdjustPosHpr()

    
    def rotateRight(self):
        if not (self.selectedObject):
            return None
        
        so = self.selectedObject
        so.dfitem.startAdjustPosHpr()
        self.iPosHpr(so)
        self.moveObjectInit()
        if so.getOnWall():
            startR = self.gridSnapNP.getR()
            newR = ROUND_TO(startR - 22.5, 22.5)
            self.gridSnapNP.setR(newR)
        else:
            startH = self.gridSnapNP.getH(self.targetNodePath)
            newH = ROUND_TO(startH + 22.5, 22.5) % 360.0
            self.gridSnapNP.setHpr(self.targetNodePath, newH, 0, 0)
            self.collisionTest()
        so.wrtReparentTo(self.targetNodePath)
        self.disableButtonFrameTask()
        so.dfitem.stopAdjustPosHpr()

    
    def moveObjectInit(self):
        self.dragPointNP.setPosHpr(self.selectedObject, self.selectedObject.dragPoint, Vec3(0))
        self.gridSnapNP.iPosHpr()
        self.collisionOffsetNP.iPosHpr()
        self.selectedObject.wrtReparentTo(self.collisionOffsetNP)

    
    def resetFurniture(self):
        for o in self.objectDict.values():
            o.resetMovableObject()
        
        self.objectDict = { }
        self.deselectObject()
        self.buttonFrame.hide()

    
    def destroy(self):
        self.ignore('enterFurnitureMode')
        self.ignore('exitFurnitureMode')
        if self.guiInterval:
            self.guiInterval.finish()
        
        if self.furnitureManager:
            self.exitFurnitureMode(self.furnitureManager)
        
        self.cleanupDialog()
        self.resetFurniture()
        self.buttonFrame.destroy()
        self.furnitureGui.destroy()
        if self.houseExtents:
            self.houseExtents.removeNode()
        
        if self.doorBlocker:
            self.doorBlocker.removeNode()
        
        self.removeNode()
        if self.verifyFrame:
            self.verifyFrame.destroy()
            self.verifyFrame = None
            self.deleteItemText = None
            self.okButton = None
            self.cancelButton = None
        

    
    def createSelectedObjectPanel(self, guiModels):
        self.buttonFrame = DirectFrame(scale = 0.5)
        self.grabUp = guiModels.find('**/handup')
        self.grabDown = guiModels.find('**/handdown')
        self.grabRollover = guiModels.find('**/handrollover')
        self.centerMarker = DirectButton(parent = self.buttonFrame, text = [
            '',
            TTLocalizer.HDMoveLabel], text_pos = (0, 1), text_scale = 0.69999999999999996, text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), image = [
            self.grabUp,
            self.grabDown,
            self.grabRollover], image_scale = 0.29999999999999999, relief = None, scale = 0.12)
        self.centerMarker.bind(B1PRESS, self.moveObjectContinue)
        self.centerMarker.bind(B1RELEASE, self.moveObjectStop)
        guiCCWArrowUp = guiModels.find('**/LarrowUp')
        guiCCWArrowDown = guiModels.find('**/LarrowDown')
        guiCCWArrowRollover = guiModels.find('**/LarrowRollover')
        self.rotateLeftButton = DirectButton(parent = self.buttonFrame, relief = None, image = (guiCCWArrowUp, guiCCWArrowDown, guiCCWArrowRollover, guiCCWArrowUp), image_pos = (0, 0, 0.10000000000000001), image_scale = 0.14999999999999999, image3_color = Vec4(0.5, 0.5, 0.5, 0.75), text = ('', TTLocalizer.HDRotateCCWLabel, TTLocalizer.HDRotateCCWLabel, ''), text_pos = (0.13500000000000001, -0.10000000000000001), text_scale = 0.10000000000000001, text_align = TextNode.ARight, text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), pos = (-0.125, 0, -0.20000000000000001), scale = 0.69999999999999996, command = self.rotateLeft)
        self.rotateLeftButton.bind(EXIT, self.enableButtonFrameTask)
        guiCWArrowUp = guiModels.find('**/RarrowUp')
        guiCWArrowDown = guiModels.find('**/RarrowDown')
        guiCWArrowRollover = guiModels.find('**/RarrowRollover')
        self.rotateRightButton = DirectButton(parent = self.buttonFrame, relief = None, image = (guiCWArrowUp, guiCWArrowDown, guiCWArrowRollover, guiCWArrowUp), image_pos = (0, 0, 0.10000000000000001), image_scale = 0.14999999999999999, image3_color = Vec4(0.5, 0.5, 0.5, 0.75), text = ('', TTLocalizer.HDRotateCWLabel, TTLocalizer.HDRotateCWLabel, ''), text_pos = (-0.13500000000000001, -0.10000000000000001), text_scale = 0.10000000000000001, text_align = TextNode.ALeft, text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), pos = (0.125, 0, -0.20000000000000001), scale = 0.69999999999999996, command = self.rotateRight)
        self.rotateRightButton.bind(EXIT, self.enableButtonFrameTask)
        self.buttonFrame.hide()

    
    def recenterButtonFrameTask(self, state):
        if self.selectedObject and self.fRecenter:
            self.buttonFrame.setPos(self.getSelectedObjectScreenXY())
        
        return Task.cont

    
    def disableButtonFrameTask(self, event = None):
        self.fRecenter = 0

    
    def enableButtonFrameTask(self, event = None):
        self.fRecenter = 1

    
    def getNearProjectionPoint(self, nodePath):
        origin = nodePath.getPos(camera)
        if origin[1] != 0.0:
            return origin * (base.camLens.getNear() / origin[1])
        else:
            return Point3(0, base.camLens.getNear(), 0)

    
    def getSelectedObjectScreenXY(self):
        tNodePath = self.selectedObject.attachNewNode('temp')
        tNodePath.setPos(self.selectedObject.center)
        nearVec = self.getNearProjectionPoint(tNodePath)
        nearVec *= base.camLens.getFocalLength() / base.camLens.getNear()
        render2dX = CLAMP(nearVec[0] / base.camLens.getFilmSize()[0] / 2.0, -0.90000000000000002, 0.90000000000000002)
        aspect2dX = render2dX * base.aspectRatio
        aspect2dZ = CLAMP(nearVec[2] / base.camLens.getFilmSize()[1] / 2.0, -0.80000000000000004, 0.90000000000000002)
        tNodePath.removeNode()
        return Vec3(aspect2dX, 0, aspect2dZ)

    
    def createMainControls(self, guiModels):
        attic = guiModels.find('**/attic')
        self.furnitureGui = DirectFrame(relief = None, pos = (-1.1899999999999999, 1, 0.33000000000000002), scale = 0.040000000000000001, image = attic)
        bMoveStopUp = guiModels.find('**/bu_atticX/bu_attic_up')
        bMoveStopDown = guiModels.find('**/bu_atticX/bu_attic_down')
        bMoveStopRollover = guiModels.find('**/bu_atticX/bu_attic_rollover')
        self.bStopMoveFurniture = DirectButton(parent = self.furnitureGui, relief = None, image = [
            bMoveStopUp,
            bMoveStopDown,
            bMoveStopRollover,
            bMoveStopUp], text = [
            '',
            TTLocalizer.HDStopMoveFurnitureButton,
            TTLocalizer.HDStopMoveFurnitureButton], text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_font = ToontownGlobals.getInterfaceFont(), pos = (-0.29999999999999999, 0, 9.4000000000000004), command = base.localAvatar.stopMoveFurniture)
        self.bindHelpText(self.bStopMoveFurniture, 'DoneMoving')
        self.atticRoof = DirectLabel(parent = self.furnitureGui, relief = None, image = guiModels.find('**/rooftile'))
        self.itemBackgroundFrame = DirectFrame(parent = self.furnitureGui, relief = None, image = guiModels.find('**/item_backgroun'), image_pos = (0, 0, -22), image_scale = (1, 1, 5))
        self.scrollUpFrame = DirectFrame(parent = self.furnitureGui, relief = None, image = guiModels.find('**/scrollup'), pos = (0, 0, -0.57999999999999996))
        self.camButtonFrame = DirectFrame(parent = self.furnitureGui, relief = None, image = guiModels.find('**/low'), pos = (0, 0, -11.69))
        tagUp = guiModels.find('**/tag_up')
        tagDown = guiModels.find('**/tag_down')
        tagRollover = guiModels.find('**/tag_rollover')
        self.inAtticButton = DirectButton(parent = self.itemBackgroundFrame, relief = None, text = TTLocalizer.HDInAtticLabel, text_pos = (-0.10000000000000001, -0.25), image = [
            tagUp,
            tagDown,
            tagRollover], pos = (2.8500000000000001, 0, 4), scale = 0.80000000000000004, command = self.showAtticPicker)
        self.bindHelpText(self.inAtticButton, 'Attic')
        self.inRoomButton = DirectButton(parent = self.itemBackgroundFrame, relief = None, text = TTLocalizer.HDInRoomLabel, text_pos = (-0.10000000000000001, -0.25), image = [
            tagUp,
            tagDown,
            tagRollover], pos = (2.8500000000000001, 0, 1.1000000000000001), scale = 0.80000000000000004, command = self.showInRoomPicker)
        self.bindHelpText(self.inRoomButton, 'Room')
        self.inTrashButton = DirectButton(parent = self.itemBackgroundFrame, relief = None, text = TTLocalizer.HDInTrashLabel, text_pos = (-0.10000000000000001, -0.25), image = [
            tagUp,
            tagDown,
            tagRollover], pos = (2.8500000000000001, 0, -1.8), scale = 0.80000000000000004, command = self.showInTrashPicker)
        self.bindHelpText(self.inTrashButton, 'Trash')
        for i in range(4):
            self.inAtticButton.component('text%d' % i).setR(-90)
            self.inRoomButton.component('text%d' % i).setR(-90)
            self.inTrashButton.component('text%d' % i).setR(-90)
        
        backInAtticUp = guiModels.find('**/bu_backinattic_up1')
        backInAtticDown = guiModels.find('**/bu_backinattic_down1')
        backInAtticRollover = guiModels.find('**/bu_backinattic_rollover2')
        self.sendToAtticButton = DirectButton(parent = self.furnitureGui, relief = None, pos = (0.40000000000000002, 0, 12.800000000000001), text = [
            '',
            TTLocalizer.HDToAtticLabel], text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_pos = (1.2, -0.29999999999999999), image = [
            backInAtticUp,
            backInAtticDown,
            backInAtticRollover], command = self.sendItemToAttic)
        self.sendToAtticButton.hide()
        self.bindHelpText(self.sendToAtticButton, 'SendToAttic')
        zoomInUp = guiModels.find('**/bu_RzoomOut_up')
        zoomInDown = guiModels.find('**/bu_RzoomOut_down')
        zoomInRollover = guiModels.find('**/bu_RzoomOut_rollover')
        self.zoomInButton = DirectButton(parent = self.camButtonFrame, image = [
            zoomInUp,
            zoomInDown,
            zoomInRollover], relief = None, pos = (0.90000000000000002, 0, -0.75), command = self.zoomCamIn)
        self.bindHelpText(self.zoomInButton, 'ZoomIn')
        zoomOutUp = guiModels.find('**/bu_LzoomIn_up')
        zoomOutDown = guiModels.find('**/bu_LzoomIn_down')
        zoomOutRollover = guiModels.find('**/buLzoomIn_rollover')
        self.zoomOutButton = DirectButton(parent = self.camButtonFrame, image = [
            zoomOutUp,
            zoomOutDown,
            zoomOutRollover], relief = None, pos = (-1.3999999999999999, 0, -0.75), command = self.zoomCamOut)
        self.bindHelpText(self.zoomOutButton, 'ZoomOut')
        camCCWUp = guiModels.find('**/bu_Rarrow_up1')
        camCCWDown = guiModels.find('**/bu_Rarrow_down1')
        camCCWRollover = guiModels.find('**/bu_Rarrow_orllover')
        self.rotateCamLeftButton = DirectButton(parent = self.camButtonFrame, image = [
            camCCWUp,
            camCCWDown,
            camCCWRollover], relief = None, pos = (0.90000000000000002, 0, -3.0), command = self.rotateCamCCW)
        self.bindHelpText(self.rotateCamLeftButton, 'RotateLeft')
        camCWUp = guiModels.find('**/bu_Larrow_up1')
        camCWDown = guiModels.find('**/bu_Larrow_down1')
        camCWRollover = guiModels.find('**/bu_Larrow_rollover2')
        self.rotateCamRightButton = DirectButton(parent = self.camButtonFrame, image = [
            camCWUp,
            camCWDown,
            camCWRollover], relief = None, pos = (-1.3999999999999999, 0, -3.0), command = self.rotateCamCW)
        self.bindHelpText(self.rotateCamRightButton, 'RotateRight')
        trashcanGui = loader.loadModelOnce('phase_3/models/gui/trashcan_gui')
        trashcanUp = trashcanGui.find('**/TrashCan_CLSD')
        trashcanDown = trashcanGui.find('**/TrashCan_OPEN')
        trashcanRollover = trashcanGui.find('**/TrashCan_RLVR')
        self.deleteEnterButton = DirectButton(parent = self.furnitureGui, image = (trashcanUp, trashcanDown, trashcanRollover, trashcanUp), text = [
            '',
            TTLocalizer.InventoryDelete,
            TTLocalizer.InventoryDelete,
            ''], text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_scale = 0.10000000000000001, text_align = TextNode.ACenter, text_pos = (0, -0.12), text_font = ToontownGlobals.getInterfaceFont(), textMayChange = 0, relief = None, pos = (3.7000000000000002, 0.0, -13.800000000000001), scale = 7.1299999999999999, command = self.enterDeleteMode)
        self.bindHelpText(self.deleteEnterButton, 'DeleteEnter')
        self.deleteExitButton = DirectButton(parent = self.furnitureGui, image = (trashcanUp, trashcanDown, trashcanRollover, trashcanUp), text = ('', TTLocalizer.InventoryDone, TTLocalizer.InventoryDone, ''), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_scale = 0.10000000000000001, text_align = TextNode.ACenter, text_pos = (0, -0.12), text_font = ToontownGlobals.getInterfaceFont(), textMayChange = 0, relief = None, pos = (3.7000000000000002, 0.0, -13.800000000000001), scale = 7.1299999999999999, command = self.exitDeleteMode)
        self.bindHelpText(self.deleteExitButton, 'DeleteExit')
        self.deleteExitButton.hide()
        self.trashcanBase = DirectLabel(parent = self.furnitureGui, image = guiModels.find('**/trashcan_base'), relief = None, pos = (0, 0, -11.640000000000001))
        self.furnitureGui.hide()
        self.helpText = DirectLabel(parent = self.furnitureGui, relief = SUNKEN, frameSize = (-0.5, 10, -3, 0.90000000000000002), frameColor = (0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.5), borderWidth = (0.01, 0.01), text = '', text_wordwrap = 12, text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_scale = 0.80000000000000004, pos = (3, 0.0, -7), scale = 1, text_align = TextNode.ALeft)
        self.helpText.hide()

    
    def createAtticPicker(self):
        self.atticItemPanels = []
        for itemIndex in range(len(self.furnitureManager.atticItems)):
            panel = FurnitureItemPanel(self.furnitureManager.atticItems[itemIndex], itemIndex, command = self.bringItemFromAttic, deleteMode = self.deleteMode, helpCategory = 'FurnitureItemPanelAttic')
            self.atticItemPanels.append(panel)
        
        self.atticWallpaperPanels = []
        for itemIndex in range(len(self.furnitureManager.atticWallpaper)):
            panel = FurnitureItemPanel(self.furnitureManager.atticWallpaper[itemIndex], itemIndex, command = self.bringWallpaperFromAttic, deleteMode = self.deleteMode, helpCategory = 'FurnitureItemPanelAttic')
            self.atticWallpaperPanels.append(panel)
        
        self.atticWindowPanels = []
        for itemIndex in range(len(self.furnitureManager.atticWindows)):
            panel = FurnitureItemPanel(self.furnitureManager.atticWindows[itemIndex], itemIndex, command = self.bringWindowFromAttic, deleteMode = self.deleteMode, helpCategory = 'FurnitureItemPanelAttic')
            self.atticWindowPanels.append(panel)
        
        self.regenerateAtticPicker()

    
    def regenerateAtticPicker(self):
        selectedIndex = 0
        if self.atticPicker:
            selectedIndex = self.atticPicker.getSelectedIndex()
            for panel in self.atticItemPanels:
                panel.detachNode()
            
            for panel in self.atticWallpaperPanels:
                panel.detachNode()
            
            for panel in self.atticWindowPanels:
                panel.detachNode()
            
            self.atticPicker.destroy()
            self.atticPicker = None
        
        itemList = self.atticItemPanels + self.atticWallpaperPanels + self.atticWindowPanels
        if self.deleteMode:
            text = TTLocalizer.HDDeletePickerLabel
        else:
            text = TTLocalizer.HDAtticPickerLabel
        self.atticPicker = self.createScrolledList(itemList, text, 'atticPicker', selectedIndex)
        if self.inRoomPicker or self.inTrashPicker:
            self.atticPicker.hide()
        else:
            self.atticPicker.show()

    
    def createInRoomPicker(self):
        self.inRoomPanels = []
        for (objectId, object) in self.objectDict.items():
            panel = FurnitureItemPanel(object.dfitem.item, objectId, command = self.requestReturnToAttic, deleteMode = self.deleteMode, withinFunc = self.pickInRoom, helpCategory = 'FurnitureItemPanelRoom')
            self.inRoomPanels.append(panel)
        
        self.regenerateInRoomPicker()

    
    def regenerateInRoomPicker(self):
        selectedIndex = 0
        if self.inRoomPicker:
            selectedIndex = self.inRoomPicker.getSelectedIndex()
            for panel in self.inRoomPanels:
                panel.detachNode()
            
            self.inRoomPicker.destroy()
            self.inRoomPicker = None
        
        if self.deleteMode:
            text = TTLocalizer.HDDeletePickerLabel
        else:
            text = TTLocalizer.HDInRoomPickerLabel
        self.inRoomPicker = self.createScrolledList(self.inRoomPanels, text, 'inRoomPicker', selectedIndex)

    
    def createInTrashPicker(self):
        self.inTrashPanels = []
        for itemIndex in range(len(self.furnitureManager.deletedItems)):
            panel = FurnitureItemPanel(self.furnitureManager.deletedItems[itemIndex], itemIndex, command = self.requestReturnToAtticFromTrash, helpCategory = 'FurnitureItemPanelTrash')
            self.inTrashPanels.append(panel)
        
        self.regenerateInTrashPicker()

    
    def regenerateInTrashPicker(self):
        selectedIndex = 0
        if self.inTrashPicker:
            selectedIndex = self.inTrashPicker.getSelectedIndex()
            for panel in self.inTrashPanels:
                panel.detachNode()
            
            self.inTrashPicker.destroy()
            self.inTrashPicker = None
        
        text = TTLocalizer.HDInTrashPickerLabel
        self.inTrashPicker = self.createScrolledList(self.inTrashPanels, text, 'inTrashPicker', selectedIndex)

    
    def createScrolledList(self, itemList, text, name, selectedIndex):
        gui = loader.loadModelOnce('phase_3.5/models/gui/friendslist_gui')
        picker = DirectScrolledList(parent = self.furnitureGui, pos = (-0.38, 0.0, 3), scale = 7.125, relief = None, items = itemList, numItemsVisible = 5, text = text, text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_scale = 0.10000000000000001, text_pos = (0, 0.40000000000000002), decButton_image = (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), decButton_relief = None, decButton_scale = (1.5, 1.5, 1.5), decButton_pos = (0, 0, 0.29999999999999999), decButton_image3_color = Vec4(1, 1, 1, 0.10000000000000001), incButton_image = (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), incButton_relief = None, incButton_scale = (1.5, 1.5, -1.5), incButton_pos = (0, 0, -1.8779999999999999), incButton_image3_color = Vec4(1, 1, 1, 0.10000000000000001))
        picker.setName(name)
        picker.scrollTo(selectedIndex)
        return picker

    
    def reset():
        self.destroy()
        furnitureMenu.destroy()

    
    def showAtticPicker(self):
        if self.inRoomPicker:
            self.inRoomPicker.destroy()
            self.inRoomPicker = None
        
        if self.inTrashPicker:
            self.inTrashPicker.destroy()
            self.inTrashPicker = None
        
        self.atticPicker.show()
        self.inAtticButton['image_color'] = Vec4(1, 1, 1, 1)
        self.inRoomButton['image_color'] = Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
        self.inTrashButton['image_color'] = Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
        self.deleteExitButton['state'] = 'normal'
        self.deleteEnterButton['state'] = 'normal'

    
    def showInRoomPicker(self):
        messenger.send('wakeup')
        if not (self.inRoomPicker):
            self.createInRoomPicker()
        
        self.atticPicker.hide()
        if self.inTrashPicker:
            self.inTrashPicker.destroy()
            self.inTrashPicker = None
        
        self.inAtticButton['image_color'] = Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
        self.inRoomButton['image_color'] = Vec4(1, 1, 1, 1)
        self.inTrashButton['image_color'] = Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
        self.deleteExitButton['state'] = 'normal'
        self.deleteEnterButton['state'] = 'normal'

    
    def showInTrashPicker(self):
        messenger.send('wakeup')
        if not (self.inTrashPicker):
            self.createInTrashPicker()
        
        self.atticPicker.hide()
        if self.inRoomPicker:
            self.inRoomPicker.destroy()
            self.inRoomPicker = None
        
        self.inAtticButton['image_color'] = Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
        self.inRoomButton['image_color'] = Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
        self.inTrashButton['image_color'] = Vec4(1, 1, 1, 1)
        self.deleteExitButton['state'] = 'disabled'
        self.deleteEnterButton['state'] = 'disabled'

    
    def sendItemToAttic(self):
        messenger.send('wakeup')
        if self.selectedObject:
            callback = PythonUtil.Functor(self._ObjectManager__sendItemToAtticCallback, self.selectedObject.id())
            self.furnitureManager.moveItemToAttic(self.selectedObject.dfitem, callback)
            self.deselectObject()
        

    
    def _ObjectManager__sendItemToAtticCallback(self, objectId, retcode, item):
        self._ObjectManager__resetDisabledButton()
        if retcode < 0:
            self.notify.info('Unable to send item %s to attic, reason %s.' % (item.getName(), retcode))
            return None
        
        del self.objectDict[objectId]
        if self.selectedObject != None and self.selectedObject.id() == objectId:
            self.selectedObject.detachNode()
            self.deselectObject()
        
        itemIndex = len(self.atticItemPanels)
        panel = FurnitureItemPanel(item, itemIndex, command = self.bringItemFromAttic, deleteMode = self.deleteMode, helpCategory = 'FurnitureItemPanelAttic')
        self.atticItemPanels.append(panel)
        self.regenerateAtticPicker()
        if self.inRoomPicker:
            for i in range(len(self.inRoomPanels)):
                if self.inRoomPanels[i].itemId == objectId:
                    del self.inRoomPanels[i]
                    self.regenerateInRoomPicker()
                    return None
                
            
        

    
    def cleanupDialog(self, buttonValue = None):
        if self.dialog:
            self.dialog.cleanup()
            self.dialog = None
            self._ObjectManager__resetDisabledButton()
        

    
    def enterDeleteMode(self):
        self.deleteMode = 1
        self._ObjectManager__updateDeleteMode()

    
    def exitDeleteMode(self):
        self.deleteMode = 0
        self._ObjectManager__updateDeleteMode()

    
    def _ObjectManager__updateDeleteMode(self):
        if not (self.atticPicker):
            return None
        
        if self.deleteMode:
            framePanelColor = DeletePickerPanelColor
            atticText = TTLocalizer.HDDeletePickerLabel
            inRoomText = TTLocalizer.HDDeletePickerLabel
            helpCategory = 'FurnitureItemPanelDelete'
        else:
            framePanelColor = NormalPickerPanelColor
            atticText = TTLocalizer.HDAtticPickerLabel
            inRoomText = TTLocalizer.HDInRoomPickerLabel
            helpCategory = None
        if self.inRoomPicker:
            self.inRoomPicker['text'] = inRoomText
            for panel in self.inRoomPicker['items']:
                panel['frameColor'] = framePanelColor
                panel.bindHelpText(helpCategory)
            
        
        if self.atticPicker:
            self.atticPicker['text'] = atticText
            for panel in self.atticPicker['items']:
                panel['frameColor'] = framePanelColor
                panel.bindHelpText(helpCategory)
            
        
        self._ObjectManager__updateDeleteButtons()

    
    def _ObjectManager__updateDeleteButtons(self):
        if self.deleteMode:
            self.deleteExitButton.show()
            self.deleteEnterButton.hide()
        else:
            self.deleteEnterButton.show()
            self.deleteExitButton.hide()

    
    def deleteItemFromRoom(self, dfitem, objectId, itemIndex):
        messenger.send('wakeup')
        callback = PythonUtil.Functor(self._ObjectManager__deleteItemFromRoomCallback, objectId, itemIndex)
        self.furnitureManager.deleteItemFromRoom(dfitem, callback)

    
    def _ObjectManager__deleteItemFromRoomCallback(self, objectId, itemIndex, retcode, item):
        self._ObjectManager__resetDisabledButton()
        if retcode < 0:
            self.notify.info('Unable to delete item %s from room, reason %s.' % (item.getName(), retcode))
            return None
        
        del self.objectDict[objectId]
        if self.selectedObject != None and self.selectedObject.id() == objectId:
            self.selectedObject.detachNode()
            self.deselectObject()
        
        if self.inRoomPicker and itemIndex is not None:
            del self.inRoomPanels[itemIndex]
            self.regenerateInRoomPicker()
        

    
    def bringItemFromAttic(self, item, itemIndex):
        messenger.send('wakeup')
        self._ObjectManager__setDisabledButton(self.atticItemPanels[itemIndex])
        if self.deleteMode:
            self.requestDelete(item, itemIndex, self.deleteItemFromAttic)
            return None
        
        pos = self.targetNodePath.getRelativePoint(base.localAvatar, Point3(0, 2, 0))
        hpr = Point3(0, 0, 0)
        if item.getFlags() & CatalogFurnitureItem.FLPainting:
            for object in self.objectDict.values():
                object.stashBuiltInCollisionNodes()
            
            self.gridSnapNP.iPosHpr()
            target = self.targetNodePath
            self.iRay.setParentNP(base.localAvatar)
            entry = self.iRay.pickBitMask3D(bitMask = ToontownGlobals.WallBitmask, targetNodePath = target, origin = Point3(0, 0, 6), dir = Vec3(0, 1, 0), skipFlags = SKIP_BACKFACE | SKIP_CAMERA | SKIP_UNPICKABLE)
            for object in self.objectDict.values():
                object.unstashBuiltInCollisionNodes()
            
            if entry:
                self.alignObject(entry, target, fClosest = 0, wallOffset = 0.10000000000000001)
                pos = self.gridSnapNP.getPos(target)
                hpr = self.gridSnapNP.getHpr(target)
                print 'painting placed on wall at %s, %s' % (repr(pos), repr(hpr))
            else:
                print 'wall not found for painting'
        
        self.furnitureManager.moveItemFromAttic(itemIndex, (pos[0], pos[1], pos[2], hpr[0], hpr[1], hpr[2]), self._ObjectManager__bringItemFromAtticCallback)

    
    def _ObjectManager__bringItemFromAtticCallback(self, retcode, dfitem, itemIndex):
        self._ObjectManager__resetDisabledButton()
        if retcode < 0:
            self.notify.info('Unable to bring furniture item %s into room, reason %s.' % (itemIndex, retcode))
            return None
        
        mo = self.loadObject(dfitem)
        objectId = mo.id()
        self.atticItemPanels[itemIndex].unload()
        del self.atticItemPanels[itemIndex]
        for i in range(itemIndex, len(self.atticItemPanels)):
            self.atticItemPanels[i].itemId -= 1
        
        self.regenerateAtticPicker()
        if self.inRoomPicker:
            panel = FurnitureItemPanel(dfitem.item, objectId, command = self.requestReturnToAttic, helpCategory = 'FurnitureItemPanelRoom')
            self.inRoomPanels.append(panel)
            self.regenerateInRoomPicker()
        

    
    def deleteItemFromAttic(self, item, itemIndex):
        messenger.send('wakeup')
        self.furnitureManager.deleteItemFromAttic(item, itemIndex, self._ObjectManager__deleteItemFromAtticCallback)

    
    def _ObjectManager__deleteItemFromAtticCallback(self, retcode, item, itemIndex):
        self._ObjectManager__resetDisabledButton()
        if retcode < 0:
            self.notify.info('Unable to delete furniture item %s, reason %s.' % (itemIndex, retcode))
            return None
        
        self.atticItemPanels[itemIndex].unload()
        del self.atticItemPanels[itemIndex]
        for i in range(itemIndex, len(self.atticItemPanels)):
            self.atticItemPanels[i].itemId -= 1
        
        self.regenerateAtticPicker()

    
    def bringWallpaperFromAttic(self, item, itemIndex):
        messenger.send('wakeup')
        self._ObjectManager__setDisabledButton(self.atticWallpaperPanels[itemIndex])
        if self.deleteMode:
            self.requestDelete(item, itemIndex, self.deleteWallpaperFromAttic)
            return None
        
        if base.localAvatar.getY() < 2.2999999999999998:
            room = 0
        else:
            room = 1
        self.furnitureManager.moveWallpaperFromAttic(itemIndex, room, self._ObjectManager__bringWallpaperFromAtticCallback)

    
    def _ObjectManager__bringWallpaperFromAtticCallback(self, retcode, itemIndex, room):
        self._ObjectManager__resetDisabledButton()
        if retcode < 0:
            self.notify.info('Unable to bring wallpaper %s into room %s, reason %s.' % (itemIndex, room, retcode))
            return None
        
        self.atticWallpaperPanels[itemIndex].unload()
        item = self.furnitureManager.atticWallpaper[itemIndex]
        panel = FurnitureItemPanel(item, itemIndex, command = self.bringWallpaperFromAttic, deleteMode = self.deleteMode, helpCategory = 'FurnitureItemPanelAttic')
        self.atticWallpaperPanels[itemIndex] = panel
        self.regenerateAtticPicker()

    
    def deleteWallpaperFromAttic(self, item, itemIndex):
        messenger.send('wakeup')
        self.furnitureManager.deleteWallpaperFromAttic(item, itemIndex, self._ObjectManager__deleteWallpaperFromAtticCallback)

    
    def _ObjectManager__deleteWallpaperFromAtticCallback(self, retcode, item, itemIndex):
        self._ObjectManager__resetDisabledButton()
        if retcode < 0:
            self.notify.info('Unable to delete wallpaper %s, reason %s.' % (itemIndex, retcode))
            return None
        
        self.atticWallpaperPanels[itemIndex].unload()
        del self.atticWallpaperPanels[itemIndex]
        for i in range(itemIndex, len(self.atticWallpaperPanels)):
            self.atticWallpaperPanels[i].itemId -= 1
        
        self.regenerateAtticPicker()

    
    def bringWindowFromAttic(self, item, itemIndex):
        messenger.send('wakeup')
        self._ObjectManager__setDisabledButton(self.atticWindowPanels[itemIndex])
        if self.deleteMode:
            self.requestDelete(item, itemIndex, self.deleteWindowFromAttic)
            return None
        
        if base.localAvatar.getY() < 2.2999999999999998:
            slot = 2
        else:
            slot = 4
        self.furnitureManager.moveWindowFromAttic(itemIndex, slot, self._ObjectManager__bringWindowFromAtticCallback)

    
    def _ObjectManager__bringWindowFromAtticCallback(self, retcode, itemIndex, slot):
        self._ObjectManager__resetDisabledButton()
        if retcode < 0:
            self.notify.info('Unable to bring window %s into slot %s, reason %s.' % (itemIndex, slot, retcode))
            return None
        
        if retcode == ToontownGlobals.FM_SwappedItem:
            self.atticWindowPanels[itemIndex].unload()
            item = self.furnitureManager.atticWindows[itemIndex]
            panel = FurnitureItemPanel(item, itemIndex, command = self.bringWindowFromAttic, deleteMode = self.deleteMode, helpCategory = 'FurnitureItemPanelAttic')
            self.atticWindowPanels[itemIndex] = panel
        else:
            self.atticWindowPanels[itemIndex].unload()
            del self.atticWindowPanels[itemIndex]
            for i in range(itemIndex, len(self.atticWindowPanels)):
                self.atticWindowPanels[i].itemId -= 1
            
        self.regenerateAtticPicker()

    
    def deleteWindowFromAttic(self, item, itemIndex):
        messenger.send('wakeup')
        self.furnitureManager.deleteWindowFromAttic(item, itemIndex, self._ObjectManager__deleteWindowFromAtticCallback)

    
    def _ObjectManager__deleteWindowFromAtticCallback(self, retcode, item, itemIndex):
        self._ObjectManager__resetDisabledButton()
        if retcode < 0:
            self.notify.info('Unable to delete window %s, reason %s.' % (itemIndex, retcode))
            return None
        
        self.atticWindowPanels[itemIndex].unload()
        del self.atticWindowPanels[itemIndex]
        for i in range(itemIndex, len(self.atticWindowPanels)):
            self.atticWindowPanels[i].itemId -= 1
        
        self.regenerateAtticPicker()

    
    def setGridSpacingString(self, spacingStr):
        spacing = eval(spacingStr)
        self.setGridSpacing(spacing)

    
    def setGridSpacing(self, gridSpacing):
        self.gridSpacing = gridSpacing

    
    def makeHouseExtentsBox(self):
        houseGeom = self.targetNodePath.findAllMatches('**/group*')
        targetBounds = houseGeom.getTightBounds()
        self.houseExtents = self.targetNodePath.attachNewNode('furnitureCollisionNode')
        mx = targetBounds[0][0]
        Mx = targetBounds[1][0]
        my = targetBounds[0][1]
        My = targetBounds[1][1]
        mz = targetBounds[0][2]
        Mz = targetBounds[1][2]
        cn = CollisionNode('extentsCollisionNode')
        cn.setIntoCollideMask(ToontownGlobals.GhostBitmask)
        self.houseExtents.attachNewNode(cn)
        cp = CollisionPolygon(Point3(mx, my, mz), Point3(mx, My, mz), Point3(mx, My, Mz), Point3(mx, my, Mz))
        cn.addSolid(cp)
        cp = CollisionPolygon(Point3(Mx, My, mz), Point3(Mx, my, mz), Point3(Mx, my, Mz), Point3(Mx, My, Mz))
        cn.addSolid(cp)
        cp = CollisionPolygon(Point3(Mx, my, mz), Point3(mx, my, mz), Point3(mx, my, Mz), Point3(Mx, my, Mz))
        cn.addSolid(cp)
        cp = CollisionPolygon(Point3(mx, My, mz), Point3(Mx, My, mz), Point3(Mx, My, Mz), Point3(mx, My, Mz))
        cn.addSolid(cp)

    
    def makeDoorBlocker(self):
        self.doorBlocker = self.targetNodePath.attachNewNode('doorBlocker')
        cn = CollisionNode('doorBlockerCollisionNode')
        cn.setIntoCollideMask(ToontownGlobals.FurnitureSideBitmask)
        self.doorBlocker.attachNewNode(cn)
        cs = CollisionSphere(Point3(-12, -33, 0), 7.5)
        cn.addSolid(cs)

    
    def createVerifyDialog(self, item, verifyText, okFunc, cancelFunc):
        if self.verifyFrame == None:
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            cancelButtonImage = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
            self.verifyFrame = DirectFrame(pos = (-0.40000000000000002, 0.10000000000000001, 0.29999999999999999), scale = 0.75, relief = None, image = getDefaultDialogGeom(), image_color = ToontownGlobals.GlobalDialogColor, image_scale = (1.2, 1, 1.3), text = '', text_wordwrap = 19, text_scale = 0.059999999999999998, text_pos = (0, 0.5), textMayChange = 1, sortOrder = NO_FADE_SORT_INDEX)
            self.okButton = DirectButton(parent = self.verifyFrame, image = okButtonImage, relief = None, text = OTPLocalizer.DialogOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (-0.22, 0.0, -0.5))
            self.cancelButton = DirectButton(parent = self.verifyFrame, image = cancelButtonImage, relief = None, text = OTPLocalizer.DialogCancel, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.22, 0.0, -0.5))
            self.deleteItemText = DirectLabel(parent = self.verifyFrame, relief = None, text = '', text_wordwrap = 16, pos = (0.0, 0.0, -0.40000000000000002), scale = 0.089999999999999997)
        
        self.verifyFrame['text'] = verifyText
        self.deleteItemText['text'] = item.getName()
        self.okButton['command'] = okFunc
        self.cancelButton['command'] = cancelFunc
        self.verifyFrame.show()
        (self.itemPanel, self.itemIval) = item.getPicture(base.localAvatar)
        if self.itemPanel:
            self.itemPanel.reparentTo(self.verifyFrame, -1)
            self.itemPanel.setPos(0, 0, 0.050000000000000003)
            self.itemPanel.setScale(0.34999999999999998)
            self.deleteItemText.setPos(0.0, 0.0, -0.40000000000000002)
        else:
            self.deleteItemText.setPos(0, 0, 0.070000000000000007)
        if self.itemIval:
            self.itemIval.loop()
        

    
    def _ObjectManager__handleVerifyDeleteOK(self):
        deleteFunction = self.verifyItems[0]
        deleteFunctionArgs = self.verifyItems[1:]
        self._ObjectManager__cleanupVerifyDelete()
        deleteFunction(*deleteFunctionArgs)

    
    def _ObjectManager__cleanupVerifyDelete(self, *args):
        if self.nonDeletableItem:
            self.nonDeletableItem.cleanup()
            self.nonDeletableItem = None
        
        if self.verifyFrame:
            self.verifyFrame.hide()
        
        if self.itemIval:
            self.itemIval.finish()
            self.itemIval = None
        
        if self.itemPanel:
            self.itemPanel.destroy()
            self.itemPanel = None
        
        self.verifyItems = None

    
    def _ObjectManager__setDisabledButton(self, button):
        self._ObjectManager__resetDisabledButton()
        self.disabledButton = button
        self.disabledButton['state'] = DISABLED

    
    def _ObjectManager__resetDisabledButton(self, *args):
        if self.disabledButton and not self.disabledButton.isEmpty():
            self.disabledButton['state'] = NORMAL
            self.disabledButton = None
        

    
    def _ObjectManager__resetAndCleanup(self, *args):
        self._ObjectManager__resetDisabledButton()
        self._ObjectManager__cleanupVerifyDelete()

    
    def requestDelete(self, item, itemIndex, deleteFunction):
        self._ObjectManager__cleanupVerifyDelete()
        if self.furnitureManager.ownerId != base.localAvatar.doId or not item.isDeletable():
            self.warnNonDeletableItem(item)
            return None
        
        self.createVerifyDialog(item, TTLocalizer.HDDeleteItem, self._ObjectManager__handleVerifyDeleteOK, self._ObjectManager__resetAndCleanup)
        self.verifyItems = (deleteFunction, item, itemIndex)

    
    def requestRoomDelete(self, dfitem, objectId, itemIndex):
        self._ObjectManager__cleanupVerifyDelete()
        item = dfitem.item
        if self.furnitureManager.ownerId != base.localAvatar.doId or not item.isDeletable():
            self.warnNonDeletableItem(item)
            return None
        
        self.createVerifyDialog(item, TTLocalizer.HDDeleteItem, self._ObjectManager__handleVerifyDeleteOK, self._ObjectManager__resetAndCleanup)
        self.verifyItems = (self.deleteItemFromRoom, dfitem, objectId, itemIndex)

    
    def warnNonDeletableItem(self, item):
        message = TTLocalizer.HDNonDeletableItem
        if not item.isDeletable():
            if item.getFlags() & CatalogFurnitureItem.FLBank:
                message = TTLocalizer.HDNonDeletableBank
            elif item.getFlags() & CatalogFurnitureItem.FLCloset:
                message = TTLocalizer.HDNonDeletableCloset
            elif item.getFlags() & CatalogFurnitureItem.FLPhone:
                message = TTLocalizer.HDNonDeletablePhone
            
        
        if self.furnitureManager.ownerId != base.localAvatar.doId:
            message = TTLocalizer.HDNonDeletableNotOwner % self.furnitureManager.ownerName
        
        self.nonDeletableItem = TTDialog.TTDialog(text = message, style = TTDialog.Acknowledge, fadeScreen = 0, command = self._ObjectManager__resetAndCleanup)
        self.nonDeletableItem.show()

    
    def requestReturnToAttic(self, item, objectId):
        self._ObjectManager__cleanupVerifyDelete()
        itemIndex = None
        for i in range(len(self.inRoomPanels)):
            if self.inRoomPanels[i].itemId == objectId:
                itemIndex = i
                self._ObjectManager__setDisabledButton(self.inRoomPanels[itemIndex])
                break
            
        
        if self.deleteMode:
            dfitem = self.objectDict[objectId].dfitem
            self.requestRoomDelete(dfitem, objectId, itemIndex)
            return None
        
        self.createVerifyDialog(item, TTLocalizer.HDReturnVerify, self._ObjectManager__handleVerifyReturnOK, self._ObjectManager__resetAndCleanup)
        self.verifyItems = (item, objectId)

    
    def _ObjectManager__handleVerifyReturnOK(self):
        (item, objectId) = self.verifyItems
        self._ObjectManager__cleanupVerifyDelete()
        self.pickInRoom(objectId)
        self.sendItemToAttic()

    
    def requestReturnToAtticFromTrash(self, item, itemIndex):
        self._ObjectManager__cleanupVerifyDelete()
        self._ObjectManager__setDisabledButton(self.inTrashPanels[itemIndex])
        self.createVerifyDialog(item, TTLocalizer.HDReturnFromTrashVerify, self._ObjectManager__handleVerifyReturnFromTrashOK, self._ObjectManager__resetAndCleanup)
        self.verifyItems = (item, itemIndex)

    
    def _ObjectManager__handleVerifyReturnFromTrashOK(self):
        (item, itemIndex) = self.verifyItems
        self._ObjectManager__cleanupVerifyDelete()
        self.recoverDeletedItem(item, itemIndex)

    
    def recoverDeletedItem(self, item, itemIndex):
        messenger.send('wakeup')
        self.furnitureManager.recoverDeletedItem(item, itemIndex, self._ObjectManager__recoverDeletedItemCallback)

    
    def _ObjectManager__recoverDeletedItemCallback(self, retcode, item, itemIndex):
        self._ObjectManager__cleanupVerifyDelete()
        if retcode < 0:
            if retcode == ToontownGlobals.FM_HouseFull:
                self.showHouseFullDialog()
            
            self.notify.info('Unable to recover deleted item %s, reason %s.' % (itemIndex, retcode))
            return None
        
        self._ObjectManager__resetDisabledButton()
        self.inTrashPanels[itemIndex].unload()
        del self.inTrashPanels[itemIndex]
        for i in range(itemIndex, len(self.inTrashPanels)):
            self.inTrashPanels[i].itemId -= 1
        
        self.regenerateInTrashPicker()
        itemType = item.getTypeCode()
        if itemType == CatalogItemTypes.WALLPAPER_ITEM and itemType == CatalogItemTypes.FLOORING_ITEM and itemType == CatalogItemTypes.MOULDING_ITEM or itemType == CatalogItemTypes.WAINSCOTING_ITEM:
            itemIndex = len(self.atticWallpaperPanels)
            bringCommand = self.bringWallpaperFromAttic
        elif itemType == CatalogItemTypes.WINDOW_ITEM:
            itemIndex = len(self.atticWindowPanels)
            bringCommand = self.bringWindowFromAttic
        else:
            itemIndex = len(self.atticItemPanels)
            bringCommand = self.bringItemFromAttic
        panel = FurnitureItemPanel(item, itemIndex, command = bringCommand, deleteMode = self.deleteMode, helpCategory = 'FurnitureItemPanelAttic')
        if itemType == CatalogItemTypes.WALLPAPER_ITEM and itemType == CatalogItemTypes.FLOORING_ITEM and itemType == CatalogItemTypes.MOULDING_ITEM or itemType == CatalogItemTypes.WAINSCOTING_ITEM:
            self.atticWallpaperPanels.append(panel)
        elif itemType == CatalogItemTypes.WINDOW_ITEM:
            self.atticWindowPanels.append(panel)
        else:
            self.atticItemPanels.append(panel)
        self.regenerateAtticPicker()

    
    def showHouseFullDialog(self):
        self.cleanupDialog()
        self.dialog = TTDialog.TTDialog(style = TTDialog.Acknowledge, text = TTLocalizer.HDHouseFull, text_wordwrap = 15, command = self.cleanupDialog)
        self.dialog.show()

    
    def bindHelpText(self, button, category):
        button.bind(ENTER, self.showHelpText, extraArgs = [
            category,
            None])
        button.bind(EXIT, self.hideHelpText)

    
    def showHelpText(self, category, itemName, xy):
        
        def showIt(task):
            helpText = TTLocalizer.HDHelpDict.get(category)
            if helpText:
                if itemName:
                    helpText = helpText % itemName
                
                self.helpText['text'] = helpText
                self.helpText.show()
            else:
                print 'category: %s not found'

        taskMgr.doMethodLater(0.75, showIt, 'showHelpTextDoLater')

    
    def hideHelpText(self, xy):
        taskMgr.remove('showHelpTextDoLater')
        self.helpText['text'] = ''
        self.helpText.hide()


