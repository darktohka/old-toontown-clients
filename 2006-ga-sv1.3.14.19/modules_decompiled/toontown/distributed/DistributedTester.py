# File: D (Python 2.2)

from direct.distributed import DistributedObject

class DistributedTester(DistributedObject.DistributedObject):
    
    def __init__(self, cr):
        print 'DistributedTester: __init__'
        DistributedObject.DistributedObject.__init__(self, cr)

    
    def disable(self):
        print 'DistributedTester: disable'
        DistributedObject.DistributedObject.disable(self)

    
    def generate(self):
        print 'DistributedTester: generate'
        DistributedObject.DistributedObject.generate(self)

    
    def generateInit(self):
        print 'DistributedTester: generateInit'
        DistributedObject.DistributedObject.generateInit(self)

    
    def delete(self):
        print 'DistributedTester: delete'
        DistributedObject.DistributedObject.delete(self)

    
    def setMovie(self, *args):
        print 'DistributedTester setMovie: doId: ', self.doId

    
    def setState(self, *args):
        print 'DistributedTester setState: doId: ', self.doId


