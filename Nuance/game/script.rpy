# =======================================
# CONFIGURAÇÕES INICIAIS
# =======================================
define narrator = Character(None)   # narração sem nome
define p = Character("[player_name]")  # jogador (nome dinâmico)
define c = Character("Carmen")
define a = Character("Alicia")
define l = Character("Lucas")
define t = Character("Thaynara")
define m = Character("Matheus")
define n = Character("Nicole")
define z = Character("Professor Zacarias")
define u = Character("Luana")
define y = Character("Trabalhador da feira de adoção")

default player_name = "???"
default lucas_confidence = 0     # aumenta conforme o jogador apoia
default alicia_follow = False
default chosen_pet = None        # "cat" ou "dog"

# =======================================
# IMAGENS
# =======================================

# Lucas
image lucas normal = "images/lucas_normal.png"
image lucas feliz = "images/lucas_feliz.png"
image lucas triste = "images/lucas_triste.png"
image lucas desconfortavel = "images/lucas_desconfortavel.png"
image lucas pensativo = "images/lucas_pensativo.png"

# gato
image cat = "images/gato.png"
image fred = "images/gato.png"

# cachorro
image dog = "images/cachorro.png"
image alfred = "images/cachorro.png"

# Player
image player normal = "images/player_normal.png"
image player feliz = "images/player_feliz.png"
image player triste = "images/player_triste.png"
image player bravo = "images/player_bravo.png"
image player pensativo = "images/player_pensativo.png"

# Alicia
image alicia normal = "images/alicia_normal.png"
image alicia feliz = "images/alicia_feliz.png"
image alicia desconfortavel = "images/alicia_desconfortavel.png"

# Carmen
image carmen normal = "images/carmen_normal.png"

# Thaynara
image thaynara normal = "images/thaynara_normal.png"
image thaynara feliz = "images/thaynara_feliz.png"
image thaynara preocupada = "images/thaynara_preocupada.png"

# Matheus
image matheus normal = "images/matheus_normal.png"
image matheus feliz = "images/matheus_feliz.png"
image matheus desconfortavel = "images/matheus_desconfortavel.png"

# Nicole
image nicole normal = "images/nicole_normal.png"
image nicole feliz = "images/nicole_feliz.png"
image nicole desconfortavel = "images/nicole_desconfortavel.png"

# Professor Zacarias
image zacarias normal = "images/zacarias_normal.png"
image zacarias bravo = "images/zacarias_bravo.png"

# Luana
image luana normal = "images/luana_normal.png"
image luana feliz = "images/luana_feliz.png"
image luana brava = "images/luana_brava.png"

# Trabalhador da feira de adoção
image trabalhador normal = "images/trabalhador_normal.png"
image trabalhador feliz = "images/trabalhador_feliz.png"

# fotos dos animais no celular de Lucas
image fred_phone = "images/fred_phone.png"
image alfred_phone = "images/alfred_phone.png"

# Fundos
image bg classroom = "images/bg_classroom.jpg"
image bg room = "images/bg_room.jpg"
image bg school_hall = "images/bg_school_hall.jpg"
image bg school_yard = "images/bg_school_yard.jpg"
image bg adoption_fair = "images/bg_adoption_fair.jpg"
image bg car_interior = "images/bg_car_interior.jpg"
image bg street_day = "images/bg_street_day.jpg"
image bg school_gate ="Images/bg_school_gate.jpg"

# =======================================
# LABEL INICIAL
# =======================================
label start:

    # Aplica o brilho definido pelo jogador antes de qualquer cena
    # Caso você ainda não tenha definido essa função, remova ou defina antes
    # $ apply_brightness()

    # Introdução narrativa
    p "Você conhece, tem um amigo ou é uma pessoa com Transtorno do Espectro Autista?"
    p "Bom, tenho um amigo… e diferente do que muitas pessoas pensam, isso não é um empecilho para nossa amizade."
    p "Nós crescemos juntos, meus pais e a mãe dele são amigos desde a adolescência. Nós jogamos, estudamos e saímos juntos..."
    p "Mas as coisas não são tão simples para ele quanto são para mim."
    p "Por ter o nível 1 do TEA, muitas pessoas não enxergam que isso é uma condição e não apenas parte de sua personalidade."
    p "Além disso, ele não consegue socializar com facilidade… e eu sou a única pessoa que ele tem amizade."
    narrator "Embarquem nessa jornada juntos."

    # Escolha do nome
    $ player_name = renpy.input("Escolha o nome do seu personagem:").strip()
    if player_name == "":
        $ player_name = "Ariel"

    jump scene1

