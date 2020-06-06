# File: C (Python 2.2)

import CatalogAtticItem
import ToontownGlobals
import Localizer
WTTextureName = 0
WTTexture2Name = 1
WTSurface = 2
WTColor = 3
WTColor2 = 4
WTBasePrice = 5
STWall = 0
STMoulding = 1
STFloor = 2
STWainscoting = 3
STBorder = 4
CTBasicWallColor = ((0.78900000000000003, 1, 0.69999999999999996), (1, 1, 0.69999999999999996), (1, 0.81999999999999995, 0.69999999999999996), (0.83899999999999997, 0.65100000000000002, 0.54900000000000004), (0.5, 0.58599999999999997, 0.40000000000000002), (0.80800000000000005, 0.67800000000000005, 0.51000000000000001), (0.875, 0.93700000000000006, 1.0))
CTFlatColor = ((1, 0.80000000000000004, 0.59999999999999998), (0.59999999999999998, 1, 0.80000000000000004), (0.59999999999999998, 0.59999999999999998, 1), (1, 0.59999999999999998, 1), (1, 1, 0.59999999999999998), (1, 0.5, 0.5))
CTFlatWhite = ((1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1))
CTFlatColorDark = []
tint = 0.75
for color in CTFlatColor:
    CTFlatColorDark.append((color[0] * tint, color[1] * tint, color[2] * tint))

