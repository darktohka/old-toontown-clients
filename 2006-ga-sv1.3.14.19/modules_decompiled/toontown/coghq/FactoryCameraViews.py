# File: F (Python 2.2)

from pandac.PandaModules import *
from direct.showbase.PythonUtil import Functor
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal

class FactoryCameraViews:
    notify = DirectNotifyGlobal.directNotify.newCategory('FactoryCameraViews')
    
    def __init__(self, factory):
        self.factory = factory
        av = base.localAvatar
        self.views = [
            [
                'signatureRoomView',
                (Point3(0.0, -14.8419799805, 13.212685584999999), Point3(0.0, -13.956348419199999, 12.749215125999999), Point3(0.0, 1.5, 15.75), Point3(0.0, 1.5, -3.9375), 1),
                [
                    'battleBlocker-20063',
                    'battleBlocker-20064',
                    'battleBlocker-20065',
                    'battleBlocker-20066',
                    'battleBlocker-20114']],
            [
                'lookoutTrigger',
                (Point3(0, -17.699999999999999, 28.800000000000001), Point3(0, 10, 0), Point3(0.0, 1.5, 15.75), Point3(0.0, 1.5, -3.9375), 1),
                []]]
        camHeight = av.getClampedAvatarHeight()
        for i in range(len(self.views)):
            camPos = self.views[i][1]
            av.auxCameraPositions.append(camPos)
            factory.accept('enter' + self.views[i][0], Functor(self.switchCamPos, i))
            for msg in self.views[i][2]:
                factory.accept(msg, Functor(self.switchCamPos, i))
            
        

    
    def delete(self):
        for i in range(len(self.views)):
            factory.ignore('enter' + self.views[i][0])
            factory.ignore('exit' + self.views[i][0])
            for msg in self.views[i][2]:
                factory.ignore(msg)
            
        
        av = base.localAvatar
        av.setCameraPositionByIndex(0)
        del self.views

    
    def switchCamPos(self, viewIndex, colEntry = None):
        av = base.localAvatar
        prevView = av.cameraIndex
        av.accept('exit' + self.views[viewIndex][0], Functor(self.prevCamPos, prevView))
        self.notify.info('auto-switching to camera position %s' % viewIndex)
        av.setCameraSettings(self.views[viewIndex][1])

    
    def prevCamPos(self, index, colEntry = None):
        av = base.localAvatar
        if len(av.cameraPositions) > index:
            av.setCameraPositionByIndex(index)
        


