# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\ai\HalloweenHolidayDecorator.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
import HolidayDecorator
from toontown.toonbase import ToontownGlobals
from toontown.safezone import Playground
from toontown.town import Street
from toontown.estate import Estate
from pandac.PandaModules import Vec4, loadDNAFile, CSDefault, TransformState, NodePath, TransparencyAttrib

class HalloweenHolidayDecorator(HolidayDecorator.HolidayDecorator):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('HalloweenHolidayDecorator')

    def __init__(self):
        HolidayDecorator.HolidayDecorator.__init__(self)

    def __checkStreetValidity(self):
        if hasattr(base.cr.playGame, 'getPlace') and base.cr.playGame.getPlace() and isinstance(base.cr.playGame.getPlace(), Street.Street) and hasattr(base.cr.playGame.getPlace(), 'loader') and base.cr.playGame.getPlace().loader and hasattr(base.cr.playGame.getPlace().loader, 'geom') and base.cr.playGame.getPlace().loader.geom:
            return True
        else:
            if hasattr(base.cr.playGame, 'getPlace') and base.cr.playGame.getPlace():
                self.notify.debug('Failed Street Check %s' % base.cr.playGame.getPlace())
            else:
                self.notify.debug('Failed Street Check')
            return False

    def __checkHoodValidity(self):
        if hasattr(base.cr.playGame, 'getPlace') and base.cr.playGame.getPlace() and (isinstance(base.cr.playGame.getPlace(), Playground.Playground) or isinstance(base.cr.playGame.getPlace(), Estate.Estate)) and hasattr(base.cr.playGame.getPlace(), 'loader') and base.cr.playGame.getPlace().loader and hasattr(base.cr.playGame.getPlace().loader, 'hood') and base.cr.playGame.getPlace().loader.hood and hasattr(base.cr.playGame.getPlace().loader.hood, 'loader') and base.cr.playGame.getPlace().loader.hood.loader and hasattr(base.cr.playGame.getPlace().loader.hood.loader, 'geom') and base.cr.playGame.getPlace().loader.hood.loader.geom:
            return True
        else:
            if hasattr(base.cr.playGame, 'getPlace') and base.cr.playGame.getPlace():
                self.notify.debug('Failed Hood Check %s' % base.cr.playGame.getPlace())
            else:
                self.notify.debug('Failed Hood Check')
            return False

    def __startSpookySky(self):
        if (self.__checkHoodValidity() or self.__checkStreetValidity()) and hasattr(base.cr.playGame.hood, 'sky') and base.cr.playGame.hood.sky:
            base.cr.playGame.hood.startSpookySky()

    def __stopSpookySky(self):
        if (self.__checkHoodValidity() or self.__checkStreetValidity()) and hasattr(base.cr.playGame.hood, 'sky') and base.cr.playGame.hood.sky:
            base.cr.playGame.hood.endSpookySky()

    def decorate(self):
        self.updateHoodDNAStore()
        self.swapIval = self.getSwapVisibleIval()
        if self.swapIval:
            self.swapIval.start()

        def __lightDecorationOn__():
            place = base.cr.playGame.getPlace()
            if hasattr(place, 'halloweenLights'):
                if not self.__checkStreetValidity():
                    return
                else:
                    place.halloweenLights = place.loader.geom.findAllMatches('**/*light*')
                    place.halloweenLights += place.loader.geom.findAllMatches('**/*lamp*')
                    place.halloweenLights += place.loader.geom.findAllMatches('**/prop_snow_tree*')
                    for light in place.halloweenLights:
                        light.setColorScaleOff(0)

            else:
                if not self.__checkHoodValidity():
                    return
                place.loader.hood.halloweenLights = place.loader.hood.loader.geom.findAllMatches('**/*light*')
                place.loader.hood.halloweenLights += place.loader.hood.loader.geom.findAllMatches('**/*lamp*')
                place.loader.hood.halloweenLights += place.loader.hood.loader.geom.findAllMatches('**/prop_snow_tree*')
                for light in place.loader.hood.halloweenLights:
                    light.setColorScaleOff(0)

        holidayIds = base.cr.newsManager.getDecorationHolidayId()
        if ToontownGlobals.HALLOWEEN_COSTUMES not in holidayIds:
            return
        if (self.__checkHoodValidity() or self.__checkStreetValidity()) and hasattr(base.cr.playGame, 'hood') and base.cr.playGame.hood and hasattr(base.cr.playGame.hood, 'sky') and base.cr.playGame.hood.sky:
            preShow = Sequence(Parallel(LerpColorScaleInterval(base.cr.playGame.hood.sky, 1.5, Vec4(1, 1, 1, 0.25)), LerpColorScaleInterval(base.cr.playGame.hood.loader.geom, 2.5, Vec4(0.55, 0.55, 0.65, 1)), Func(__lightDecorationOn__)), Func(self.__startSpookySky))
            preShow.start()
        distributedEstate = base.cr.doFind('DistributedEstate')
        if distributedEstate:
            distributedEstate.loadWitch()

    def undecorate(self):
        if (self.__checkHoodValidity() or self.__checkStreetValidity()) and hasattr(base.cr.playGame.hood, 'sky') and base.cr.playGame.hood.sky:
            postShow = Sequence(Parallel(LerpColorScaleInterval(base.cr.playGame.hood.sky, 1.5, Vec4(1, 1, 1, 1)), LerpColorScaleInterval(base.cr.playGame.hood.loader.geom, 2.5, Vec4(1, 1, 1, 1))), Func(self.__stopSpookySky))
            postShow.start()
        distributedEstate = base.cr.doFind('DistributedEstate')
        if distributedEstate:
            distributedEstate.unloadWitch()
        holidayIds = base.cr.newsManager.getDecorationHolidayId()
        if len(holidayIds) > 0:
            self.decorate()
            return
        storageFile = base.cr.playGame.hood.storageDNAFile
        if storageFile:
            loadDNAFile(self.dnaStore, storageFile, CSDefault)
        self.swapIval = self.getSwapVisibleIval()
        if self.swapIval:
            self.swapIval.start()