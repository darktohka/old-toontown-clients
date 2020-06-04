# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\cygwin\home\toonpub\player\wintools\sdk\python\Python-2.4.1\Lib\email\Errors.py


class MessageError(Exception):
    __module__ = __name__


class MessageParseError(MessageError):
    __module__ = __name__


class HeaderParseError(MessageParseError):
    __module__ = __name__


class BoundaryError(MessageParseError):
    __module__ = __name__


class MultipartConversionError(MessageError, TypeError):
    __module__ = __name__


class MessageDefect:
    __module__ = __name__

    def __init__(self, line=None):
        self.line = line


class NoBoundaryInMultipartDefect(MessageDefect):
    __module__ = __name__


class StartBoundaryNotFoundDefect(MessageDefect):
    __module__ = __name__


class FirstHeaderLineIsContinuationDefect(MessageDefect):
    __module__ = __name__


class MisplacedEnvelopeHeaderDefect(MessageDefect):
    __module__ = __name__


class MalformedHeaderDefect(MessageDefect):
    __module__ = __name__


class MultipartInvariantViolationDefect(MessageDefect):
    __module__ = __name__