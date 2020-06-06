# File: t (Python 2.2)

from __future__ import generators
import sys
NoneType = type(None)
TypeType = type
ObjectType = object
IntType = int
LongType = long
FloatType = float

try:
    ComplexType = complex
except NameError:
    pass

StringType = str

try:
    UnicodeType = unicode
    StringTypes = (StringType, UnicodeType)
except NameError:
    StringTypes = (StringType,)

BufferType = type(buffer(''))
TupleType = tuple
ListType = list
DictType = dict
DictionaryType = dict

def _f():
    pass

FunctionType = type(_f)
LambdaType = type(lambda : None)

try:
    CodeType = type(_f.func_code)
except RuntimeError:
    pass


def g():
    yield 1

GeneratorType = type(g())
del g

class _C:
    
    def _m(self):
        pass


ClassType = type(_C)
UnboundMethodType = type(_C._m)
_x = _C()
InstanceType = type(_x)
MethodType = type(_x._m)
BuiltinFunctionType = type(len)
BuiltinMethodType = type([].append)
ModuleType = type(sys)
FileType = file
XRangeType = type(xrange(0))

try:
    raise TypeError
except TypeError:
    
    try:
        tb = sys.exc_info()[2]
        TracebackType = type(tb)
        FrameType = type(tb.tb_frame)
    except AttributeError:
        pass

    tb = None
    del tb

SliceType = type(slice(0))
EllipsisType = type(Ellipsis)
DictProxyType = type(TypeType.__dict__)
del sys
del _f
del _C
del _x
del generators
