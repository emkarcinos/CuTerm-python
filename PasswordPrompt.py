from InnerWindow import InnerWindow
import os

class PasswordPrompt(InnerWindow):
    def __init__(self, frameChar = ' ', winTitle = ""):
        super().__init__()
        self.setDimmensions(51, 6)
        self.initMatrix()
        self.setFrame(frameChar)
        self.setTitle(winTitle)
        self.addPassText()
        self.drawPromptBox()

    def addPassText(self):
        text = "Enter Password:"
        startPos = self.sizeX//2 - len(text)//2
        for pos in range(0, len(text)):
            self.drawingMatrix[1][startPos + pos]=text[pos]

    def moveCursor(self):
        destinationX=self.posX+3
        destinationY=self.posY + self.sizeY - 3
        for row in range(0, destinationY):
            print(u"\033[1B", end="")
        for col in range(0, destinationX):
            print(u"\033[1C", end="")

    def drawPromptBox(self):
        startX=3
        startY=self.sizeY-4
        for row in range(0,3):
            for col in range(0, self.sizeX-5):
                if row!=1:
                    self.drawingMatrix[row+startY][col+startX]=self.frame
        
    def addTextObject(self, textObj):
        pass
    
    def removeTextObject(self, textObj):
        pass

    def prompt(self):
        self.moveCursor()
        print("> ", end="")
        os.system("setterm -cursor on")
        output = str(input())
        os.system("setterm -cursor off")
        return output

    def clear(self):
        pass