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

win1.__del__()

userInput=""
win2=PromptWindow(textObj, '*', " User input ")
terminal.append(win2)
userInput=win2.prompt()

print(userInput)
win2.__del__()

textObj2 = TextObject(userInput, 41, 3)
textObj2.format("center")
win3 = TextWindow(textObj2, '*', " You ")
terminal.append(win3)

input()

win3.__del__()

winPassword = PasswordPrompt('*')
terminal.append(winPassword)
password = winPassword.prompt()

winPassword.__del__()

terminal.__del__()
    