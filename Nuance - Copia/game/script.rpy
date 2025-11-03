# ======================================================
# CONFIGURAÇÃO DE AUTO VOICE E PERSONAGENS
# ======================================================

# Ativa o sistema de auto voice (Ren'Py vai procurar os áudios automaticamente)
define config.auto_voice = "audio/voices"
define config.has_voice = True

# ------------------------------------------------------
# Personagens do jogo (cores harmoniosas com #B78AE0)
# ------------------------------------------------------

define narrator = Character(None, color="#FFFFFF")   # narração sem nome
define p = Character("[player_name]", color="#000000")  # jogador (nome dinâmico)

define c = Character("Carmen", color="#ff1389")          
define a = Character("Alicia", color="#9C27B0")         
define l = Character("Lucas", color="#54008f")           
define t = Character("Thaynara", color="#cd0174")     
define m = Character("Matheus", color="#001b91")       
define n = Character("Nicole", color="#9a0069", )         
define z = Character("Professor Zacarias", color="#5d00ff") 
define u = Character("Luana", color="#9700a5", voice_tag="luana")          
define y = Character("Trabalhador da feira de adoção", color="#1f004a")



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


init python:
    # Função para mostrar escolhas no meio da tela
    def middle_choice(choices, actions):
        result = renpy.call_screen("middle_choice_screen", choices=choices)
        if result is not None:
            actions[result]()

# Screen para mostrar escolhas centralizadas
screen middle_choice_screen(choices):
    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5
        xmaximum 600
        ymaximum 400
        background Frame(Solid("#00000080"), 10, 10)  # Fundo semi-transparente

        vbox:
            spacing 20
            for i, choice in enumerate(choices):
                textbutton choice action Return(i) xalign 0.5 yalign 0.5


# =======================================
# LABEL INICIAL
# =======================================
label start:
    stop music fadeout 1.0
    play music "audio/musics/jogo.mp3" fadein 1.0
    scene bg_room with fade
    show player normal at left

    p "Você conhece, tem um amigo ou é uma pessoa com Transtorno do Espectro Autista?"
    p "Bom, tenho um amigo… e diferente do que muitas pessoas pensam, isso não é um empecilho para nossa amizade."
    p "Nós crescemos juntos, meus pais e a mãe dele são amigos desde a adolescência. Nós jogamos, estudamos e saímos juntos..."
    p "Mas as coisas não são tão simples para ele quanto são para mim."
    p "Por ter o nível 1 do TEA, muitas pessoas não enxergam que isso é uma condição e não apenas parte de sua personalidade."
    p "Além disso, ele não consegue socializar com facilidade… e eu sou a única pessoa que ele tem amizade."
    narrator "Embarquem nessa jornada juntos."

    $ player_name = renpy.input("Escolha o nome do seu personagem:").strip()
    if player_name == "":
        $ player_name = "Ariel"

    jump scene1

# =======================================
# CENA 1 – QUARTO
# =======================================
label scene1:

    scene bg_room with fade
    show carmen normal at right
    show player normal at left

    c "Vem, [player_name], você vai se atrasar!"
    c "Bom dia! Não esqueça de levar seu lanche!"
    c "Eu estou indo trabalhar, não vá sem tomar seu café. Boa aula, tente não se atrasar."

    $ choices = [
        "Pode deixar, mãe.",
        "Não vou atrasar, vai ser tranquilo.",
        "Vou pegar uma fruta e comer no caminho. Tô indo já, tchau!"
    ]
    $ actions = [
        lambda: p("Pode deixar, mãe."),
        lambda: p("Não vou atrasar, vai ser tranquilo."),
        lambda: p("Vou pegar uma fruta e comer no caminho. Tô indo já, tchau!")
    ]
    $ middle_choice(choices, actions)

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

    $ choices = ["Conversar educadamente com Alicia", "Ignorar Alicia"]
    $ actions = [
        lambda: renpy.store.__setattr__("alicia_follow", True),
        lambda: renpy.store.__setattr__("alicia_follow", False)
    ]
    $ middle_choice(choices, actions)

    hide alicia
    jump scene3

