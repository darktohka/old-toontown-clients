# File: l (Python 2.2)

import types
import libpandaexpress
import Iostream
import Ostream
import TypedReferenceCount
import ReferenceCount
import ISocketStream
import Istream
import OSocketStream
import SocketStream

def downcastToIostreamFromOstream(this):
    returnValue = libpandaexpress._inPKoxtHU9t(this.this)
    import Iostream
    returnObject = Iostream.Iostream(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def downcastToTypedReferenceCountFromReferenceCount(this):
    returnValue = libpandaexpress._inPKoxtsWXj(this.this)
    import TypedReferenceCount
    returnObject = TypedReferenceCount.TypedReferenceCount(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToISocketStreamFromIstream(this):
    returnValue = libpandaexpress._inP2KOdKSzi(this.this)
    import ISocketStream
    returnObject = ISocketStream.ISocketStream(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def downcastToOSocketStreamFromOstream(this):
    returnValue = libpandaexpress._inP2KOdf_gd(this.this)
    import OSocketStream
    returnObject = OSocketStream.OSocketStream(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def downcastToSocketStreamFromIostream(this):
    returnValue = libpandaexpress._inP2KOdvaoG(this.this)
    import SocketStream
    returnObject = SocketStream.SocketStream(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject

