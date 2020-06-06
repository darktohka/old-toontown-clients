import os

# PLEASE RUN WITH PYTHON 3
# Made by Disyer 2020/06/06 for 2005/08/26 build

for root, _, files in os.walk('.'):
    for file in files:
        if not file.endswith('.pyc_dis'):
            continue

        split_root = root.split(os.sep)
        split_root[1] = split_root[1] + '_decompiled'
        split_root = os.sep.join(split_root)

        if not os.path.exists(split_root):
            os.makedirs(split_root)

        os.rename(os.path.join(root, file), os.path.join(split_root, file.replace('.pyc_dis', '.py')))