import os

# PLEASE RUN WITH PYTHON 3
# Made by Disyer 2020/06/04 for 2002/11/26 build by Prof. McMouse

for root, _, files in os.walk('.'):
    for file in files:
        if not file.endswith('.pyc_dis'):
            continue
        decompiled_folder = root + '_decompiled'
        if not os.path.exists(decompiled_folder):
            os.mkdir(decompiled_folder)
        os.rename(os.path.join(root, file), os.path.join(decompiled_folder, file.replace('.pyc_dis', '.py')))