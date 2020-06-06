# File: T (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

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
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpandaexpress._inPKoxtfza9()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxt3ZE7:
            libpandaexpress._inPKoxt3ZE7(self.this)
        

    
    def setDefaultEncoding(encoding):
        returnValue = libpandaexpress._inPKoxtFCJv(encoding)
        return returnValue

    setDefaultEncoding = staticmethod(setDefaultEncoding)
    
    def getDefaultEncoding():
        returnValue = libpandaexpress._inPKoxtroPl()
        return returnValue

    getDefaultEncoding = staticmethod(getDefaultEncoding)
    
    def reencodeText(text, _from, to):
        returnValue = libpandaexpress._inPKoxtT63X(text, _from, to)
        return returnValue

    reencodeText = staticmethod(reencodeText)
    
    def unicodeIsalpha(character):
        returnValue = libpandaexpress._inPKoxtojqf(character)
        return returnValue

    unicodeIsalpha = staticmethod(unicodeIsalpha)
    
    def unicodeIsdigit(character):
        returnValue = libpandaexpress._inPKoxtvaR4(character)
        return returnValue

    unicodeIsdigit = staticmethod(unicodeIsdigit)
    
    def unicodeIspunct(character):
        returnValue = libpandaexpress._inPKoxtIDmv(character)
        return returnValue

    unicodeIspunct = staticmethod(unicodeIspunct)
    
    def unicodeIslower(character):
        returnValue = libpandaexpress._inPKoxtX0SC(character)
        return returnValue

    unicodeIslower = staticmethod(unicodeIslower)
    
    def unicodeIsupper(character):
        returnValue = libpandaexpress._inPKoxtrvC8(character)
        return returnValue

    unicodeIsupper = staticmethod(unicodeIsupper)
    
    def unicodeToupper(character):
        returnValue = libpandaexpress._inPKoxt0HrF(character)
        return returnValue

    unicodeToupper = staticmethod(unicodeToupper)
    
    def unicodeTolower(character):
        returnValue = libpandaexpress._inPKoxtFs8L(character)
        return returnValue

    unicodeTolower = staticmethod(unicodeTolower)
    
    def _TextEncoder__overloaded_upper_atomicstring(source):
        returnValue = libpandaexpress._inPKoxts0pk(source)
        return returnValue

    _TextEncoder__overloaded_upper_atomicstring = staticmethod(_TextEncoder__overloaded_upper_atomicstring)
    
    def _TextEncoder__overloaded_upper_atomicstring___enum__Encoding(source, encoding):
        returnValue = libpandaexpress._inPKoxtxe6q(source, encoding)
        return returnValue

    _TextEncoder__overloaded_upper_atomicstring___enum__Encoding = staticmethod(_TextEncoder__overloaded_upper_atomicstring___enum__Encoding)
    
    def _TextEncoder__overloaded_lower_atomicstring(source):
        returnValue = libpandaexpress._inPKoxtiTMW(source)
        return returnValue

    _TextEncoder__overloaded_lower_atomicstring = staticmethod(_TextEncoder__overloaded_lower_atomicstring)
    
    def _TextEncoder__overloaded_lower_atomicstring___enum__Encoding(source, encoding):
        returnValue = libpandaexpress._inPKoxt9Pec(source, encoding)
        return returnValue

    _TextEncoder__overloaded_lower_atomicstring___enum__Encoding = staticmethod(_TextEncoder__overloaded_lower_atomicstring___enum__Encoding)
    
    def getClassType():
        returnValue = libpandaexpress._inPKoxtnTj2()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setEncoding(self, encoding):
        returnValue = libpandaexpress._inPKoxtrlQJ(self.this, encoding)
        return returnValue

    
    def getEncoding(self):
        returnValue = libpandaexpress._inPKoxtMWo7(self.this)
        return returnValue

    
    def _TextEncoder__overloaded_setText_ptrTextEncoder_atomicstring(self, text):
        returnValue = libpandaexpress._inPKoxtNXzC(self.this, text)
        return returnValue

    
    def _TextEncoder__overloaded_setText_ptrTextEncoder_atomicstring___enum__Encoding(self, text, encoding):
        returnValue = libpandaexpress._inPKoxt5aXk(self.this, text, encoding)
        return returnValue

    
    def clearText(self):
        returnValue = libpandaexpress._inPKoxtz_D5(self.this)
        return returnValue

    
    def hasText(self):
        returnValue = libpandaexpress._inPKoxt97oh(self.this)
        return returnValue

    
    def makeUpper(self):
        returnValue = libpandaexpress._inPKoxtqMP7(self.this)
        return returnValue

    
    def makeLower(self):
        returnValue = libpandaexpress._inPKoxtT0Ve(self.this)
        return returnValue

    
    def _TextEncoder__overloaded_getText_ptrConstTextEncoder(self):
        returnValue = libpandaexpress._inPKoxtp9Te(self.this)
        return returnValue

    
    def _TextEncoder__overloaded_getText_ptrConstTextEncoder___enum__Encoding(self, encoding):
        returnValue = libpandaexpress._inPKoxtJTNv(self.this, encoding)
        return returnValue

    
    def appendText(self, text):
        returnValue = libpandaexpress._inPKoxt2ChQ(self.this, text)
        return returnValue

    
    def appendUnicodeChar(self, character):
        returnValue = libpandaexpress._inPKoxtoBY2(self.this, character)
        return returnValue

    
    def getNumChars(self):
        returnValue = libpandaexpress._inPKoxt5x3n(self.this)
        return returnValue

    
    def getUnicodeChar(self, index):
        returnValue = libpandaexpress._inPKoxtjULv(self.this, index)
        return returnValue

    
    def setUnicodeChar(self, index, character):
        returnValue = libpandaexpress._inPKoxtSkrk(self.this, index, character)
        return returnValue

    
    def _TextEncoder__overloaded_getEncodedChar_ptrConstTextEncoder_int(self, index):
        returnValue = libpandaexpress._inPKoxtIGUu(self.this, index)
        return returnValue

    
    def _TextEncoder__overloaded_getEncodedChar_ptrConstTextEncoder_int___enum__Encoding(self, index, encoding):
        returnValue = libpandaexpress._inPKoxtJIi_(self.this, index, encoding)
        return returnValue

    
    def getTextAsAscii(self):
        returnValue = libpandaexpress._inPKoxtzcrI(self.this)
        return returnValue

    
    def upper(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return TextEncoder._TextEncoder__overloaded_upper_atomicstring(*_args)
        elif numArgs == 2:
            return TextEncoder._TextEncoder__overloaded_upper_atomicstring___enum__Encoding(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    upper = staticmethod(upper)
    
    def lower(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return TextEncoder._TextEncoder__overloaded_lower_atomicstring(*_args)
        elif numArgs == 2:
            return TextEncoder._TextEncoder__overloaded_lower_atomicstring___enum__Encoding(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    lower = staticmethod(lower)
    
    def getEncodedChar(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextEncoder__overloaded_getEncodedChar_ptrConstTextEncoder_int(*_args)
        elif numArgs == 2:
            return self._TextEncoder__overloaded_getEncodedChar_ptrConstTextEncoder_int___enum__Encoding(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setText(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._TextEncoder__overloaded_setText_ptrTextEncoder_atomicstring(*_args)
        elif numArgs == 2:
            return self._TextEncoder__overloaded_setText_ptrTextEncoder_atomicstring___enum__Encoding(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getText(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._TextEncoder__overloaded_getText_ptrConstTextEncoder(*_args)
        elif numArgs == 1:
            return self._TextEncoder__overloaded_getText_ptrConstTextEncoder___enum__Encoding(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


