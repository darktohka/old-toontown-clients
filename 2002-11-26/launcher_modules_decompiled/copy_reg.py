# File: c (Python 2.2)

from types import ClassType as _ClassType
__all__ = [
    'pickle',
    'constructor']
dispatch_table = { }
safe_constructors = { }

def pickle(ob_type, pickle_function, constructor_ob = None):
    if type(ob_type) is _ClassType:
        raise TypeError('copy_reg is not intended for use with classes')
    
    if not callable(pickle_function):
        raise TypeError('reduction functions must be callable')
    
    dispatch_table[ob_type] = pickle_function
    if constructor_ob is not None:
        constructor(constructor_ob)
    


def constructor(object):
    if not callable(object):
        raise TypeError('constructors must be callable')
    
    safe_constructors[object] = 1


def pickle_complex(c):
    return (complex, (c.real, c.imag))

pickle(type((0.0+1.0j)), pickle_complex, complex)

def _reconstructor(cls, base, state):
    obj = base.__new__(cls, state)
    base.__init__(obj, state)
    return obj

_reconstructor.__safe_for_unpickling__ = 1
_HEAPTYPE = 1 << 9

def _reduce(self):
    for base in self.__class__.__mro__:
        if hasattr(base, '__flags__') and not (base.__flags__ & _HEAPTYPE):
            break
        
    else:
        base = object
    if base is object:
        state = None
    else:
        state = base(self)
    args = (self.__class__, base, state)
    
    try:
        getstate = self.__getstate__
    except AttributeError:
        
        try:
            dict = self.__dict__
        except AttributeError:
            dict = None


    dict = getstate()
    if dict:
        return (_reconstructor, args, dict)
    else:
        return (_reconstructor, args)

