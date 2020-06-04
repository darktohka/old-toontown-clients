# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\cygwin\home\toonpub\player\wintools\sdk\python\Python-2.4.1\Lib\email\__init__.py
__version__ = '3.0+'
__all__ = [
 'base64MIME', 'Charset', 'Encoders', 'Errors', 'Generator', 'Header', 'Iterators', 'Message', 'MIMEAudio', 'MIMEBase', 'MIMEImage', 'MIMEMessage', 'MIMEMultipart', 'MIMENonMultipart', 'MIMEText', 'Parser', 'quopriMIME', 'Utils', 'message_from_string', 'message_from_file']

def message_from_string(s, *args, **kws):
    from email.Parser import Parser
    return Parser(*args, **kws).parsestr(s)


def message_from_file(fp, *args, **kws):
    from email.Parser import Parser
    return Parser(*args, **kws).parse(fp)