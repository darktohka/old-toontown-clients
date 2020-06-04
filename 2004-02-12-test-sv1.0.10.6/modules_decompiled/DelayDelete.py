# File: D (Python 2.2)


class DelayDelete:
    
    def __init__(self, distObj):
        self.distObj = distObj
        self.distObj.delayDelete(1)

    
    def __del__(self):
        self.distObj.delayDelete(0)


