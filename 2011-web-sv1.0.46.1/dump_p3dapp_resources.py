from panda3d.core import Multifile
import os

# PLEASE RUN WITH PYTHON 3
# Made by Disyer 2020/06/04 for 2011 ActiveX sv1.0.46.1 build

# Extracts all Toontown phase files into the "resources" folder

def extract(extraction_folder, mfPath):
    mf = Multifile()
    mf.openRead(mfPath)

    for i in range(mf.getNumSubfiles()):
        name = mf.get_subfile_name(i)
        filename = os.path.join(extraction_folder, name)
        folder = os.path.dirname(filename)
        
        if not os.path.exists(folder):
            os.makedirs(folder)

        mf.extract_subfile(i, filename)

if __name__ == '__main__':
    # ToontownOnline/panda3d/toontown ----> ToontownOnline
    for root, _, files in os.walk('../..'):
        for file in files:
            if not file.endswith('.mf') or not file.startswith('tt_'):
                continue
            
            print('Extracting...', file)
            extract('resources', os.path.join(root, file))