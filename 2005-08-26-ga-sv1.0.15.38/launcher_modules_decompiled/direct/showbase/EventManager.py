# File: E (Python 2.2)

from MessengerGlobal import *
from direct.task.TaskManagerGlobal import *
from direct.directnotify.DirectNotifyGlobal import *

class EventManager:
    notify = None
    
    def __init__(self, eventQueue = None):
        if EventManager.notify == None:
            EventManager.notify = directNotify.newCategory('EventManager')
        
        self.eventQueue = eventQueue
        self.eventHandler = None

    
    def doEvents(self):
        while not self.eventQueue.isQueueEmpty():
            self.processEvent(self.eventQueue.dequeueEvent())

    
    def eventLoopTask(self, task):
        self.doEvents()
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
            if self.eventHandler:
                self.eventHandler.dispatchEvent(event)
            
        else:
            EventManager.notify.warning('unnamed event in processEvent')

    
    def restart(self):
        EventQueue = EventQueue
        EventHandler = EventHandler
        import pandac.PandaModules
        if self.eventQueue == None:
            self.eventQueue = EventQueue.getGlobalEventQueue()
        
        if self.eventHandler == None:
            if self.eventQueue == EventQueue.getGlobalEventQueue():
                self.eventHandler = EventHandler.getGlobalEventHandler(self.eventQueue)
            else:
                self.eventHandler = EventHandler(self.eventQueue)
        
        taskMgr.add(self.eventLoopTask, 'eventManager')

    
    def shutdown(self):
        taskMgr.remove('eventManager')


