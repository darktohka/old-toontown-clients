# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\parties\PartyReplyInfo.py


class SingleReply:
    __module__ = __name__

    def __init__(self, inviteeId, status):
        self.inviteeId = inviteeId
        self.status = status


class PartyReplyInfoBase:
    __module__ = __name__

    def __init__(self, partyId, partyReplies):
        self.partyId = partyId
        self.replies = []
        for oneReply in partyReplies:
            self.replies.append(SingleReply(*oneReply))

    def __str__(self):
        string = 'partyId=%d ' % self.partyId
        for reply in self.replies:
            string += '(%d:%d) ' % (reply.inviteeId, reply.status)

        return string