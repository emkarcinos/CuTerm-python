from InnerWindow import InnerWindow

class PromptWindow(InnerWindow):
    def __init__(self, textObj, frameChar = ' ', winTitle = ""):
        super().__init__(self)
        self.setDimmensions(textObj.sizeX+4, textObj.sizeY+6)
        self.initMatrix()
        self.setFrame(frameChar)
        self.setTitle(winTitle)
        self.addTextObject(textObj)
        self.drawSeparator()

    def moveCursor(self):
        destinationX=self.posX+2
        destinationY=self.posY + self.sizeY - 2
        for row in range(0, destinationY):
            print(u"\033[1B", end="")
        for col in range(0, destinationX):
            print(u"\033[1C", end="")

    def drawSeparator(self):
        for pos in range(1, self.sizeX):
            self.drawingMatrix[self.sizeY-3][pos]=self.frame

    def addTextObject(self, textObj):
        if textObj.sizeX > self.sizeX-2 and textObj.sizeY > self.sizeY-3:
            return
        textObj.parent=self
        startX = self.sizeX//2 - textObj.sizeX//2
        startY = self.sizeY//2 - textObj.sizeY//2
        lineCount=0
        ptr=0
        for ch in textObj.finalStr:
            if ch=='\n':
                lineCount+=1
                ptr=0
            else:
                self.drawingMatrix[startY+lineCount][startX+ptr]=ch
                ptr+=1

    def removeTextObject(self, textObj):
        startY=self.sizeY//2 - textObj.sizeY//2
        startX=self.sizeX//2 - textObj.sizeX//2 - 1
        for row in range (0, textObj.sizeY):
            for col in range(0, textObj.sizeX):
                self.drawingMatrix[row+startY][col+startX]=' '
        textObj.parent=None

    def prompt(self, input):
        self.moveCursor()
        print("> ", end="")
        input=str(input())
        print(u"\033[2J\033[1;1H", end="")
    
    def clear(self):
        for row in range(0, self.sizeY-2):
            for col in range(0, self.sizeX):
                self.drawingMatrix[row][col]=' '

    def __del__(self):
        pass

    