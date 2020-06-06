# File: M (Python 2.2)

import ShtikerPage
from toontown.toonbase import ToontownGlobals
from direct.showbase import PythonUtil
from toontown.hood import ZoneUtil
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer

class MapPage(ShtikerPage.ShtikerPage):
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)

    
    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        mapModel = loader.loadModel('phase_3.5/models/gui/toontown_map')
        self.map = DirectFrame(parent = self, relief = None, image = mapModel.find('**/toontown_map'), image_scale = (1.8, 1, 1.3500000000000001), scale = 0.96999999999999997, pos = (0, 0, 0.077499999999999999))
        mapModel.removeNode()
        self.allZones = []
        for hood in ToontownGlobals.Hoods:
            self.allZones.append(hood)
        
        self.cloudScaleList = (((0.55000000000000004, 0, 0.40000000000000002), (0.34999999999999998, 0, 0.25)), (), ((0.45000000000000001, 0, 0.45000000000000001), (0.5, 0, 0.40000000000000002)), ((0.86645000000000005, 0, 0.45500000000000002),), ((0.55000000000000004, 0, 0.40000000000000002),), ((0.59999999999999998, 0, 0.40000000000000002), (0.53320000000000001, 0, 0.32000000000000001)), ((0.69999999999999996, 0, 0.45000000000000001),), ((0.69999999999999996, 0, 0.45000000000000001),), ((0.79979999999999996, 0, 0.39000000000000001),), ((0.5, 0, 0.34999999999999998),), ((-0.45000000000000001, 0, 0.40000000000000002),), ((-0.45000000000000001, 0, 0.34999999999999998),), ((0.5, 0, 0.40000000000000002),))
        self.cloudPosList = (((0.57499999999999996, 0.0, -0.040000000000000001), (0.45000000000000001, 0.0, -0.25)), (), ((0.375, 0.0, 0.40000000000000002), (0.5625, 0.0, 0.20000000000000001)), ((-0.062399999999999997, 0.0, 0.23000000000000001),), ((-0.29999999999999999, 0.0, -0.40000000000000002),), ((0.25, 0.0, -0.42499999999999999), (0.125, 0.0, -0.35999999999999999)), ((-0.45000000000000001, 0.0, 0.21249999999999999),), ((-0.5625, 0.0, -0.070000000000000007),), ((-0.125, 0.0, 0.5),), ((0.66000000000000003, 0.0, 0.5),), ((-0.68000000000000005, 0.0, -0.44400000000000001),), ((-0.59999999999999998, 0.0, 0.45000000000000001),), ((0.66000000000000003, 0.0, -0.40000000000000002),))
        self.labelPosList = ((0.59399999999999997, 0.0, -0.074999999999999997), (0.0, 0.0, -0.10000000000000001), (0.47499999999999998, 0.0, 0.25), (0.10000000000000001, 0.0, 0.14999999999999999), (-0.29999999999999999, 0.0, -0.375), (0.20000000000000001, 0.0, -0.45000000000000001), (-0.438, 0.0, 0.22), (-0.55000000000000004, 0.0, -0.125), (-0.087999999999999995, 0.0, 0.46999999999999997), (0.69999999999999996, 0.0, 0.5), (-0.69999999999999996, 0.0, -0.5), (-0.69999999999999996, 0.0, 0.5), (0.69999999999999996, 0.0, -0.5))
        self.labels = []
        self.clouds = []
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        buttonLoc = (0.45000000000000001, 0, -0.73999999999999999)
        if base.housingEnabled:
            buttonLoc = (0.55000000000000004, 0, -0.73999999999999999)
        
        self.safeZoneButton = DirectButton(parent = self.map, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (1.3, 1.1000000000000001, 1.1000000000000001), pos = buttonLoc, text = TTLocalizer.MapPageBackToPlayground, text_scale = 0.055, text_pos = (0, -0.02), textMayChange = 0, command = self.backToSafeZone)
        self.goHomeButton = DirectButton(parent = self.map, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (0.66000000000000003, 1.1000000000000001, 1.1000000000000001), pos = (0.14999999999999999, 0, -0.73999999999999999), text = TTLocalizer.MapPageGoHome, text_scale = 0.055, text_pos = (0, -0.02), textMayChange = 0, command = self.goHome)
        self.goHomeButton.hide()
        guiButton.removeNode()
        self.hoodLabel = DirectLabel(parent = self.map, relief = None, pos = (-0.42999999999999999, 0, -0.72599999999999998), text = '', text_scale = 0.059999999999999998, text_pos = (0, 0), text_wordwrap = 14)
        self.hoodLabel.hide()
        cloudModel = loader.loadModel('phase_3.5/models/gui/cloud')
        cloudImage = cloudModel.find('**/cloud')
        for hood in self.allZones:
            abbrev = base.cr.hoodMgr.getNameFromId(hood)
            fullname = base.cr.hoodMgr.getFullnameFromId(hood)
            hoodIndex = self.allZones.index(hood)
            label = DirectButton(parent = self.map, relief = None, pos = self.labelPosList[hoodIndex], pad = (0.20000000000000001, 0.16), text = ('', fullname, fullname), text_bg = Vec4(1, 1, 1, 0.40000000000000002), text_scale = 0.055, rolloverSound = None, clickSound = None, pressEffect = 0, command = self._MapPage__buttonCallback, extraArgs = [
                hood])
            label.resetFrameSize()
            self.labels.append(label)
            hoodClouds = []
            for (cloudScale, cloudPos) in zip(self.cloudScaleList[hoodIndex], self.cloudPosList[hoodIndex]):
                cloud = DirectFrame(parent = self.map, relief = None, state = DISABLED, image = cloudImage, scale = (cloudScale[0], cloudScale[1], cloudScale[2]), pos = (cloudPos[0], cloudPos[1], cloudPos[2]))
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
            zone = base.cr.playGame.getPlace().getZoneId()
        except:
            zone = 0

        if base.localAvatar.lastHood >= ToontownGlobals.BossbotHQ:
            self.safeZoneButton['text'] = TTLocalizer.MapPageBackToCogHQ
        else:
            self.safeZoneButton['text'] = TTLocalizer.MapPageBackToPlayground
        if zone and ZoneUtil.isPlayground(zone) or self.book.safeMode:
            self.safeZoneButton.hide()
        else:
            self.safeZoneButton.show()
        if base.cr.playGame.getPlaceId() == ToontownGlobals.MyEstate and base.cr.playGame.hood.loader.atMyEstate() or self.book.safeMode:
            self.goHomeButton.hide()
        elif base.housingEnabled:
            self.goHomeButton.show()
        
        if base.cr.playGame.getPlaceId() == ToontownGlobals.MyEstate:
            if base.cr.playGame.hood.loader.atMyEstate():
                self.hoodLabel['text'] = TTLocalizer.MapPageYouAreAtHome
                self.hoodLabel.show()
            else:
                avatar = base.cr.identifyAvatar(base.cr.playGame.hood.loader.estateOwnerId)
                if avatar:
                    avName = avatar.getName()
                    self.hoodLabel['text'] = TTLocalizer.MapPageYouAreAtSomeonesHome % TTLocalizer.GetPossesive(avName)
                    self.hoodLabel.show()
                
        elif zone:
            hoodName = ToontownGlobals.hoodNameMap.get(ZoneUtil.getCanonicalHoodId(zone), ('',))[-1]
            streetName = ToontownGlobals.StreetNames.get(ZoneUtil.getCanonicalBranchZone(zone), ('',))[-1]
            if hoodName:
                self.hoodLabel['text'] = TTLocalizer.MapPageYouAreHere % (hoodName, streetName)
                self.hoodLabel.show()
            else:
                self.hoodLabel.hide()
        else:
            self.hoodLabel.hide()
        if base.localAvatar.teleportCheat:
            safeZonesVisited = ToontownGlobals.Hoods
        else:
            safeZonesVisited = base.localAvatar.hoodsVisited
        hoodsAvailable = base.cr.hoodMgr.getAvailableZones()
        hoodVisibleList = PythonUtil.intersection(safeZonesVisited, hoodsAvailable)
        if base.localAvatar.teleportCheat:
            hoodTeleportList = hoodVisibleList
        else:
            hoodTeleportList = base.localAvatar.getTeleportAccess()
        for hood in self.allZones:
            label = self.labels[self.allZones.index(hood)]
            clouds = self.clouds[self.allZones.index(hood)]
            if not (self.book.safeMode) and hood in hoodVisibleList:
                label.show()
                for cloud in clouds:
                    cloud.hide()
                
                fullname = base.cr.hoodMgr.getFullnameFromId(hood)
                if hood in hoodTeleportList:
                    text = TTLocalizer.MapPageGoTo % fullname
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
            'hood': base.localAvatar.lastHood }
        messenger.send(self.doneEvent)

    
    def goHome(self):
        self.doneStatus = {
            'mode': 'gohome',
            'hood': base.localAvatar.lastHood }
        messenger.send(self.doneEvent)

    
    def _MapPage__buttonCallback(self, hood):
        if base.localAvatar.teleportCheat and hood in base.cr.playGame.Hood2StateDict.keys() or hood in base.localAvatar.getTeleportAccess():
            self.doneStatus = {
                'mode': 'teleport',
                'hood': hood }
            messenger.send(self.doneEvent)
        


