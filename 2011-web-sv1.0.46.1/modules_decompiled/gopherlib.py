# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\cygwin\home\toonpub\player\wintools\sdk\python\Python-2.4.1\Lib\gopherlib.py
__all__ = [
 'send_selector', 'send_query']
DEF_SELECTOR = '1/'
DEF_HOST = 'gopher.micro.umn.edu'
DEF_PORT = 70
A_TEXT = '0'
A_MENU = '1'
A_CSO = '2'
A_ERROR = '3'
A_MACBINHEX = '4'
A_PCBINHEX = '5'
A_UUENCODED = '6'
A_INDEX = '7'
A_TELNET = '8'
A_BINARY = '9'
A_DUPLICATE = '+'
A_SOUND = 's'
A_EVENT = 'e'
A_CALENDAR = 'c'
A_HTML = 'h'
A_TN3270 = 'T'
A_MIME = 'M'
A_IMAGE = 'I'
A_WHOIS = 'w'
A_QUERY = 'q'
A_GIF = 'g'
A_HTML = 'h'
A_WWW = 'w'
A_PLUS_IMAGE = ':'
A_PLUS_MOVIE = ';'
A_PLUS_SOUND = '<'
_names = dir()
_type_to_name_map = {}

def type_to_name(gtype):
    global _type_to_name_map
    if _type_to_name_map == {}:
        for name in _names:
            if name[:2] == 'A_':
                _type_to_name_map[eval(name)] = name[2:]

    if gtype in _type_to_name_map:
        return _type_to_name_map[gtype]
    return 'TYPE=%r' % (gtype,)


CRLF = '\r\n'
TAB = '\t'

def send_selector(selector, host, port=0):
    import socket
    if not port:
        i = host.find(':')
        if i >= 0:
            host, port = host[:i], int(host[i + 1:])
    if not port:
        port = DEF_PORT
    elif type(port) == type(''):
        port = int(port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(selector + CRLF)
    s.shutdown(1)
    return s.makefile('rb')


def send_query(selector, query, host, port=0):
    return send_selector(selector + '\t' + query, host, port)


def path_to_selector(path):
    if path == '/':
        return '/'
    else:
        return path[2:]


def path_to_datatype_name(path):
    if path == '/':
        return "TYPE='unknown'"
    else:
        return type_to_name(path[1])


def get_directory(f):
    entries = []
    while 1:
        line = f.readline()
        if not line:
            print '(Unexpected EOF from server)'
            break
        if line[-2:] == CRLF:
            line = line[:-2]
        elif line[-1:] in CRLF:
            line = line[:-1]
        if line == '.':
            break
        if not line:
            print '(Empty line from server)'
            continue
        gtype = line[0]
        parts = line[1:].split(TAB)
        if len(parts) < 4:
            print '(Bad line from server: %r)' % (line,)
            continue
        if len(parts) > 4:
            if parts[4:] != ['+']:
                print '(Extra info from server:',
                print parts[4:], ')'
        else:
            parts.append('')
        parts.insert(0, gtype)
        entries.append(parts)

    return entries


def get_textfile(f):
    lines = []
    get_alt_textfile(f, lines.append)
    return lines


def get_alt_textfile(f, func):
    while 1:
        line = f.readline()
        if not line:
            print '(Unexpected EOF from server)'
            break
        if line[-2:] == CRLF:
            line = line[:-2]
        elif line[-1:] in CRLF:
            line = line[:-1]
        if line == '.':
            break
        if line[:2] == '..':
            line = line[1:]
        func(line)


def get_binary(f):
    data = f.read()
    return data


def get_alt_binary(f, func, blocksize):
    while 1:
        data = f.read(blocksize)
        if not data:
            break
        func(data)


def test():
    import sys, getopt
    (opts, args) = getopt.getopt(sys.argv[1:], '')
    selector = DEF_SELECTOR
    type = selector[0]
    host = DEF_HOST
    if args:
        host = args[0]
        args = args[1:]
    if args:
        type = args[0]
        args = args[1:]
        if len(type) > 1:
            type, selector = type[0], type
        else:
            selector = ''
            if args:
                selector = args[0]
                args = args[1:]
        query = ''
        if args:
            query = args[0]
            args = args[1:]
    if type == A_INDEX:
        f = send_query(selector, query, host)
    else:
        f = send_selector(selector, host)
    if type == A_TEXT:
        lines = get_textfile(f)
        for item in lines:
            print item

    elif type in (A_MENU, A_INDEX):
        entries = get_directory(f)
        for item in entries:
            print item

    else:
        data = get_binary(f)
        print 'binary data:', len(data), 'bytes:', repr(data[:100])[:40]


if __name__ == '__main__':
    test()