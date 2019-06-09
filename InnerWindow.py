from Window import Window

class InnerWindow(Window):
    def __init__(self):
        self.posX=0
        self.posY=0
        self.sizeX=0
        self.sizeY=0
        self.frame=''
        self.parent=None

    def initMatrix(self):
        for row in range(0, self.sizeY):
            for col in range(0, self.sizeX):
                self.drawingMatrix[row][col]=" "

    def setDimmensions(self, _x, _y):
        self.sizeX=_x
        self.sizeY=_y

    def setPos(self, _x, _y):
        self.posX=_x
        self.posY=_y

    def setFrame(self, frameChar):
        self.frame=frameChar
        for row in range(0,self.sizeY):
            for col in range(0, self.sizeX):
                if row==0 or row==self.sizeY-1 or col==0 or col==self.sizeX-1:
                    self.drawingMatrix[row][col]=frameChar

    def setTitle(self, winTitle):
        titleLength=len(winTitle)
        writePos=self.sizeX/2 - titleLength/2
        for i in range(0, titleLength):
            self.drawingMatrix[0][writePos+i]=winTitle[i]

    def addTextObject(self, textObj):
        pass

    def removeTextObject(self, textObj):
        pass

    def clear(self):
        pass

    def __del__(self):
        self.parent.removeWindow(self)

    