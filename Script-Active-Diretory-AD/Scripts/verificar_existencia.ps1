# Lista de usuários a serem verificados
$listaUsuarios = @(
    "Anderson José Batista Freire da Silva",
"Arthur Firmino Zirpoli",
"Artur alves de farias neto Neto",
"Artur Santos da Silva Cavalcanti",
"Beatriz Magalhães",
"Beatriz Patriota Tavares",
"Benicio Augusto Ramirez Lorenzi",
"Benício De Biase Oliveira Siqueira Campos",
"Bernardo Dias de pontes ramos",
"Bernardo Farias Sukar",
"Betina Nascimento de Lima Guilherme",
"Caio Augusto Silva",
"Cecília Leal Lapa",
"Damiano Afonso Guerra",
"Eduardo Fonseca Lima Luchsinger",
"Eduardo Raposo Ferreira Lima",
"Fernanda Mariano Jucá",
"Flora Brennand",
"Gerson Carneiro Leao Filho",
"Guilherme Dowsley de Andrade Rodrigues",
"Guilherme Girard Tavares Pereira",
"Guilhermina Moura de Albuquerque Maranhão",
"Gustavo Pontual Lima Pinto Coelho",
"HELENA Magalhães Oliveira",
"Henrique Albuquerque Nobrega Cavalcanti",
"Henrique Júlio Patriota de Albuquerque Maranhão",
"Hugo Firmino Zirpoli",
"Isabela Da Fonte de Souza Leão",
"Isabela Naslavsky Pereira Lima",
"Isadora Negreiros Brandt",
"João Antônio meneses Bruno de Assis",
"João Felipe Gomes Queiroz",
"João Gabriel de Almeida Vieira",
"Joaquim Júlio Patriota de Albuquerque Maranhão",
"José Alberto Nunes Correia de Oliveira Pragana",
"José Jaime Monteiro Brennand Neto",
"José Maranhão Neto",
"Julia Ficher Marques Maciel",
"Julia de Ventura Urbano Lima",
"Laércio Viriato de Medeiros Silva",
"Laura Fernandes Pessoa de Mello",
"Laura Melo Leitão Rocha de Sá",
"Letícia Andrade Calado Tenório",
"Letícia Sobral Callou",
"Luana Ribeiro Laurentino de Souza",
"Lucas Barros Teixeira",
"Lucas Lucchese",
"Lucas Nascimento Aretakis Cordeiro",
"Luiz Filipe Gomes Sande Medeiros",
"Luiza Brennand Lima",
"Luiza Rossiter Braun",
"Marcela Rocha Schwambach Mota",
"Maria Beatriz Pita Leão da Costa",
"Maria Braga Maranhão",
"Maria Eduarda Albertotti Paoletti",
"Maria Eduarda De Vasconcellos pires",
"Maria Eduarda Ferreira da Fonte",
"Maria Eduarda Ferreira Diamant",
"Maria Luísa Cordeiro Magalhães",
"Maria Sophia Rodrigues Santos Rosa",
"Marina Bezerra Vasconcellos",
"Marina Cavalcanti de Morais Botelho",
"Marina Maia Chaves",
"Marina Orn Scalco",
"Marina Rosa Albuquerque",
"Mateus de Oliveira Leal",
"Matheus Amaral Correia Sá",
"Matheus Vieira Serrano de Andrade",
"Mércia De Moura Rabelo",
"Miguel Bortoletti Croccia",
"Miguel Bradley Lima",
"Olívia Carneiro Da Cunha Lapa Dalla Nora Pimentel",
"Paulo Renato Bezerra de Sá Pereira",
"Pietra Magalhaes Bezerra de Menezes Lyra",
"Rafael Breghirolli Serpa Souza",
"Rafael Francisco Mariano Maciel Canazart",
"Rafael Perez",
"SOPHIE KONRAD FONTES",
"Taney Eduardo Fernandes Farias",
"Julia Neiva Coelho Deak",
"Uler Benicio Zanardi"
)

# Inicializar uma lista para usuários não encontrados
$usuariosNaoEncontrados = @()

# Iterar sobre cada usuário na lista
foreach ($nomeUsuario in $listaUsuarios) {
    # Verificar se o usuário existe no Active Directory (usando -like para correspondência parcial)
    $usuarioExistente = Get-ADUser -Filter {Name -like $nomeUsuario}

    if ($usuarioExistente -eq $null) {
        $usuariosNaoEncontrados += $nomeUsuario
        Write-Host "O usuário $nomeUsuario não foi encontrado no Active Directory."
        # Pode adicionar outras ações desejadas para usuários não encontrados aqui
    }
}

# Exibir a lista de usuários não encontrados
Write-Host "`nUsuários não encontrados no Active Directory:`n"
$usuariosNaoEncontrados