# =======================================
# CENA 3 – LUCAS NA SALA
# =======================================
label scene3:

    scene bg classroom with fade
    narrator "Você vê Lucas sentado sozinho na última cadeira."

    $ choices = ["Acenar de longe", "Gritar 'oi'"]
    $ actions = [
        lambda: renpy.store.__setattr__("lucas_confidence", lucas_confidence + 1),
        lambda: renpy.store.__setattr__("lucas_confidence", lucas_confidence)
    ]
    $ middle_choice(choices, actions)

    a "Estranho ver você cumprimentando ele assim… ele nunca fala com ninguém. Sempre é tão chato…"

    $ choices = [
        "Ele é legal, Alicia. Só tem dificuldade em fazer amigos.",
        "Ele não é chato, só precisa de tempo para se abrir."
    ]
    $ actions = [
        lambda: renpy.store.__setattr__("lucas_confidence", lucas_confidence + 1),
        lambda: renpy.store.__setattr__("lucas_confidence", lucas_confidence)
    ]
    $ middle_choice(choices, actions)

    jump scene3_choice

label scene3_choice:


    a "Sei lá. É estranho. Ele age estranho e fala que é culpa do autismo, mas ele nem parece ser autista."

    $ choices = [
        "Sair de perto da Alicia",
        "E pessoas com TEA tem aparencia? Acorda para a vida, Alicia! Isso é bullying."
    ]
    $ actions = [
        lambda: renpy.store.__setattr__("lucas_confidence", lucas_confidence),
        lambda: renpy.store.__setattr__("lucas_confidence", lucas_confidence + 1)
    ]
    $ middle_choice(choices, actions)

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

    $ choices = [
        "Ela parece ser legal mesmo, você só vai saber se tentar conversar com ela.",
        "Relaxa… só espera tomar coragem.",
        "(Você apenas acena com a cabeça, em silêncio.)"
    ]
    $ actions = [
        lambda: renpy.store.__setattr__("lucas_confidence", lucas_confidence + 1),
        lambda: renpy.store.__setattr__("lucas_confidence", lucas_confidence),
        lambda: renpy.store.__setattr__("lucas_confidence", lucas_confidence - 1)
    ]
    $ middle_choice(choices, actions)

    jump scene4

