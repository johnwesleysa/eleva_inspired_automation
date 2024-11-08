# Caminho da nova OU
$caminhoDestino = "OU=6,OU=Fundamental 2,OU=Alunos,OU=Contas,OU=Escola Eleva Recife,OU=PE,DC=escolaeleva,DC=local"

# Obter todos os usuários na nova OU
$usuariosNaNovaOU = Get-ADUser -Filter * -SearchBase $caminhoDestino

# Atualizar atributo Job Title para todos os usuários na nova OU
foreach ($usuarioNaNovaOU in $usuariosNaNovaOU) {
    Set-ADUser -Identity $usuarioNaNovaOU -Title "Grade 6" -Office "Escola-Eleva-Recife" -Description "Escola-Eleva-Recife"
    Write-Host "Atributo Job Title atualizado para o usuário $($usuarioNaNovaOU.Name)."
}
