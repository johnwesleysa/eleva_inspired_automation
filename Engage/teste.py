import pyautogui
from datetime import datetime

# Define o nome do arquivo com a data e hora atuais
filename = datetime.now().strftime("screenshot_%Y-%m-%d_%H-%M-%S.png")

# Captura a tela e salva como imagem
screenshot = pyautogui.screenshot()
screenshot.save(filename)

print(f"Screenshot salva como {filename}")
