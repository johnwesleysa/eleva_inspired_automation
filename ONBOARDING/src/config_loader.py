# src/config_loader.py
import os
from google.oauth2.service_account import Credentials

def load_google_credentials():
    # Caminho para o arquivo de credenciais
    cred_path = os.path.join("config", "credentials", "automacao-onboarding-440312-791006d38824.json")
    
    # Verifica se o arquivo existe
    if not os.path.exists(cred_path):
        raise FileNotFoundError(f"Arquivo de credenciais não encontrado: {cred_path}")
    
    # Define os escopos necessários para acessar o Google Sheets e o Google Drive
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    
    # Carrega as credenciais
    credentials = Credentials.from_service_account_file(cred_path, scopes=scopes)
    return credentials