CTBasicWoodColor = ((1.0, 1.0, 1.0), (0.68999999999999995, 0.74099999999999999, 0.70999999999999996))
CTBasicWoodColorOnWhite = ((0.54900000000000004, 0.41199999999999998, 0.25900000000000001), (0.443, 0.33300000000000002, 0.17599999999999999), (1.0, 0.81200000000000006, 0.48999999999999999), (0.70999999999999996, 0.40799999999999997, 0.26700000000000002), (0.96099999999999997, 0.65900000000000003, 0.40000000000000002))
WallpaperTypes = {
    1: ('phase_3.5/maps/stripeB5.jpg', None, STWall, CTBasicWallColor, None, 180),
    2: ('phase_5.5/maps/squiggle1.jpg', None, STWall, CTBasicWallColor, None, 180),
    3: ('phase_5.5/maps/diamonds2_cherries.jpg', None, STWall, CTBasicWallColor, None, 180),
    4: ('phase_5.5/maps/big_stripes4.jpg', 'phase_5.5/maps/diamonds_border2.jpg', STWall, CTBasicWallColor, None, 180),
    5: ('phase_5.5/maps/flat_wallpaper1.jpg', None, STWall, CTBasicWallColor, None, 180),
    101: ('phase_5.5/maps/floor_wood_neutral.jpg', None, STFloor, CTBasicWoodColorOnWhite, None, 150),
    102: ('phase_5.5/maps/flooring_carpetA_neutral.jpg', None, STFloor, CTFlatColorDark, None, 150),
    103: ('phase_5.5/maps/flooring_tile_neutral.jpg', None, STFloor, CTFlatColorDark, None, 150),
    104: ('phase_5.5/maps/flooring_tileB2.jpg', None, STFloor, None, None, 150),
    105: ('phase_4/maps/grass.jpg', None, STFloor, None, None, 150),
    106: ('phase_4/maps/floor_tile_brick_diagonal2.jpg', None, STFloor, None, None, 150),
    107: ('phase_4/maps/floor_tile_brick_diagonal.jpg', None, STFloor, None, None, 150),
    108: ('phase_4/maps/plazz_tile.jpg', None, STFloor, None, None, 150),
    109: ('phase_4/maps/sidewalk.jpg', None, STFloor, CTFlatColorDark, None, 150),
    110: ('phase_3.5/maps/boardwalk_floor.jpg', None, STFloor, None, None, 150),
    111: ('phase_3.5/maps/dustroad.jpg', None, STFloor, None, None, 150),
    151: ('phase_3.5/maps/molding_wood1.jpg', None, STMoulding, CTBasicWoodColorOnWhite, None, 150),
    152: ('phase_3.5/maps/molding_wood2.jpg', None, STMoulding, CTBasicWoodColor, None, 150),
    153: ('phase_5.5/maps/bd_grey_border1.jpg', None, STMoulding, CTFlatColorDark, None, 150),
    201: ('phase_3.5/maps/wall_paper_b3.jpg', None, STWainscoting, CTFlatColorDark, None, 200),
    202: ('phase_5.5/maps/wall_paper_b4_greyscale.jpg', None, STWainscoting, CTBasicWoodColorOnWhite, None, 200),
    1000: ('phase_5.5/maps/flat_wallpaper1.jpg', None, STWall, CTFlatColor, None, 180),
    1010: ('phase_5.5/maps/flat_wallpaper1.jpg', 'phase_5.5/maps/bd_grey_border1.jpg', STWall, CTFlatColor, CTFlatColorDark, 180),
    1100: ('phase_5.5/maps/big_stripes1.jpg', None, STWall, None, None, 180),
    1102: ('phase_5.5/maps/big_stripes1.jpg', 'phase_5.5/maps/diamonds_border2.jpg', STWall, None, None, 180),
    1110: ('phase_5.5/maps/big_stripes2.jpg', None, STWall, None, None, 180),
    1112: ('phase_5.5/maps/big_stripes2.jpg', 'phase_5.5/maps/diamonds_border4ch.jpg', STWall, None, None, 180),
    1120: ('phase_5.5/maps/big_stripes3.jpg', None, STWall, None, None, 180),
    1122: ('phase_5.5/maps/big_stripes3.jpg', 'phase_5.5/maps/diamonds_border3ch.jpg', STWall, None, None, 180),
    1130: ('phase_5.5/maps/big_stripes4.jpg', None, STWall, None, None, 180),
    1132: ('phase_5.5/maps/big_stripes4.jpg', 'phase_5.5/maps/diamonds_border2.jpg', STWall, None, None, 180),
    1140: ('phase_5.5/maps/big_stripes5.jpg', None, STWall, None, None, 180),
    1142: ('phase_5.5/maps/big_stripes5.jpg', 'phase_5.5/maps/diamonds_border2ch.jpg', STWall, None, None, 180),
    1150: ('phase_5.5/maps/big_stripes6.jpg', None, STWall, None, None, 180),
    1152: ('phase_5.5/maps/big_stripes6.jpg', 'phase_5.5/maps/diamonds_border2ch.jpg', STWall, None, None, 180),
    1200: ('phase_5.5/maps/stripeB1.jpg', None, STWall, None, None, 180),
    1210: ('phase_5.5/maps/stripeB2.jpg', None, STWall, None, None, 180),
    1220: ('phase_5.5/maps/stripeB3.jpg', None, STWall, None, None, 180),
    1230: ('phase_5.5/maps/stripeB4.jpg', None, STWall, None, None, 180),
    1240: ('phase_3.5/maps/stripeB5.jpg', None, STWall, None, None, 180),
    1250: ('phase_5.5/maps/stripeB6.jpg', None, STWall, None, None, 180),
    1260: ('phase_5.5/maps/stripeB7.jpg', None, STWall, None, None, 180),
    1300: ('phase_5.5/maps/squiggle1.jpg', None, STWall, None, None, 180),
    1310: ('phase_5.5/maps/squiggle2.jpg', None, STWall, None, None, 180),
    1320: ('phase_5.5/maps/squiggle3.jpg', None, STWall, None, None, 180),
    1330: ('phase_5.5/maps/squiggle4.jpg', None, STWall, None, None, 180),
    1340: ('phase_5.5/maps/squiggle5.jpg', None, STWall, None, None, 180),
    1350: ('phase_5.5/maps/squiggle6.jpg', None, STWall, None, None, 180),
    1400: ('phase_5.5/maps/stripes_cyan.jpg', None, STWall, None, None, 180),
    1410: ('phase_5.5/maps/stripes_green.jpg', None, STWall, None, None, 180),
    1420: ('phase_5.5/maps/stripes_magenta.jpg', None, STWall, None, None, 180),
    1430: ('phase_5.5/maps/two_stripes1.jpg', None, STWall, None, None, 180),
    1440: ('phase_5.5/maps/two_stripes2.jpg', None, STWall, None, None, 180),
    1450: ('phase_5.5/maps/two_stripes3.jpg', None, STWall, None, None, 180),
    1500: ('phase_5.5/maps/leaves1.jpg', None, STWall, None, None, 180),
    1510: ('phase_5.5/maps/leaves2.jpg', None, STWall, None, None, 180),
    1520: ('phase_5.5/maps/leaves3.jpg', None, STWall, None, None, 180),
    1600: ('phase_5.5/maps/diamonds2_cherries.jpg', None, STWall, None, None, 180),
    1610: ('phase_5.5/maps/diamonds3_cherries.jpg', None, STWall, None, None, 180),
    1620: ('phase_5.5/maps/diamonds3_cherries.jpg', None, STWall, None, None, 180),
    1630: ('phase_5.5/maps/diamonds4_cherries.jpg', None, STWall, None, None, 180),
    1640: ('phase_5.5/maps/diamonds4_cherry.jpg', None, STWall, None, None, 180),
    1650: ('phase_5.5/maps/diamonds5_cherries.jpg', None, STWall, None, None, 180),
    1660: ('phase_5.5/maps/diamonds6_cherry.jpg', None, STWall, None, None, 180),
    1700: ('phase_5.5/maps/moon1.jpg', None, STWall, None, None, 180),
    1710: ('phase_5.5/maps/moon2.jpg', None, STWall, None, None, 180),
    1720: ('phase_5.5/maps/moon3.jpg', None, STWall, None, None, 180),
    1730: ('phase_5.5/maps/moon4.jpg', None, STWall, None, None, 180),
    1740: ('phase_5.5/maps/moon5.jpg', None, STWall, None, None, 180),
    1750: ('phase_5.5/maps/moon6.jpg', None, STWall, None, None, 180),
    1760: ('phase_5.5/maps/moon7.jpg', None, STWall, None, None, 180),
    1800: ('phase_5.5/maps/stars1.jpg', None, STWall, ((1, 1, 1),), None, 180),
    1810: ('phase_5.5/maps/stars2.jpg', None, STWall, ((0.59999999999999998, 0.59999999999999998, 1), (1, 0.59999999999999998, 1), (1, 0.5, 0.5)), None, 180),
    1820: ('phase_5.5/maps/stars3.jpg', None, STWall, ((0.59999999999999998, 0.59999999999999998, 1), (1, 0.59999999999999998, 1), (1, 0.5, 0.5), (1, 1, 1)), None, 180),
    1830: ('phase_5.5/maps/stars4.jpg', None, STWall, None, None, 180),
    1840: ('phase_5.5/maps/stars5.jpg', None, STWall, None, None, 180),
    1850: ('phase_5.5/maps/stars6.jpg', None, STWall, None, None, 180),
    1860: ('phase_5.5/maps/stars7.jpg', None, STWall, ((1, 1, 0.59999999999999998), (1, 1, 1)), None, 180),
    1900: ('phase_5.5/maps/wall_paper_flower1.jpg', None, STWall, None, None, 180),
    1910: ('phase_5.5/maps/wall_paper_flower2.jpg', None, STWall, None, None, 180),
    1920: ('phase_5.5/maps/wall_paper_flower3.jpg', None, STWall, None, None, 180),
    1930: ('phase_5.5/maps/wall_paper_flower4.jpg', None, STWall, None, None, 180),
    1940: ('phase_5.5/maps/wall_paper_flower5.jpg', None, STWall, None, None, 180),
    1950: ('phase_5.5/maps/wall_paper_flower6.jpg', None, STWall, None, None, 180),
    2000: ('phase_5.5/maps/flat_wallpaper1.jpg', 'phase_5.5/maps/flower_border2.jpg', STWall, ((1, 0.80000000000000004, 0.59999999999999998), (1, 1, 0.59999999999999998), (1, 0.5, 0.5)), CTFlatWhite, 180),
    2010: ('phase_5.5/maps/flat_wallpaper1.jpg', 'phase_5.5/maps/flower_border5.jpg', STWall, ((0.59999999999999998, 0.59999999999999998, 1), (1, 0.59999999999999998, 1)), CTFlatWhite, 180),
    2020: ('phase_5.5/maps/flat_wallpaper1.jpg', 'phase_5.5/maps/flower_border6.jpg', STWall, ((1, 0.80000000000000004, 0.59999999999999998), (0.59999999999999998, 0.59999999999999998, 1), (1, 0.59999999999999998, 1), (1, 1, 0.59999999999999998), (1, 0.5, 0.5)), CTFlatWhite, 180),
    2100: ('phase_5.5/maps/big_stripes1.jpg', 'phase_5.5/maps/flower_border2.jpg', STWall, None, None, 180),
    2110: ('phase_5.5/maps/big_stripes2.jpg', 'phase_5.5/maps/flower_border2.jpg', STWall, None, None, 180),
    2120: ('phase_5.5/maps/big_stripes3.jpg', 'phase_5.5/maps/flower_border5.jpg', STWall, None, None, 180),
    2130: ('phase_5.5/maps/big_stripes3.jpg', 'phase_5.5/maps/flower_border6.jpg', STWall, None, None, 180),
    2140: ('phase_5.5/maps/big_stripes6.jpg', 'phase_5.5/maps/flower_border6.jpg', STWall, None, None, 180) }

