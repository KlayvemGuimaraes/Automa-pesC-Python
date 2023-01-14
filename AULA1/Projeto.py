# biblioteca do python, que acessa e controla o mouse, teclado e a tela do computador -> pyautogui
# vamos usar a biblioteca do pyautogui

# pip install pyautogui

#  pyautogui.click (clicar)
#  pyautogui.write (escrever)
#  pyautogui.press (pressionar)
#  pyautogui.hotkey (atalho)
#  button="right" = Clica com o botão direito 
#  pyautogui.sleep = Dá um tempo/pausa 
#  r = raw/cru = sem caracteres especiais, considere como caminho. 


# Vamos para o código !

# passo 1 : entrar no sistema

import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)


# passo 2 : navegar até o local do relatório (exportar)

# passo 3 : exportar o relatório(download)

# passo 4 : calcular os indicadores

# passo 5 : enviar o email para a diretoria

# PASSO A PASSO PRIMEIRO EM PORTUGUES = PSEUDOCODIGO 