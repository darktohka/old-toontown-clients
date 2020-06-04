# File: F (Python 2.2)

from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal
import types
import string

class FSM(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('FSM')
    
    def __init__(self, name):
        self.name = name
        self.state = 'Off'
        self.defaultTransitions = None

    
    def __del__(self):
        self.cleanup()

    
    def cleanup(self):
        if self.state != 'Off':
            self._FSM__setState('Off')
        

    
    def forceTransition(self, newState):
        self._FSM__setState(newState)

    
    def request(self, request, *args):
        self.notify.debug('%s.request(%s, %s' % (self.name, request, str(args)[1:]))
        if not (self.state):
            self.notify.warning('rejecting request %s while FSM is in transition.' % request)
            return None
        
        func = getattr(self, 'filter' + self.state, None)
        if not func:
            func = self.defaultFilter
        
        result = func(request, args)
        if result:
            if isinstance(result, types.StringTypes):
                result = (result,)
            
            self._FSM__setState(*result)
        
        return result

    
    def defaultFilter(self, request, args):
        if request == 'Off':
            return (request,) + args
        
        if self.defaultTransitions is None:
            if request[0] in string.uppercase:
                return (request,) + args
            
        elif request in self.defaultTransitions.get(self.state, []):
            return (request,) + args
        
        if request[0] in string.uppercase:
            self.notify.error('%s rejecting request %s from state %s.' % (self.name, request, self.state))
        
        return None

    
    def filterOff(self, request, args):
        if request[0] in string.uppercase:
            return (request,) + args
        
        return self.defaultFilter(request, args)

    
    def setStateArray(self, stateArray):
        self.stateArray = stateArray

    
    def requestNext(self, *args):
        curIndex = self.stateArray.index(self.state)
        newIndex = (curIndex + 1) % len(self.stateArray)
        self.request(self.stateArray[newIndex], args)

    
    def requestPrev(self, *args):
        curIndex = self.stateArray.index(self.state)
        newIndex = (curIndex - 1) % len(self.stateArray)
        self.request(self.stateArray[newIndex], args)

    
    def _FSM__setState(self, newState, *args):
        self.oldState = self.state
        self.newState = newState
        self.state = None
        self._FSM__callTransitionFunc('exit' + self.oldState)
        self._FSM__callTransitionFunc('enter' + self.newState, *args)
        self.state = newState
        del self.oldState
        del self.newState

    
    def _FSM__callTransitionFunc(self, name, *args):
        func = getattr(self, name, None)
        if func:
            func(*args)
        

    
    def __repr__(self):
        return self.__str__()

    
    def __str__(self):
        if self.state:
            str = 'FSM ' + self.name + ' in state "' + self.state + '"'
        else:
            str = 'FSM ' + self.name + ' not in any state'
        return str