# =======================================
# CENA 4 – INTERVALO / DECISÃO-CHAVE
# =======================================
label scene4:

    scene bg school_yard with fade
    show lucas normal at left
    show player normal at right
    show lucas pensativo

    narrator "Pátio da escola, sol da manhã, alguns alunos conversando ao fundo. Você e Lucas estão sentados em um banco."

    l "(olhando para o chão) Sabe, eu me sinto sozinho às vezes."
    p "Você não está sozinho, eu tô aqui."
    l "Eu sei, mas é insuportável isso."
    p "Eu estar aqui?"
    l "Não e Sim. Quer dizer, ter amizade com você é ótimo. Mas eu não queria ter amizade só com você."
    l "Tipo, eu já não consigo conversar com as pessoas direito e, às vezes, quando vou conversar parece que a pessoa tem medo, dó, não sei, de mim."
    l "Eu me sinto errado, saca? Às vezes até você me trata como se eu fosse um brinquedo prestes a quebrar."

    narrator "Você fica em silêncio por um instante, pensando no que dizer..."

    $ choices = [
        "Responder com sinceridade e empatia",
        "Tentar mudar o assunto para algo mais leve",
        "Responder de forma defensiva"
    ]
    $ actions = [
        lambda: renpy.store.__setattr__("lucas_confidence", lucas_confidence + 2),
        lambda: renpy.store.__setattr__("lucas_confidence", lucas_confidence + 1),
        lambda: renpy.store.__setattr__("lucas_confidence", lucas_confidence - 1)
    ]
    $ middle_choice(choices, actions)

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

    # Escolha do jogador
    $ choices = ["Ajudar Lucas a escolher um gato", "Ajudar Lucas a escolher um cachorro"]
    $ choice_result = renpy.call_screen("middle_choice_screen", choices)

    # Gato
    if choice_result == 0:
        $ chosen_pet = "cat"

        "Eles vão andando em direção aos animais escolhidos."

        show cat at center with fade
        "Lucas observa os animais, até encontrar um gato preto entre alguns outros (listrados, laranjas, etc.). Ele se aproxima da gaiola e o gatinho se aproxima devagar, como se estivesse com medo."

        l "Olha só. O gatinho é tímido, mas parece que quer carinho."
        p "Parece estar esperando por você. Será que ele tem nome?"
        t "Será que ele tem nome?"
        y "Não, não tem nome."
        l "Vou chamar ele de Fred."
        y "Fico feliz que queiram ele. Sabe, as pessoas não costumam querer os gatos pretos."
        l "Ué, por que?"
        y "Por causa daquela superstição de que gato preto traz azar. As pessoas realmente acreditam e evitam eles a todo custo. Fico feliz que ele finalmente tenha sido escolhido."
        "O gato ronrona com o carinho de Lucas."
        y "Parece que ele gostou de você."
        hide m with fade
        t "Sabe, dizem que os gatos que escolhem seus donos e não o contrário."
        l "Como assim?"
        p "É, como assim?"
        t "É como se ele sentisse que você é a pessoa certa pra ele. Não é só você escolhendo, ele também te escolheu."
        l "Então, acho que começamos uma amizade de verdade, né?" 
        p "Pelo jeito, sim." 

    # Cachorro
    elif choice_result == 1:
        $ chosen_pet = "dog"

        "Os três andam juntos vendo um monte de cachorros. Ao longe, Lucas se aproxima e vê um cão caramelo que parece ser mais velho. Ele abana o rabo empolgado assim que Lucas se aproxima."

        l "Oi, amigão… você quer brincar?"
        p "Parece que ele gosta de você!"
        l "Eu gosto dele também."
        t "Qual será o nome dele?"
        y "Chamamos ele de Totó mesmo. Ele tá com a gente há muito tempo, já é adulto. Muita gente quer adotar só os filhotes."
        l "Podemos mudar o nome dele?"
        y "Poder pode, mas talvez ele demore a se acostumar."
        l "Alfred. Ele vai se chamar Alfred."
        p "Ótimo nome! Igual ao…"
        l "Mordomo do Batman? Eu sei."
        p "Adorei."
        t "Vocês vão se divertir juntos. Ele adora companhia e é ótimo para se socializar."
        "O cachorro late animado."
        l "Eu realmente gostei."

    # Momento visual final
    if chosen_pet == "cat":
        show fred_holding at center with fade
    else:
        show alfred_running at center with fade

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
        $ pet_name = "Fred"
    else:
        show lucas feliz at center
        show alfred at center
        $ pet_name = "Alfred"

    l "Nunca pensei em ter um animal de estimação…"
    p "Eu tinha um hamster quando era criança, era legal."
    t "Eu lembro! Ele fugiu né?"
    p "Fugiu…"
    l "(em tom de piada) Tomara que o [pet_name] não ouça isso e siga o exemplo do Jerry."
    p "Só não deixe a jaula dele aberta que tá tudo certo."
    l "No caso, a porta de casa né? (ri)"
    "Thaynara ri no banco da frente enquanto dirige até a casa do jogador."

    l "(segurando [pet_name] com cuidado) Valeu por me acompanhar hoje. Sério, eu não sei o que faria sem você."
    p "(sorrindo) Imagina! foi divertido. E eu adorei ele."
    l "(timidamente) Obrigado, nós agradecemos."
    p "Qualquer hora a gente joga ou passeia de novo, tá?"
    l "Combinado e se você quiser adotar um animal também, ou, sei lá, só jogar papo fora antes de ir viajar, pode me chamar."
    p "Acho que só vai rolar quando eu voltar de viagem. Mas eu te ligo para a gente jogar junto."
    l "Beleza, falou!"
    p "Tchau!"

    "Lucas acena, acariciando [pet_name], e o jogador começa a caminhar em direção à sua casa."

    # Momento visual final
    if chosen_pet == "cat":
        show fred_walking at center with fade
    else:
        show alfred_walking at center with fade

    "O jogador caminha pela calçada, Lucas acenando ao fundo, [pet_name] aninhado nos braços ou correndo animado ao lado dele."

    jump scene7

# =======================================
# CENA 7 – DEPOIS DA VIAGEM
# =======================================
label scene7:

    scene bg school_gate with fade

    narrator "Algumas semanas haviam se passado desde o dia em que Lucas adotou seu novo amigo, as férias já haviam acabado e era o primeiro dia de aula de Agosto."

    if chosen_pet == "cat":
        show lucas feliz at center
        show fred_phone at right
    else:
        show lucas feliz at center
        show alfred_phone at right

    $ choices = [
        "Sério? O que aconteceu?",
        "Você parece diferente. Tá mais animado.",
        "Você descobriu um quarto secreto na sua casa cheio de dinheiro? (brincando)"
    ]
    $ actions = [
        lambda: renpy.store.__setattr__("lucas_confidence", lucas_confidence + 1),
        lambda: renpy.store.__setattr__("lucas_confidence", lucas_confidence + 1),
        lambda: renpy.store.__setattr__("lucas_confidence", lucas_confidence)
    ]
    $ middle_choice(choices, actions)

    jump scene8

