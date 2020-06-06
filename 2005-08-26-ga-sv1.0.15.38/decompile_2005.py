import marshal, zlib, os

# PLEASE RUN WITH PYTHON 2.2
# Made by Disyer 2020/06/06 for 2005/08/26 build

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
    data = data[1]

    for name, obj in data.iteritems():
        print 'Dumping', name
        name = name.replace('.', os.sep)
        mod_filename = os.path.join(folder, name)
        mod_folder = os.path.dirname(mod_filename)
        if not os.path.exists(mod_folder):
            os.makedirs(mod_folder)
        new_filename = mod_filename + '.pyc'
        dump_file(new_filename, obj)

dump_archive('Phase2.pyz', offset=1018, folder='launcher_modules')
dump_archive('Phase3.pyz', offset=1018, folder='modules')