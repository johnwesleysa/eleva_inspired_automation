# Lista de usuários a serem verificados
$listaUsuarios = @(
"Alice Leal Lapa",
"Alice Paiva Guimarães",
"Ana Bruch Acioli Lins",
"Ana Clara Peri Falcão",
"Artur Appolonio Rocha",
"Bernardo Calado Gondim de Andrade",
"Bernardo Galliza Favaro Nunes Nogueira",
"Bruna Carvalho Ferreira",
"Caio Medeiros Brasileiro Clemente",
"Carlos Eduardo Sasson Negreiros",
"Chloe Carneiro Leão Barbalho",
"Clara Ventura Urbano Lima",
"Daniel Alexandre Silva Queiroz",
"Daniel Da Costa Queiroz de Oliveira Filho",
"Davi Negreiros Brandt",
"Diego Antônio Soares Farias Filho",
"Dora Wolfenson Brandão Cavalcanti",
"Eduardo Dias Brody da Fonte",
"Eduardo Póvoa Da Silva",
"Elisa De Deus e Mello Dias",
"Gabriela Leocadio Silva de Barros Marques",
"Helena Oliveira Costa",
"Isadora Da Fonte Carrazzone Henriques Mongiovi",
"Ivan Pimentel Dantas Lemos",
"Joanna Dantas Tavares Cardinot",
"João Brennand de Petribú Ventura",
"João Kauffman Lamartine",
"João Lucas Boaretto Cintra",
"João Pedro Sasson Negreiros",
"José Henrique Vieira de Andrade",
"Laura Pinto Fernandes",
"Leticia Belo Oliveira",
"Letícia Gayão Diniz Oliveira",
"Livia Nascimento Aretakis Cordeiro",
"Lucas Ebrahim Leite Zarzar Nunes",
"Lucas Vieira Lima",
"Lucca Albuquerque Guedes",
"Luísa Ferreira de Almeida",
"Luiz Antonio Vieira de Melo Ramos",
"Luiz Miguel Tavares Pereira",
"Luiza Girard Tavares Pereira",
"Luiza Guirão Carriço de Souza",
"Manuela Figueiredo Cabral",
"Maria Clara Croccia Leal Ribeiro",
"Maria Manuela Fischer Pacheco Monte Studart",
"Pedro Bezerra de Melo Calife",
"Pedro Henrique Pessoa Beltrão",
"Rafael Faria Lima da Costa Lins",
"Raphael Eugene Egan Santos",
"Ricardo Dias Bezerra Leite",
"Sofia Bello Mertens Fittipaldi",
"Sofia Marinho Viegas",
"Thiago Nóbrega Menezes de Matos",
"Vitor Hugo Tavares Vieira"

)

# Inicializar uma lista para logon names encontrados
$logonNamesEncontrados = @()
$logonNamesNaoEncontrados = @()

# Iterar sobre cada usuário na lista
foreach ($nomeUsuario in $listaUsuarios) {
    # Obter o logon name do usuário no Active Directory
    $logonName = (Get-ADUser -Filter {Name -like $nomeUsuario}).SamAccountName

    if ($logonName -ne $null) {
        $logonNamesEncontrados += "${nomeUsuario}; ${logonName}"
        Write-Host "O logon name do usuário $nomeUsuario é $logonName."
        # Pode adicionar outras ações desejadas para usuários encontrados aqui
    } else {
        Write-Host "O logon name do usuário $nomeUsuario não foi encontrado no Active Directory."
        $logonNamesNaoEncontrados += "${nomeUsuario}"
        # Pode adicionar outras ações desejadas para usuários não encontrados aqui
    }
}

# Exibir a lista de logon names encontrados
Write-Host "`nLogon names encontrados no Active Directory:`n"
$logonNamesEncontrados
Write-Host "`nLogon names NÃO encontrados no Active Directory:`n"
$logonNamesNaoEncontrados