# Lista de nomes de usu�rios a serem movidos
$nomesUsuarios ="Maria Luiza De Castro Costa Erlich",
"Matheus Bandeira de Melo J Silva",
"Joao Vitor Magalhaes Bittencourt Freire de Oliveira",
"Bella Barreto Villar"
    # ... adicione os outros nomes aqui ...

# Inicializar listas para usu�rios movidos e n�o movidos
$usuariosMovidos = @()
$usuariosNaoMovidos = @()

# Loop atrav�s da lista de nomes
foreach ($nomeUsuario in $nomesUsuarios) {
    # Obter informa��es do usu�rio
    $usuario = Get-ADUser -Filter {Name -eq $nomeUsuario}

    # Verificar se o usu�rio foi encontrado
    if ($usuario -ne $null) {
        # Construir os caminhos de origem e destino
        $caminhoOrigem = $usuario.DistinguishedName
        $caminhoDestino = "OU=I5,OU=Infantil,OU=Alunos,OU=Contas,OU=Escola Eleva Recife,OU=PE,DC=escolaeleva,DC=local"

        # Tentar mover o usu�rio
        try {
            Move-ADObject -Identity $caminhoOrigem -TargetPath $caminhoDestino -ErrorAction Stop
            $usuariosMovidos += $usuario
            Write-Host "Usu�rio $($usuario.Name) movido com sucesso!"
        } catch {
            $usuariosNaoMovidos += $usuario
            Write-Host "Falha ao mover usu�rio $($usuario.Name): $_"
        }
    } else {
        Write-Host "Usu�rio com nome '$nomeUsuario' n�o encontrado."
    }
}

# Exibir resultados
Write-Host "Usu�rios movidos:"
$usuariosMovidos | Select-Object Name, DistinguishedName | Format-Table


Write-Host "Usu�rios n�o movidos:"
$usuariosNaoMovidos | Select-Object Name, DistinguishedName | Format-Table
