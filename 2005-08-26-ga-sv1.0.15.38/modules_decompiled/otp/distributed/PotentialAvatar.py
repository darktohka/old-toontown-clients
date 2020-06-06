# File: P (Python 2.2)


class PotentialAvatar:
    
    def __init__(self, id, names, dna, position, allowedName):
        self.id = id
        self.name = names[0]
        self.dna = dna
        self.avatarType = None
        self.position = position
        self.wantName = names[1]
        self.approvedName = names[2]
        self.rejectedName = names[3]
        self.allowedName = allowedName


