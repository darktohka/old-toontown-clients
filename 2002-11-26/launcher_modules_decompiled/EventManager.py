# File: E (Python 2.2)

from libpandaexpressModules import *
from MessengerGlobal import *
from TaskManagerGlobal import *
from DirectNotifyGlobal import *

class EventManager:
    notify = None
    
    def __init__(self):
        if EventManager.notify == None:
            EventManager.notify = directNotify.newCategory('EventManager')
        
        self.eventQueue = EventQueue.getGlobalEventQueue()
        self.eventHandler = EventHandler(self.eventQueue)

    
    def eventLoop(self, task):
        while not self.eventQueue.isQueueEmpty():
            self.processEvent(self.eventQueue.dequeueEvent())
        return Task.cont

    
    def parseEventParameter(self, eventParameter):
        if eventParameter.isInt():
            return eventParameter.getIntValue()
        elif eventParameter.isDouble():
            return eventParameter.getDoubleValue()
        elif eventParameter.isString():
            return eventParameter.getStringValue()
        else:
            return eventParameter.getPtr()

    
    def processEvent(self, event):
        eventName = event.getName()
        if eventName:
            paramList = []
            for i in range(event.getNumParameters()):
                eventParameter = event.getParameter(i)
                eventParameterData = self.parseEventParameter(eventParameter)
                paramList.append(eventParameterData)
            
            if EventManager.notify.getDebug() and eventName != 'NewFrame':
                EventManager.notify.debug('received C++ event named: ' + eventName + ' parameters: ' + `paramList`)
            
            if paramList:
                messenger.send(eventName, paramList)
            else:
                messenger.send(eventName)
            self.eventHandler.dispatchEvent(event)
        else:
            EventManager.notify.warning('unnamed event in processEvent')

    
    def restart(self):
        taskMgr.add(self.eventLoop, 'eventManager')

    
    def shutdown(self):
        taskMgr.remove('eventManager')


