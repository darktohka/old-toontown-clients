# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\cygwin\home\toonpub\player\wintools\sdk\python\Python-2.4.1\Lib\getpass.py
import sys
__all__ = [
 'getpass', 'getuser']

def unix_getpass(prompt='Password: '):
    try:
        fd = sys.stdin.fileno()
    except:
        return default_getpass(prompt)

    old = termios.tcgetattr(fd)
    new = old[:]
    new[3] = new[3] & ~termios.ECHO
    try:
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        passwd = _raw_input(prompt)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    sys.stdout.write('\n')
    return passwd


def win_getpass(prompt='Password: '):
    if sys.stdin is not sys.__stdin__:
        return default_getpass(prompt)
    import msvcrt
    for c in prompt:
        msvcrt.putch(c)

    pw = ''
    while 1:
        c = msvcrt.getch()
        if c == '\r' or c == '\n':
            break
        if c == '\x03':
            raise KeyboardInterrupt
        if c == '\x08':
            pw = pw[:-1]
        else:
            pw = pw + c

    msvcrt.putch('\r')
    msvcrt.putch('\n')
    return pw


def default_getpass(prompt='Password: '):
    print 'Warning: Problem with getpass. Passwords may be echoed.'
    return _raw_input(prompt)


def _raw_input(prompt=''):
    prompt = str(prompt)
    if prompt:
        sys.stdout.write(prompt)
    line = sys.stdin.readline()
    if not line:
        raise EOFError
    if line[(-1)] == '\n':
        line = line[:-1]
    return line


def getuser():
    import os
    for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
        user = os.environ.get(name)
        if user:
            return user

    import pwd
    return pwd.getpwuid(os.getuid())[0]


try:
    import termios
    (
     termios.tcgetattr, termios.tcsetattr)
except (ImportError, AttributeError):
    try:
        import msvcrt
    except ImportError:
        try:
            from EasyDialogs import AskPassword
        except ImportError:
            getpass = default_getpass
        else:
            getpass = AskPassword
    else:
        getpass = win_getpass
else:
    getpass = unix_getpass