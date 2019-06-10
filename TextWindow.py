from InnerWindow import InnerWindow

class TextWindow(InnerWindow):
    def __init__(self, textObj, frameChar='*', winName=""):
        super().__init__()
        self.setDimmensions(textObj.sizeX+4, textObj.sizeY+4)
        self.initMatrix()
        self.setFrame(frameChar)
        self.setTitle(winName)
        self.addTextObject(textObj)
        
    def clear(self):
        for row in range(0,self.sizeY):
            for col in range(0, self.sizeX):
                self.drawingMatrix[row][col]=' '

    def addTextObject(self, textObj):
        if (textObj.sizeX > self.sizeX-2 and textObj.sizeY > self.sizeY-2):
            return
        textObj.parent=self
        startX = self.sizeX//2 - textObj.sizeX//2
        startY = self.sizeY//2 - textObj.sizeY//2 
        lineCount = 0
        ptr = 0
        for ch in textObj.finalStr:
            if ch=='\n':
                lineCount+=1
                ptr=0
            elif(lineCount < self.sizeY-3):
                self.drawingMatrix[startY+lineCount][startX+ptr]=ch
                ptr+=1
        
    def removeTextObject(self, textObj):
        startX = self.sizeX//2 - textObj.sizeX//2
        startY = self.sizeY//2 - textObj.sizeY//2
        for row in range(0,self.sizeY):
            for col in range(0, self.sizeX):
                self.drawingMatrix[row+startY][col+startX]=' '
        textObj.parent=None

    def __del__(self):
        super(TextWindow, self).__del__()
    