# =======================================
# CENA 8 – Explicação da mudança
# =======================================
label scene8:

    if chosen_pet == "dog":
        l "Eu comecei a levar o Alfred no parque, né? No começo fiquei com medo de ficar deslocado lá, mas sabe o que aconteceu? Ele puxava tanta atenção que as pessoas vinham até mim. Eu conheci o Victor assim, ele também tem TEA, mas nível 2 de suporte. A gente se encontrou porque o Alfred não parava de latir para o cachorro dele."
    else:
        l "Eu levei o Fred no veterinário, e lá conheci um cara chamado Victor. Ele estava com a mãe e o gato dele. A gente ficou conversando enquanto esperava, e foi… diferente. Quer dizer, ele também tem TEA, só que nível 2 de suporte. Então, sei lá, ele entendeu coisas de mim que às vezes você não entende. Tipo, quando eu não consigo responder rápido, ele não acha estranho."

    # Escolha do jogador
    $ choices = [
        "Que bom que você fez outro amigo!",
        "Eu tô com um pouco de ciúme, viu?",
        "E como ele é?"
    ]
    $ choice_result = renpy.call_screen("middle_choice_screen", choices)

    if choice_result == 0:
        # Impacto 1
        l "O melhor é que nossos amigos de quatro patas viraram amigos também."
    elif choice_result == 1:
        # Impacto 2
        l "Relaxa, ninguém vai te substituir na minha vida."
    elif choice_result == 2:
        # Impacto 3
        l "O Victor faz equoterapia, o que ajuda muito no meu tratamento."

    jump scene9


# =======================================
# CENA 9 – PÁTIO / INTERAÇÃO COM LUANA
# =======================================
label scene9:

    scene bg school_courtyard with fade

    show lucas feliz at left
    show player normal at right
    show luana normal at right

    if chosen_pet == "cat":
        $ pet_name = "Fred"
    else:
        $ pet_name = "Alfred"

    l "Olha, essa foi ontem! O [pet_name] quase derrubou o pote de ração. Minha mãe ficou muito brava, tipo, muito mesmo, mas foi engraçado."

    "Enquanto os dois riem, Luana se aproxima."

    u "Oi, gente. Desculpa a intromissão, mas eu adoro animais e vi a foto de longe. Esse é seu [pet_name], Lucas?"

    "Lucas fica nervoso e olha para você."

    # Escolha do jogador
    $ choices = [
        "Incentivar Lucas a responder sussurrando: 'Vai, conversa com ela, é sua chance'",
        "Responder no lugar de Lucas: 'É sim, o nome dele é em referência ao Batman, sabe o Alfred..'",
        "Ficar quieto e observar"
    ]
    $ choice_result = renpy.call_screen("middle_choice_screen", choices)

    if choice_result == 0:
        # Impacto 1
        l "É. Adotei ele nas férias. Você também tem um?"
        "Início de uma conversa real entre Lucas e Luana."
    elif choice_result == 1:
        # Impacto 2
        l "É sim, o nome dele é [pet_name]."
        "Lucas fica sem graça, mas Luana continua interessada e conversa com os dois."
    elif choice_result == 2:
        # Impacto 3
        l "(acena timidamente)"
        "Luana sorri educadamente e vai embora. Perda de oportunidade de socialização."

    jump scene10

# =======================================
# CENA 10 – AULA / Defesa de Lucas
# =======================================
label scene10:

    scene bg classroom with fade

    show lucas feliz at left
    show player normal at right
    show alicia feliz at center
    show nicole normal at right

    p "..."  # Placeholder caso queira narrar o ambiente

    z "Turma, vamos começar a aula de hoje com algo leve. Quero que cada um diga, em poucas palavras, algo que aprendeu e viveu nas férias."

    a "Eu viajei com a minha namorada e conheci lugares incríveis. Foi maravilhoso!"
    n "Ah, eu fui a muitas festas… nem lembro de tudo, mas foi divertido."

    z "Ótimo. E você, Lucas?"
    l "(hesitante, respirando fundo) Eu… eu adotei um [pet_name]. Fui a parques, conheci pessoas novas e até fiz alguns amigos. Acho que aprendi bastante nesses dias."

    "A sala fica em silêncio por um instante. Alguns colegas cochicham."

    z "Já chega! Aqui na Escola Estadual Stefani Joanne G. Lopes Luz não aceitamos esse tipo de conduta com nenhum estudante!"
    m "(baixo, debochado) Que conduta? Só estamos surpresos que agora ele fala até de [pet_name], que evolução…"

    # Escolha do jogador para responder a Matheus
    $ choices = [
        "Pelo menos ele tem alguma coisa boa pra contar, né?",
        "Você podia aprender com ele.",
        "Ignorar"
    ]
    $ choice_result = renpy.call_screen("middle_choice_screen", choices)

    if choice_result == 0:
        l "E é verdade. Eu aprendi muito cuidando dele. Não é pouca coisa, não."
        "Lucas se sente apoiado e ainda mais confiante por complementar a defesa do amigo."
        z "Muito bem. Todos merecem respeito. Próximo."
    elif choice_result == 1:
        l "(respira fundo, encarando Matheus) Pois é. Enquanto eu tava aprendendo, você só ficou zoando. Acho que prefiro meu jeito."
        "A sala se cala, impressionada."
        z "Muito bem. Todos merecem respeito. Próximo."
    elif choice_result == 2:
        l "(segurando firme o caderno e olhando para Matheus) Você pode achar engraçado, mas cuidar de um animal é responsabilidade. Eu aprendi mais nessas férias do que você imagina."
        "Luana reforça logo em seguida: 'Concordo. Adotar um animal é uma atitude ótima. Parabéns, Lucas.'"
        "Lucas fica surpreso, mas sorri tímido, agradecido."
        z "Excelente colocação, Lucas. Todos aprendemos de formas diferentes."


    jump scene11


