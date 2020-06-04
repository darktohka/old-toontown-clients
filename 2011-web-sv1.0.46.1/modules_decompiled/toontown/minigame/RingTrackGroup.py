# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\RingTrackGroup.py


class RingTrackGroup:
    __module__ = __name__

    def __init__(self, tracks, period, trackTOffsets=None, reverseFlag=0, tOffset=0.0):
        if trackTOffsets == None:
            trackTOffsets = [
             0] * len(tracks)
        self.tracks = tracks
        self.period = period
        self.trackTOffsets = trackTOffsets
        self.reverseFlag = reverseFlag
        self.tOffset = tOffset
        return