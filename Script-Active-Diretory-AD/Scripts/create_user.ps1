# Importando o módulo Active Directory
Import-Module ActiveDirectory

# Caminho para o arquivo CSV
$caminhoCSV = "C:\Users\john.alencar\Desktop\create_user_g4.csv"

# Importar dados do arquivo CSV
$dadosCSV = Import-Csv $caminhoCSV

# Iterar sobre cada linha do CSV
foreach ($linha in $dadosCSV) {
    # Extrair informações do CSV
    $nome = $linha.Nome
    $sobrenome = $linha.Sobrenome
    $nomeCompleto = "$nome $sobrenome"
    $usuario = $linha.Usuario
    $senha = $linha.Senha
    $descricao = $linha.Descricao
    $cargo = $linha.Cargo
    $email = $linha.Email
    $grupos = $linha.MemberOf
    $title = $linha.Title
    $ouDestino = "OU=4,OU=Fundamental 1,OU=Alunos,OU=Contas,OU=Escola Eleva Recife,OU=PE,DC=escolaeleva,DC=local"

    # Criar senha segura
    $senhaSegura = ConvertTo-SecureString $senha -AsPlainText -Force

    # Definir propriedades do novo usuário
    $parametros = @{
        Name = $nomeCompleto
        SamAccountName = $usuario
        UserPrincipalName = "$usuario@seu-dominio.local"
        AccountPassword = $senhaSegura
        Description = $descricao
        Office = $cargo
        EmailAddress = $email
        Title = $title
        PasswordNeverExpires = $true
        Enabled = $true
    }

    # Criar o usuário no Active Directory
    $novoUsuario = New-ADUser @parametros

    # Adicionar o usuário aos grupos especificados
    foreach ($grupo in $grupos) {
        Add-ADGroupMember -Identity $grupo -Members $usuario
    }

    # Mover o usuário para a OU de destino
    Move-ADObject -Identity $novoUsuario -TargetPath $ouDestino

    Write-Host "Usuário $nomeCompleto criado e movido para $ouDestino com sucesso."
}
