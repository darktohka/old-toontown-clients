# File: T (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class TextEncoder(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    EIso8859 = 0
    EUtf8 = 1
    EUnicode = 2
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpandaexpress._inPJoxtcza9()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxt0ZE7:
            libpandaexpress._inPJoxt0ZE7(self.this)
        

    
    def setDefaultEncoding(encoding):
        returnValue = libpandaexpress._inPJoxtGCJv(encoding)
        return returnValue

    setDefaultEncoding = staticmethod(setDefaultEncoding)
    
    def getDefaultEncoding():
        returnValue = libpandaexpress._inPJoxtooPl()
        return returnValue

    getDefaultEncoding = staticmethod(getDefaultEncoding)
    
    def reencodeText(text, _from, to):
        returnValue = libpandaexpress._inPJoxtT63X(text, _from, to)
        return returnValue

    reencodeText = staticmethod(reencodeText)
    
    def unicodeIsalpha(character):
        returnValue = libpandaexpress._inPJoxtojqf(character)
        return returnValue

    unicodeIsalpha = staticmethod(unicodeIsalpha)
    
    def unicodeIsdigit(character):
        returnValue = libpandaexpress._inPJoxtsaR4(character)
        return returnValue

    unicodeIsdigit = staticmethod(unicodeIsdigit)
    
    def unicodeIspunct(character):
        returnValue = libpandaexpress._inPJoxtJDmv(character)
        return returnValue

    unicodeIspunct = staticmethod(unicodeIspunct)
    
    def unicodeIslower(character):
        returnValue = libpandaexpress._inPJoxtX0SC(character)
        return returnValue

    unicodeIslower = staticmethod(unicodeIslower)
    
    def unicodeIsupper(character):
        returnValue = libpandaexpress._inPJoxtqvC8(character)
        return returnValue

    unicodeIsupper = staticmethod(unicodeIsupper)
    
    def unicodeToupper(character):
        returnValue = libpandaexpress._inPJoxt0HrF(character)
        return returnValue

    unicodeToupper = staticmethod(unicodeToupper)
    
    def unicodeTolower(character):
        returnValue = libpandaexpress._inPJoxtFs8L(character)
        return returnValue

    unicodeTolower = staticmethod(unicodeTolower)
    
    def _TextEncoder__overloaded_upper_atomicstring(source):
        returnValue = libpandaexpress._inPJoxtt0pk(source)
        return returnValue

    _TextEncoder__overloaded_upper_atomicstring = staticmethod(_TextEncoder__overloaded_upper_atomicstring)
    
    def _TextEncoder__overloaded_upper_atomicstring___enum__Encoding(source, encoding):
        returnValue = libpandaexpress._inPJoxtwe6q(source, encoding)
        return returnValue

    _TextEncoder__overloaded_upper_atomicstring___enum__Encoding = staticmethod(_TextEncoder__overloaded_upper_atomicstring___enum__Encoding)
    
    def _TextEncoder__overloaded_lower_atomicstring(source):
        returnValue = libpandaexpress._inPJoxtiTMW(source)
        return returnValue

    _TextEncoder__overloaded_lower_atomicstring = staticmethod(_TextEncoder__overloaded_lower_atomicstring)
    
    def _TextEncoder__overloaded_lower_atomicstring___enum__Encoding(source, encoding):
        returnValue = libpandaexpress._inPJoxt9Pec(source, encoding)
        return returnValue

    _TextEncoder__overloaded_lower_atomicstring___enum__Encoding = staticmethod(_TextEncoder__overloaded_lower_atomicstring___enum__Encoding)
    
    def getClassType():
        returnValue = libpandaexpress._inPJoxtoTj2()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setEncoding(self, encoding):
        returnValue = libpandaexpress._inPJoxtrlQJ(self.this, encoding)
        return returnValue

    
    def getEncoding(self):
        returnValue = libpandaexpress._inPJoxtLWo7(self.this)
        return returnValue

    
    def _TextEncoder__overloaded_setText_ptrTextEncoder_atomicstring(self, text):
        returnValue = libpandaexpress._inPJoxtNXzC(self.this, text)
        return returnValue

    
    def _TextEncoder__overloaded_setText_ptrTextEncoder_atomicstring___enum__Encoding(self, text, encoding):
        returnValue = libpandaexpress._inPJoxt4aXk(self.this, text, encoding)
        return returnValue

    
    def clearText(self):
        returnValue = libpandaexpress._inPJoxt0_D5(self.this)
        return returnValue

    
    def hasText(self):
        returnValue = libpandaexpress._inPJoxt_7oh(self.this)
        return returnValue

    
    def makeUpper(self):
        returnValue = libpandaexpress._inPJoxtlMP7(self.this)
        return returnValue

    
    def makeLower(self):
        returnValue = libpandaexpress._inPJoxtT0Ve(self.this)
        return returnValue

    
    def _TextEncoder__overloaded_getText_ptrConstTextEncoder(self):
        returnValue = libpandaexpress._inPJoxtp9Te(self.this)
        return returnValue

    
    def _TextEncoder__overloaded_getText_ptrConstTextEncoder___enum__Encoding(self, encoding):
        returnValue = libpandaexpress._inPJoxtGTNv(self.this, encoding)
        return returnValue

    
    def appendText(self, text):
        returnValue = libpandaexpress._inPJoxt2ChQ(self.this, text)
        return returnValue

    
    def appendUnicodeChar(self, character):
        returnValue = libpandaexpress._inPJoxtXBY2(self.this, character)
        return returnValue

    
    def getNumChars(self):
        returnValue = libpandaexpress._inPJoxt4x3n(self.this)
        return returnValue

    
    def getUnicodeChar(self, index):
        returnValue = libpandaexpress._inPJoxtkULv(self.this, index)
        return returnValue

    
    def setUnicodeChar(self, index, character):
        returnValue = libpandaexpress._inPJoxtTkrk(self.this, index, character)
        return returnValue

    
    def _TextEncoder__overloaded_getEncodedChar_ptrConstTextEncoder_int(self, index):
        returnValue = libpandaexpress._inPJoxtPGUu(self.this, index)
        return returnValue

    
    def _TextEncoder__overloaded_getEncodedChar_ptrConstTextEncoder_int___enum__Encoding(self, index, encoding):
        returnValue = libpandaexpress._inPJoxtKIi_(self.this, index, encoding)
        return returnValue

    
    def getTextAsAscii(self):
        returnValue = libpandaexpress._inPJoxtzcrI(self.this)
        return returnValue

    
    def upper(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return TextEncoder._TextEncoder__overloaded_upper_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return TextEncoder._TextEncoder__overloaded_upper_atomicstring___enum__Encoding(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    upper = staticmethod(upper)
    
    def lower(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return TextEncoder._TextEncoder__overloaded_lower_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return TextEncoder._TextEncoder__overloaded_lower_atomicstring___enum__Encoding(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    lower = staticmethod(lower)
    
    def getEncodedChar(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._TextEncoder__overloaded_getEncodedChar_ptrConstTextEncoder_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    return self._TextEncoder__overloaded_getEncodedChar_ptrConstTextEncoder_int___enum__Encoding(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setText(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._TextEncoder__overloaded_setText_ptrTextEncoder_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.StringType):
                if isinstance(_args[1], types.IntType):
                    return self._TextEncoder__overloaded_setText_ptrTextEncoder_atomicstring___enum__Encoding(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getText(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._TextEncoder__overloaded_getText_ptrConstTextEncoder()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._TextEncoder__overloaded_getText_ptrConstTextEncoder___enum__Encoding(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


