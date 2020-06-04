# File: H (Python 2.2)

import ToontownGlobals
from IntervalGlobal import Parallel, Sequence, Func, Wait
from PandaModules import Vec4, loadDNAFile, CSDefault, TransformState, NodePath

class HolidayDecorator:
    
    def __init__(self):
        self.dnaStore = toonbase.tcr.playGame.dnaStore
        self.swapIval = None

    
    def exit(self):
        if self.swapIval is not None and self.swapIval.isPlaying():
            self.swapIval.finish()
        

    
    def decorate(self):
        self.updateHoodDNAStore()
        self.swapIval = self.getSwapVisibleIval()
        if self.swapIval:
            self.swapIval.start()
        

    
    def undecorate(self):
        storageFile = toonbase.tcr.playGame.hood.storageDNAFile
        if storageFile:
            loadDNAFile(self.dnaStore, storageFile, CSDefault)
        
        self.swapIval = self.getSwapVisibleIval()
        if self.swapIval:
            self.swapIval.start()
        

    
    def updateHoodDNAStore(self):
        hood = toonbase.tcr.playGame.hood
        holidayId = toonbase.tcr.newsManager.getDecorationHolidayId()
        for storageFile in hood.holidayStorageDNADict.get(holidayId, []):
            loadDNAFile(self.dnaStore, storageFile, CSDefault)
        

    
    def getSwapVisibleIval(self, wait = 5.0, tFadeOut = 3.0, tFadeIn = 3.0):
        loader = toonbase.tcr.playGame.hood.loader
        npl = render.findAllMatches('**/=DNARoot=holiday_prop;+s')
        p = Parallel()
        for i in range(npl.getNumPaths()):
            np = npl.getPath(i)
            np.setTransparency(1)
            if not np.hasTag('DNACode'):
                continue
            
            dnaCode = np.getTag('DNACode')
            dnaNode = self.dnaStore.findNode(dnaCode)
            if dnaNode.isEmpty():
                continue
            
            newNP = dnaNode.copyTo(np.getParent())
            newNP.setTag('DNARoot', 'holiday_prop')
            newNP.setTag('DNACode', dnaCode)
            newNP.setColorScale(1, 1, 1, 0)
            newNP.setTransparency(1)
            if np.hasTag('transformIndex'):
                index = int(np.getTag('transformIndex'))
                transform = loader.holidayPropTransforms.get(index, TransformState.makeIdentity())
                newNP.setTransform(NodePath(), transform)
                newNP.setTag('transformIndex', `index`)
            
            s = Sequence(Wait(wait), np.colorScaleInterval(tFadeOut, Vec4(1, 1, 1, 0), startColorScale = Vec4(1, 1, 1, 1), blendType = 'easeInOut'), Func(np.detachNode), Func(np.clearTransparency), newNP.colorScaleInterval(tFadeOut, Vec4(1, 1, 1, 1), startColorScale = Vec4(1, 1, 1, 0), blendType = 'easeInOut'), Func(newNP.clearTransparency), Func(newNP.clearColorScale))
            p.append(s)
        
        return p


