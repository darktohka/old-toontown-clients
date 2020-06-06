# File: C (Python 2.2)

import CatalogFurnitureItem
TI_CatalogFurnitureItem = 1

class CatalogItemDecoder:
    
    def makeItem(self, di):
        typeIndex = di.getUint8()


