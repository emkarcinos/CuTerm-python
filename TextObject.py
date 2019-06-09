from StringTools import *

class TextObject():
    def __init__(self, text, x, y, spacing=0):
        self.sizeX=x
        self.sizeY=y
        self.spacing=spacing
        self.textStr=text
        self.finalStr=""
        self.parent=None

    def appendString(self, text):
        pass

    def format(self, method, spacing=9999):
        if spacing!=9999):
            self.spacing=spacing
        if method=="right":
            finalStr
    
    def __str__(self):
        return self.finalStr
    
    def __del__(self):
        pass