# =======================================
# CENA 1 – COZINHA
# =======================================
label scene1:

    scene bg room with fade
    show carmen normal at right
    show player normal at left

    c "Vem, [player_name], você vai se atrasar!"
    c "Bom dia! Não esqueça de levar seu lanche!"
    p "Não vou esquecer, valeu!"
    c "Eu estou indo trabalhar, não vá sem tomar seu café. Boa aula, tente não se atrasar."

    # Escolha usando screen choice_screen
    $ _choices = ["Pode deixar, mãe.", "Não vou atrasar, vai ser tranquilo.", "Vou pegar uma fruta e comer no caminho. Tô indo já, tchau!"]
    $ _actions = [
        Function(p, "Pode deixar, mãe."),  # aqui você pode colocar ações adicionais
        Function(p, "Não vou atrasar, vai ser tranquilo."),
        Function(p, "Vou pegar uma fruta e comer no caminho. Tô indo já, tchau!")
    ]
    call screen choice_screen

    hide carmen
    hide player
    narrator "Você sai de casa em direção à escola."
    jump scene2

# =======================================
# CENA 2 – CHEGADA NA ESCOLA
# =======================================
label scene2:

    scene bg school_hall with fade
    show alicia normal at right
    show player normal at left

    narrator "Você está no último ano do ensino médio."
    narrator "As férias de julho estão chegando, esse é o último dia de aula antes delas."
    a "Oi! Que bom te ver por aqui! Como tá a ansiedade para as férias?"
    narrator "Essa é Alicia, ela pode parecer uma pessoa muito legal, mas não é."
    narrator "Ela e seus amigos excluem e ficam fazendo piadas com Lucas apenas por ele não ser neurotípico."

    $ _choices = ["Conversar educadamente com Alicia", "Ignorar Alicia"]
    $ _actions = [
        Function(assign, "alicia_follow", True),
        Function(assign, "alicia_follow", False)
    ]
    call screen choice_screen

    hide alicia
    jump scene3

# =======================================
# CENA 3 – LUCAS NA SALA
# =======================================
label scene3:

    scene bg classroom with fade

    narrator "Você vê Lucas sentado sozinho na última cadeira."

    $ _choices = ["Acenar de longe", "Gritar 'oi'"]
    $ _actions = [
        Function(assign, "lucas_confidence", lucas_confidence + 1),
        Function(assign, "lucas_confidence", lucas_confidence)
    ]
    call screen choice_screen

    # Reação da Alicia
    a "Estranho ver você cumprimentando ele assim… ele nunca fala com ninguém. Sempre é tão chato…"

    $ _choices = [
        "Ele é legal, Alicia. Só tem dificuldade em fazer amigos.",
        "Ele não é chato, só precisa de tempo para se abrir."
    ]
    $ _actions = [
        Function(assign, "lucas_confidence", lucas_confidence + 1),
        Function(assign, "lucas_confidence", lucas_confidence)
    ]
    call screen choice_screen

    # Continua com a narrativa e decisão
    jump scene3_choice

label scene3_choice:

    $ _choices = ["Sair de perto da Alicia", "Isso é bullying, Alicia! O que você tem na cabeça pra pensar em algo assim?"]
    $ _actions = [
        Function(assign, "lucas_confidence", lucas_confidence),
        Function(assign, "lucas_confidence", lucas_confidence + 1)
    ]
    call screen choice_screen

    narrator "Você vai até Lucas."
    p "Oi Lucas! Animado para as férias?"
    show lucas pensativo
    l "Se eu tô animado? Demais. Vai passar uns dias lá em casa?"
    p "Não vai rolar dessa vez. Meus pais tiraram férias também, vamos viajar pro Nordeste."
    l "Ah…"
    p "Mas de noite acho que consigo jogar com você."
    l "Não precisa, pode se divertir, não gosto de incomodar…"
    narrator "Você percebe que Lucas já não está olhando mais para você quando fala isso, mas sim para Luana."
    narrator "Luana é a garota que ele quer fazer amizade, mas como tem dificuldades em socializar, acaba não conversando com ela."

    $ _choices = [
        "Ela parece ser legal mesmo, você só vai saber se tentar conversar com ela.",
        "Relaxa… só espera tomar coragem.",
        "(Você apenas acena com a cabeça, em silêncio.)"
    ]
    $ _actions = [
        Function(assign, "lucas_confidence", lucas_confidence + 1),
        Function(assign, "lucas_confidence", lucas_confidence),
        Function(assign, "lucas_confidence", lucas_confidence - 1)
    ]
    call screen choice_screen

    jump scene4