# =======================================
# CENA 11 – Fim da manhã
# =======================================
label scene11:

    scene bg classroom with fade

    if chosen_pet == "cat":
        $ pet_name = "Fred"
    else:
        $ pet_name = "Alfred"

    show lucas feliz at left
    show player normal at right

    narrator "O período da manhã termina. Lucas parece mais confiante do que no começo do dia."

    # Escolha do jogador sobre a manhã
    $ choices = ["Conversar sobre o intervalo", "Planejar jogar à tarde"]
    $ choice_result = renpy.call_screen("middle_choice_screen", choices)
    $ lucas_confidence += 1


    "A turma sai para o intervalo. Lucas caminha ao lado do jogador, visivelmente mais leve depois da participação."

    l "(tímido, mas sorridente) Você percebeu? Eu falei na frente da sala toda. E… não foi tão ruim assim."

    # Escolha de resposta do jogador
    $ choices = [
        "Você mandou muito bem, eu sabia que conseguiria.",
        "E o melhor é que o Matheus ficou sem graça."
    ]
    $ choice_result = renpy.call_screen("middle_choice_screen", choices)

    if choice_result == 0:
        "Lucas sorri orgulhoso, confiança reforçada."
    elif choice_result == 1:
        "Lucas ri pela primeira vez de uma provocação envolvendo Matheus."

    l "(segurando a mochila e olhando para frente) Hoje foi diferente. Tipo, eu me sinto diferente. E eu sei que não foi só por causa do [pet_name], foi porque eu não me senti sozinho."

    $ choices = [
        "Eu sempre vou estar aqui, mas você provou que pode se virar também e isso é muito importante.",
        "Viu? As pessoas só precisavam conhecer o verdadeiro Lucas."
    ]
    $ choice_result = renpy.call_screen("middle_choice_screen", choices)

    if choice_result == 0:
        "Lucas sente orgulho de si mesmo, equilíbrio entre apoio e independência."
    elif choice_result == 1:
        "Lucas sente que finalmente foi enxergado."

    l "(tom leve) Tá preparado pra próxima? Porque agora não tem mais volta!"
    "Lucas ri alto, mostrando um lado descontraído raramente visto."

    narrator "Naquele semestre, Lucas deu seus primeiros passos para fora da zona de isolamento que sempre o cercou. Um novo amigo, um animal de estimação, e pequenas doses de coragem abriram portas que antes pareciam inalcançáveis. Ele ainda tinha desafios — muitos — mas agora sabia que não estava sozinho."

    # Última escolha simbólica do jogador
    $ choices = [
        "Dar tchau com um simples aceno",
        "Dar um abraço rápido de amizade",
        "Brincar dizendo 'Até amanhã, Batman'"
    ]
    $ choice_result = renpy.call_screen("middle_choice_screen", choices)

    if choice_result == 0:
        "Lucas retribui, sorrindo discretamente."
    elif choice_result == 1:
        "Lucas se surpreende, mas corresponde ao abraço."
    elif choice_result == 2:
        "Lucas ri genuinamente, marcando um momento de cumplicidade."

    # Tela final com ilustração
    scene bg ending with fade
    show lucas feliz at left
    show player normal at right
    if chosen_pet == "cat":
        show fred at center
    else:
        show alfred at center

    narrator "Amizade, empatia e paciência podem transformar a forma como enxergamos o mundo. Para Lucas, o futuro já não parecia tão assustador."

    return
