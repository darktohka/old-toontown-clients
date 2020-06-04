# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\parties\activityFSMMixins.py
from BaseActivityFSM import BaseActivityFSM

class IdleMixin:
    __module__ = __name__

    def enterIdle(self, *args):
        BaseActivityFSM.notify.info("enterIdle: '%s' -> '%s'" % (self.oldState, self.newState))
        if len(args) > 0:
            self.activity.startIdle(*args)
        else:
            self.activity.startIdle()

    def filterIdle(self, request, args):
        BaseActivityFSM.notify.debug("filterIdle( '%s', '%s' )" % (request, args))
        if request == 'Idle':
            return
        else:
            return self.defaultFilter(request, args)
        return

    def exitIdle(self):
        BaseActivityFSM.notify.debug("exitIdle: '%s' -> '%s'" % (self.oldState, self.newState))
        self.activity.finishIdle()


class ActiveMixin:
    __module__ = __name__

    def enterActive(self, *args):
        BaseActivityFSM.notify.info("enterActive: '%s' -> '%s'" % (self.oldState, self.newState))
        if len(args) > 0:
            self.activity.startActive(*args)
        else:
            self.activity.startActive()

    def filterActive(self, request, args):
        BaseActivityFSM.notify.debug("filterActive( '%s', '%s' )" % (request, args))
        if request == 'Active':
            return
        else:
            return self.defaultFilter(request, args)
        return

    def exitActive(self):
        BaseActivityFSM.notify.debug("exitActive: '%s' -> '%s'" % (self.oldState, self.newState))
        self.activity.finishActive()


class DisabledMixin:
    __module__ = __name__

    def enterDisabled(self, *args):
        BaseActivityFSM.notify.info("enterDisabled: '%s' -> '%s'" % (self.oldState, self.newState))
        if len(args) > 0:
            self.activity.startDisabled(*args)
        else:
            self.activity.startDisabled()

    def filterDisabled(self, request, args):
        BaseActivityFSM.notify.debug("filterDisabled( '%s', '%s' )" % (request, args))
        if request == 'Disabled':
            return
        else:
            return self.defaultFilter(request, args)
        return

    def exitDisabled(self):
        BaseActivityFSM.notify.debug("exitDisabled: '%s' -> '%s'" % (self.oldState, self.newState))
        self.activity.finishDisabled()


class RulesMixin:
    __module__ = __name__

    def enterRules(self, *args):
        BaseActivityFSM.notify.info("enterRules: '%s' -> '%s'" % (self.oldState, self.newState))
        if len(args) > 0:
            self.activity.startRules(*args)
        else:
            self.activity.startRules()

    def filterRules(self, request, args):
        BaseActivityFSM.notify.debug("filterRules( '%s', '%s' )" % (request, args))
        if request == 'Rules':
            return
        else:
            return self.defaultFilter(request, args)
        return

    def exitRules(self):
        BaseActivityFSM.notify.debug("exitRules: '%s' -> '%s'" % (self.oldState, self.newState))
        self.activity.finishRules()


class WaitForEnoughMixin:
    __module__ = __name__

    def enterWaitForEnough(self, *args):
        BaseActivityFSM.notify.info("enterWaitForEnough: '%s' -> '%s'" % (self.oldState, self.newState))
        if len(args) > 0:
            self.activity.startWaitForEnough(*args)
        else:
            self.activity.startWaitForEnough()

    def filterWaitForEnough(self, request, args):
        BaseActivityFSM.notify.debug("filterWaitForEnough( '%s', '%s' )" % (request, args))
        if request == 'WaitForEnough':
            return
        else:
            return self.defaultFilter(request, args)
        return

    def exitWaitForEnough(self):
        BaseActivityFSM.notify.debug("exitWaitForEnough: '%s' -> '%s'" % (self.oldState, self.newState))
        self.activity.finishWaitForEnough()


class WaitToStartMixin:
    __module__ = __name__

    def enterWaitToStart(self, *args):
        BaseActivityFSM.notify.info("enterWaitToStart: '%s' -> '%s'" % (self.oldState, self.newState))
        if len(args) > 0:
            self.activity.startWaitToStart(*args)
        else:
            self.activity.startWaitToStart()

    def filterWaitToStart(self, request, args):
        BaseActivityFSM.notify.debug("filterWaitToStart( '%s', '%s' )" % (request, args))
        if request == 'WaitToStart':
            return
        else:
            return self.defaultFilter(request, args)
        return

    def exitWaitToStart(self):
        BaseActivityFSM.notify.debug("exitWaitToStart: '%s' -> '%s'" % (self.oldState, self.newState))
        self.activity.finishWaitToStart()


class WaitClientsReadyMixin:
    __module__ = __name__

    def enterWaitClientsReady(self, *args):
        BaseActivityFSM.notify.info("enterWaitClientsReady: '%s' -> '%s'" % (self.oldState, self.newState))
        if len(args) > 0:
            self.activity.startWaitClientsReady(*args)
        else:
            self.activity.startWaitClientsReady()

    def filterWaitClientsReady(self, request, args):
        BaseActivityFSM.notify.debug("filterWaitClientsReady( '%s', '%s' )" % (request, args))
        if request == 'WaitClientsReady':
            return
        else:
            return self.defaultFilter(request, args)
        return

    def exitWaitClientsReady(self):
        BaseActivityFSM.notify.debug("exitWaitClientsReady: '%s' -> '%s'" % (self.oldState, self.newState))
        self.activity.finishWaitClientsReady()


class WaitForServerMixin:
    __module__ = __name__

    def enterWaitForServer(self, *args):
        BaseActivityFSM.notify.info("enterWaitForServer: '%s' -> '%s'" % (self.oldState, self.newState))
        if len(args) > 0:
            self.activity.startWaitForServer(*args)
        else:
            self.activity.startWaitForServer()

    def filterWaitForServer(self, request, args):
        BaseActivityFSM.notify.debug("filterWaitForServer( '%s', '%s' )" % (request, args))
        if request == 'WaitForServer':
            return
        else:
            return self.defaultFilter(request, args)
        return

    def exitWaitForServer(self):
        BaseActivityFSM.notify.debug("exitWaitForServer: '%s' -> '%s'" % (self.oldState, self.newState))
        self.activity.finishWaitForServer()


class ConclusionMixin:
    __module__ = __name__

    def enterConclusion(self, *args):
        BaseActivityFSM.notify.info("enterConclusion: '%s' -> '%s'" % (self.oldState, self.newState))
        if len(args) > 0:
            self.activity.startConclusion(*args)
        else:
            self.activity.startConclusion()

    def filterConclusion(self, request, args):
        BaseActivityFSM.notify.debug("filterConclusion( '%s', '%s' )" % (request, args))
        if request == 'Conclusion':
            return
        else:
            return self.defaultFilter(request, args)
        return

    def exitConclusion(self):
        BaseActivityFSM.notify.debug("exitConclusion: '%s' -> '%s'" % (self.oldState, self.newState))
        self.activity.finishConclusion()