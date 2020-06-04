# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\stdpy\file.py
__all__ = [
 'file', 'open', 'listdir', 'walk', 'join', 'isfile', 'isdir', 'exists', 'lexists', 'getmtime', 'getsize']
from pandac import PandaModules as pm
import types
_vfs = pm.VirtualFileSystem.getGlobalPtr()

class file:
    __module__ = __name__

    def __init__(self, filename, mode='r', bufsize=None, autoUnwrap=False):
        self.__stream = None
        self.__needsVfsClose = False
        self.__reader = None
        self.__writer = None
        self.closed = True
        self.encoding = None
        self.errors = None
        self.__lastWrite = False
        self.mode = mode
        self.name = None
        self.filename = None
        self.newlines = None
        self.softspace = False
        readMode = False
        writeMode = False
        if isinstance(filename, pm.Istream) or isinstance(filename, pm.Ostream):
            self.__stream = filename
            readMode = isinstance(filename, pm.Istream)
            writeMode = isinstance(filename, pm.Ostream)
        elif isinstance(filename, pm.VirtualFile):
            self.__stream = filename.openReadFile(autoUnwrap)
            if not self.__stream:
                message = 'Could not read virtual file %s' % repr(filename)
                raise IOError, message
            self.__needsVfsClose = True
            readMode = True
        else:
            if isinstance(filename, types.StringTypes):
                filename = pm.Filename.fromOsSpecific(filename)
            else:
                filename = pm.Filename(filename)
            self.filename = filename
            self.name = filename.toOsSpecific()
            binary = False
            if 'b' in mode:
                i = mode.index('b')
                mode = mode[:i] + mode[i + 1:]
                binary = True
            if 'U' in mode:
                i = mode.index('U')
                mode = mode[:i] + mode[i + 1:]
                binary = False
            if mode == '':
                mode = 'r'
            if binary:
                filename.setBinary()
            else:
                filename.setText()
            if mode == 'w':
                self.__stream = pm.OFileStream()
                if not filename.openWrite(self.__stream, True):
                    message = 'Could not open %s for writing' % filename
                    raise IOError, message
                writeMode = True
            elif mode == 'a':
                self.__stream = pm.OFileStream()
                if not filename.openAppend(self.__stream):
                    message = 'Could not open %s for writing' % filename
                    raise IOError, message
                writeMode = True
            elif mode == 'w+':
                self.__stream = pm.FileStream()
                if not filename.openReadWrite(self.__stream, True):
                    message = 'Could not open %s for writing' % filename
                    raise IOError, message
                readMode = True
                writeMode = True
            elif mode == 'a+':
                self.__stream = pm.FileStream()
                if not filename.openReadAppend(self.__stream):
                    message = 'Could not open %s for writing' % filename
                    raise IOError, message
                readMode = True
                writeMode = True
            elif mode == 'r+':
                self.__stream = pm.FileStream()
                if not filename.exists():
                    message = 'No such file: %s' % filename
                    raise IOError, message
                if not filename.openReadWrite(self.__stream, False):
                    message = 'Could not open %s for writing' % filename
                    raise IOError, message
                readMode = True
                writeMode = True
            elif mode == 'r':
                self.__stream = _vfs.openReadFile(filename, autoUnwrap)
                if not self.__stream:
                    if not filename.exists():
                        message = 'No such file: %s' % filename
                    else:
                        message = 'Could not open %s for reading' % filename
                    raise IOError, message
                self.__needsVfsClose = True
                readMode = True
        if readMode:
            self.__reader = pm.StreamReader(self.__stream, False)
        if writeMode:
            self.__writer = pm.StreamWriter(self.__stream, False)
        return

    def __del__(self):
        self.close()

    def close(self):
        if self.__needsVfsClose:
            _vfs.closeReadFile(self.__stream)
            self.__needsVfsClose = False
        self.__stream = None
        self.__needsVfsClose = False
        self.__reader = None
        self.__writer = None
        return

    def flush(self):
        if self.__stream:
            self.__stream.flush()

    def __iter__(self):
        return self

    def next(self):
        line = self.readline()
        if line:
            return line
        raise StopIteration

    def read(self, size=-1):
        if not self.__reader:
            if not self.__writer:
                message = 'I/O operation on closed file'
                raise ValueError, message
            message = 'Attempt to read from write-only stream'
            raise IOError, message
        self.__lastWrite = False
        if size >= 0:
            return self.__reader.extractBytes(size)
        else:
            result = ''
            while not self.__stream.eof():
                result += self.__reader.extractBytes(1024)

            return result

    def readline(self, size=-1):
        if not self.__reader:
            if not self.__writer:
                message = 'I/O operation on closed file'
                raise ValueError, message
            message = 'Attempt to read from write-only stream'
            raise IOError, message
        self.__lastWrite = False
        return self.__reader.readline()

    def readlines(self, sizehint=-1):
        lines = []
        line = self.readline()
        while line:
            lines.append(line)
            line = self.readline()

        return lines

    xreadlines = readlines

    def seek(self, offset, whence=0):
        if self.__reader:
            self.__stream.seekg(offset, whence)
        if self.__writer:
            self.__stream.seekp(offset, whence)

    def tell(self):
        if self.__lastWrite:
            if self.__writer:
                return self.__stream.tellp()
        elif self.__reader:
            return self.__stream.tellg()
        message = 'I/O operation on closed file'
        raise ValueError, message

    def truncate(self):
        raise NotImplementedError

    def write(self, str):
        if not self.__writer:
            if not self.__reader:
                message = 'I/O operation on closed file'
                raise ValueError, message
            message = 'Attempt to write to read-only stream'
            raise IOError, message
        self.__writer.appendData(str)
        self.__lastWrite = True

    def writelines(self, lines):
        if not self.__writer:
            if not self.__reader:
                message = 'I/O operation on closed file'
                raise ValueError, message
            message = 'Attempt to write to read-only stream'
            raise IOError, message
        for line in lines:
            self.__writer.appendData(line)

        self.__lastWrite = True

    def __enter__(self):
        return self

    def __exit__(self, t, v, tb):
        self.close()


