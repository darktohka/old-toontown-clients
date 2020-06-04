# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\cygwin\home\toonpub\player\wintools\sdk\python\Python-2.4.1\Lib\uu.py
import binascii, os, sys
from types import StringType
__all__ = [
 'Error', 'encode', 'decode']

class Error(Exception):
    __module__ = __name__


def encode(in_file, out_file, name=None, mode=None):
    if in_file == '-':
        in_file = sys.stdin
    elif isinstance(in_file, StringType):
        if name is None:
            name = os.path.basename(in_file)
        if mode is None:
            try:
                mode = os.stat(in_file).st_mode
            except AttributeError:
                pass

        in_file = open(in_file, 'rb')
    if out_file == '-':
        out_file = sys.stdout
    elif isinstance(out_file, StringType):
        out_file = open(out_file, 'w')
    if name is None:
        name = '-'
    if mode is None:
        mode = 438
    out_file.write('begin %o %s\n' % (mode & 511, name))
    str = in_file.read(45)
    while len(str) > 0:
        out_file.write(binascii.b2a_uu(str))
        str = in_file.read(45)

    out_file.write(' \nend\n')
    return


def decode(in_file, out_file=None, mode=None, quiet=0):
    if in_file == '-':
        in_file = sys.stdin
    elif isinstance(in_file, StringType):
        in_file = open(in_file)
    while 1:
        hdr = in_file.readline()
        if not hdr:
            raise Error, 'No valid begin line found in input file'
        if hdr[:5] != 'begin':
            continue
        hdrfields = hdr.split(' ', 2)
        if len(hdrfields) == 3 and hdrfields[0] == 'begin':
            try:
                int(hdrfields[1], 8)
                break
            except ValueError:
                pass

    if out_file is None:
        out_file = hdrfields[2].rstrip()
        if os.path.exists(out_file):
            raise Error, 'Cannot overwrite existing file: %s' % out_file
    if mode is None:
        mode = int(hdrfields[1], 8)
    if out_file == '-':
        out_file = sys.stdout
    elif isinstance(out_file, StringType):
        fp = open(out_file, 'wb')
        try:
            os.path.chmod(out_file, mode)
        except AttributeError:
            pass
        else:
            out_file = fp
    s = in_file.readline()
    while s and s.strip() != 'end':
        try:
            data = binascii.a2b_uu(s)
        except binascii.Error, v:
            nbytes = ((ord(s[0]) - 32 & 63) * 4 + 5) / 3
            data = binascii.a2b_uu(s[:nbytes])
            if not quiet:
                sys.stderr.write('Warning: %s\n' % str(v))

        out_file.write(data)
        s = in_file.readline()

    if not s:
        raise Error, 'Truncated input file'
    return


def test():
    import getopt
    dopt = 0
    topt = 0
    input = sys.stdin
    output = sys.stdout
    ok = 1
    try:
        (optlist, args) = getopt.getopt(sys.argv[1:], 'dt')
    except getopt.error:
        ok = 0

    if not ok or len(args) > 2:
        print 'Usage:', sys.argv[0], '[-d] [-t] [input [output]]'
        print ' -d: Decode (in stead of encode)'
        print ' -t: data is text, encoded format unix-compatible text'
        sys.exit(1)
    for (o, a) in optlist:
        if o == '-d':
            dopt = 1
        if o == '-t':
            topt = 1

    if len(args) > 0:
        input = args[0]
    if len(args) > 1:
        output = args[1]
    if dopt:
        if topt:
            if isinstance(output, StringType):
                output = open(output, 'w')
            else:
                print sys.argv[0], ': cannot do -t to stdout'
                sys.exit(1)
        decode(input, output)
    else:
        if topt:
            if isinstance(input, StringType):
                input = open(input, 'r')
            else:
                print sys.argv[0], ': cannot do -t from stdin'
                sys.exit(1)
        encode(input, output)


if __name__ == '__main__':
    test()