# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\showbase\EventGroup.py
__all__ = [
 'EventGroup']
from direct.showbase import DirectObject
from direct.showbase.PythonUtil import SerialNumGen, Functor

class EventGroup(DirectObject.DirectObject):
    __module__ = __name__
    _SerialNumGen = SerialNumGen()

    def __init__(self, name, subEvents=None, doneEvent=None):
        self._name = name
        self._subEvents = set()
        self._completedEvents = set()
        if doneEvent is None:
            doneEvent = 'EventGroup-%s-%s-Done' % (EventGroup._SerialNumGen.next(), self._name)
        self._doneEvent = doneEvent
        self._completed = False
        if subEvents is not None:
            for event in subEvents:
                self.addEvent(event)

        return

    def destroy(self):
        if hasattr(self, '_name'):
            del self._name
            del self._subEvents
            del self._completedEvents
            self.ignoreAll()

    def getName(self):
        return self._name

    def getDoneEvent(self):
        return self._doneEvent

    def isCompleted(self):
        return self._completed

    def addEvent(self, eventName):
        if self._completed:
            self.notify.error("addEvent('%s') called on completed EventGroup '%s'" % (eventName, self.getName()))
        if eventName in self._subEvents:
            self.notify.error("addEvent('%s'): event already in EventGroup '%s'" % (eventName, self.getName()))
        self._subEvents.add(eventName)
        self.acceptOnce(eventName, Functor(self._subEventComplete, eventName))
        return eventName

    def newEvent(self, name):
        return self.addEvent('%s-SubEvent-%s-%s' % (self._name, EventGroup._SerialNumGen.next(), name))

    def _subEventComplete(self, subEventName, *args, **kwArgs):
        if subEventName in self._completedEvents:
            self.notify.warning("_subEventComplete: '%s' already received" % subEventName)
        else:
            self._completedEvents.add(subEventName)
            if self._completedEvents == self._subEvents:
                self._signalComplete()

    def _signalComplete(self):
        self._completed = True
        messenger.send(self._doneEvent)
        self.destroy()

    def __repr__(self):
        return "%s('%s', %s, doneEvent='%s') # completed=%s" % (self.__class__.__name__, self._name, tuple(self._subEvents), self._doneEvent, tuple(self._completedEvents))