# File: F (Python 2.2)

import FFIConstants
WrapperClassMap = { }
DowncastMap = { }

def registerInTypeMap(pythonClass):
    TypedObject = TypedObject
    import pandac
    if issubclass(pythonClass, TypedObject.TypedObject):
        typeIndex = pythonClass.getClassType().getIndex()
        WrapperClassMap[typeIndex] = pythonClass
    


class FFIExternalObject:
    
    def __init__(self, *_args):
        self.userManagesMemory = 0
        self.this = 0

    
    def destructor(self):
        pass

    
    def getLineage(self, thisClass, targetBaseClass):
        return self.getLineageInternal(thisClass, targetBaseClass, [
            thisClass])

    
    def getLineageInternal(self, thisClass, targetBaseClass, chain):
        if targetBaseClass in thisClass.__bases__:
            return chain + [
                targetBaseClass]
        elif len(thisClass.__bases__) == 0:
            return 0
        else:
            for base in thisClass.__bases__:
                res = self.getLineageInternal(base, targetBaseClass, chain + [
                    base])
                if res:
                    return res
                
            
            return 0

    
    def getDowncastFunctions(self, thisClass, baseClass):
        lineage = self.getLineage(thisClass, baseClass)
        downcastFunctionList = []
        if not lineage:
            return []
        
        top = len(lineage) - 1
        for i in range(top):
            toClass = lineage[top - i - 1]
            fromClass = lineage[top - i]
            downcastFuncName = 'downcastTo' + toClass.__name__ + 'From' + fromClass.__name__
            for globmod in toClass.__CModuleDowncasts__:
                func = globmod.__dict__.get(downcastFuncName)
                if func:
                    downcastFunctionList.append(func)
                
            
        
        return downcastFunctionList

    
    def lookUpNewType(self, typeHandle, rootType):
        if typeHandle.getNumParentClasses() == 0:
            FFIConstants.notify.warning('Unknown class type: %s has no parents!' % typeHandle.getName())
            return None
        
        parentType = typeHandle.getParentTowards(rootType, self)
        parentIndex = parentType.getIndex()
        parentWrapperClass = WrapperClassMap.get(parentIndex)
        if parentWrapperClass == None:
            parentWrapperClass = self.lookUpNewType(parentType, rootType)
        
        if parentWrapperClass != None:
            WrapperClassMap[typeHandle.getIndex()] = parentWrapperClass
        
        return parentWrapperClass

    
    def setPointer(self):
        index = self.getTypeIndex()
        exactWrapperClass = WrapperClassMap.get(index)
        if exactWrapperClass == None:
            exactWrapperClass = self.lookUpNewType(self.getType(), self.getClassType())
        
        if exactWrapperClass and exactWrapperClass != self.__class__:
            exactObject = exactWrapperClass(None)
            downcastObject = self.downcast(exactWrapperClass)
            exactObject.this = downcastObject.this
            exactObject.userManagesMemory = downcastObject.userManagesMemory
            downcastObject.userManagesMemory = 0
            return exactObject
        else:
            return self

    
    def downcast(self, toClass):
        fromClass = self.__class__
        downcastChain = DowncastMap.get((fromClass, toClass))
        if downcastChain == None:
            downcastChain = self.getDowncastFunctions(toClass, fromClass)
            DowncastMap[(fromClass, toClass)] = downcastChain
        
        newObject = self
        for downcastFunc in downcastChain:
            newObject = downcastFunc(newObject)
        
        return newObject

    
    def compareTo(self, other):
        
        try:
            if self.this < other.this:
                return -1
            
            if self.this > other.this:
                return 1
            else:
                return 0
        except:
            return 1


    
    def __cmp__(self, other):
        if isinstance(other, self.__class__):
            return self.compareTo(other)
        else:
            return cmp(id(self), id(other))

    
    def __repr__(self):
        
        try:
            LineStream = LineStream
            import pandac
            lineStream = LineStream.LineStream()
            self.output(lineStream)
            baseRepr = lineStream.getLine()
        except AssertionError:
            e = None
            raise AssertionError, e
        except:
            baseRepr = '[' + self.__class__.__name__ + ' at: ' + `self.this` + ']'

        return baseRepr

    
    def __str__(self):
        baseRepr = '[' + self.__class__.__name__ + ' at: ' + `self.this` + ']'
        LineStream = LineStream
        import pandac
        lineStream = LineStream.LineStream()
        
        try:
            self.write(lineStream)
            while lineStream.isTextAvailable():
                baseRepr = baseRepr + '\n' + lineStream.getLine()
        except AssertionError:
            e = None
            raise AssertionError, e
        except:
            
            try:
                self.write(lineStream, 0)
                while lineStream.isTextAvailable():
                    baseRepr = baseRepr + '\n' + lineStream.getLine()
            except AssertionError:
                e = None
                raise AssertionError, e
            except:
                
                try:
                    self.output(lineStream)
                    while lineStream.isTextAvailable():
                        baseRepr = baseRepr + '\n' + lineStream.getLine()
                except AssertionError:
                    e = None
                    raise AssertionError, e
                except:
                    pass



        return baseRepr

    
    def __hash__(self):
        return self.this


