from Window import Window
import os

class TerminalWindow(Window):
    def __init__(self, frameChar=' ', winTitle = ""):
        super().__init__()
        self.rows=0
        self.cols=0
        os.system('setterm -cursor off')
        self.updateTerminalSize()
        self.initMatrix()
        self.setFrame(frameChar)
        if(winTitle!=None):
            self.setTitle(winTitle)

    def draw(self):
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                print(*self.drawingMatrix[row][col], end="")
            if row != self.rows-1:
                print()
        print("\033[H", end="")

    def append(self, win):
        if win.sizeX > self.cols or win.sizeY > self.rows:
            return
        win.parent=self
        startX=self.cols//2 - win.sizeX//2
        startY=self.rows//2 - win.sizeY//2
        win.setPos(startX, startY)
        for row in range(0,win.sizeY):
            for col in range(0, win.sizeX):
                self.drawingMatrix[row+startY][col+startX]=win.drawingMatrix[row][col]
        self.draw()

    def clear(self):
        print("\033[2J\033[1;1H", end="")

    def removeWindow(self, win):
        startY=win.posY
        startX=win.posX
        for row in range(0, win.sizeY):
            for col in range(0, win.sizeX):
                self.drawingMatrix[row+startY][col+startX]=' '
        win.parent=None
        self.draw()

    def updateTerminalSize(self):
        self.cols, self.rows = os.get_terminal_size(0)
        
    def initMatrix(self):
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                self.drawingMatrix[row][col]=' '
    
    def setFrame(self, frameChar):
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                if row==0 or row==self.rows-1 or col==0 or col==self.cols-1:
                    self.drawingMatrix[row][col]=frameChar

    def setTitle(self, winTitle):
        titleLength=len(winTitle)
        writePos=self.cols//2 - titleLength//2
        for i in range(0, titleLength):
            self.drawingMatrix[0][writePos+i]=winTitle[i]
    
    def __del__(self):
        self.clear()
        os.system('setterm -cursor off')