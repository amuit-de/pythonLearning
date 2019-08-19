import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
print('test')
pyautogui.position()
x, y = pyautogui.position()   # Position Mauszeiger abrufen
positionStr = 'X:  ' + str(x).rjust(4) +  'Y: ' + str(y).rjust(4)
print (positionStr)
print('test')