import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
import time
from datetime import datetime
import pyautogui
import os

LOGS_DIR = r'C:\Users\john.alencar\Documents\GitHub\programacao\Engage\LOGS\daVinciEmail_log.txt'
NOME_ARQUIVO_LOG = r'daVinciEmail_log.txt'
CAMINHO_ARQUIVO_EMAIL = r"C:\Users\john.alencar\Documents\GitHub\programacao\Engage\Da Vinci\META QUEST - DaVinci  - Email.csv"


def save_screenshot(directory, email):
    # Gera o nome completo do arquivo
    full_path = f"{directory}\\{email}.png"
    # Captura a tela
    screenshot = pyautogui.screenshot()
    time.sleep(0.5)
    # Salva a captura de tela
    screenshot.save(full_path)

# Define o diretório e o nome base da captura de tela
CAMINHO_SCREENSHOT = r'C:\Users\john.alencar\Documents\GitHub\programacao\Engage\Da Vinci'
screenshot_name = datetime.now().strftime("screenshot_daVinci_%Y-%m-%d_%H-%M-%S_")

def save_logs(email):
    # Caminho para o arquivo de log dentro do diretório de logs
    log_file = os.path.join(LOGS_DIR)
    
    # Abre o arquivo de log no modo de adição
    with open(log_file, 'a') as f:
        f.write(f'-----')
        f.write(f'E-mail: {email}: Verificado;')
        f.write(f'-----\n')
    

# Função para abrir o navegador, preencher os campos e fechar
def realizar_cadastro(email, password, cont):
    # Inicializando uma nova instância do Google Chrome para cada cadastro
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=164&ct=1730400405&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26RpsCsrfState%3d8b7f043c-28df-007e-233f-352222f987a9&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c'
    driver.get(url)

    # Define um tempo máximo de espera
    wait = WebDriverWait(driver, 30)
    time.sleep(1)

    try:
        #clicar no campo de e-mail
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="i0116"]'))).send_keys(email)
        time.sleep(1)

        #clicar em avançar
        driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
        time.sleep(1)

        #clicar em password
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="i0118"]'))).send_keys(password)
        time.sleep(1)

        #clicar em avançar
        driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
        time.sleep(1)

        try:
            #aguarda até aparecer o campo de: continuar conectado?
            try:
                element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="lightbox"]/div[3]/div/div[2]/div/div[1]')))
                time.sleep(1)

                #clicar em sim
                driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
                time.sleep(1)
            except TimeoutException:
                print("Tela de 'continuar conectado?' não apareceu, seguindo para a próxima etapa.")

            time.sleep(1)

            try:
                #aguarda até aparecer o nome caixa de entrada
                element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="topSearchInput"]')))
            except TimeoutException:
                print("Tela de 'entrada' não apareceu, seguindo para a próxima etapa.")

            time.sleep(1)
            search_input = driver.find_element(By.XPATH, '//*[@id="topSearchInput"]')
            time.sleep(2)
            search_input.send_keys('Welcome to ENGAGE! Please verify your email address.')
            time.sleep(1)
            search_input.send_keys(Keys.ENTER)
            time.sleep(1)


        except Exception as e:
            # Clicar em pesquisar e pesquisar pelo e-mail de confirmação se um erro ocorrer
            print(f"Ocorreu um erro: {e}")
            

    finally:
        # clicar no e-mail
        time.sleep(1)
        pyautogui.click(392,409)
        time.sleep(1)

        # confirmar que o remetente é confiavel
        pyautogui.click(707,569)
        time.sleep(1)
        time.sleep(5)
        # clicar para verificar o e-mail
        driver.find_element(By.XPATH, '//*[@id="x_templateBody"]/table[2]/tbody/tr/td/table/tbody/tr/td/p[3]/a').click()
        time.sleep(10)
        save_logs(email)

        # Fechar o navegador
        # Captura a tela e salva como imagem
        save_screenshot(CAMINHO_SCREENSHOT, email)
        time.sleep(2)
        driver.quit()
        time.sleep(1)  # Aguarda 2 segundos antes de reiniciar o navegador para o próximo registro

# Lendo o arquivo de texto e processando cada linha
with open(CAMINHO_ARQUIVO_EMAIL) as arquivo:
    cont = 0
    for linha in arquivo:
        cont += 1
        email, password = linha.strip().split(',')  # Certifique-se de que não há espaços
        realizar_cadastro(email, password, cont)
