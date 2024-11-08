import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import pyautogui
import os


CAMINHO_ARQUIVO_ENGAGE = r"C:\Users\john.alencar\Documents\GitHub\programacao\Engage\LandSchool\META QUEST - LandSchool - Engage.csv"

LOGS_DIR = r'C:\Users\john.alencar\Documents\GitHub\programacao\Engage\LOGS\engage'
NOME_ARQUIVO_LOG = r'land.txt'

def save_logs(email):
    # Caminho para o arquivo de log dentro do diretório de logs
    log_file = os.path.join(LOGS_DIR, NOME_ARQUIVO_LOG)
    
    # Abre o arquivo de log no modo de adição
    with open(log_file, 'a') as f:
        f.write(f'-----')
        f.write(f'E-mail: {email}: Verificado;')
        f.write(f'-----\n')

# Função para abrir o navegador, preencher os campos e fechar
def realizar_cadastro(userName, email, firstName, lastName, password):
    # Inicializando uma nova instância do Google Chrome para cada cadastro
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://app.engagevr.io/register'
    driver.get(url)

    # Define um tempo máximo de espera (ex: 30 segundos)
    time.sleep(5)
    wait = WebDriverWait(driver, 30)
    time.sleep(5)
    pyautogui.click(359,953)


    # Preenche o formulário de registro
    try:
        # First name
        driver.find_element(By.XPATH, '//*[@id="register-first_name"]').send_keys(firstName)

        # Last name
        driver.find_element(By.ID, 'register-last_name').send_keys(lastName)

        # Email
        driver.find_element(By.ID, 'register-email').send_keys(email)

        # Password
        driver.find_element(By.ID, 'register-password').send_keys(password)

        # Confirm password
        driver.find_element(By.ID, 'register_confirm_password-password').send_keys(password)

        # Clicar na caixinha de aceitar termos
        driver.find_element(By.XPATH, '//*[@id="registrationForm"]/div[6]/div/div/label/span').click()

        # Clicar no botão de confirmar
        driver.find_element(By.ID, 'register-create_account_submit_btn').click()

        # Aguarda até que o elemento esteja presente e visível (verificando se a página seguinte carregou)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="profile_edit-h3"]')))
        time.sleep(0.5)

        # Clicar em username e preencher
        time.sleep(2)
        driver.find_element(By.ID, 'profile_edit-username').send_keys(userName)
        time.sleep(1)


        # Clicar em country
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="web-container"]/div[2]/main/div/div[1]/div/div/div/div/form/div[2]/div/div[5]/div[1]/div/div/div/div[2]/span'))).click()
        #driver.find_element(By.XPATH, '//*[@id="web-container"]/div[2]/main/div/div[1]/div/div/div/div/form/div[2]/div/div[5]/div[1]/div/div/div/div[2]/span').click()
        time.sleep(1)                               

        # Enviar timezone "Brazil" e pressionar Enter
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="profile_edit-country"]').send_keys("Brazil")
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="profile_edit-country"]').send_keys(Keys.ENTER)
        time.sleep(0.5)


        # Clicar em timezone
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="web-container"]/div[2]/main/div/div[1]/div/div/div/div/form/div[2]/div/div[6]/div[2]/div/div/div/div[2]/span').click()
        time.sleep(1)


        # Enviar timezone "America/Sao_Paulo" e pressionar Enter
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="profile_edit-timezone"]').send_keys("America/Sao_Paulo")
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="profile_edit-timezone"]').send_keys(Keys.ENTER)
        time.sleep(0.5)


        # Clicar no botão de update profile
        driver.find_element(By.ID, 'profile_edit-submit').click()

        # Aguarda até que o perfil seja editado e a página carregue
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="profile-edit"]')))
        save_logs(email)

    finally:
        # Fechar o navegador
        driver.quit()
        time.sleep(2)  # Aguarda 2 segundos antes de reiniciar o navegador para o próximo registro

# Lendo o arquivo de texto e processando cada linha
with open(CAMINHO_ARQUIVO_ENGAGE) as arquivo:
    for linha in arquivo:
        userName = linha.split(',')[1]
        email = linha.split(',')[0]
        firstName = linha.split(',')[2]
        lastName = linha.split(',')[3]
        password = linha.split(',')[4]

        # Realiza o cadastro para a linha atual
        realizar_cadastro(userName, email, firstName, lastName, password)
