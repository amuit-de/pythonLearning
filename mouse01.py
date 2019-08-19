import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
print('test')
pyautogui.position()

for i in range(3):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)    
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
    #Position Mauszeiger abrufen
    #x, y = pyautogui.position()
    #positionStr = 'X:  ' + str(x).rjust(4) +  'Y: ' + str(y).rjust(4)
    #print (positionStr)
    #print('test')
