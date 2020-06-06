# File: A (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ReferenceCount

class AnimControl(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPn9gMuTrw:
            libpanda._inPn9gMuTrw(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPn9gMtoch()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _AnimControl__overloaded_play_ptrAnimControl_ptrConstEvent(self, stopEvent):
        returnValue = libpanda._inPn9gMVPKG(self.this, stopEvent.this)
        return returnValue

    
    def _AnimControl__overloaded_play_ptrAnimControl(self):
        returnValue = libpanda._inPn9gMp7rs(self.this)
        return returnValue

    
    def _AnimControl__overloaded_play_ptrAnimControl_int_int_ptrConstEvent(self, _from, to, stopEvent):
        returnValue = libpanda._inPn9gMId_s(self.this, _from, to, stopEvent.this)
        return returnValue

    
    def _AnimControl__overloaded_play_ptrAnimControl_int_int(self, _from, to):
        returnValue = libpanda._inPn9gMfBT0(self.this, _from, to)
        return returnValue

    
    def _AnimControl__overloaded_loop_ptrAnimControl_bool(self, restart):
        returnValue = libpanda._inPn9gMKXO_(self.this, restart)
        return returnValue

    
    def _AnimControl__overloaded_loop_ptrAnimControl_bool_int_int(self, restart, _from, to):
        returnValue = libpanda._inPn9gMuHvR(self.this, restart, _from, to)
        return returnValue

    
    def pingpong(self, restart, _from, to):
        returnValue = libpanda._inPn9gM61RK(self.this, restart, _from, to)
        return returnValue

    
    def stop(self):
        returnValue = libpanda._inPn9gMDhaN(self.this)
        return returnValue

    
    def pose(self, frame):
        returnValue = libpanda._inPn9gMSFkS(self.this, frame)
        return returnValue

    
    def addEvent(self, frame, event):
        returnValue = libpanda._inPn9gMZe3u(self.this, frame, event.this)
        return returnValue

    
    def removeEvent(self, eventName):
        returnValue = libpanda._inPn9gM9ujl(self.this, eventName)
        return returnValue

    
    def removeAllEvents(self):
        returnValue = libpanda._inPn9gMM5B1(self.this)
        return returnValue

    
    def setPlayRate(self, playRate):
        returnValue = libpanda._inPn9gMHjlM(self.this, playRate)
        return returnValue

    
    def getPlayRate(self):
        returnValue = libpanda._inPn9gM_e1Y(self.this)
        return returnValue

    
    def getFrameRate(self):
        returnValue = libpanda._inPn9gMpJSW(self.this)
        return returnValue

    
    def getFrame(self):
        returnValue = libpanda._inPn9gMYo5O(self.this)
        return returnValue

    
    def getNumFrames(self):
        returnValue = libpanda._inPn9gMRZad(self.this)
        return returnValue

    
    def isPlaying(self):
        returnValue = libpanda._inPn9gM3i0D(self.this)
        return returnValue

    
    def getPart(self):
        returnValue = libpanda._inPn9gMjnR8(self.this)
        import PartBundle
        returnObject = PartBundle.PartBundle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getAnim(self):
        returnValue = libpanda._inPn9gMfBvN(self.this)
        import AnimBundle
        returnObject = AnimBundle.AnimBundle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def play(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._AnimControl__overloaded_play_ptrAnimControl()
        elif numArgs == 1:
            import Event
            if isinstance(_args[0], Event.Event):
                return self._AnimControl__overloaded_play_ptrAnimControl_ptrConstEvent(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Event.Event> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    return self._AnimControl__overloaded_play_ptrAnimControl_int_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    import Event
                    if isinstance(_args[2], Event.Event):
                        return self._AnimControl__overloaded_play_ptrAnimControl_int_int_ptrConstEvent(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <Event.Event> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 '

    
    def loop(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._AnimControl__overloaded_loop_ptrAnimControl_bool(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.IntType):
                        return self._AnimControl__overloaded_loop_ptrAnimControl_bool_int_int(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