class CatalogWallpaperItem(CatalogAtticItem.CatalogAtticItem):
    
    def makeNewItem(self, wallpaperType, colorIndex):
        self.wallpaperType = wallpaperType
        self.colorIndex = colorIndex
        CatalogAtticItem.CatalogAtticItem.makeNewItem(self)

    
    def saveHistory(self):
        return 1

    
    def getTypeName(self):
        surface = WallpaperTypes[self.wallpaperType][WTSurface]
        return Localizer.WallpaperSurfaceNames[surface]

    
    def getName(self):
        name = Localizer.WallpaperNames.get(self.wallpaperType)
        if name == None:
            century = self.wallpaperType - self.wallpaperType % 100
            name = Localizer.WallpaperNames.get(century)
        
        if name:
            return name
        
        return self.getTypeName()

    
    def getSurfaceType(self):
        return WallpaperTypes[self.wallpaperType][WTSurface]

    
    def recordPurchase(self, avatar, optional):
        (house, retcode) = self.getHouseInfo(avatar)
        if retcode >= 0:
            house.addWallpaper(self)
        
        return retcode

    
    def getDeliveryTime(self):
        return 60

    
    def getPicture(self, avatar):
        frame = self.makeFrame()
        sample = loader.loadModelCopy('phase_5.5/models/estate/wallpaper_sample')
        a = sample.find('**/a')
        b = sample.find('**/b')
        c = sample.find('**/c')
        surface = WallpaperTypes[self.wallpaperType][WTSurface]
        if surface == STWall:
            a.setTexture(self.loadTexture(), 1)
            a.setColorScale(*self.getColor())
            b.setTexture(self.loadTexture(), 1)
            b.setColorScale(*self.getColor())
            c.setTexture(self.loadTexture2(), 1)
            c.setColorScale(*self.getColor2())
        elif surface == STMoulding:
            a.setTexture(self.loadTexture(), 1)
            a.setColorScale(*self.getColor())
            b.hide()
            c.hide()
        elif surface == STWainscoting:
            a.hide()
            b.hide()
            c.setTexture(self.loadTexture(), 1)
            c.setColorScale(*self.getColor())
        else:
            a.setTexture(self.loadTexture(), 1)
            a.setColorScale(*self.getColor())
            b.setTexture(self.loadTexture(), 1)
            b.setColorScale(*self.getColor())
            c.setTexture(self.loadTexture(), 1)
            c.setColorScale(*self.getColor())
        sample.reparentTo(frame)
        return (frame, None)

    
    def output(self, store = -1):
        return 'CatalogWallpaperItem(%s, %s%s)' % (self.wallpaperType, self.colorIndex, self.formatOptionalData(store))

    
    def compareTo(self, other):
        if self.wallpaperType != other.wallpaperType:
            return self.wallpaperType - other.wallpaperType
        
        return self.colorIndex - other.colorIndex

    
    def getBasePrice(self):
        return WallpaperTypes[self.wallpaperType][WTBasePrice]

    
    def loadTexture(self):
        Texture = Texture
        import PandaModules
        filename = WallpaperTypes[self.wallpaperType][WTTextureName]
        texture = loader.loadTexture(filename)
        texture.setMinfilter(Texture.FTLinearMipmapLinear)
        texture.setMagfilter(Texture.FTLinear)
        return texture

    
    def loadTexture2(self):
        Texture = Texture
        import PandaModules
        filename = WallpaperTypes[self.wallpaperType][WTTexture2Name]
        if filename == None:
            return self.loadTexture()
        
        texture = loader.loadTexture(filename)
        texture.setMinfilter(Texture.FTLinearMipmapLinear)
        texture.setMagfilter(Texture.FTLinear)
        return texture

    
    def getColor(self):
        colors = WallpaperTypes[self.wallpaperType][WTColor]
        if colors:
            if self.colorIndex < len(colors):
                return colors[self.colorIndex] + (1,)
            else:
                print 'Warning: colorIndex not in colors. Returning white.'
                return (1, 1, 1, 1)
        else:
            return (1, 1, 1, 1)

    
    def getColor2(self):
        colors = WallpaperTypes[self.wallpaperType][WTColor2]
        if colors:
            return colors[self.colorIndex] + (1,)
        else:
            return self.getColor()

    
    def decodeDatagram(self, di, versionNumber, store):
        CatalogAtticItem.CatalogAtticItem.decodeDatagram(self, di, versionNumber, store)
        if versionNumber < 3:
            self.wallpaperType = di.getUint8()
        else:
            self.wallpaperType = di.getUint16()
        self.colorIndex = di.getUint8()

    
    def encodeDatagram(self, dg, store):
        CatalogAtticItem.CatalogAtticItem.encodeDatagram(self, dg, store)
        dg.addUint16(self.wallpaperType)
        dg.addUint8(self.colorIndex)



