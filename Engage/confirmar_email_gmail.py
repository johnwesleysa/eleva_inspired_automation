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


LOGS_DIR = r'C:\Users\john.alencar\Documents\GitHub\programacao\PADRAO-AUTOMACAO-WEB\LOGS'
NOME_ARQUIVO_LOG = r'landSchoolEmail_log.txt'
CAMINHO_ARQUIVO_EMAIL = r"C:\Users\john.alencar\Documents\GitHub\programacao\Engage\LandSchool\META QUEST - LandSchool - Email.csv"

def save_screenshot(screenshot, directory, email):
    # Gera o nome completo do arquivo
    full_path = f"{directory}\\{email}.png"
    # Salva a captura de tela
    screenshot.save(full_path)

# Define o diretório e o nome base do arquivo
CAMINHO_SCREENSHOT = r'C:\Users\john.alencar\Documents\GitHub\programacao\PADRAO-AUTOMACAO-WEB\LandSchool'
screenshot_name = datetime.now().strftime("screenshot_landSchool_%Y-%m-%d_%H-%M-%S_")

def save_logs(email):
    # Caminho para o arquivo de log dentro do diretório de logs
    log_file = os.path.join(LOGS_DIR, NOME_ARQUIVO_LOG)
    
    # Abre o arquivo de log no modo de adição
    with open(log_file, 'a') as f:
        f.write(f'-----')
        f.write(f'E-mail: {email}: Verificado;')
        f.write(f'-----\n')
    



# Função para abrir o navegador, preencher os campos e fechar
def realizar_cadastro(email, password):
    # Inicializando uma nova instância do Google Chrome para cada cadastro
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%26ogbl%2F&emr=1&ifkv=ARpgrqcGpktLM1xXav7DhLNKZ9-hF1Jt3YkrSAjBkPYZThv5w0c3I6kQA6L7quk-0wBr8epZccbk5A&ltmpl=default&ltmplcache=2&osid=1&passive=true&rm=false&scc=1&service=mail&ss=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S369749740%3A1729603431810947&ddm=0'
    driver.get(url)

    # Define um tempo máximo de espera
    wait = WebDriverWait(driver, 30)
    time.sleep(1)

    try:
        # Preenche o e-mail
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierId"]'))).send_keys(email)
        driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
        time.sleep(1)

        # Aguarda até aparecer o campo de usuário no CyberArk
        element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="usernameForm"]/div[2]/div/div[1]/input')))
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="usernameForm"]/div[2]/div/div[1]/input').send_keys(email)
        time.sleep(1)

        # Clicar em próximo
        driver.find_element(By.XPATH, '//*[@id="usernameForm"]/div[2]/button').click()
        time.sleep(1)

        # Aguarda aparecer o campo de senha do CyberArk
        element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="passwordForm"]/div[3]/div/div[1]/input')))
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="passwordForm"]/div[3]/div/div[1]/input').send_keys(password)
        time.sleep(1)

        # Clicar em próximo
        driver.find_element(By.XPATH, '//*[@id="passwordForm"]/div[3]/button').click()
        time.sleep(10)

        # Aguardar tela para confirmar se existe
        element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')))
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
        time.sleep(1)

        try:
            # Aguardar tela de bem-vindo
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gaplustosNext"]/div/button/span')))
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="gaplustosNext"]/div/button/span').click()
            except TimeoutException:
                print("Tela de bem-vindo não apareceu, seguindo para a próxima etapa.")

            time.sleep(1)
            # Aguardar tela "este é o Gmail"
            wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[21]/div[2]/div/div[2]/div/div/button/span[5]'))).click()
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[21]/div[2]/div/div[2]/div/div/button/span[5]').click()
            time.sleep(1)

            # Clicar no X do tutorial
            time.sleep(1)
            pyautogui.click(384,203)
            time.sleep(1)


            # Clicar em OK
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bubble-47"]/div/div[2]/div'))).click()
            time.sleep(0.5)


        except Exception as e:
            # Clicar em pesquisar e pesquisar pelo e-mail de confirmação se um erro ocorrer
            print(f"Ocorreu um erro: {e}")
            

    finally:
        # Clicar no X do tutorial
        time.sleep(1)
        pyautogui.click(384,203)
        time.sleep(2)
    
        search_input = driver.find_element(By.XPATH, '//*[@id="gs_lc50"]/input[1]')
        time.sleep(2)
        search_input.send_keys('Welcome to ENGAGE! Please verify your email address.')
        time.sleep(1)
        search_input.send_keys(Keys.ENTER)
        time.sleep(1)

        # clicar na posição especifica do e-mail
        time.sleep(1)
        pyautogui.click(457, 328)
        time.sleep(1)

        # fechar notificação
        pyautogui.click(882, 683)
        time.sleep(1)

        # clicar para verificar o e-mail
        pyautogui.click(578, 760)
        time.sleep(10)
        save_logs(email)

        # Fechar o navegador
        # Captura a tela e salva como imagem
        screenshot = pyautogui.screenshot()
        time.sleep(0.5)
        save_screenshot(screenshot, CAMINHO_SCREENSHOT, email)
        time.sleep(2)
        driver.quit()
        time.sleep(1)  # Aguarda 2 segundos antes de reiniciar o navegador para o próximo registro

# Lendo o arquivo de texto e processando cada linha
with open(CAMINHO_ARQUIVO_EMAIL) as arquivo:
    cont = 0
    for linha in arquivo:
        cont += 1  # Corrigido para incrementar o contador
        email, password = linha.strip().split(',')  # Certifique-se de que não há espaços
        realizar_cadastro(email, password)
