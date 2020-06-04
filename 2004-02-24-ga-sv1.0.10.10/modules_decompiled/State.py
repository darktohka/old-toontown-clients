# File: S (Python 2.2)

from DirectObject import *
import types
FsmRedefine = 0
EnterFuncRedefineMap = { }
ExitFuncRedefineMap = { }

def redefineEnterFunc(oldMethod, newFunction):
    import new
    if not FsmRedefine:
        return None
    
    for method in EnterFuncRedefineMap.keys():
        if type(method) == types.MethodType:
            function = method.im_func
        else:
            function = method
        if function == oldMethod:
            newMethod = new.instancemethod(newFunction, method.im_self, method.im_class)
            stateList = EnterFuncRedefineMap[method]
            for state in stateList:
                state.setEnterFunc(newMethod)
            
            return 1
        
    
    return 0


def redefineExitFunc(oldMethod, newFunction):
    import new
    if not FsmRedefine:
        return None
    
    for method in ExitFuncRedefineMap.keys():
        if type(method) == types.MethodType:
            function = method.im_func
        else:
            function = method
        if function == oldMethod:
            newMethod = new.instancemethod(newFunction, method.im_self, method.im_class)
            stateList = ExitFuncRedefineMap[method]
            for state in stateList:
                state.setExitFunc(newMethod)
            
            return 1
        
    
    return 0


class State(DirectObject):
    notify = directNotify.newCategory('State')
    Any = 'ANY'
    
    def __init__(self, name, enterFunc = None, exitFunc = None, transitions = Any, inspectorPos = []):
        self._State__enterFunc = None
        self._State__exitFunc = None
        self.setName(name)
        self.setEnterFunc(enterFunc)
        self.setExitFunc(exitFunc)
        self.setTransitions(transitions)
        self.setInspectorPos(inspectorPos)
        self._State__FSMList = []

    
    def getName(self):
        return self._State__name

    
    def setName(self, stateName):
        self._State__name = stateName

    
    def getEnterFunc(self):
        return self._State__enterFunc

    
    def redefineFunc(self, oldMethod, newMethod, map):
        if not FsmRedefine:
            return None
        
        if oldMethod is None:
            return None
        
        if map.has_key(oldMethod):
            stateList = map[oldMethod]
            stateList.remove(self)
            if not stateList:
                del map[oldMethod]
            
        
        stateList = map.get(newMethod, [])
        stateList.append(self)
        map[newMethod] = stateList

    
    def setEnterFunc(self, stateEnterFunc):
        self.redefineFunc(self._State__enterFunc, stateEnterFunc, EnterFuncRedefineMap)
        self._State__enterFunc = stateEnterFunc

    
    def getExitFunc(self):
        return self._State__exitFunc

    
    def setExitFunc(self, stateExitFunc):
        self.redefineFunc(self._State__exitFunc, stateExitFunc, ExitFuncRedefineMap)
        self._State__exitFunc = stateExitFunc

    
    def transitionsToAny(self):
        return self._State__transitions is State.Any

    
    def getTransitions(self):
        if self.transitionsToAny():
            return []
        
        return self._State__transitions

    
    def isTransitionDefined(self, otherState):
        if self.transitionsToAny():
            return 1
        
        if type(otherState) != type(''):
            otherState = otherState.getName()
        
        return otherState in self._State__transitions

    
    def setTransitions(self, stateTransitions):
        self._State__transitions = stateTransitions

    
    def addTransition(self, transition):
        if not self.transitionsToAny():
            self._State__transitions.append(transition)
        else:
            State.notify.warning('attempted to add transition %s to state that transitions to any state')

    
    def getInspectorPos(self):
        return self._State__inspectorPos

    
    def setInspectorPos(self, inspectorPos):
        self._State__inspectorPos = inspectorPos

    
    def getChildren(self):
        return self._State__FSMList

    
    def setChildren(self, FSMList):
        self._State__FSMList = FSMList

    
    def addChild(self, FSM):
        self._State__FSMList.append(FSM)

    
    def removeChild(self, FSM):
        if FSM in self._State__FSMList:
            self._State__FSMList.remove(FSM)
        

    
    def hasChildren(self):
        return len(self._State__FSMList) > 0

    
    def _State__enterChildren(self, argList):
        for fsm in self._State__FSMList:
            if fsm.getCurrentState():
                fsm.conditional_request(fsm.getInitialState().getName())
            else:
                fsm.enterInitialState()
        

    
    def _State__exitChildren(self, argList):
        for fsm in self._State__FSMList:
            fsm.request(fsm.getFinalState().getName())
        

    
    def enter(self, argList = []):
        self._State__enterChildren(argList)
        if self._State__enterFunc != None:
            apply(self._State__enterFunc, argList)
        

    
    def exit(self, argList = []):
        self._State__exitChildren(argList)
        if self._State__exitFunc != None:
            apply(self._State__exitFunc, argList)
        

    
    def __str__(self):
        return 'State: name = %s, enter = %s, exit = %s, trans = %s, children = %s' % (self._State__name, self._State__enterFunc, self._State__exitFunc, self._State__transitions, self._State__FSMList)


