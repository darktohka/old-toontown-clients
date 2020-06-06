# File: C (Python 2.2)

import DirectNotifyGlobal
import FSM
import State
import Hood

class CogHood(Hood.Hood):
    notify = DirectNotifyGlobal.directNotify.newCategory('CogHood')
    
    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        Hood.Hood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.fsm = FSM.FSM('Hood', [
            State.State('start', self.enterStart, self.exitStart, [
                'cogHQLoader']),
            State.State('cogHQLoader', self.enterCogHQLoader, self.exitCogHQLoader, [
                'quietZone']),
            State.State('quietZone', self.enterQuietZone, self.exitQuietZone, [
                'cogHQLoader']),
            State.State('final', self.enterFinal, self.exitFinal, [])], 'start', 'final')
        self.fsm.enterInitialState()

    
    def enterCogHQLoader(self, requestStatus):
        self.accept(self.loaderDoneEvent, self.handleCogHQLoaderDone)
        self.loader.enter(requestStatus)
        self.spawnTitleText(requestStatus['zoneId'])

    
    def exitCogHQLoader(self):
        taskMgr.remove('titleText')
        self.hideTitleText()
        self.ignore(self.loaderDoneEvent)
        self.loader.exit()
        self.loader.unload()
        del self.loader

    
    def handleCogHQLoaderDone(self):
        doneStatus = self.loader.getDoneStatus()
        if self.isSameHood(doneStatus):
            self.fsm.request('quietZone', [
                doneStatus])
        else:
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)


