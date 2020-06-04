import marshal, zlib, os

# PLEASE RUN WITH PYTHON 2.2
# Made by Disyer 2020/05/18 for 2002/11/26 build by Prof. McMouse

def dump_file(filename, obj):
    file = open(filename, 'wb')
    bytecode = marshal.dumps(obj)
    file.write('2ded0d0a'.decode('hex'))
    file.write('\x00\x00\x00\x00')
    file.write(bytecode)

def dump_archive(filename, offset, folder):
    archive = open(filename, 'rb')
    data = archive.read()[offset:]
    archive.close()

    data = marshal.loads(zlib.decompress(data))

    if not os.path.exists(folder):
        os.mkdir(folder)

    for name, obj in data.iteritems():
        print 'Dumping', name
        new_filename = os.path.join(folder, name + '.pyc')
        dump_file(new_filename, obj)

dump_archive('Phase2.pyz', offset=888, folder='launcher_modules')