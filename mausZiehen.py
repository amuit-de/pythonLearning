import pyautogui, time
time.sleep(5)
pyautogui.click() # Klick, um dem Zeichenprogramm den Fokus zu geben
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2) # nach rechts
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2) # nach unten
    pyautogui.dragRel(-distance, 0, duration=0.2) #nach links
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2) # nach oben