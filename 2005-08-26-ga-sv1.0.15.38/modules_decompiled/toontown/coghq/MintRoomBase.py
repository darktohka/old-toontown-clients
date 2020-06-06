# File: M (Python 2.2)

from toontown.toonbase import ToontownGlobals

class MintRoomBase:
    
    def __init__(self):
        pass

    
    def setMintId(self, mintId):
        self.mintId = mintId
        self.cogTrack = ToontownGlobals.cogHQZoneId2dept(mintId)

    
    def setRoomId(self, roomId):
        self.roomId = roomId

    
    def getCogTrack(self):
        return self.cogTrack

    if __dev__:
        
        def getMintEntityTypeReg(self):
            import FactoryEntityTypes
            EntityTypeRegistry = EntityTypeRegistry
            import otp.level
            typeReg = EntityTypeRegistry.EntityTypeRegistry(FactoryEntityTypes)
            return typeReg

    

