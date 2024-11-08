# Lista de nomes de usuários a serem movidos
$nomesUsuarios ="Maria Luiza De Castro Costa Erlich",
"Matheus Bandeira de Melo J Silva",
"Joao Vitor Magalhaes Bittencourt Freire de Oliveira",
"Bella Barreto Villar"
    # ... adicione os outros nomes aqui ...

# Inicializar listas para usuários movidos e não movidos
$usuariosMovidos = @()
$usuariosNaoMovidos = @()

# Loop através da lista de nomes
foreach ($nomeUsuario in $nomesUsuarios) {
    # Obter informações do usuário
    $usuario = Get-ADUser -Filter {Name -eq $nomeUsuario}

    # Verificar se o usuário foi encontrado
    if ($usuario -ne $null) {
        # Construir os caminhos de origem e destino
        $caminhoOrigem = $usuario.DistinguishedName
        $caminhoDestino = "OU=I5,OU=Infantil,OU=Alunos,OU=Contas,OU=Escola Eleva Recife,OU=PE,DC=escolaeleva,DC=local"

        # Tentar mover o usuário
        try {
            Move-ADObject -Identity $caminhoOrigem -TargetPath $caminhoDestino -ErrorAction Stop
            $usuariosMovidos += $usuario
            Write-Host "Usuário $($usuario.Name) movido com sucesso!"
        } catch {
            $usuariosNaoMovidos += $usuario
            Write-Host "Falha ao mover usuário $($usuario.Name): $_"
        }
    } else {
        Write-Host "Usuário com nome '$nomeUsuario' não encontrado."
    }
}

# Exibir resultados
Write-Host "Usuários movidos:"
$usuariosMovidos | Select-Object Name, DistinguishedName | Format-Table


Write-Host "Usuários não movidos:"
$usuariosNaoMovidos | Select-Object Name, DistinguishedName | Format-Table
