import pyautogui
import pyperclip


pyautogui.click(153,332); 
#pyautogui.typewrite('Hello World', 0.25)
# pyautogui.typewrite(['a', 'b', 'left', 'left','X', 'Y'] , 0.25)

testString = ('1234.ü.ö.ß.Ä.Ö.Ü.912345.789')
testString2 = ('123456789012345678901234567890')
pyperclip.copy(str(testString) [0:25])
pyautogui.hotkey('ctrl', 'v')
pyautogui.typewrite(testString)