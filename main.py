from TerminalWindow import TerminalWindow
from TextObject import TextObject
from TextWindow import TextWindow
from PromptWindow import PromptWindow
from PasswordPrompt import PasswordPrompt
from StringTools import StringTools

terminal=TerminalWindow('#', " Terminal Window ")
sampleText="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

textObj=TextObject(sampleText, 61, 5)
textObj.format("center")

win1=TextWindow(textObj, '*', " Lorem Ipsum ")
terminal.append(win1)

input()

del win1

win2=PromptWindow(textObj, '*', " User input ")
terminal.append(win2)
userInput=win2.prompt()

del win2

textObj2 = TextObject(userInput, 61, 1)
win3 = TextWindow(textObj2, '*', " You: ")
terminal.append(win3)
input()

del win3

winPassword = PasswordPrompt('*')
terminal.append(winPassword)
password = winPassword.prompt()
del winPassword

del terminal
    