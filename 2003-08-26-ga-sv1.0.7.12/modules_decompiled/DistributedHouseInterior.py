# File: D (Python 2.2)

from ToontownGlobals import *
from ToonBaseGlobal import *
from PandaModules import *
from IntervalGlobal import *
from ClockDelta import *
import DirectNotifyGlobal
import DistributedObject
import DNADoor
import HouseGlobals
import CatalogItemList
import CatalogItem
WindowPlugNames = ('**/windowcut_a*', '**/windowcut_b*', '**/windowcut_c*', '**/windowcut_d*', '**/windowcut_e*', '**/windowcut_f*')
RoomNames = ('**/group2', '**/group1')
WallNames = ('ceiling*', 'wall_side_middle*', 'wall_front_middle*', 'windowcut_*')
MouldingNames = ('wall_side_top*', 'wall_front_top*')
FloorNames = ('floor*',)
WainscotingNames = ('wall_side_bottom*', 'wall_front_bottom*')
BorderNames = ('wall_side_middle*_border', 'wall_front_middle*_border', 'windowcut_*_border')
WallpaperPieceNames = (WallNames, MouldingNames, FloorNames, WainscotingNames, BorderNames)

class DistributedHouseInterior(DistributedObject.DistributedObject):
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.houseId = 0
        self.houseIndex = 0
        self.interior = None
        self.exteriorWindowsHidden = 0

    
    def generate(self):
        DistributedObject.DistributedObject.generate(self)

    
    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        self.setup()

    
    def disable(self):
        self.interior.removeNode()
        del self.interior

    
    def delete(self):
        self.ignore(self.uniqueName('enterclosetSphere'))
        DistributedObject.DistributedObject.delete(self)

    
    def setup(self):
        dnaStore = toonbase.tcr.playGame.dnaStore
        self.interior = loader.loadModel('phase_5.5/models/estate/house_interiorA.bam')
        self.interior.reparentTo(render)
        doorModelName = 'door_double_round_ur'
        if doorModelName[-1:] == 'r':
            doorModelName = doorModelName[:-1] + 'l'
        else:
            doorModelName = doorModelName[:-1] + 'r'
        door = dnaStore.findNode(doorModelName)
        door_origin = self.interior.find('**/door_origin')
        door_origin.setH(180)
        doorNP = door.copyTo(door_origin)
        doorNP.ls()
        door_origin.setScale(0.80000000000000004, 0.80000000000000004, 0.80000000000000004)
        door_origin.setPos(door_origin, 0, -0.025000000000000001, 0)
        houseColor = HouseGlobals.atticWood
        color = Vec4(houseColor[0], houseColor[1], houseColor[2], 1)
        DNADoor.DNADoor.setupDoor(doorNP, self.interior, door_origin, dnaStore, str(self.houseId), color)
        doorFrame = doorNP.find('door_*_flat')
        doorFrame.wrtReparentTo(self.interior)
        doorFrame.setColor(color)
        self.interior.flattenMedium()
        self.windowSlots = []
        for name in WindowPlugNames:
            plugNodes = self.interior.findAllMatches(name)
            if plugNodes.isEmpty():
                self.windowSlots.append((None, None))
            else:
                viewBase = plugNodes[0].getParent().attachNewNode('view')
                viewBase.setTransform(plugNodes[0].getTransform())
                plug = plugNodes[0].getParent().attachNewNode('plug')
                plugNodes.reparentTo(plug)
                plug.flattenLight()
                self.windowSlots.append((plug, viewBase))
        
        self.windowSlots[2][1].setPosHpr(16.0, -12.0, 5.5099999999999998, -90, 0, 0)
        self.windowSlots[4][1].setPosHpr(-12.0, 26.0, 5.5099999999999998, 0, 0, 0)
        self._DistributedHouseInterior__colorWalls()
        self._DistributedHouseInterior__setupWindows()

    
    def _DistributedHouseInterior__colorWalls(self):
        if not (self.wallpaper):
            self.notify.info('No wallpaper in interior; clearing.')
            for str in WallNames + WainscotingNames:
                nodes = self.interior.findAllMatches('**/%s' % str)
                for node in nodes.asList():
                    node.setTextureOff(1)
                
            
            return None
        
        numRooms = min(len(self.wallpaper) / 4, len(RoomNames))
        for room in range(numRooms):
            roomName = RoomNames[room]
            roomNode = self.interior.find(roomName)
            if not roomNode.isEmpty():
                for surface in range(4):
                    slot = room * 4 + surface
                    wallpaper = self.wallpaper[slot]
                    color = wallpaper.getColor()
                    texture = wallpaper.loadTexture()
                    color2 = wallpaper.getColor2()
                    texture2 = wallpaper.loadTexture2()
                    for str in WallpaperPieceNames[surface]:
                        nodes = roomNode.findAllMatches('**/%s' % str)
                        for node in nodes.asList():
                            if str == 'ceiling*':
                                (r, g, b, a) = color
                                scale = 0.66000000000000003
                                r *= scale
                                g *= scale
                                b *= scale
                                node.setColorScale(r, g, b, a)
                            else:
                                node.setColorScale(*color)
                                node.setTexture(texture, 1)
                        
                        nodes = roomNode.findAllMatches('**/%s_border' % str)
                        for node in nodes.asList():
                            node.setColorScale(*color2)
                            node.setTexture(texture2, 1)
                        
                    
                
            
        
        nodes = self.interior.findAllMatches('**/arch*')
        for node in nodes.asList():
            node.setColorScale(*HouseGlobals.archWood + (1,))
        

    
    def _DistributedHouseInterior__setupWindows(self):
        for (plug, viewBase) in self.windowSlots:
            if plug:
                plug.show()
            
            if viewBase:
                viewBase.getChildren().detach()
            
        
        if not (self.windows):
            self.notify.info('No windows in interior; returning.')
            return None
        
        for item in self.windows:
            (plug, viewBase) = self.windowSlots[item.placement]
            if plug:
                plug.hide()
            
            if viewBase:
                model = item.loadModel()
                model.reparentTo(viewBase)
                if self.exteriorWindowsHidden:
                    model.findAllMatches('**/outside').stash()
                
            
        

    
    def hideExteriorWindows(self):
        self.exteriorWindowsHidden = 1
        for item in self.windows:
            (plug, viewBase) = self.windowSlots[item.placement]
            if viewBase:
                viewBase.findAllMatches('**/outside').stash()
            
        

    
    def showExteriorWindows(self):
        self.exteriorWindowsHidden = 0
        for item in self.windows:
            (plug, viewBase) = self.windowSlots[item.placement]
            if viewBase:
                viewBase.findAllMatches('**/outside;+s').unstash()
            
        

    
    def setHouseId(self, index):
        self.houseId = index

    
    def setHouseIndex(self, index):
        self.houseIndex = index

    
    def setWallpaper(self, items):
        self.wallpaper = CatalogItemList.CatalogItemList(items, store = CatalogItem.Customization)
        if self.interior:
            self._DistributedHouseInterior__colorWalls()
        

    
    def setWindows(self, items):
        self.windows = CatalogItemList.CatalogItemList(items, store = CatalogItem.Customization | CatalogItem.WindowPlacement)
        if self.interior:
            self._DistributedHouseInterior__setupWindows()
        

    
    def testWallpaperCombo(self, wallpaperType, wallpaperColorIndex, mouldingType, mouldingColorIndex, flooringType, flooringColorIndex, wainscotingType, wainscotingColorIndex):
        import CatalogWallpaperItem
        wallpaperItem = CatalogWallpaperItem.CatalogWallpaperItem(wallpaperType, wallpaperColorIndex)
        mouldingItem = CatalogWallpaperItem.CatalogWallpaperItem(mouldingType, mouldingColorIndex)
        flooringItem = CatalogWallpaperItem.CatalogWallpaperItem(flooringType, flooringColorIndex)
        wainscotingItem = CatalogWallpaperItem.CatalogWallpaperItem(wainscotingType, wainscotingColorIndex)
        self.wallpaper = CatalogItemList.CatalogItemList([
            wallpaperItem,
            mouldingItem,
            flooringItem,
            wainscotingItem,
            wallpaperItem,
            mouldingItem,
            flooringItem,
            wainscotingItem], store = CatalogItem.Customization)
        if self.interior:
            self._DistributedHouseInterior__colorWalls()
        

    
    def colorWallsNew(self, wallpaperList = None):
        if not wallpaperList:
            self.notify.info('No wallpaper in interior; clearing.')
            for str in WallNames + WainscotingNames:
                nodes = self.interior.findAllMatches('**/%s' % str)
                for node in nodes.asList():
                    node.setTextureOff(1)
                
            
            return None
        
        numRooms = min(len(wallpaperList) / 5, len(RoomNames))
        for room in range(numRooms):
            roomName = RoomNames[room]
            roomNode = self.interior.find(roomName)
            if not roomNode.isEmpty():
                for surface in range(5):
                    slot = room * 5 + surface
                    wallpaper = wallpaperList[slot]
                    color = wallpaper.getColor()
                    texture = wallpaper.loadTexture()
                    for str in WallpaperPieceNames[surface]:
                        nodes = roomNode.findAllMatches('**/%s' % str)
                        for node in nodes.asList():
                            if str == 'ceiling*':
                                (r, g, b, a) = color
                                scale = 0.66000000000000003
                                r *= scale
                                g *= scale
                                b *= scale
                                node.setColorScale(r, g, b, a)
                            else:
                                node.setColorScale(*color)
                                node.setTexture(texture, 1)
                        
                    
                
            
        
        nodes = self.interior.findAllMatches('**/arch*')
        for node in nodes.asList():
            node.setColorScale(*HouseGlobals.archWood + (1,))
        

    
    def testWallpaperComboNew(self, wallpaperType, wallpaperColorIndex, mouldingType = 151, mouldingColorIndex = 1000, flooringType = 105, flooringColorIndex = 1000, wainscotingType = 201, wainscotingColorIndex = 1000, borderType = 250, borderColorIndex = 1000):
        import CatalogWallpaperItem
        wallpaperItem = CatalogWallpaperItem.CatalogWallpaperItemNew(wallpaperType, wallpaperColorIndex)
        mouldingItem = CatalogWallpaperItem.CatalogWallpaperItemNew(mouldingType, mouldingColorIndex)
        flooringItem = CatalogWallpaperItem.CatalogWallpaperItemNew(flooringType, flooringColorIndex)
        wainscotingItem = CatalogWallpaperItem.CatalogWallpaperItemNew(wainscotingType, wainscotingColorIndex)
        borderItem = CatalogWallpaperItem.CatalogWallpaperItemNew(borderType, borderColorIndex)
        wallpaper = CatalogItemList.CatalogItemList([
            wallpaperItem,
            mouldingItem,
            flooringItem,
            wainscotingItem,
            borderItem] * 2, store = CatalogItem.Customization)
        if self.interior:
            self.colorWallsNew(wallpaper)
        


