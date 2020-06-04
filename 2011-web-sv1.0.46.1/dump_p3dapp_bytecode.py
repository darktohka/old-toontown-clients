from panda3d.core import Multifile
import os

# PLEASE RUN WITH PYTHON 3
# Made by Disyer 2020/06/04 for 2011 ActiveX sv1.0.46.1 build

# Extracts all bytecode objects from panda3d.toontown.win32.mf into the "modules" folder

def extract(mf):
    mf = Multifile()
    mf.openRead(mf)
    extraction_folder = 'modules'

    for i in range(mf.getNumSubfiles()):
        name = mf.get_subfile_name(i)
        print(name)

        filename = os.path.join(extraction_folder, name)
        folder = os.path.dirname(filename)
        
        if not os.path.exists(folder):
            os.makedirs(folder)

        mf.extract_subfile(i, filename)

if __name__ == '__main__':
    extract('panda3d.toontown.win32.mf')