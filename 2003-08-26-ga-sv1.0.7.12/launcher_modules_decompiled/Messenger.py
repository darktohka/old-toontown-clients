# File: M (Python 2.2)

from PythonUtil import *
from DirectNotifyGlobal import *

class Messenger:
    notify = None
    
    def __init__(self):
        self.dict = { }
        if Messenger.notify == None:
            Messenger.notify = directNotify.newCategory('Messenger')
        

    
    def accept(self, event, object, method, extraArgs = [], persistent = 1):
        if Messenger.notify.getDebug():
            Messenger.notify.debug('object: ' + `object` + '\n now accepting: ' + `event` + '\n method: ' + `method` + '\n extraArgs: ' + `extraArgs` + '\n persistent: ' + `persistent`)
        
        acceptorDict = self.dict.setdefault(event, { })
        acceptorDict[object] = [
            method,
            extraArgs,
            persistent]

    
    def ignore(self, event, object):
        if Messenger.notify.getDebug():
            Messenger.notify.debug(`object` + '\n now ignoring: ' + `event`)
        
        acceptorDict = self.dict.get(event)
        if acceptorDict and acceptorDict.has_key(object):
            del acceptorDict[object]
            if len(acceptorDict) == 0:
                del self.dict[event]
            
        

    
    def isAccepting(self, event, object):
        if self.dict.has_key(event):
            if self.dict[event].has_key(object):
                return 1
            
        
        return 0

    
    def whoAccepts(self, event):
        return self.dict.get(event, None)

    
    def isIgnoring(self, event, object):
        return not self.isAccepting(event, object)

    
    def send(self, event, sentArgs = []):
        if Messenger.notify.getDebug() and event != 'NewFrame':
            Messenger.notify.debug('sent event: ' + event + ' sentArgs: ' + `sentArgs`)
        
        acceptorDict = self.dict.get(event)
        if not acceptorDict:
            return None
        
        for object in acceptorDict.keys():
            callInfo = acceptorDict.get(object)
            if callInfo:
                (method, extraArgs, persistent) = callInfo
                if not persistent:
                    object._INTERNAL_acceptOnceExpired(event)
                    del acceptorDict[object]
                    if self.dict.has_key(event) and len(self.dict[event]) == 0:
                        del self.dict[event]
                    
                
                apply(method, extraArgs + sentArgs)
            
        

    
    def clear(self):
        self.dict.clear()

    
    def replaceMethod(self, oldMethod, newFunction):
        import new
        retFlag = 0
        for entry in self.dict.items():
            (event, objectDict) = entry
            for objectEntry in objectDict.items():
                (object, params) = objectEntry
                method = params[0]
                if type(method) == types.MethodType:
                    function = method.im_func
                else:
                    function = method
                if function == oldMethod:
                    newMethod = new.instancemethod(newFunction, method.im_self, method.im_class)
                    params[0] = newMethod
                    retFlag += 1
                
            
        
        return retFlag

    
    def toggleVerbose(self):
        Messenger.notify.setDebug(1 - Messenger.notify.getDebug())

    
    def __repr__(self):
        str = '=' * 64 + '\n'
        keys = self.dict.keys()
        keys.sort()
        for event in keys:
            str = str + event.ljust(32) + '\t'
            acceptorDict = self.dict[event]
            for object in acceptorDict.keys():
                (method, extraArgs, persistent) = acceptorDict[object]
                className = object.__class__.__name__
                methodName = method.__name__
                str = str + className + '.' + methodName + ' '
            
            str = str + '\n'
        
        return str

    
    def detailedRepr(self):
        import types
        str = 'Messenger\n'
        str = str + '=' * 50 + '\n'
        keys = self.dict.keys()
        keys.sort()
        for event in keys:
            acceptorDict = self.dict[event]
            str = str + 'Event: ' + event + '\n'
            for object in acceptorDict.keys():
                (function, extraArgs, persistent) = acceptorDict[object]
                if type(object) == types.InstanceType:
                    className = object.__class__.__name__
                else:
                    className = 'Not a class'
                functionName = function.__name__
                str = str + '\t' + 'Acceptor:     ' + className + ' instance' + '\n\t' + 'Function name:' + functionName + '\n\t' + 'Extra Args:   ' + `extraArgs` + '\n\t' + 'Persistent:   ' + `persistent` + '\n'
                if type(function) == types.MethodType:
                    str = str + '\t' + 'Method:       ' + `function` + '\n\t' + 'Function:     ' + `function.im_func` + '\n'
                else:
                    str = str + '\t' + 'Function:     ' + `function` + '\n'
            
        
        str = str + '=' * 50 + '\n'
        return str


