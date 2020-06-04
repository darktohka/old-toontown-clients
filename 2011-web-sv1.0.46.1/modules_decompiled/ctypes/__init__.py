# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\cygwin\home\toonpub\player_1_0_46_qa\wintools\sdk\python\Python-2.4.1\lib\site-packages\ctypes\__init__.py
import os as _os, sys
_magicfile = _os.path.join(_os.path.dirname(__file__), '.CTYPES_DEVEL')
if _os.path.isfile(_magicfile):
    execfile(_magicfile)
del _magicfile
__version__ = '0.9.6'
from _ctypes import Union, Structure, Array
from _ctypes import _Pointer
from _ctypes import CFuncPtr as _CFuncPtr
from _ctypes import __version__ as _ctypes_version
from _ctypes import ArgumentError
from struct import calcsize as _calcsize
if __version__ != _ctypes_version:
    raise Exception, ('Version number mismatch', __version__, _ctypes_version)
if _os.name == 'nt':
    from _ctypes import FormatError
from _ctypes import FUNCFLAG_CDECL as _FUNCFLAG_CDECL, FUNCFLAG_PYTHONAPI as _FUNCFLAG_PYTHONAPI

def create_string_buffer(init, size=None):
    if isinstance(init, (str, unicode)):
        if size is None:
            size = len(init) + 1
        buftype = c_char * size
        buf = buftype()
        buf.value = init
        return buf
    elif isinstance(init, (int, long)):
        buftype = c_char * init
        buf = buftype()
        return buf
    raise TypeError, init
    return


def c_buffer(init, size=None):
    return create_string_buffer(init, size)


_c_functype_cache = {}

def CFUNCTYPE(restype, *argtypes):
    try:
        return _c_functype_cache[(restype, argtypes)]
    except KeyError:

        class CFunctionType(_CFuncPtr):
            __module__ = __name__
            _argtypes_ = argtypes
            _restype_ = restype
            _flags_ = _FUNCFLAG_CDECL

        _c_functype_cache[(restype, argtypes)] = CFunctionType
        return CFunctionType


if _os.name == 'nt':
    from _ctypes import LoadLibrary as _LoadLibrary, FreeLibrary as _FreeLibrary
    from _ctypes import FUNCFLAG_HRESULT as _FUNCFLAG_HRESULT, FUNCFLAG_STDCALL as _FUNCFLAG_STDCALL
    _win_functype_cache = {}

    def WINFUNCTYPE(restype, *argtypes):
        try:
            return _win_functype_cache[(restype, argtypes)]
        except KeyError:

            class WinFunctionType(_CFuncPtr):
                __module__ = __name__
                _argtypes_ = argtypes
                _restype_ = restype
                _flags_ = _FUNCFLAG_STDCALL

            _win_functype_cache[(restype, argtypes)] = WinFunctionType
            return WinFunctionType


elif _os.name == 'posix':
    from _ctypes import dlopen as _LoadLibrary
    _FreeLibrary = None
from _ctypes import sizeof, byref, addressof, alignment
from _ctypes import _SimpleCData

class py_object(_SimpleCData):
    __module__ = __name__
    _type_ = 'O'


class c_short(_SimpleCData):
    __module__ = __name__
    _type_ = 'h'

    def __repr__(self):
        return 'c_short(%d)' % self.value


class c_ushort(_SimpleCData):
    __module__ = __name__
    _type_ = 'H'

    def __repr__(self):
        return 'c_ushort(%d)' % self.value


class c_long(_SimpleCData):
    __module__ = __name__
    _type_ = 'l'

    def __repr__(self):
        return 'c_long(%d)' % self.value


class c_ulong(_SimpleCData):
    __module__ = __name__
    _type_ = 'L'

    def __repr__(self):
        return 'c_ulong(%d)' % self.value


if _calcsize('i') == _calcsize('l'):
    c_int = c_long
    c_uint = c_ulong
else:

    class c_int(_SimpleCData):
        __module__ = __name__
        _type_ = 'i'

        def __repr__(self):
            return 'c_int(%d)' % self.value


    class c_uint(_SimpleCData):
        __module__ = __name__
        _type_ = 'I'

        def __repr__(self):
            return 'c_uint(%d)' % self.value


class c_float(_SimpleCData):
    __module__ = __name__
    _type_ = 'f'

    def __repr__(self):
        return '%s(%f)' % (self.__class__.__name__, self.value)


class c_double(_SimpleCData):
    __module__ = __name__
    _type_ = 'd'

    def __repr__(self):
        return '%s(%f)' % (self.__class__.__name__, self.value)


if _calcsize('l') == _calcsize('q'):
    c_longlong = c_long
    c_ulonglong = c_ulong
else:

    class c_longlong(_SimpleCData):
        __module__ = __name__
        _type_ = 'q'

        def __repr__(self):
            return 'c_longlong(%s)' % self.value


    class c_ulonglong(_SimpleCData):
        __module__ = __name__
        _type_ = 'Q'

        def __repr__(self):
            return 'c_ulonglong(%s)' % self.value


class c_ubyte(_SimpleCData):
    __module__ = __name__
    _type_ = 'B'

    def __repr__(self):
        return 'c_ubyte(%s)' % self.value


class c_byte(_SimpleCData):
    __module__ = __name__
    _type_ = 'b'

    def __repr__(self):
        return 'c_byte(%s)' % self.value


class c_char(_SimpleCData):
    __module__ = __name__
    _type_ = 'c'

    def __repr__(self):
        return 'c_char(%r)' % self.value


class c_char_p(_SimpleCData):
    __module__ = __name__
    _type_ = 'z'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.value)


class c_void_p(_SimpleCData):
    __module__ = __name__
    _type_ = 'P'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.value)