# =======================================
# CENA 4 – INTERVALO / DECISÃO-CHAVE
# =======================================
label scene4:

    scene bg school_yard with fade
    show lucas normal at left
    show player normal at right

    narrator "Pátio da escola, sol da manhã, alguns alunos conversando ao fundo. Você e Lucas estão sentados em um banco."

    show lucas pensativo

    l "(olhando para o chão) Sabe, eu me sinto sozinho às vezes."
    p "Você não está sozinho, eu tô aqui."
    l "Eu sei, mas é insuportável isso."
    p "Eu estar aqui?"  # jogador confuso
    l "Não e Sim. Quer dizer, ter amizade com você é ótimo. Mas eu não queria ter amizade só com você."
    l "Tipo, eu já não consigo conversar com as pessoas direito e, às vezes, quando vou conversar parece que a pessoa tem medo, dó, não sei, de mim."
    l "Eu me sinto errado, saca? Às vezes até você me trata como se eu fosse um brinquedo prestes a quebrar."

    narrator "Você fica em silêncio por um instante, pensando no que dizer..."

    $ _choices = [
        "Responder com sinceridade e empatia",
        "Tentar mudar o assunto para algo mais leve",
        "Responder de forma defensiva"
    ]
    $ _actions = [
        Function(assign, "lucas_confidence", lucas_confidence + 2),
        Function(assign, "lucas_confidence", lucas_confidence + 1),
        Function(assign, "lucas_confidence", lucas_confidence - 1)
    ]
    call screen choice_screen

    jump scene5

# =======================================
# CENA 5 – VISITA AO ABRIGO / FEIRA DE ADOÇÃO
# =======================================
label scene5:

    scene bg adoption_fair with fade

    show thaynara feliz at left
    t "Obrigada por ter vindo, [player_name]. O Lucas falou que você gosta de animais."

    show player normal at right
    p "Eu gosto mesmo, tia."

    show lucas pensativo at center
    l "Esse lugar é muito grande, vocês não acham?"

    show thaynara feliz
    t "É porque ele é dividido em partes: tem cachorros, gatos, porquinhos-da-índia, coelhos…"

    l "Quero ver os…"

    show cat at center with fade
    show dog at right with fade

    $ _choices = ["Escolher o gato", "Escolher o cachorro"]
    $ _actions = [
        Function(assign, "chosen_pet", "cat"),
        Function(assign, "chosen_pet", "dog")
    ]
    call screen choice_screen

    jump scene6

# =======================================
# CENA 6 – CARRO
# =======================================
label scene6:

    scene bg car_interior with fade
    show thaynara feliz at left
    show player normal at right

    if chosen_pet == "cat":
        show lucas feliz at center
        show fred at center
    else:
        show lucas feliz at center
        show alfred at center

    jump scene7

# =======================================
# CENA 7 – DEPOIS DA VIAGEM
# =======================================
label scene7:

    scene bg school_gate with fade

    if chosen_pet == "cat":
        show lucas feliz at center
        show fred_phone at right
    else:
        show lucas feliz at center
        show alfred_phone at right

    $ _choices = [
        "Sério? O que aconteceu?",
        "Você parece diferente. Tá mais animado.",
        "Você descobriu um quarto secreto na sua casa cheio de dinheiro? (brincando)"
    ]
    $ _actions = [
        Function(assign, "lucas_confidence", lucas_confidence + 1),
        Function(assign, "lucas_confidence", lucas_confidence + 1),
        Function(assign, "lucas_confidence", lucas_confidence)
    ]
    call screen choice_screen

    jump scene8

# =======================================
# CENA 8 – Explicação da mudança
# =======================================
label scene8:

    if chosen_pet == "dog":
        l "Eu comecei a levar o Alfred no parque, né? No começo fiquei com medo de ficar deslocado, mas agora me sinto bem."
    else:
        l "Eu comecei a cuidar do Fred. Ele é muito fofo!"

    jump scene9

# =======================================
# CENA 9 – Reunião com amigos
# =======================================
label scene9:

    scene bg school_hall with fade
    show lucas feliz at left
    show player normal at right
    show alicia normal at center

    $ _choices = ["Falar com Alicia sobre Lucas", "Ignorar Alicia"]
    $ _actions = [
        Function(assign, "alicia_follow", True),
        Function(assign, "alicia_follow", False)
    ]
    call screen choice_screen

    jump scene10

# =======================================
# CENA 10 – Festa / Convívio
# =======================================
label scene10:

    scene bg school_yard with fade
    show lucas feliz at left
    show player normal at right

    $ _choices = ["Conversar sobre viagem", "Conversar sobre animais"]
    $ _actions = [
        Function(assign, "lucas_confidence", lucas_confidence + 1),
        Function(assign, "lucas_confidence", lucas_confidence + 1)
    ]
    call screen choice_screen

    jump scene11

# =======================================
# CENA 11 – Fim da manhã
# =======================================
label scene11:

    scene bg classroom with fade
    show lucas feliz at left
    show player normal at right

    narrator "O período da manhã termina. Lucas parece mais confiante do que no começo do dia."

    $ _choices = ["Conversar sobre o intervalo", "Planejar jogar à tarde"]
    $ _actions = [
        Function(assign, "lucas_confidence", lucas_confidence + 1),
        Function(assign, "lucas_confidence", lucas_confidence + 1)
    ]
    call screen choice_screen

    return
