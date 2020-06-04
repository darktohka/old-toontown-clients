# File: F (Python 2.2)

from DirectObject import *
import types

class FSM(DirectObject):
    notify = directNotify.newCategory('FSM')
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
        self._FSM__currentState = None
        self._FSM__internalStateInFlux = 0

    
    def __repr__(self):
        return self.__str__()

    
    def __str__(self):
        currentState = self.getCurrentState()
        if currentState:
            str = 'FSM ' + self.getName() + ' in state "' + currentState.getName() + '"'
        else:
            str = 'FSM ' + self.getName() + ' not in any state'
        return str

    
    def enterInitialState(self, argList = []):
        if self._FSM__currentState == self._FSM__initialState:
            return None
        
        self._FSM__internalStateInFlux = 1
        self._FSM__enter(self._FSM__initialState, argList)

    
    def __str_not__(self):
        return 'FSM: name = %s \n states = %s \n initial = %s \n final = %s \n current = %s' % (self._FSM__name, self._FSM__states, self._FSM__initialState, self._FSM__finalState, self._FSM__currentState)

    
    def getName(self):
        return self._FSM__name

    
    def setName(self, name):
        self._FSM__name = name

    
    def getStates(self):
        return self._FSM__states

    
    def setStates(self, states):
        self._FSM__states = states

    
    def addState(self, state):
        self._FSM__states.append(state)

    
    def getInitialState(self):
        return self._FSM__initialState

    
    def setInitialState(self, initialStateName):
        self._FSM__initialState = self.getStateNamed(initialStateName)

    
    def getFinalState(self):
        return self._FSM__finalState

    
    def setFinalState(self, finalStateName):
        self._FSM__finalState = self.getStateNamed(finalStateName)

    
    def requestFinalState(self):
        self.request(self._FSM__finalState.getName())

    
    def getCurrentState(self):
        return self._FSM__currentState

    
    def getStateNamed(self, stateName):
        for state in self._FSM__states:
            if state.getName() == stateName:
                return state
            
        
        FSM.notify.warning('[%s] : getStateNamed: %s, no such state' % (self._FSM__name, str(stateName)))

    
    def _FSM__exitCurrent(self, argList):
        if FSM.notify.getDebug():
            FSM.notify.debug('[%s]: exiting %s' % (self._FSM__name, self._FSM__currentState.getName()))
        
        self._FSM__currentState.exit(argList)
        if self.inspecting:
            messenger.send(self.getName() + '_' + self._FSM__currentState.getName() + '_exited')
        
        self._FSM__currentState = None

    
    def _FSM__enter(self, aState, argList = []):
        if aState in self._FSM__states:
            if FSM.notify.getDebug():
                FSM.notify.debug('[%s]: entering %s' % (self._FSM__name, aState.getName()))
            
            self._FSM__currentState = aState
            if self.inspecting:
                messenger.send(self.getName() + '_' + aState.getName() + '_entered')
            
            self._FSM__internalStateInFlux = 0
            aState.enter(argList)
        else:
            self._FSM__internalStateInFlux = 0
            FSM.notify.error('[%s]: enter: no such state' % self._FSM__name)

    
    def _FSM__transition(self, aState, enterArgList = [], exitArgList = []):
        self._FSM__internalStateInFlux = 1
        self._FSM__exitCurrent(exitArgList)
        self._FSM__enter(aState, enterArgList)

    
    def request(self, aStateName, enterArgList = [], exitArgList = [], force = 0):
        if not (self._FSM__currentState):
            FSM.notify.warning('[%s]: request: never entered initial state' % self._FSM__name)
            self._FSM__currentState = self._FSM__initialState
        
        if isinstance(aStateName, types.StringType):
            aState = self.getStateNamed(aStateName)
        else:
            aState = aStateName
            aStateName = aState.getName()
        if aState == None:
            FSM.notify.error('[%s]: request: %s, no such state' % (self._FSM__name, aStateName))
        
        transitionDefined = self._FSM__currentState.isTransitionDefined(aStateName)
        transitionAllowed = transitionDefined
        if self.onUndefTransition == FSM.ALLOW:
            transitionAllowed = 1
            if not transitionDefined:
                FSM.notify.warning('[%s]: performing undefined transition from %s to %s' % (self._FSM__name, self._FSM__currentState.getName(), aStateName))
            
        
        if transitionAllowed or force:
            self._FSM__transition(aState, enterArgList, exitArgList)
            return 1
        elif aStateName == self._FSM__finalState.getName():
            if self._FSM__currentState == self._FSM__finalState:
                if FSM.notify.getDebug():
                    FSM.notify.debug('[%s]: already in final state: %s' % (self._FSM__name, aStateName))
                
                return 1
            elif FSM.notify.getDebug():
                FSM.notify.debug('[%s]: implicit transition to final state: %s' % (self._FSM__name, aStateName))
            
            self._FSM__transition(aState, enterArgList, exitArgList)
            return 1
        elif aStateName == self._FSM__currentState.getName():
            if FSM.notify.getDebug():
                FSM.notify.debug('[%s]: already in state %s and no self transition' % (self._FSM__name, aStateName))
            
            return 0
        else:
            msg = '[%s]: no transition exists from %s to %s' % (self._FSM__name, self._FSM__currentState.getName(), aStateName)
            if self.onUndefTransition == FSM.ERROR:
                FSM.notify.error(msg)
            elif self.onUndefTransition == FSM.DISALLOW_VERBOSE:
                FSM.notify.warning(msg)
            
            return 0

    
    def forceTransition(self, aStateName, enterArgList = [], exitArgList = []):
        self.request(aStateName, enterArgList, exitArgList, force = 1)

    
    def conditional_request(self, aStateName, enterArgList = [], exitArgList = []):
        if not (self._FSM__currentState):
            FSM.notify.warning('[%s]: request: never entered initial state' % self._FSM__name)
            self._FSM__currentState = self._FSM__initialState
        
        if isinstance(aStateName, types.StringType):
            aState = self.getStateNamed(aStateName)
        else:
            aState = aStateName
            aStateName = aState.getName()
        if aState == None:
            FSM.notify.error('[%s]: request: %s, no such state' % (self._FSM__name, aStateName))
        
        if not self._FSM__currentState.isTransitionDefined(aStateName):
            pass
        transitionDefined = aStateName in [
            self._FSM__currentState.getName(),
            self._FSM__finalState.getName()]
        if transitionDefined:
            return self.request(aStateName, enterArgList, exitArgList)
        else:
            FSM.notify.debug('[%s]: condition_request: %s, transition doesnt exist' % (self._FSM__name, aStateName))
            return 0

    
    def view(self):
        import FSMInspector
        FSMInspector.FSMInspector(self)


