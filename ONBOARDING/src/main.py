import os
import gspread
import pandas as pd
from config_loader import load_google_credentials

def get_google_sheet_data(worksheet_name):
    # Carregar credenciais usando o módulo configurado
    credentials = load_google_credentials()
    
    # Autenticar e acessar o Google Sheets
    gc = gspread.authorize(credentials)

    # Abra a planilha e selecione uma aba
    spreadsheet = gc.open("Solicitações de Acesso - TI")
    worksheet = spreadsheet.worksheet(worksheet_name) 

    # Ler a coluna única da planilha (começando da segunda linha para evitar o cabeçalho)
    data = worksheet.col_values(1)[1:]  # Ignora o cabeçalho da primeira linha

    # Separar os dados por vírgula e criar um DataFrame
    data_split = [list(map(str.strip, row.split(','))) for row in data]  # Limpa os espaços
    columns = ['givenName', 'sn', 'userPrincipalName', 'sAMAccountName', 'displayName',
               'name/cn', 'description', 'physicalDeliveryOfficeName', 'mail', 'title', 'company']
    
    return pd.DataFrame(data_split, columns=columns)

# Ler o arquivo CSV
def get_csv_data(csv_file_path):
    try:
        return pd.read_csv(csv_file_path)
    except FileNotFoundError:
        return pd.DataFrame()  # Retorna um DataFrame vazio se o arquivo não existir

# Função para adicionar novas linhas do CSV se houver alteração na planilha
def append_new_rows(google_sheet_df, csv_df, csv_file_path):
    #chave para comparação
    key_columns = ['userPrincipalName']

    # Realiza um merge para identificar novas linhas
    merged_df = pd.merge(google_sheet_df, csv_df[key_columns], how="left", on=key_columns, indicator=True)

    # Encontrando novas linhas que não estão no CSV
    new_rows = merged_df[merged_df['_merge'] == 'left_only'].copy()  # Faz uma cópia para evitar o SettingWithCopyWarning
    new_rows.drop(columns=['_merge'], inplace=True)  # Remove a coluna de merge

    # Adicionando novas linhas ao CSV
    if not new_rows.empty:
        # Limpa os espaços nas linhas e remove colunas vazias
        new_rows = new_rows.apply(lambda x: x.str.strip(), axis=1)  # Limpa os espaços nas linhas
        new_rows.dropna(axis=1, how='all', inplace=True)  # Remove colunas vazias
        new_rows.dropna(how='all', inplace=True)  # Remove linhas vazias
        
        # Verifica se o CSV já existe
        file_exists = os.path.exists(csv_file_path)

        
        
        
        # Adiciona novas linhas ao CSV sem repetir o cabeçalho
        new_rows.to_csv(csv_file_path, mode='a', header=not file_exists, index=False)

        print(f"{len(new_rows)} novas linhas adicionadas ao arquivo CSV")
    else:
        print("Não há novas linhas para adicionar")


def main():
    # Nome da aba e caminho do arquivo CSV
    worksheet_name = "Planilha3"
    csv_file_path = r"C:\Users\john.alencar\Documents\GitHub\programacao\ONBOARDING\automacao\automacao copy.csv"
    
    # Obtendo dados da planilha e do CSV
    google_sheet_data = get_google_sheet_data(worksheet_name)
    csv_data = get_csv_data(csv_file_path)

    # Adicionando novas linhas no CSV
    append_new_rows(google_sheet_data, csv_data, csv_file_path)

if __name__ == "__main__":
    main()
