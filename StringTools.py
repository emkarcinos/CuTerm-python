DELIM = " \t,.-\0"

class StringTools(object):
    @staticmethod
    def isDelimeter(ch):
        for delimeter in DELIM:
            if ch==delimeter:
                return True
        return False

    @staticmethod
    def splitStringToLines(text, sizeX, sizeY, spacing = 0):
        finalStr=""
        lastEndPos=0
        cursorPos=0
        lastDelimOccurrence=0
        for line in range(0, sizeY):
            cursorPos=lastEndPos
            lastDelimOccurrence=cursorPos
            for cursorPos in range(cursorPos, len(text)):
                if StringTools().isDelimeter(text[cursorPos]):
                    if cursorPos-lastEndPos<sizeX:
                        lastDelimOccurrence=cursorPos
                    else:
                        for i in range(0, lastDelimOccurrence):
                            finalStr+=text[i+lastEndPos]
                        for spac in range(0, spacing):
                            if spac>=1:
                                line+=1
                            if line>=sizeY: 
                                break
                            finalStr+="\n"
                        lastEndPos=lastDelimOccurrence+1
                        break
        if cursorPos==len(text):
            for i in range(lastEndPos, len(text)):
                finalStr+=text[i]
        return finalStr

    @staticmethod
    def alignLineCenter(text, sizeX, sizeY):
        finalString=""
        lines=text.splitlines()
        

    @staticmethod
    def alignLineLeft(text, sizeX, sizeY):
        pass

    @staticmethod
    def alignLineRight(text, sizeX, sizeY):
        pass