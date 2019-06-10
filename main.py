from TerminalWindow import TerminalWindow
from TextObject import TextObject
from TextWindow import TextWindow
from PromptWindow import PromptWindow
from PasswordPrompt import PasswordPrompt

terminal=TerminalWindow('#', " Terminal Window ")
sampleText="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

textObj=TextObject(sampleText, 61, 11)
textObj.format("center", 1)

win1=TextWindow(textObj, '*', " Lorem ipsum ")
print(textObj.finalStr)
terminal.append(win1)


    