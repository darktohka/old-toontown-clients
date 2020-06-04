# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\launcher\procapi.py
import ctypes
from ctypes.wintypes import *
TH32CS_SNAPPROCESS = 2
INVALID_HANDLE_VALUE = -1
cwk = ctypes.windll.kernel32

class PROCESSENTRY32(ctypes.Structure):
    __module__ = __name__
    _fields_ = [('dwSize', DWORD), ('cntUsage', DWORD), ('th32ProcessID', DWORD), ('th32DefaultHeapId', HANDLE), ('th32ModuleID', DWORD), ('cntThreads', DWORD), ('th32ParentProcessID', DWORD), ('pcPriClassBase', LONG), ('dwFlags', DWORD), ('szExeFile', c_char * MAX_PATH)]


class ProcessEntryPY:
    __module__ = __name__

    def __init__(self, name, pid):
        self.name = name
        self.pid = pid


def getProcessList():
    hProcessSnap = cwk.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
    processList = []
    if hProcessSnap != INVALID_HANDLE_VALUE:
        pe32 = PROCESSENTRY32()
        pe32.dwSize = sizeof(pe32)
        if cwk.Process32First(hProcessSnap, ctypes.byref(pe32)):
            while 1:
                processList.append(ProcessEntryPY(pe32.szExeFile.lower(), int(pe32.th32ProcessID)))
                if not cwk.Process32Next(hProcessSnap, ctypes.byref(pe32)):
                    break

        cwk.CloseHandle(hProcessSnap)
    return processList