def getAllWallpapers(*wallpaperTypes):
    list = []
    for wallpaperType in wallpaperTypes:
        colors = WallpaperTypes[wallpaperType][WTColor]
        if colors:
            for n in range(len(colors)):
                list.append(CatalogWallpaperItem(wallpaperType, n))
            
        else:
            list.append(CatalogWallpaperItem(wallpaperType, 0))
    
    return list


def getWallpaperRange(fromIndex, toIndex, *otherRanges):
    list = []
    froms = [
        fromIndex]
    tos = [
        toIndex]
    i = 0
    while i < len(otherRanges):
        froms.append(otherRanges[i])
        tos.append(otherRanges[i + 1])
        i += 2
    for wallpaperType in WallpaperTypes.keys():
        for (fromIndex, toIndex) in zip(froms, tos):
            if wallpaperType >= fromIndex and wallpaperType <= toIndex:
                colors = WallpaperTypes[wallpaperType][WTColor]
                if colors:
                    for n in range(len(colors)):
                        list.append(CatalogWallpaperItem(wallpaperType, n))
                    
                else:
                    list.append(CatalogWallpaperItem(wallpaperType, 0))
            
        
    
    return list

WD_TEXTURE_NAME = 0
WD_SURFACE = 1
WD_BASE_PRICE = 2
SurfaceColorDict = {
    1000: (1.0, 1.0, 1.0, 1.0),
    1010: (1.0, 0.5, 0.5, 1.0),
    1020: (0.64100000000000001, 0.35499999999999998, 0.27000000000000002, 1.0),
    1030: (0.83899999999999997, 0.65100000000000002, 0.54900000000000004, 1.0),
    1040: (0.996, 0.69499999999999995, 0.51200000000000001, 1.0),
    1050: (0.99199999999999999, 0.47999999999999998, 0.16800000000000001, 1.0),
    1060: (0.83199999999999996, 0.5, 0.29699999999999999, 1.0),
    1070: (1.0, 0.81999999999999995, 0.69999999999999996, 1.0),
    1080: (1.0, 0.80000000000000004, 0.59999999999999998, 1.0),
    1090: (0.80800000000000005, 0.67800000000000005, 0.51000000000000001, 1.0),
    1100: (0.56999999999999995, 0.44900000000000001, 0.16400000000000001, 1.0),
    1110: (0.996, 0.89800000000000002, 0.32000000000000001, 1.0),
    1120: (0.996, 0.95699999999999996, 0.59799999999999998, 1.0),
    1130: (1.0, 1.0, 0.59999999999999998, 1.0),
    1140: (1.0, 1.0, 0.69999999999999996, 1.0),
    1150: (0.85499999999999998, 0.93400000000000005, 0.49199999999999999, 1.0),
    1160: (0.5, 0.58599999999999997, 0.40000000000000002, 1.0),
    1170: (0.55100000000000005, 0.82399999999999995, 0.32400000000000001, 1.0),
    1180: (0.78900000000000003, 1.0, 0.69999999999999996, 1.0),
    1190: (0.30499999999999999, 0.96899999999999997, 0.40200000000000002, 1.0),
    1200: (0.59999999999999998, 1.0, 0.80000000000000004, 1.0),
    1210: (0.24199999999999999, 0.74199999999999999, 0.51600000000000001, 1.0),
    1220: (0.434, 0.90600000000000003, 0.83599999999999997, 1.0),
    1230: (0.34799999999999998, 0.81999999999999995, 0.95299999999999996, 1.0),
    1240: (0.191, 0.56299999999999994, 0.77300000000000002, 1.0),
    1250: (0.875, 0.93700000000000006, 1.0, 1.0),
    1260: (0.55900000000000005, 0.58999999999999997, 0.875, 1.0),
    1270: (0.28499999999999998, 0.32800000000000001, 0.72699999999999998, 1.0),
    1280: (0.69999999999999996, 0.69999999999999996, 0.80000000000000004, 1.0),
    1290: (0.59999999999999998, 0.59999999999999998, 1.0, 1.0),
    1300: (0.46100000000000002, 0.379, 0.82399999999999995, 1.0),
    1310: (0.54700000000000004, 0.28100000000000003, 0.75, 1.0),
    1320: (0.72699999999999998, 0.47299999999999998, 0.85899999999999999, 1.0),
    1330: (0.89800000000000002, 0.61699999999999999, 0.90600000000000003, 1.0),
    1340: (1.0, 0.59999999999999998, 1.0, 1.0),
    1350: (0.71099999999999997, 0.23400000000000001, 0.438, 1.0),
    1360: (0.96899999999999997, 0.69099999999999995, 0.69899999999999995, 1.0),
    1370: (0.86299999999999999, 0.40600000000000003, 0.41799999999999998, 1.0),
    1380: (0.93400000000000005, 0.26600000000000001, 0.28100000000000003, 1.0) }
