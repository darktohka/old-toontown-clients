# File: E (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToonBaseGlobal import *
from toontown.toonbase.ToontownGlobals import *
from toontown.distributed.ToontownMsgTypes import *
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.fsm import State
from toontown.minigame import Purchase
from otp.avatar import DistributedAvatar
import SkyUtil
import Hood
from toontown.estate import EstateLoader
from toontown.estate import HouseGlobals
import ZoneUtil

class EstateHood(Hood.Hood):
    notify = DirectNotifyGlobal.directNotify.newCategory('EstateHood')
    
    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        Hood.Hood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.fsm = ClassicFSM.ClassicFSM('Hood', [
            State.State('start', self.enterStart, self.exitStart, [
                'safeZoneLoader']),
            State.State('safeZoneLoader', self.enterSafeZoneLoader, self.exitSafeZoneLoader, [
                'quietZone']),
            State.State('quietZone', self.enterQuietZone, self.exitQuietZone, [
                'safeZoneLoader']),
            State.State('final', self.enterFinal, self.exitFinal, [])], 'start', 'final')
        self.fsm.enterInitialState()
        self.id = MyEstate
        self.safeZoneLoaderClass = EstateLoader.EstateLoader
        self.storageDNAFile = 'phase_5.5/dna/storage_estate.dna'
        self.holidayStorageDNADict = {
            WINTER_DECORATIONS: [
                'phase_5.5/dna/winter_storage_estate.dna'] }
        self.skyFile = 'phase_3.5/models/props/TT_sky'
        self.popupInfo = None

    
    def load(self):
        Hood.Hood.load(self)

    
    def unload(self):
        del self.safeZoneLoaderClass
        if self.popupInfo:
            self.popupInfo.destroy()
            self.popupInfo = None
        
        if not wantOtpServer:
            base.cr.disableAll()
        
        Hood.Hood.unload(self)

    
    def enter(self, requestStatus):
        hoodId = requestStatus['hoodId']
        zoneId = requestStatus['zoneId']
        self.accept('kickToPlayground', self.kickToPlayground)
        self.fsm.request(requestStatus['loader'], [
            requestStatus])

    
    def exit(self):
        if self.loader:
            self.loader.exit()
            self.loader.unload()
            del self.loader
        
        Hood.Hood.exit(self)

    
    def loadLoader(self, requestStatus):
        loaderName = requestStatus['loader']
        if loaderName == 'safeZoneLoader':
            self.loader = self.safeZoneLoaderClass(self, self.fsm.getStateNamed('safeZoneLoader'), self.loaderDoneEvent)
            self.loader.load()
        

    
    def spawnTitleText(self, zoneId):
        return None

    
    def hideTitleTextTask(self, task):
        return Task.done

    
    def kickToPlayground(self, retCode):
        if retCode == 0:
            msg = TTLocalizer.EstateOwnerLeftMessage % HouseGlobals.BOOT_GRACE_PERIOD
            self._EstateHood__popupKickoutMessage(msg)
        elif retCode == 1:
            zoneId = base.localAvatar.lastHood
            self.doneStatus = {
                'loader': ZoneUtil.getBranchLoaderName(zoneId),
                'where': ZoneUtil.getToonWhereName(zoneId),
                'how': 'teleportIn',
                'hoodId': zoneId,
                'zoneId': zoneId,
                'shardId': None,
                'avId': -1 }
            messenger.send(self.doneEvent)
        elif retCode == 2:
            zoneId = base.localAvatar.lastHood
            self.doneStatus = {
                'loader': ZoneUtil.getBranchLoaderName(zoneId),
                'where': ZoneUtil.getToonWhereName(zoneId),
                'how': 'teleportIn',
                'hoodId': zoneId,
                'zoneId': zoneId,
                'shardId': None,
                'avId': -1 }
            messenger.send(self.doneEvent)
        else:
            self.notify.error('unknown reason for exiting estate')

    
    def _EstateHood__popupKickoutMessage(self, msg):
        if self.popupInfo != None:
            self.popupInfo.destroy()
            self.popupInfo = None
        
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
        self.popupInfo = DirectFrame(parent = hidden, relief = None, state = 'normal', text = msg, frameSize = (-1, 1, -1, 1), text_wordwrap = 10, geom = getDefaultDialogGeom(), geom_color = GlobalDialogColor, geom_scale = (0.88, 1, 0.75), geom_pos = (0, 0, -0.080000000000000002), text_scale = 0.080000000000000002, text_pos = (0, 0.10000000000000001))
        DirectButton(self.popupInfo, image = okButtonImage, relief = None, text = TTLocalizer.EstatePopupOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.0, 0.0, -0.29999999999999999), command = self._EstateHood__handleKickoutOk)
        buttons.removeNode()
        self.popupInfo.reparentTo(aspect2d)

    
    def _EstateHood__handleKickoutOk(self):
        self.popupInfo.reparentTo(hidden)

    
    def skyTrack(self, task):
        return SkyUtil.cloudSkyTrack(task)

    
    def startSky(self):
        SkyUtil.startCloudSky(self)
        if base.cloudPlatformsEnabled:
            self.loader.startCloudPlatforms()
        

    
    def stopSky(self):
        Hood.Hood.stopSky(self)
        self.loader.stopCloudPlatforms()


