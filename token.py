class Token:
    def __init__(self, pos=(0, 0), dire=(1, 0)):
        self.position = pos
        self.direction = dire

    def getPos(self):
        return self.position

    def getDir(self):
        return self.direction

    def move(self):
        self.position = (self.position[0] + self.direction[0], self.position[1] + self.direction[1])

    def setDir(self, new):
        self.direction = new
