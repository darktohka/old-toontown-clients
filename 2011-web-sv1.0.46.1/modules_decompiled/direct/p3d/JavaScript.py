# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\p3d\JavaScript.py
import types

class UndefinedObject:
    __module__ = __name__

    def __nonzero__(self):
        return False

    def __str__(self):
        return 'Undefined'


Undefined = UndefinedObject()

class ConcreteStruct:
    __module__ = __name__

    def __init__(self):
        pass

    def getConcreteProperties(self):
        return self.__dict__.items()


class BrowserObject:
    __module__ = __name__

    def __init__(self, runner, objectId):
        self.__dict__['_BrowserObject__runner'] = runner
        self.__dict__['_BrowserObject__objectId'] = objectId
        self.__dict__['_BrowserObject__childObject'] = (None, None)
        self.__dict__['_BrowserObject__methods'] = {}
        return

    def __del__(self):
        self.__runner.dropObject(self.__objectId)

    def __cacheMethod(self, methodName):
        method = self.__methods.get(methodName, None)
        if method is None:
            method = MethodWrapper(self.__runner, self, methodName)
            self.__methods[methodName] = method
        return method

    def __str__(self):
        (parentObj, attribName) = self.__childObject
        if parentObj:
            return '%s.%s' % (parentObj, attribName)
        else:
            return 'BrowserObject(%s)' % self.__objectId

    def __nonzero__(self):
        return True

    def __call__(self, *args, **kw):
        needsResponse = True
        if 'needsResponse' in kw:
            needsResponse = kw['needsResponse']
            del kw['needsResponse']
        if kw:
            raise ArgumentError, 'Keyword arguments not supported'
        try:
            (parentObj, attribName) = self.__childObject
            if parentObj:
                if parentObj is self.__runner.dom and attribName == 'alert':
                    needsResponse = False
                if parentObj is self.__runner.dom and attribName == 'eval' and len(args) == 1 and isinstance(args[0], types.StringTypes):
                    if args[0].startswith('void '):
                        needsResponse = False
                    result = self.__runner.scriptRequest('eval', parentObj, value=args[0], needsResponse=needsResponse)
                else:
                    try:
                        result = self.__runner.scriptRequest('call', parentObj, propertyName=attribName, value=args, needsResponse=needsResponse)
                    except EnvironmentError:
                        raise AttributeError

                parentObj.__cacheMethod(attribName)
            else:
                result = self.__runner.scriptRequest('call', self, value=args, needsResponse=needsResponse)
        except EnvironmentError:
            raise TypeError

        return result

    def __getattr__(self, name):
        method = self.__methods.get(name, None)
        if method:
            return method
        try:
            value = self.__runner.scriptRequest('get_property', self, propertyName=name)
        except EnvironmentError:
            if self.__runner.scriptRequest('has_method', self, propertyName=name):
                return self.__cacheMethod(name)
            raise AttributeError(name)

        if isinstance(value, BrowserObject):
            value.__dict__['_BrowserObject__childObject'] = (
             self, name)
        return value

    def __setattr__(self, name, value):
        if name in self.__dict__:
            self.__dict__[name] = value
            return
        result = self.__runner.scriptRequest('set_property', self, propertyName=name, value=value)
        if not result:
            raise AttributeError(name)

    def __delattr__(self, name):
        if name in self.__dict__:
            del self.__dict__[name]
            return
        result = self.__runner.scriptRequest('del_property', self, propertyName=name)
        if not result:
            raise AttributeError(name)

    def __getitem__(self, key):
        try:
            value = self.__runner.scriptRequest('get_property', self, propertyName=str(key))
        except EnvironmentError:
            if isinstance(key, types.StringTypes):
                raise KeyError(key)
            else:
                raise IndexError(key)

        return value

    def __setitem__(self, key, value):
        result = self.__runner.scriptRequest('set_property', self, propertyName=str(key), value=value)
        if not result:
            if isinstance(key, types.StringTypes):
                raise KeyError(key)
            else:
                raise IndexError(key)

    def __delitem__(self, key):
        result = self.__runner.scriptRequest('del_property', self, propertyName=str(key))
        if not result:
            if isinstance(key, types.StringTypes):
                raise KeyError(key)
            else:
                raise IndexError(key)


class MethodWrapper:
    __module__ = __name__

    def __init__(self, runner, parentObj, objectId):
        self.__dict__['_MethodWrapper__runner'] = runner
        self.__dict__['_MethodWrapper__childObject'] = (parentObj, objectId)

    def __str__(self):
        (parentObj, attribName) = self.__childObject
        return '%s.%s' % (parentObj, attribName)

    def __nonzero__(self):
        return True

    def __call__(self, *args, **kw):
        needsResponse = True
        if 'needsResponse' in kw:
            needsResponse = kw['needsResponse']
            del kw['needsResponse']
        if kw:
            raise ArgumentError, 'Keyword arguments not supported'
        try:
            (parentObj, attribName) = self.__childObject
            if parentObj is self.__runner.dom and attribName == 'alert':
                needsResponse = False
            if parentObj is self.__runner.dom and attribName == 'eval' and len(args) == 1 and isinstance(args[0], types.StringTypes):
                if args[0].startswith('void '):
                    needsResponse = False
                result = self.__runner.scriptRequest('eval', parentObj, value=args[0], needsResponse=needsResponse)
            else:
                try:
                    result = self.__runner.scriptRequest('call', parentObj, propertyName=attribName, value=args, needsResponse=needsResponse)
                except EnvironmentError:
                    raise AttributeError

        except EnvironmentError:
            raise TypeError

        return result

    def __setattr__(self, name, value):
        raise AttributeError(name)

    def __delattr__(self, name):
        raise AttributeError(name)