SurfaceColorKeys = SurfaceColorDict.keys()
SurfaceColorKeys.sort()
WallpaperDict = {
    1: ('phase_3.5/maps/stripeB5.jpg', STWall, 180),
    2: ('phase_5.5/maps/squiggle1.jpg', STWall, 180),
    3: ('phase_5.5/maps/diamonds2_cherries.jpg', STWall, 180),
    4: ('phase_5.5/maps/big_stripes4.jpg', STWall, 180),
    5: ('phase_5.5/maps/flat_wallpaper1.jpg', STWall, 180),
    101: ('phase_5.5/maps/floor_wood_neutral.jpg', STFloor, 150),
    102: ('phase_5.5/maps/flooring_carpetA_neutral.jpg', STFloor, 150),
    103: ('phase_5.5/maps/flooring_tile_neutral.jpg', STFloor, 150),
    104: ('phase_5.5/maps/flooring_tileB2.jpg', STFloor, 150),
    105: ('phase_4/maps/grass.jpg', STFloor, 150),
    106: ('phase_4/maps/floor_tile_brick_diagonal2.jpg', STFloor, 150),
    107: ('phase_4/maps/floor_tile_brick_diagonal.jpg', STFloor, 150),
    108: ('phase_4/maps/plazz_tile.jpg', STFloor, 150),
    109: ('phase_4/maps/sidewalk.jpg', STFloor, 150),
    110: ('phase_3.5/maps/boardwalk_floor.jpg', STFloor, 150),
    111: ('phase_3.5/maps/dustroad.jpg', STFloor, 150),
    151: ('phase_3.5/maps/molding_wood1.jpg', STMoulding, 150),
    152: ('phase_3.5/maps/molding_wood2.jpg', STMoulding, 150),
    153: ('phase_5.5/maps/bd_grey_border1.jpg', STMoulding, 150),
    201: ('phase_3.5/maps/wall_paper_b3.jpg', STWainscoting, 200),
    202: ('phase_3.5/maps/wall_paper_b4.jpg', STWainscoting, 200),
    250: ('phase_5.5/maps/bd_grey_border1.jpg', STBorder, 100),
    251: ('phase_5.5/maps/diamonds_border2.jpg', STBorder, 100),
    252: ('phase_5.5/maps/diamonds_border2ch.jpg', STBorder, 100),
    253: ('phase_5.5/maps/diamonds_border3ch.jpg', STBorder, 100),
    254: ('phase_5.5/maps/diamonds_border4ch.jpg', STBorder, 100),
    255: ('phase_5.5/maps/flower_border2.jpg', STBorder, 100),
    256: ('phase_5.5/maps/flower_border5.jpg', STBorder, 100),
    257: ('phase_5.5/maps/flower_border6.jpg', STBorder, 100),
    258: ('phase_5.5/maps/flower_border7.jpg', STBorder, 100),
    259: ('phase_5.5/maps/flower_border8.jpg', STBorder, 100),
    1000: ('phase_5.5/maps/flat_wallpaper1.jpg', STWall, 180),
    1100: ('phase_5.5/maps/big_stripes1.jpg', STWall, 180),
    1110: ('phase_5.5/maps/big_stripes2.jpg', STWall, 180),
    1120: ('phase_5.5/maps/big_stripes3.jpg', STWall, 180),
    1130: ('phase_5.5/maps/big_stripes4.jpg', STWall, 180),
    1140: ('phase_5.5/maps/big_stripes5.jpg', STWall, 180),
    1150: ('phase_5.5/maps/big_stripes6.jpg', STWall, 180),
    1200: ('phase_5.5/maps/stripeB1.jpg', STWall, 180),
    1210: ('phase_5.5/maps/stripeB2.jpg', STWall, 180),
    1220: ('phase_5.5/maps/stripeB3.jpg', STWall, 180),
    1230: ('phase_5.5/maps/stripeB4.jpg', STWall, 180),
    1240: ('phase_3.5/maps/stripeB5.jpg', STWall, 180),
    1250: ('phase_5.5/maps/stripeB6.jpg', STWall, 180),
    1260: ('phase_5.5/maps/stripeB7.jpg', STWall, 180),
    1300: ('phase_5.5/maps/squiggle1.jpg', STWall, 180),
    1310: ('phase_5.5/maps/squiggle2.jpg', STWall, 180),
    1320: ('phase_5.5/maps/squiggle3.jpg', STWall, 180),
    1330: ('phase_5.5/maps/squiggle4.jpg', STWall, 180),
    1340: ('phase_5.5/maps/squiggle5.jpg', STWall, 180),
    1350: ('phase_5.5/maps/squiggle6.jpg', STWall, 180),
    1400: ('phase_5.5/maps/stripes_cyan.jpg', STWall, 180),
    1410: ('phase_5.5/maps/stripes_green.jpg', STWall, 180),
    1420: ('phase_5.5/maps/stripes_magenta.jpg', STWall, 180),
    1430: ('phase_5.5/maps/two_stripes1.jpg', STWall, 180),
    1440: ('phase_5.5/maps/two_stripes2.jpg', STWall, 180),
    1450: ('phase_5.5/maps/two_stripes3.jpg', STWall, 180),
    1500: ('phase_5.5/maps/leaves1.jpg', STWall, 180),
    1510: ('phase_5.5/maps/leaves2.jpg', STWall, 180),
    1520: ('phase_5.5/maps/leaves3.jpg', STWall, 180),
    1600: ('phase_5.5/maps/diamonds2_cherries.jpg', STWall, 180),
    1610: ('phase_5.5/maps/diamonds3_cherries.jpg', STWall, 180),
    1630: ('phase_5.5/maps/diamonds4_cherries.jpg', STWall, 180),
    1640: ('phase_5.5/maps/diamonds4_cherry.jpg', STWall, 180),
    1650: ('phase_5.5/maps/diamonds5_cherries.jpg', STWall, 180),
    1660: ('phase_5.5/maps/diamonds6_cherry.jpg', STWall, 180),
    1700: ('phase_5.5/maps/moon1.jpg', STWall, 180),
    1710: ('phase_5.5/maps/moon2.jpg', STWall, 180),
    1720: ('phase_5.5/maps/moon3.jpg', STWall, 180),
    1730: ('phase_5.5/maps/moon4.jpg', STWall, 180),
    1740: ('phase_5.5/maps/moon5.jpg', STWall, 180),
    1750: ('phase_5.5/maps/moon6.jpg', STWall, 180),
    1760: ('phase_5.5/maps/moon7.jpg', STWall, 180),
    1800: ('phase_5.5/maps/stars1.jpg', STWall, 180),
    1810: ('phase_5.5/maps/stars2.jpg', STWall, 180),
    1820: ('phase_5.5/maps/stars3.jpg', STWall, 180),
    1830: ('phase_5.5/maps/stars4.jpg', STWall, 180),
    1840: ('phase_5.5/maps/stars5.jpg', STWall, 180),
    1850: ('phase_5.5/maps/stars6.jpg', STWall, 180),
    1860: ('phase_5.5/maps/stars7.jpg', STWall, 180),
    1900: ('phase_5.5/maps/wall_paper_flower1.jpg', STWall, 180),
    1910: ('phase_5.5/maps/wall_paper_flower2.jpg', STWall, 180),
    1920: ('phase_5.5/maps/wall_paper_flower3.jpg', STWall, 180),
    1930: ('phase_5.5/maps/wall_paper_flower4.jpg', STWall, 180),
    1940: ('phase_5.5/maps/wall_paper_flower5.jpg', STWall, 180),
    1950: ('phase_5.5/maps/wall_paper_flower6.jpg', STWall, 180),
    2000: ('phase_5.5/maps/flat_wallpaper1.jpg', STWall, 180),
    2100: ('phase_5.5/maps/big_stripes1.jpg', STWall, 180),
    2110: ('phase_5.5/maps/big_stripes2.jpg', STWall, 180),
    2120: ('phase_5.5/maps/big_stripes3.jpg', STWall, 180),
    2130: ('phase_5.5/maps/big_stripes3.jpg', STWall, 180),
    2140: ('phase_5.5/maps/big_stripes6.jpg', STWall, 180) }
