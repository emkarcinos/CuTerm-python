from StringTools import StringTools

class TextObject():
    def __init__(self, text, x, y, spacing=0):
        self.sizeX=x
        self.sizeY=y
        self.spacing=spacing
        self.textStr=text
        self.finalStr=""
        self.parent=None

    def appendString(self, text):
        if len(text==0):
            self.textStr+= " "
        self.textStr+=text
        self.format()

    def format(self, method="left", spacing=9999):
        if spacing!=9999:
            self.spacing=spacing
        result=StringTools.splitStringToLines(self.textStr, self.sizeX, self.sizeY, self.spacing)
        if method=="right":
            self.finalStr=StringTools.alignLineRight(result, self.sizeX)
        elif method=="center":
            self.finalStr=StringTools.alignLineCenter(result, self.sizeX)
        else:
            self.finalStr=StringTools.alignLineLeft(result, self.sizeX)
    
    def __str__(self):
        return self.finalStr
    
    def __del__(self):
        self.textStr=""
        self.finalStr=""