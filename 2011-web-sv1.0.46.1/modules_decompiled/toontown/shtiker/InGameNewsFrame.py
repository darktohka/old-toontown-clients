# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\shtiker\InGameNewsFrame.py
import datetime
from toontown.shtiker import HtmlView

class InGameNewsFrame(HtmlView.HtmlView):
    __module__ = __name__
    TaskName = 'HtmlViewUpdateTask'

    def __init__(self, parent=aspect2d):
        HtmlView.HtmlView.__init__(self, parent)
        self.initialLoadDone = False
        self.accept('newsSnapshot', self.doSnapshot)

    def activate(self):
        self.quad.show()
        self.calcMouseLimits()
        if not self.initialLoadDone:
            inGameNewsUrl = self.getInGameNewsUrl()
            self.webView.loadURL2(inGameNewsUrl)
            self.initialLoadDone = True
        taskMgr.add(self.update, self.TaskName)

    def deactivate(self):
        self.quad.hide()
        taskMgr.remove(self.TaskName)

    def unload(self):
        self.deactivate()
        HtmlView.HtmlView.unload(self)
        self.ignore('newsSnapshot')

    def doSnapshot(self):
        curtime = datetime.datetime.now()
        filename = 'news_snapshot_' + curtime.isoformat()
        filename = filename.replace(':', '-')
        filename = filename.replace('.', '-')
        pngfilename = filename + '.png'
        self.writeTex(pngfilename)
        jpgfilename = filename + '.jpg'
        self.writeTex(jpgfilename)
        return jpgfilename