WallpaperKeys = []
MouldingKeys = []
FlooringKeys = []
WainscotingKeys = []
BorderKeys = []
keys = WallpaperDict.keys()
keys.sort()
for key in keys:
    surface = WallpaperDict[key][WD_SURFACE]
    if surface == STWall:
        WallpaperKeys.append(key)
    elif surface == STMoulding:
        MouldingKeys.append(key)
    elif surface == STFloor:
        FlooringKeys.append(key)
    elif surface == STWainscoting:
        WainscotingKeys.append(key)
    elif surface == STBorder:
        BorderKeys.append(key)
    


class CatalogWallpaperItemNew(CatalogAtticItem.CatalogAtticItem):
    
    def makeNewItem(self, wallpaperType, colorIndex):
        self.wallpaperType = wallpaperType
        self.colorIndex = colorIndex
        CatalogAtticItem.CatalogAtticItem.makeNewItem(self)

    
    def saveHistory(self):
        return 1

    
    def getTypeName(self):
        surface = WallpaperDict[self.wallpaperType][WD_SURFACE]
        return Localizer.WallpaperSurfaceNames[surface]

    
    def getName(self):
        name = Localizer.WallpaperNames.get(self.wallpaperType)
        if name == None:
            century = self.wallpaperType - self.wallpaperType % 100
            name = Localizer.WallpaperNames.get(century)
        
        if name:
            return name
        
        return self.getTypeName()

    
    def getSurfaceType(self):
        return WallpaperDict[self.wallpaperType][WD_SURFACE]

    
    def recordPurchase(self, avatar, optional):
        (house, retcode) = self.getHouseInfo(avatar)
        if retcode >= 0:
            house.addWallpaper(self)
        
        return retcode

    
    def getDeliveryTime(self):
        return 60

    
    def getPicture(self, avatar):
        frame = self.makeFrame()
        sample = loader.loadModelCopy('phase_5.5/models/estate/wallpaper_sample')
        a = sample.find('**/a')
        b = sample.find('**/b')
        c = sample.find('**/c')
        surface = WallpaperDict[self.wallpaperType][WD_SURFACE]
        if surface == STWall:
            texture = self.loadTexture()
            color = self.getColor()
            a.setTexture(texture, 1)
            a.setColorScale(*color)
            b.setTexture(texture, 1)
            b.setColorScale(*color)
            c.setTexture(texture, 1)
            c.setColorScale(*color)
        elif surface == STMoulding:
            a.setTexture(self.loadTexture(), 1)
            a.setColorScale(*self.getColor())
            b.hide()
            c.hide()
        elif surface == STWainscoting or surface == STBorder:
            a.hide()
            b.hide()
            c.setTexture(self.loadTexture(), 1)
            c.setColorScale(*self.getColor())
        else:
            a.setTexture(self.loadTexture(), 1)
            a.setColorScale(*self.getColor())
            b.setTexture(self.loadTexture(), 1)
            b.setColorScale(*self.getColor())
            c.setTexture(self.loadTexture(), 1)
            c.setColorScale(*self.getColor())
        sample.reparentTo(frame)
        return (frame, None)

    
    def output(self, store = -1):
        return 'CatalogWallpaperItem(%s, %s%s)' % (self.wallpaperType, self.colorIndex, self.formatOptionalData(store))

    
    def compareTo(self, other):
        if self.wallpaperType != other.wallpaperType:
            return self.wallpaperType - other.wallpaperType
        
        return self.colorIndex - other.colorIndex

    
    def getBasePrice(self):
        return WallpaperDict[self.wallpaperType][WD_BASE_PRICE]

    
    def loadTexture(self):
        Texture = Texture
        import PandaModules
        filename = WallpaperDict[self.wallpaperType][WD_TEXTURE_NAME]
        texture = loader.loadTexture(filename)
        texture.setMinfilter(Texture.FTLinearMipmapLinear)
        texture.setMagfilter(Texture.FTLinear)
        return texture

    
    def getColor(self):
        colors = SurfaceColorDict.get(self.colorIndex)
        if colors:
            return colors
        else:
            return (1, 1, 1, 1)

    
    def decodeDatagram(self, di, versionNumber, store):
        CatalogAtticItem.CatalogAtticItem.decodeDatagram(self, di, versionNumber, store)
        if versionNumber < 3:
            self.wallpaperType = di.getUint8()
        else:
            self.wallpaperType = di.getUint16()
        self.colorIndex = di.getUint8()

    
    def encodeDatagram(self, dg, store):
        CatalogAtticItem.CatalogAtticItem.encodeDatagram(self, dg, store)
        dg.addUint16(self.wallpaperType)
        dg.addUint8(self.colorIndex)


