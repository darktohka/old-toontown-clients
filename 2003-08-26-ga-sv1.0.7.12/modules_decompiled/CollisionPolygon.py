# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import CollisionPlane

class CollisionPolygon(CollisionPlane.CollisionPlane, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _CollisionPolygon__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f(self, begin, end):
        self.this = libpanda._inPHwcaKCpw(begin.this, end.this)
        self.userManagesMemory = 1

    
    def _CollisionPolygon__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f(self, a, b, c):
        self.this = libpanda._inPHwcayiiq(a.this, b.this, c.this)
        self.userManagesMemory = 1

    
    def _CollisionPolygon__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f(self, a, b, c, d):
        self.this = libpanda._inPHwcaF9sC(a.this, b.this, c.this, d.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcaFL82:
            libpanda._inPHwcaFL82(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHwcaI99a()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                import Point3
                if isinstance(_args[1], Point3.Point3):
                    return self._CollisionPolygon__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
        elif numArgs == 3:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                import Point3
                if isinstance(_args[1], Point3.Point3):
                    import Point3
                    if isinstance(_args[2], Point3.Point3):
                        return self._CollisionPolygon__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
        elif numArgs == 4:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                import Point3
                if isinstance(_args[1], Point3.Point3):
                    import Point3
                    if isinstance(_args[2], Point3.Point3):
                        import Point3
                        if isinstance(_args[3], Point3.Point3):
                            return self._CollisionPolygon__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <Point3.Point3> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 4 '


