#! python3
# mouseNow.py  -  display the current position of the mouse pointer

import pyautogui
print('Press Ctrl-C to quit.')

try:
    while True:
        # TODO:Retieve coordinates of the mouse point and output
        x, y = pyautogui.position()   # Position Mauszeiger abrufen
        positionStr = 'X:  ' + str(x).rjust(4) +  '   Y: ' + str(y).rjust(4)
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        positionStr += ' RGB: ('    + str(pixelColor[0]).rjust(3)
        positionStr += ', '         + str(pixelColor[1]).rjust(3)
        positionStr += ', '         + str(pixelColor[2]).rjust(3) +')'
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.') 

