import uncompyle6
import os

# PLEASE RUN WITH PYTHON 3
# Made by Disyer 2020/06/04 for 2011 ActiveX sv1.0.46.1 build

# Decompiles all .pyo files in the "modules" folder using uncompyle6
# Make sure to install uncompyle6:
# python -m pip install uncompyle6

for root, _, files in os.walk('modules'):
    for file in files:
        if not file.endswith('.pyo'):
            continue

        path = os.path.join(root, file)
        fixed_path = path.split(os.sep)
        fixed_path[0] = 'modules_decompiled'
        fixed_path = os.sep.join(fixed_path).replace('.pyo', '.py')
        folder = os.path.dirname(fixed_path)
        
        if not os.path.exists(folder):
            os.makedirs(folder)

        if os.path.exists(fixed_path):
            continue

        print('Decompiling...', fixed_path)

        with open(fixed_path, 'w') as f:
            try:
                uncompyle6.decompile_file(path, f)
            except:
                print('FAILED DECOMPILATION', fixed_path)