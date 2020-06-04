# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\task\MiniTask.py
__all__ = [
 'MiniTask', 'MiniTaskManager']

class MiniTask:
    __module__ = __name__
    done = 0
    cont = 1

    def __init__(self, callback):
        self.__call__ = callback


class MiniTaskManager:
    __module__ = __name__

    def __init__(self):
        self.taskList = []
        self.running = 0

    def add(self, task, name):
        task.name = name
        self.taskList.append(task)

    def remove(self, task):
        try:
            self.taskList.remove(task)
        except ValueError:
            pass

    def __executeTask(self, task):
        return task(task)

    def step(self):
        i = 0
        while i < len(self.taskList):
            task = self.taskList[i]
            ret = task(task)
            if ret == task.cont:
                pass
            try:
                self.taskList.remove(task)
            except ValueError:
                pass
            else:
                continue

            i += 1

    def run(self):
        self.running = 1
        while self.running:
            self.step()

    def stop(self):
        self.running = 0