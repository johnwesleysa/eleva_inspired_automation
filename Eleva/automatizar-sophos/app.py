import pyautogui
import time


#clciar em add
pyautogui.click(4628,313,duration=1)
time.sleep(1)

#clicar em add mail box
pyautogui.click(4544,361,duration=1)
time.sleep(1)
 

#abrir txt
with open ("produtos.txt", 'r') as arquivo:
    for linha in arquivo:
        coluna_um = linha.split(',')[0]
        coluna_dois = linha.split(',')[1]

        #clicar e confirmar o mailbox
        pyautogui.click(3379,289, duration=1)
        time.sleep(0.5)

        #clicar em distribuition list
        pyautogui.click(3379,334, duration=1)
        time.sleep(0.5)
        

        #clicar e digitar nome
        pyautogui.click(3353,365, duration=2)
        pyautogui.hotkey('ctrl','a')
        pyautogui.press('del')
        pyautogui.write(coluna_um)

        #clicar e digitar e-mail
        pyautogui.click(3358,455, duration=2)
        pyautogui.hotkey('ctrl','a')
        pyautogui.press('del')
        pyautogui.write(coluna_dois)