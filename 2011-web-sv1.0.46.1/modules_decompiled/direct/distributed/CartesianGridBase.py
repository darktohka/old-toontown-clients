# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\distributed\CartesianGridBase.py
from pandac.PandaModules import Vec3

class CartesianGridBase:
    __module__ = __name__

    def isValidZone(self, zoneId):

        def checkBounds(self=self, zoneId=zoneId):
            if zoneId < self.startingZone or zoneId > self.startingZone + self.gridSize * self.gridSize - 1:
                return 0
            return 1

        if self.style == 'Cartesian':
            return checkBounds()
        elif self.style == 'CartesianStated':
            if zoneId >= 0 and zoneId < self.startingZone:
                return 1
            else:
                return checkBounds()
        else:
            return 0

    def getZoneFromXYZ(self, pos, wantRowAndCol=False):
        dx = self.cellWidth * self.gridSize * 0.5
        x = pos[0] + dx
        y = pos[1] + dx
        col = x // self.cellWidth
        row = y // self.cellWidth
        zoneId = int(self.startingZone + (row * self.gridSize + col))
        if wantRowAndCol:
            return (
             zoneId, col, row)
        else:
            return zoneId

    def getGridSizeFromSphereRadius(self, sphereRadius, cellWidth, gridRadius):
        sphereRadius = max(sphereRadius, gridRadius * cellWidth)
        return 2 * (sphereRadius // cellWidth)

    def getGridSizeFromSphere(self, sphereRadius, spherePos, cellWidth, gridRadius):
        xMax = abs(spherePos[0]) + sphereRadius
        yMax = abs(spherePos[1]) + sphereRadius
        sphereRadius = Vec3(xMax, yMax, 0).length()
        return max(2 * (sphereRadius // cellWidth), 1)

    def getZoneCellOrigin(self, zoneId):
        dx = self.cellWidth * self.gridSize * 0.5
        zone = zoneId - self.startingZone
        row = zone // self.gridSize
        col = zone % self.gridSize
        x = col * self.cellWidth - dx
        y = row * self.cellWidth - dx
        return (
         x, y, 0)

    def getZoneCellOriginCenter(self, zoneId):
        dx = self.cellWidth * self.gridSize * 0.5
        center = self.cellWidth * 0.5
        zone = zoneId - self.startingZone
        row = zone // self.gridSize
        col = zone % self.gridSize
        x = col * self.cellWidth - dx + center
        y = row * self.cellWidth - dx + center
        return (
         x, y, 0)

    def getConcentricZones(self, zoneId, radius):
        zones = []
        zone = zoneId - self.startingZone
        row = zone // self.gridSize
        col = zone % self.gridSize
        leftOffset = min(col, radius)
        rightOffset = min(self.gridSize - (col + 1), radius)
        topOffset = min(row, radius)
        bottomOffset = min(self.gridSize - (row + 1), radius)
        ulZone = zoneId - leftOffset - topOffset * self.gridSize
        for currCol in range(int(rightOffset + leftOffset + 1)):
            if currCol == 0 and leftOffset == radius or currCol == rightOffset + leftOffset and rightOffset == radius:
                possibleRows = range(int(bottomOffset + topOffset + 1))
            else:
                possibleRows = []
                if topOffset == radius:
                    possibleRows.append(0)
                if bottomOffset == radius:
                    possibleRows.append(bottomOffset + topOffset)
            for currRow in possibleRows:
                newZone = ulZone + currRow * self.gridSize + currCol
                zones.append(int(newZone))

        return zones