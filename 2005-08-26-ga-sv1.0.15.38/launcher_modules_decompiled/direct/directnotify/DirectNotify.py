# File: D (Python 2.2)

import Notifier
import Logger

class DirectNotify:
    
    def __init__(self):
        self._DirectNotify__categories = { }
        self.logger = Logger.Logger()
        self.streamWriter = None

    
    def __str__(self):
        return 'DirectNotify categories: %s' % self._DirectNotify__categories

    
    def getCategories(self):
        return self._DirectNotify__categories.keys()

    
    def getCategory(self, categoryName):
        return self._DirectNotify__categories.get(categoryName, None)

    
    def newCategory(self, categoryName, logger = None):
        if not self._DirectNotify__categories.has_key(categoryName):
            self._DirectNotify__categories[categoryName] = Notifier.Notifier(categoryName, logger)
            self.setDconfigLevel(categoryName)
        else:
            print "Warning: DirectNotify: category '%s' already exists" % categoryName
        return self.getCategory(categoryName)

    
    def setDconfigLevel(self, categoryName):
        
        try:
            pass
        except:
            return 0

        dconfigParam = 'notify-level-' + categoryName
        level = config.GetString(dconfigParam, '')
        if not level:
            level = config.GetString('default-directnotify-level', '')
        
        if level:
            print 'Setting DirectNotify category: ' + categoryName + ' to severity: ' + level
            category = self.getCategory(categoryName)
            if level == 'error':
                category.setWarning(0)
                category.setInfo(0)
                category.setDebug(0)
            elif level == 'warning':
                category.setWarning(1)
                category.setInfo(0)
                category.setDebug(0)
            elif level == 'info':
                category.setWarning(1)
                category.setInfo(1)
                category.setDebug(0)
            elif level == 'debug':
                category.setWarning(1)
                category.setInfo(1)
                category.setDebug(1)
            else:
                print 'DirectNotify: unknown notify level: ' + str(level) + ' for category: ' + str(categoryName)
        

    
    def setDconfigLevels(self):
        for categoryName in self.getCategories():
            self.setDconfigLevel(categoryName)
        

    
    def popupControls(self, tl = None):
        NotifyPanel = NotifyPanel
        import direct.tkpanels
        NotifyPanel.NotifyPanel(self, tl)