c_voidp = c_void_p
_pointer_type_cache = {}

def POINTER(cls):
    try:
        return _pointer_type_cache[cls]
    except KeyError:
        pass

    if type(cls) is str:
        klass = type(_Pointer)('LP_%s' % cls, (
         _Pointer,), {})
        _pointer_type_cache[id(klass)] = klass
        return klass
    else:
        name = 'LP_%s' % cls.__name__
        klass = type(_Pointer)(name, (
         _Pointer,), {'_type_': cls})
        _pointer_type_cache[cls] = klass
    return klass


try:
    from _ctypes import set_conversion_mode
except ImportError:
    pass
else:
    if _os.name == 'nt':
        set_conversion_mode('mbcs', 'ignore')
    else:
        set_conversion_mode('ascii', 'strict')

    class c_wchar_p(_SimpleCData):
        __module__ = __name__
        _type_ = 'Z'

        def __repr__(self):
            return '%s(%r)' % (self.__class__.__name__, self.value)


    class c_wchar(_SimpleCData):
        __module__ = __name__
        _type_ = 'u'

        def __repr__(self):
            return 'c_wchar(%r)' % self.value


    POINTER(c_wchar).from_param = c_wchar_p.from_param

    def create_unicode_buffer(init, size=None):
        if isinstance(init, (str, unicode)):
            if size is None:
                size = len(init) + 1
            buftype = c_wchar * size
            buf = buftype()
            buf.value = init
            return buf
        elif isinstance(init, (int, long)):
            buftype = c_wchar * init
            buf = buftype()
            return buf
        raise TypeError, init
        return


    from _ctypes import wstring_at

POINTER(c_char).from_param = c_char_p.from_param

def SetPointerType(pointer, cls):
    if _pointer_type_cache.get(cls, None) is not None:
        raise RuntimeError, 'This type already exists in the cache'
    if not _pointer_type_cache.has_key(id(pointer)):
        raise RuntimeError, "What's this???"
    pointer.set_type(cls)
    _pointer_type_cache[cls] = pointer
    del _pointer_type_cache[id(pointer)]
    return


def pointer(inst):
    return POINTER(type(inst))(inst)


def ARRAY(typ, len):
    return typ * len


class CDLL:
    __module__ = __name__

    class _CdeclFuncPtr(_CFuncPtr):
        __module__ = __name__
        _flags_ = _FUNCFLAG_CDECL
        _restype_ = c_int

    _handle = 0

    def __init__(self, name, handle=None):
        self._name = name
        if handle is None:
            self._handle = _LoadLibrary(self._name)
        else:
            self._handle = handle
        return

    def __repr__(self):
        return "<%s '%s', handle %x at %x>" % (self.__class__.__name__, self._name, self._handle & sys.maxint * 2 + 1, id(self))

    def __getattr__(self, name):
        if name[:2] == '__' and name[-2:] == '__':
            raise AttributeError, name
        func = self._CdeclFuncPtr(name, self)
        func.__name__ = name
        setattr(self, name, func)
        return func

    def __getitem__(self, name):
        return getattr(self, name)


class PyDLL(CDLL):
    __module__ = __name__

    class _CdeclFuncPtr(_CFuncPtr):
        __module__ = __name__
        _flags_ = _FUNCFLAG_CDECL | _FUNCFLAG_PYTHONAPI
        _restype_ = c_int


if _os.name == 'nt':

    class WinDLL(CDLL):
        __module__ = __name__

        class _StdcallFuncPtr(_CFuncPtr):
            __module__ = __name__
            _flags_ = _FUNCFLAG_STDCALL
            _restype_ = c_int

        def __getattr__(self, name):
            if name[:2] == '__' and name[-2:] == '__':
                raise AttributeError, name
            func = self._StdcallFuncPtr(name, self)
            func.__name__ = name
            setattr(self, name, func)
            return func


    from _ctypes import _check_HRESULT

    class HRESULT(c_long):
        __module__ = __name__
        _check_retval_ = _check_HRESULT


    class OleDLL(CDLL):
        __module__ = __name__

        class _OlecallFuncPtr(_CFuncPtr):
            __module__ = __name__
            _flags_ = _FUNCFLAG_STDCALL | _FUNCFLAG_HRESULT
            _restype_ = c_int

        def __getattr__(self, name):
            if name[:2] == '__' and name[-2:] == '__':
                raise AttributeError, name
            func = self._OlecallFuncPtr(name, self)
            func.__name__ = name
            setattr(self, name, func)
            return func


class _DLLS:
    __module__ = __name__

    def __init__(self, dlltype):
        self._dlltype = dlltype

    def __getattr__(self, name):
        if name[0] == '_':
            raise AttributeError, name
        dll = self._dlltype(name)
        setattr(self, name, dll)
        return dll

    def __getitem__(self, name):
        return getattr(self, name)

    def LoadLibrary(self, name):
        return self._dlltype(name)


cdll = _DLLS(CDLL)
pydll = _DLLS(PyDLL)
if _os.name == 'nt':
    pythonapi = PyDLL('python dll', sys.dllhandle)
elif sys.platform == 'cygwin':
    pythonapi = PyDLL('libpython%d.%d.dll' % sys.version_info[:2])
else:
    pythonapi = PyDLL(None)
if _os.name == 'nt':
    windll = _DLLS(WinDLL)
    oledll = _DLLS(OleDLL)
    GetLastError = windll.kernel32.GetLastError

    def WinError(code=None, descr=None):
        if code is None:
            code = GetLastError()
        if descr is None:
            descr = FormatError(code).strip()
        return WindowsError(code, descr)


_pointer_type_cache[None] = c_void_p
from _ctypes import memmove, memset, string_at, cast
from decorators import cdecl
if _os.name == 'nt':
    from decorators import stdcall