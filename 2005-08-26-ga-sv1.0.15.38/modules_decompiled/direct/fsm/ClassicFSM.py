# File: C (Python 2.2)

from direct.showbase.DirectObject import *
import types
import weakref

class ClassicFSM(DirectObject):
    notify = directNotify.newCategory('ClassicFSM')
    ALLOW = 0
    DISALLOW = 1
    DISALLOW_VERBOSE = 2
    ERROR = 3
    
    def __init__(self, name, states = [], initialStateName = None, finalStateName = None, onUndefTransition = DISALLOW_VERBOSE):
        self.setName(name)
        self.setStates(states)
        self.setInitialState(initialStateName)
        self.setFinalState(finalStateName)
        self.onUndefTransition = onUndefTransition
        self.inspecting = 0
        self._ClassicFSM__currentState = None
        self._ClassicFSM__internalStateInFlux = 0

    
    def __repr__(self):
        return self.__str__()

    
    def __str__(self):
        currentState = self.getCurrentState()
        if currentState:
            str = 'ClassicFSM ' + self.getName() + ' in state "' + currentState.getName() + '"'
        else:
            str = 'ClassicFSM ' + self.getName() + ' not in any state'
        return str

    
    def enterInitialState(self, argList = []):
        if self._ClassicFSM__currentState == self._ClassicFSM__initialState:
            return None
        
        self._ClassicFSM__internalStateInFlux = 1
        self._ClassicFSM__enter(self._ClassicFSM__initialState, argList)

    
    def getName(self):
        return self._ClassicFSM__name

    
    def setName(self, name):
        self._ClassicFSM__name = name

    
    def getStates(self):
        return self._ClassicFSM__states.values()

    
    def setStates(self, states):
        self._ClassicFSM__states = { }
        for state in states:
            self._ClassicFSM__states[state.getName()] = state
        

    
    def addState(self, state):
        self._ClassicFSM__states[state.getName()] = state

    
    def getInitialState(self):
        return self._ClassicFSM__initialState

    
    def setInitialState(self, initialStateName):
        self._ClassicFSM__initialState = self.getStateNamed(initialStateName)

    
    def getFinalState(self):
        return self._ClassicFSM__finalState

    
    def setFinalState(self, finalStateName):
        self._ClassicFSM__finalState = self.getStateNamed(finalStateName)

    
    def requestFinalState(self):
        self.request(self._ClassicFSM__finalState.getName())

    
    def getCurrentState(self):
        return self._ClassicFSM__currentState

    
    def getStateNamed(self, stateName):
        state = self._ClassicFSM__states.get(stateName)
        if state:
            return state
        else:
            ClassicFSM.notify.warning('[%s] : getStateNamed: %s, no such state' % (self._ClassicFSM__name, stateName))

    
    def _ClassicFSM__exitCurrent(self, argList):
        self._ClassicFSM__currentState.exit(argList)
        if self.inspecting:
            messenger.send(self.getName() + '_' + self._ClassicFSM__currentState.getName() + '_exited')
        
        self._ClassicFSM__currentState = None

    
    def _ClassicFSM__enter(self, aState, argList = []):
        stateName = aState.getName()
        if stateName in self._ClassicFSM__states:
            self._ClassicFSM__currentState = aState
            if self.inspecting:
                messenger.send(self.getName() + '_' + stateName + '_entered')
            
            self._ClassicFSM__internalStateInFlux = 0
            aState.enter(argList)
        else:
            self._ClassicFSM__internalStateInFlux = 0
            ClassicFSM.notify.error('[%s]: enter: no such state' % self._ClassicFSM__name)

    
    def _ClassicFSM__transition(self, aState, enterArgList = [], exitArgList = []):
        self._ClassicFSM__internalStateInFlux = 1
        self._ClassicFSM__exitCurrent(exitArgList)
        self._ClassicFSM__enter(aState, enterArgList)

    
    def request(self, aStateName, enterArgList = [], exitArgList = [], force = 0):
        if not (self._ClassicFSM__currentState):
            ClassicFSM.notify.warning('[%s]: request: never entered initial state' % self._ClassicFSM__name)
            self._ClassicFSM__currentState = self._ClassicFSM__initialState
        
        if isinstance(aStateName, types.StringType):
            aState = self.getStateNamed(aStateName)
        else:
            aState = aStateName
            aStateName = aState.getName()
        if aState == None:
            ClassicFSM.notify.error('[%s]: request: %s, no such state' % (self._ClassicFSM__name, aStateName))
        
        transitionDefined = self._ClassicFSM__currentState.isTransitionDefined(aStateName)
        transitionAllowed = transitionDefined
        if self.onUndefTransition == ClassicFSM.ALLOW:
            transitionAllowed = 1
            if not transitionDefined:
                ClassicFSM.notify.warning('[%s]: performing undefined transition from %s to %s' % (self._ClassicFSM__name, self._ClassicFSM__currentState.getName(), aStateName))
            
        
        if transitionAllowed or force:
            self._ClassicFSM__transition(aState, enterArgList, exitArgList)
            return 1
        elif aStateName == self._ClassicFSM__finalState.getName():
            if self._ClassicFSM__currentState == self._ClassicFSM__finalState:
                return 1
            else:
                self._ClassicFSM__transition(aState, enterArgList, exitArgList)
                return 1
        elif aStateName == self._ClassicFSM__currentState.getName():
            return 0
        else:
            msg = '[%s]: no transition exists from %s to %s' % (self._ClassicFSM__name, self._ClassicFSM__currentState.getName(), aStateName)
            if self.onUndefTransition == ClassicFSM.ERROR:
                ClassicFSM.notify.error(msg)
            elif self.onUndefTransition == ClassicFSM.DISALLOW_VERBOSE:
                ClassicFSM.notify.warning(msg)
            
            return 0

    
    def forceTransition(self, aStateName, enterArgList = [], exitArgList = []):
        self.request(aStateName, enterArgList, exitArgList, force = 1)

    
    def conditional_request(self, aStateName, enterArgList = [], exitArgList = []):
        if not (self._ClassicFSM__currentState):
            ClassicFSM.notify.warning('[%s]: request: never entered initial state' % self._ClassicFSM__name)
            self._ClassicFSM__currentState = self._ClassicFSM__initialState
        
        if isinstance(aStateName, types.StringType):
            aState = self.getStateNamed(aStateName)
        else:
            aState = aStateName
            aStateName = aState.getName()
        if aState == None:
            ClassicFSM.notify.error('[%s]: request: %s, no such state' % (self._ClassicFSM__name, aStateName))
        
        if not self._ClassicFSM__currentState.isTransitionDefined(aStateName):
            pass
        transitionDefined = aStateName in [
            self._ClassicFSM__currentState.getName(),
            self._ClassicFSM__finalState.getName()]
        if transitionDefined:
            return self.request(aStateName, enterArgList, exitArgList)
        else:
            return 0

    
    def view(self):
        FSMInspector = FSMInspector
        import direct.tkpanels
        FSMInspector.FSMInspector(self)


