import pyautogui
import re
import pyperclip
import time

with open('Texto.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

frases = conteudo.split('- ')[1:]

pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')

def remover_espacos_extras(texto):
    return re.sub(r'\s+', ' ', texto)

for i in range(0, len(frases), 2):
    frase_ingles = frases[i].strip().replace("\n", "")
    frase_ingles = remover_espacos_extras(frase_ingles)
    frase_portugues = frases[i+1].strip().replace("\n", "")
    frase_portugues = remover_espacos_extras(frase_portugues)
    
    # print(frase_ingles)
    # print(frase_portugues)
    time.sleep(1)
    pyperclip.copy(frase_ingles)
    pyautogui.click(590, 226)
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')

    pyautogui.press("enter")
    time.sleep(1)

    pyautogui.click(623, 77)
    time.sleep(1)

    pyautogui.click(976, 614)
    time.sleep(2)

    pyperclip.copy(frase_portugues)
    pyautogui.click(623, 155)
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')

    time.sleep(1)

    pyautogui.click( 1101, 834)