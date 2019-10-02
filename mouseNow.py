#! python3
# mouseNow.py  -  display the current position of the mouse pointer

import pyautogui
import time

print('Press Ctrl-C to quit.')

try:
    while True:
        # TODO:Retieve coordinates of the mouse point and output
        x, y = pyautogui.position()   # Position Mauszeiger abrufen
        positionStr = 'X:  ' + str(x).rjust(4) +  '   Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        time.sleep(0.50)
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.') 

