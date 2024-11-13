import pyautogui

pyautogui.sleep(5)
currentMouseX, currentMouseY = pyautogui.position()
print(f"Coordenadas (x, y): {currentMouseX}, {currentMouseY}")
