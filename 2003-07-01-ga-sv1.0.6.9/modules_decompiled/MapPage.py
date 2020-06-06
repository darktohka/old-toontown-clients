# File: M (Python 2.2)

import ShtikerPage
import ToontownGlobals
import PythonUtil
import ZoneUtil
from DirectGui import *
import Localizer

class MapPage(ShtikerPage.ShtikerPage):
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)

    
    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        mapModel = loader.loadModel('phase_3.5/models/gui/toontown_map')
        self.map = DirectFrame(parent = self, relief = None, image = mapModel.find('**/toontown_map'), image_scale = (1.8, 1, 1.3500000000000001), scale = 0.96999999999999997, pos = (0, 0, 0.077499999999999999))
        mapModel.removeNode()
        self.allZones = [
            ToontownGlobals.DonaldsDock,
            ToontownGlobals.ToontownCentral,
            ToontownGlobals.TheBrrrgh,
            ToontownGlobals.MinniesMelodyland,
            ToontownGlobals.DaisyGardens,
            ToontownGlobals.ConstructionZone,
            ToontownGlobals.FunnyFarm,
            ToontownGlobals.GoofyStadium,
            ToontownGlobals.DonaldsDreamland,
            ToontownGlobals.BossbotHQ,
            ToontownGlobals.SellbotHQ,
            ToontownGlobals.CashbotHQ,
            ToontownGlobals.LawbotHQ]
        self.cloudScaleList = ((-0.5,), (), (0.40000000000000002, 0.5), (0.65000000000000002,), (0.59999999999999998, -0.45000000000000001), (0.5, 0.40000000000000002), (-0.45000000000000001, -0.59999999999999998), (0.55000000000000004,), (0.59999999999999998,), (0.40000000000000002,), (0.40000000000000002,), (-0.40000000000000002,), (-0.45000000000000001,))
        self.cloudSquishList = ((1,), (), (1, 1), (0.69999999999999996,), (0.5, 0.80000000000000004), (0.84999999999999998, 0.80000000000000004), (0.69999999999999996, 0.84999999999999998), (1,), (0.65000000000000002,), (1,), (1,), (1,), (1,))
        self.cloudPosList = (((0.46999999999999997, 0.0, -0.070000000000000007),), (), ((0.29999999999999999, 0.0, 0.40000000000000002), (0.45000000000000001, 0.0, 0.29999999999999999)), ((-0.050000000000000003, 0.0, 0.23000000000000001),), ((-0.25, 0.0, -0.5), (-0.33000000000000002, 0.0, -0.40000000000000002)), ((0.28000000000000003, 0.0, -0.45000000000000001), (0.14999999999999999, 0.0, -0.45000000000000001)), ((-0.5, 0.0, 0.14999999999999999), (-0.45000000000000001, 0.0, 0.32000000000000001)), ((-0.45000000000000001, 0.0, -0.10000000000000001),), ((-0.10000000000000001, 0.0, 0.5),), ((-0.55000000000000004, 0.0, 0.5),), ((0.55000000000000004, 0.0, 0.5),), ((-0.55000000000000004, 0.0, -0.5),), ((0.55000000000000004, 0.0, -0.42999999999999999),))
        self.labelPosList = ((0.59399999999999997, 0.0, -0.074999999999999997), (0.0, 0.0, -0.20000000000000001), (0.47499999999999998, 0.0, 0.25), (0.063, 0.0, 0.14999999999999999), (-0.25, 0.0, -0.47499999999999998), (0.313, 0.0, -0.47499999999999998), (-0.438, 0.0, 0.22), (-0.55000000000000004, 0.0, -0.125), (-0.087999999999999995, 0.0, 0.46999999999999997), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
        self.labels = []
        self.clouds = []
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        buttonLoc = (0.45000000000000001, 0, -0.73999999999999999)
        if toonbase.housingEnabled:
            buttonLoc = (0.55000000000000004, 0, -0.73999999999999999)
        
        self.safeZoneButton = DirectButton(parent = self.map, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (1.3, 1.1000000000000001, 1.1000000000000001), pos = buttonLoc, text = Localizer.MapPageBackToPlayground, text_scale = 0.055, text_pos = (0, -0.02), textMayChange = 0, command = self.backToSafeZone)
        self.goHomeButton = DirectButton(parent = self.map, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (0.66000000000000003, 1.1000000000000001, 1.1000000000000001), pos = (0.14999999999999999, 0, -0.73999999999999999), text = Localizer.MapPageGoHome, text_scale = 0.055, text_pos = (0, -0.02), textMayChange = 0, command = self.goHome)
        self.goHomeButton.hide()
        guiButton.removeNode()
        self.hoodLabel = DirectLabel(parent = self.map, relief = None, pos = (-0.42999999999999999, 0, -0.72599999999999998), text = '', text_scale = 0.059999999999999998, text_pos = (0, 0), text_wordwrap = 14)
        self.hoodLabel.hide()
        cloudModel = loader.loadModel('phase_3.5/models/gui/cloud')
        cloudImage = cloudModel.find('**/cloud')
        for hood in self.allZones:
            abbrev = toonbase.tcr.hoodMgr.getNameFromId(hood)
            fullname = toonbase.tcr.hoodMgr.getFullnameFromId(hood)
            hoodIndex = self.allZones.index(hood)
            label = DirectButton(parent = self.map, relief = None, pos = self.labelPosList[hoodIndex], pad = (0.20000000000000001, 0.16), text = ('', fullname, fullname), text_bg = Vec4(1, 1, 1, 0.40000000000000002), text_scale = 0.055, rolloverSound = None, clickSound = None, pressEffect = 0, command = self._MapPage__buttonCallback, extraArgs = [
                hood])
            label.resetFrameSize()
            self.labels.append(label)
            hoodClouds = []
            for (cloudScale, cloudPos, cloudSquish) in zip(self.cloudScaleList[hoodIndex], self.cloudPosList[hoodIndex], self.cloudSquishList[hoodIndex]):
                cloud = DirectFrame(parent = self.map, relief = None, state = DISABLED, image = cloudImage, scale = (cloudScale * 1.333, abs(cloudScale), abs(cloudScale) * cloudSquish), pos = (cloudPos[0] * 1.25, cloudPos[1], cloudPos[2]))
                cloud.hide()
                hoodClouds.append(cloud)
            
            self.clouds.append(hoodClouds)
        
        cloudModel.removeNode()
        self.resetFrameSize()
        return None

    
    def unload(self):
        del self.labels
        del self.clouds
        ShtikerPage.ShtikerPage.unload(self)

    
    def enter(self):
        ShtikerPage.ShtikerPage.enter(self)
        
        try:
            zone = toonbase.tcr.playGame.getPlace().getZoneId()
        except:
            zone = 0

        if zone and ZoneUtil.isPlayground(zone) or self.book.safeMode:
            self.safeZoneButton.hide()
        else:
            self.safeZoneButton.show()
        if toonbase.localToon.estate != None and toonbase.tcr.playGame.estateLoader.atMyEstate() or self.book.safeMode:
            self.goHomeButton.hide()
        elif toonbase.housingEnabled:
            self.goHomeButton.show()
        
        if toonbase.tcr.playGame.hood == None and toonbase.tcr.playGame.estateLoader != None:
            if toonbase.tcr.playGame.estateLoader.atMyEstate():
                self.hoodLabel['text'] = Localizer.MapPageYouAreAtHome
                self.hoodLabel.show()
            else:
                avatar = toonbase.tcr.identifyAvatar(toonbase.tcr.playGame.estateLoader.estateOwnerId)
                if avatar:
                    avName = avatar.getName()
                    self.hoodLabel['text'] = Localizer.MapPageYouAreAtSomeonesHome % Localizer.GetPossesive(avName)
                    self.hoodLabel.show()
                
        elif zone:
            hoodName = ToontownGlobals.hoodNameMap.get(ZoneUtil.getHoodId(zone), ('', ''))[1]
            streetName = ToontownGlobals.StreetNames.get(ZoneUtil.getBranchZone(zone), ('', ''))[1]
            if hoodName:
                self.hoodLabel['text'] = Localizer.MapPageYouAreHere % (hoodName, streetName)
                self.hoodLabel.show()
            else:
                self.hoodLabel.hide()
        else:
            self.hoodLabel.hide()
        if toonbase.localToon.teleportCheat:
            safeZonesVisited = ToontownGlobals.Hoods
        else:
            safeZonesVisited = toonbase.localToon.safeZonesVisited
        hoodsAvailable = toonbase.tcr.hoodMgr.getAvailableZones()
        hoodVisibleList = PythonUtil.intersection(safeZonesVisited, hoodsAvailable)
        if toonbase.localToon.teleportCheat:
            hoodTeleportList = hoodVisibleList
        else:
            hoodTeleportList = toonbase.localToon.getTeleportAccess()
        for hood in self.allZones:
            label = self.labels[self.allZones.index(hood)]
            clouds = self.clouds[self.allZones.index(hood)]
            if not (self.book.safeMode) and hood in hoodVisibleList:
                label.show()
                for cloud in clouds:
                    cloud.hide()
                
                fullname = toonbase.tcr.hoodMgr.getFullnameFromId(hood)
                if hood in hoodTeleportList:
                    text = Localizer.MapPageGoTo % fullname
                    label['text'] = ('', text, text)
                else:
                    label['text'] = ('', fullname, fullname)
            else:
                label.hide()
                for cloud in clouds:
                    cloud.show()
                
        
        return None

    
    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)

    
    def backToSafeZone(self):
        self.doneStatus = {
            'mode': 'teleport',
            'hood': toonbase.localToon.lastHood }
        messenger.send(self.doneEvent)

    
    def goHome(self):
        self.doneStatus = {
            'mode': 'gohome',
            'hood': toonbase.localToon.lastHood }
        messenger.send(self.doneEvent)

    
    def _MapPage__buttonCallback(self, hood):
        if toonbase.localToon.teleportCheat or hood in toonbase.localToon.getTeleportAccess():
            self.doneStatus = {
                'mode': 'teleport',
                'hood': hood }
            messenger.send(self.doneEvent)
        