open = file

def listdir(path):
    files = []
    dirlist = _vfs.scanDirectory(pm.Filename.fromOsSpecific(path))
    if dirlist is None:
        message = 'No such file or directory: %s' % path
        raise OSError, message
    for file in dirlist:
        files.append(file.getFilename().getBasename())

    return files


def walk(top, topdown=True, onerror=None, followlinks=True):
    dirnames = []
    filenames = []
    dirlist = _vfs.scanDirectory(top)
    if dirlist:
        for file in dirlist:
            if file.isDirectory():
                dirnames.append(file.getFilename().getBasename())
            else:
                filenames.append(file.getFilename().getBasename())

    if topdown:
        yield (
         top, dirnames, filenames)
    for dir in dirnames:
        next = join(top, dir)
        for tuple in walk(next, topdown=topdown):
            yield tuple

    if not topdown:
        yield (
         top, dirnames, filenames)


def join(a, b):
    return '%s/%s' % (a, b)


def isfile(path):
    return _vfs.isRegularFile(pm.Filename.fromOsSpecific(path))


def isdir(path):
    return _vfs.isDirectory(pm.Filename.fromOsSpecific(path))


def exists(path):
    return _vfs.exists(pm.Filename.fromOsSpecific(path))


def lexists(path):
    return _vfs.exists(pm.Filename.fromOsSpecific(path))


def getmtime(path):
    file = _vfs.getFile(pm.Filename.fromOsSpecific(path), True)
    if not file:
        raise os.error
    return file.getTimestamp()


def getsize(path):
    file = _vfs.getFile(pm.Filename.fromOsSpecific(path), True)
    if not file:
        raise os.error
    return file.getFileSize()