#import pandas as pd
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#==============================================================================================


#Abrindo Chrome
service = Service()

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

url = 'http://10.17.64.11:9191/admin'

driver.get(url)

driver.maximize_window()
time.sleep(5)

#==============================================================================================


#Autenticação
driver.find_element(By.XPATH, '//*[@id="inputUsername"]').send_keys('john.alencar')
time.sleep(0.5)

#senha
driver.find_element(By.XPATH, '//*[@id="inputPassword"]').send_keys('Geforce@1050')
time.sleep(0.5)

#clicar em entrar
driver.find_element(By.XPATH, '//*[@id="login"]/input').click()
time.sleep(5)

#==============================================================================================

#Alterando o valor emr reais

valor_usuarios = '400,00'

#clicando em usuários
driver.find_element(By.XPATH, '//*[@id="mainnav"]/ul/li[2]/div/a').click()
time.sleep(0.5)

#clicando em ações em lote
driver.find_element(By.XPATH, '//*[@id="pageactions"]/ul/li[2]/a').click()
time.sleep(0.5)

#clicando em "Ajustar o crédito para"
driver.find_element(By.XPATH, '//*[@id="radSet"]').click()
time.sleep(0.5)

# Apagando o campo de valor antes de inserir
credit_field = driver.find_element(By.XPATH, '//*[@id="txtSet"]')
credit_field.clear()  # Clear the field

# inserindo o valor de 400
credit_field.send_keys(valor_usuarios)
time.sleep(0.5)

#clicando em "Ok"
driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/table/tbody/tr[2]/td[2]/form/div/table/tbody/tr[7]/td/input[3]').click()
time.sleep(1)

#clicando no pop-up
pyautogui.click(1025,208)
time.sleep(10)
pyautogui.click(381,598)
time.sleep(0.5)


#==============================================================================================

#Def para Usuários Específicos

def user_especific(user, valor):
    time.sleep(1)
    #apagando o campo o nome do usuario
    driver.find_element(By.XPATH,'//*[@id="quickFindAuto"]').clear()
    time.sleep(0.5)

    #enviando o nome do usuario
    driver.find_element(By.XPATH,'//*[@id="quickFindAuto"]').send_keys(user)
    time.sleep(0.5)

    #clicando para enviar
    driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[3]/table/tbody/tr[2]/td[2]/div/form/table/tbody/tr/td[2]/input[1]').click()
    time.sleep(1)

    #apagando o valor em "Saldo"
    driver.find_element(By.XPATH, '//*[@id="userBalance"]').clear()
    time.sleep(0.5)

    #digitando 1400,00
    driver.find_element(By.XPATH, '//*[@id="userBalance"]').send_keys(valor)
    time.sleep(0.5)

    #clicando em ok
    driver.find_element(By.CSS_SELECTOR, '#content > div.tabContent > div.box > table > tbody > tr:nth-child(2) > td.box-content > form > table > tbody > tr.footer > td > input[type=submit]:nth-child(3)').click()
    time.sleep(0.5)

#==============================================================================================

#Usuários Específicos e valor
valor = '1400,00'
users_list = ['amanda.nascimento', 'helena.gomes']

for user in users_list:
    user_especific(user, valor)

