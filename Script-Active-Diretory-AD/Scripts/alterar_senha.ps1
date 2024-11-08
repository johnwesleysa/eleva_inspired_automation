# Caminho para o arquivo CSV
$caminhoCSV = "C:\Users\john.alencar\Desktop\Alterar Senha\alunosg6.csv"

# Importar dados do arquivo CSV
$dadosCSV = Import-Csv $caminhoCSV

# Iterar sobre cada linha do CSV
foreach ($linha in $dadosCSV) {
    # Obter o nome de usuário e senha da linha atual
    $usuario = $linha.usuario
    $senha = $linha.senha

    # Obter o usuário do Active Directory
    $usuarioAD = Get-ADUser -Filter {SamAccountName -eq $usuario}

    if ($usuarioAD -ne $null) {
        # Converter a senha em um formato seguro
        $senhaSegura = ConvertTo-SecureString $senha -AsPlainText -Force

        # Definir a senha para o usuário
        Set-ADAccountPassword -Identity $usuarioAD -NewPassword $senhaSegura -Reset

        # Garantir que a senha não expire
        Set-ADUser -Identity $usuarioAD -PasswordNeverExpires $true

        Write-Host "A senha foi definida para o usuário $usuario."
    } else {
        Write-Host "O usuário $usuario não foi encontrado no Active Directory."
    }
}
