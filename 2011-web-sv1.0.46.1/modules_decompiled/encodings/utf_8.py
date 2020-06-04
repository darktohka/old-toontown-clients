# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\cygwin\home\toonpub\player\wintools\sdk\python\Python-2.4.1\Lib\encodings\utf_8.py
import codecs
encode = codecs.utf_8_encode

def decode(input, errors='strict'):
    return codecs.utf_8_decode(input, errors, True)


class StreamWriter(codecs.StreamWriter):
    __module__ = __name__
    encode = codecs.utf_8_encode


class StreamReader(codecs.StreamReader):
    __module__ = __name__
    decode = codecs.utf_8_decode


def getregentry():
    return (
     encode, decode, StreamReader, StreamWriter)