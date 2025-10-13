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
image bg kitchen = "images/bg_kitchen.jpg"
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

    # Introdução narrativa
    narrator "Você conhece, tem um amigo ou é uma pessoa com Transtorno do Espectro Autista?"
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

    scene bg kitchen with fade
    show carmen normal at right
    show player normal at left

    c "Vem, [player_name], você vai se atrasar!"
    c "Bom dia! Não esqueça de levar seu lanche!"
    p "Não vou esquecer, valeu!"
    c "Eu estou indo trabalhar, não vá sem tomar seu café. Boa aula, tente não se atrasar."

    menu:
        "Pode deixar, mãe.":
            p "Pode deixar, mãe."
            c "E toma cuidado na rua!"
        "Não vou atrasar, vai ser tranquilo.":
            p "Não vou atrasar, vai ser tranquilo."
            c "'vai ser tranquilo' você sempre fala isso e sempre se atrasa."
            p "Eu não vou atrasar hoje, relaxa."
        "Vou pegar uma fruta e comer no caminho. Tô indo já, tchau!":
            p "Vou pegar uma fruta e comer no caminho. Tô indo já, tchau!"

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

    menu:
        "Conversar educadamente com Alicia":
            p "Ah, eu vou viajar essa semana, então só consigo pensar nisso."
            a "Que legal, eu vou viajar também com a família da minha namorada. Vai com alguém também?"
            p "Não, só minha família mesmo."
            $ alicia_follow = True
        "Ignorar Alicia":
            narrator "Você passa direto, sem responder."
            a "Ei, espera! Eu tô falando com você!"
            $ alicia_follow = False

    hide alicia
    jump scene3

label scene3:

    scene bg classroom with fade

    narrator "Você vê Lucas sentado sozinho na última cadeira."

    menu:
        "Acenar de longe":
            p "(acena)"
            show lucas feliz
            l "(sorri e acena de volta)"
            $ lucas_confidence += 1
        "Gritar 'oi'":
            p "Oi, Lucas!"
            show lucas pensativo
            l "(fica tímido, acena de longe)"

    # Reação da Alicia
    a "Estranho ver você cumprimentando ele assim… ele nunca fala com ninguém. Sempre é tão chato…"

    menu:
        "Ele é legal, Alicia. Só tem dificuldade em fazer amigos.":
            p "Ele é legal, só tem dificuldade em fazer amigos."
            a "Dificuldade para fazer amigos? Conta outra!"
            a "Que ele é autista! Olha só pra ele. Ele nem parece autista, só é esquisito."
            jump scene3_choice
        "Ele não é chato, só precisa de tempo para se abrir.":
            p "Ele não é chato, só precisa de tempo para se abrir."
            a "Claro né, [player_name]. Quem quer tentar ser amigo de alguém esquisito igual a ele?"
            jump scene3_choice

label scene3_choice:

    menu:
        "Sair de perto da Alicia":
            narrator "Você se afasta dela com irritação."
        "Isso é bullying, Alicia! O que você tem na cabeça pra pensar em algo assim?":
            p "Isso é bullying, Alicia! O que você tem na cabeça pra pensar em algo assim?"
            narrator "Você sai de perto logo em seguida."

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
    p "Você não me incomoda! É meu melhor amigo."
    l "Você também é meu melhor amigo."
    p "Viu só? Eu não te incomodo ou incomodo?"
    l "Às vezes..."
    narrator "Algumas pessoas autistas podem fazer comentários diretos e sinceros demais porque têm dificuldade em controlar os impulsos e filtrar o que dizem antes de falar."
    narrator "Isso não significa falta de educação ou consideração, mas uma característica da forma como processam e expressam seus pensamentos."
    p "Bom, mas você não me incomoda."
    l "Dúvido."
    p "Tô falando sério! E tenho certeza que não incomoda ela também."
    l "Sabe… eu queria falar com a Luana antes das férias."
    l "Ela… parece legal, às vezes pede meus lápis emprestados e…"
    l "Ela gosta de Batman. Acho que ninguém que gosta do Batman pode ser uma pessoa chata, né?"
    l "Mas, sei lá, eu fico nervoso só de pensar em ir lá falar com ela, sabe?"
    l "Ela tá sempre perto dos amigos e… Sei lá, sempre travo e acabo desistindo."

    menu:
        "Ela parece ser legal mesmo, você só vai saber se tentar conversar com ela.":
            p "Ela parece ser legal mesmo, você só vai saber se tentar conversar com ela."
            $ lucas_confidence += 1
            show lucas feliz
            l "Ok… vou tentar."
            narrator "Lucas ganha um pouco de confiança e se levanta para falar com Luana."
            narrator "Mas Matheus passa correndo e tromba de propósito em Lucas."
            narrator "Ele perde o equilíbrio, abaixa a cabeça e desiste."
            show lucas triste
            l "Acho que não era pra ser…"
            narrator "Pessoas no espectro autista podem se sentir muito desconfortáveis com mudanças inesperadas, pois precisam de previsibilidade pra se sentirem seguras."

        "Relaxa… só espera tomar coragem.":
            p "Relaxa… só espera tomar coragem."
            show lucas pensativo
            l "Hmm… valeu."
            narrator "Lucas se sente um pouco mais seguro, mas continua no lugar sem tentar se aproximar."

        "(Você apenas acena com a cabeça, em silêncio.)":
            p "(Você apenas acena com a cabeça, em silêncio.)"
            $ lucas_confidence -= 1
            show lucas triste
            l "É, melhor não tentar falar com ela… vou acabar passando vergonha."
            narrator "Lucas se fecha ainda mais, mostrando como o apoio do amigo é crucial."

    jump scene4


# =======================================
# CENA 4 – INTERVALO / DECISÃO-CHAVE
# =======================================
label scene4:

    scene bg school_yard with fade
    with dissolve
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

    menu:
        "Responder com sinceridade e empatia":
            p "Foi mal. Talvez eu erre às vezes tentando te proteger demais, mas é porque eu me importo."
            p "Eu sei que você aguenta muito mais do que imagina."
            p "Mas o jeito que as pessoas falam de você… (dá de ombros) Acho que eu só quero que você saiba que eu tô com você, cara."
            show lucas feliz
            $ lucas_confidence += 2
            l "(sorri timidamente) Eu não quero parecer ingrato. É só que eu quero que você saiba que eu não sou frágil assim, sei me defender e entender as coisas."

        "Tentar mudar o assunto para algo mais leve":
            p "Ei, ninguém é perfeito em conversar. Você já me viu falando com alguém? Eu sempre fico sem jeito também."
            show lucas pensativo
            $ lucas_confidence += 1
            l "(ri de leve) Talvez… é, talvez eu leve a sério demais. Mas ainda é complicado, sabe?"

        "Responder de forma defensiva":
            p "Nossa, eu não te trato como um brinquedo! Eu só tento ser um bom amigo."
            show lucas triste
            $ lucas_confidence -= 1
            l "(desvia o olhar) Tá, deixa quieto. Eu não devia ter falado nada."

    # Continuação da conversa sobre adotar um animal
    l "Enfim. Minha mãe conversou com a psicóloga e sugeriu que eu poderia adotar um animal de estimação…"
    l "Ela disse que me ajudaria a me sentir mais confiante, sei lá."

    menu:
        "Sim, vou com você para te ajudar a decidir.":
            p "Claro que sim, vou com você para te ajudar a decidir."
            show lucas feliz
            l "Obrigado! Vou avisar minha mãe."

        "Já sabe qual animal você quer?":
            p "Já sabe qual animal você quer?"
            show lucas pensativo
            l "Não sei, você pode me ajudar na hora."

    jump scene5



# =======================================
# CENA 5 – VISITA AO ABRIGO / FEIRA DE ADOÇÃO
# =======================================
label scene5:

    scene bg adoption_fair with fade
    with dissolve

    narrator "Você chega à feira de adoção junto com Lucas e a mãe dele."

    show thaynara feliz at left
    t "Obrigada por ter vindo, [player_name]. O Lucas falou que você gosta de animais."

    show player normal at right
    p "Eu gosto mesmo, tia."

    show lucas pensativo at center
    l "Esse lugar é muito grande, vocês não acham?"

    show thaynara feliz
    t "É porque ele é dividido em partes: tem cachorros, gatos, porquinhos-da-índia, coelhos…"

    l "Quero ver os…"

    # Mostrar imagens dos animais antes do menu
    show cat at center with fade
    show dog at right with fade

    menu:
        "Escolher o gato":
            $ chosen_pet = "cat"
            $ chosen_pet_name = "Fred"
            $ lucas_confidence += 2
            hide cat
            hide dog
            l "Vamos ver os gatos então."
            narrator "Lucas observa os animais, até encontrar um gato preto entre alguns outros. Ele se aproxima da gaiola e o gatinho se aproxima devagar, parecendo tímido."
            l "Olha só. O gatinho é tímido, mas parece que quer carinho."
            p "Parece estar esperando por você. Será que ele tem nome?"
            show thaynara normal
            t "Será que ele tem nome?"
            show trabalhador normal
            y "Não, não tem nome."
            l "Vou chamar ele de Fred."
            y "Fico feliz que queiram ele. Sabe, as pessoas não costumam querer os gatos pretos."
            p "Ué, por que?"
            y "Por causa daquela superstição de que gato preto traz azar. Fico feliz que ele finalmente tenha sido escolhido."
            show lucas feliz
            narrator "O gato ronrona com o carinho de Lucas."
            y "Parece que ele gostou de você."
            hide trabalhador
            show thaynara feliz
            t "Sabe, dizem que os gatos que escolhem seus donos e não o contrário."
            l "Como assim?"
            p "É, como assim?"
            t "É como se ele sentisse que você é a pessoa certa pra ele. Não é só você escolhendo, ele também te escolheu."
            show lucas feliz
            l "Então, acho que começamos uma amizade de verdade, né?"
            p "Pelo jeito, sim."

        "Escolher o cachorro":
            $ chosen_pet = "dog"
            $ chosen_pet_name = "Alfred"
            $ lucas_confidence += 2
            hide cat
            hide dog
            l "Vamos ver os cachorros então."
            narrator "Os três andam juntos vendo um monte de cachorros. Ao longe, Lucas se aproxima e vê um cão caramelo que parece ser mais velho. Ele abana o rabo empolgado assim que Lucas se aproxima."
            l "Oi, amigão… você quer brincar?"
            p "Parece que ele gosta de você!"
            l "Eu gosto dele também."
            show thaynara feliz
            t "Qual será o nome dele?"
            show trabalhador normal
            y "Chamamos ele de Totó. Ele tá com a gente há muito tempo, já é adulto. Muita gente quer adotar só os filhotes."
            l "Podemos mudar o nome dele?"
            y "Pode, mas talvez ele demore a se acostumar."
            show lucas feliz
            l "Alfred. Ele vai se chamar Alfred."
            p "Ótimo nome! Igual ao…"
            l "(interrompendo) Mordomo do Batman? Eu sei."
            p "Adorei."
            t "Vocês vão se divertir juntos. Ele adora companhia e é ótimo para se socializar."
            narrator "O cachorro late animado."
            l "Eu realmente gostei."

    narrator "A convivência com animais de estimação ajuda pessoas no espectro autista a desenvolverem habilidades sociais, emocionais e físicas."
    narrator "Estudos mostram que crianças e adolescentes com TEA que têm animais de estimação criam vínculos fortes, já que essa interação reduz a ansiedade e promove bem-estar."

    jump scene6



# =======================================
# CENA 6 – CARRO
# =======================================
label scene6:

    scene bg car_interior with fade
    with dissolve

    # Mostrar personagens no carro
    show thaynara feliz at left
    show player normal at right
    if chosen_pet == "cat":
        show lucas feliz at center
        show fred at center
    else:
        show lucas feliz at center
        show alfred at center

    l "Nunca pensei em ter um animal de estimação…"
    p "Eu tinha um hamster quando era criança, era legal."
    t "Eu lembro! Ele fugiu, né?"
    p "Fugiu…"
    l "(em tom de piada) Tomara que o [chosen_pet_name] não ouça isso e siga o exemplo do Jerry."
    p "Só não deixe a jaula dele aberta que tá tudo certo."
    l "(ri) No caso, a porta de casa, né?"
    t "(ri no banco da frente enquanto dirige até a casa do [player_name])"

    # Lucas segura o animal com cuidado
    if chosen_pet == "cat":
        l "Valeu por me acompanhar hoje. Sério, eu não sei o que faria sem você." 
        show fred at center
    else:
        l "Valeu por me acompanhar hoje. Sério, eu não sei o que faria sem você."
        show alfred at center

    p "(sorrindo) Imagina! Foi divertido. E eu adorei ele."
    l "(timidamente) Obrigado, nós agradecemos."
    p "Qualquer hora a gente joga ou passeia de novo, tá?"
    l "Combinado, e se você quiser adotar um animal também, ou, sei lá, só jogar papo fora antes de ir viajar, pode me chamar."
    p "Acho que só vai rolar quando eu voltar de viagem. Mas eu te ligo para a gente jogar junto."
    l "Beleza, falou!"
    p "Tchau!"

    # Momento visual: Player caminhando, Lucas acena
    scene bg street_day with fade
    show player normal at right
    if chosen_pet == "cat":
        show fred at right
    else:
        show alfred at right
    show lucas feliz at left

    narrator "Você começa a caminhar em direção à sua casa. Lucas acena, acariciando [chosen_pet_name], enquanto o animal se aninha em seus braços."

    jump scene7


# =======================================
# cena 7 dps da viagem
# =======================================
label scene7:

    # Cenário
    scene bg school_gate with fade
    with dissolve

    # Mostrar Lucas no portão
    if chosen_pet == "cat":
        show lucas feliz at center
        show fred_phone at right  # imagem do Fred no celular
    else:
        show lucas feliz at center
        show alfred_phone at right  # imagem do Alfred no celular

    narrator "Depois de alguns dias viajando com a família, [player_name] volta para a rotina. Enquanto caminhava para a escola, se perguntava como Lucas estaria. Afinal… seria possível que um animal de estimação pudesse mudar tanto uma pessoa?"

    l "(sorrindo) [player_name]! Você não sabe quanta coisa eu tenho pra te contar!"

    menu:
        "Sério? O que aconteceu?":
            p "Sério? O que aconteceu?"
            narrator "Lucas começa a falar com entusiasmo sobre o animal, contando pequenas histórias e aventuras que tiveram juntos."
            $ lucas_confidence += 1

        "Você parece diferente. Tá mais animado.":
            p "Você parece diferente. Tá mais animado."
            narrator "Lucas sorri, reconhece que mudou e liga isso ao bichinho. Ele parece mais confiante e feliz."
            $ lucas_confidence += 1

        "Você descobriu um quarto secreto na sua casa cheio de dinheiro? (brincando)":
            p "Você descobriu um quarto secreto na sua casa cheio de dinheiro?"
            l "(ri) Não, eu não te contaria isso, guardaria tudo para mim."
            narrator "Lucas ri da brincadeira, mantendo seu jeito tímido, mas mostrando leve descontração."

    jump scene8



# =======================================
# CENA 8 – Explicação da mudança
# =======================================
label scene8:

    if chosen_pet == "dog":
        l "Eu comecei a levar o Alfred no parque, né? No começo fiquei com medo de ficar deslocado lá, mas sabe o que aconteceu? Ele puxava tanta atenção que as pessoas vinham até mim. Eu conheci o Victor assim, ele também tem TEA, mas nível 2 de suporte. A gente se encontrou porque o Alfred não parava de latir para o cachorro dele."
    elif chosen_pet == "cat":
        l "Eu levei o Fred no veterinário, e lá conheci um cara chamado Victor. Ele estava com a mãe e o gato dele. A gente ficou conversando enquanto esperava, e foi… diferente. Quer dizer, ele também tem TEA, só que nível 2 de suporte. Então, sei lá, ele entendeu coisas de mim que às vezes você não entende. Tipo, quando eu não consigo responder rápido, ele não acha estranho."

    menu:
        "Que bom que você fez outro amigo!":
            p "Que bom que você fez outro amigo!"
            if chosen_pet == "dog":
                l "O melhor é que nossos amigos de quatro patas viraram amigos também."
            elif chosen_pet == "cat":
                l "Ele também curtiu o Fred, foi bem legal."

        "Eu tô com um pouco de ciúme, viu?":
            p "Eu tô com um pouco de ciúme, viu?"  # tom leve/brincadeira
            l "Relaxa, ninguém vai te substituir na minha vida."

        "E como ele é?":
            p "E como ele é?"
            l "Ah, o Victor faz equoterapia, o que ajuda muito no meu tratamento. Ele é bem legal e paciente."
    
    jump scene9 # prossiga para a próxima cena

# =======================================
# CENA 9 – INTERVALO NA ESCOLA
# =======================================
label scene9:

    scene bg school_yard with fade
    with dissolve

    narrator "Pátio da escola, alguns grupos de alunos conversando. Alicia e Nicole aparecem ao fundo rindo de algo."

    if chosen_pet == "dog":
        l "Olha, essa foi ontem! O Alfred quase derrubou o pote de ração. Minha mãe ficou muito brava, tipo, muito mesmo, mas foi engraçado."
    elif chosen_pet == "cat":
        l "Olha, essa foi ontem! O Fred quase derrubou o pote de ração. Minha mãe ficou muito brava, tipo, muito mesmo, mas foi engraçado."

    narrator "Enquanto os dois riem, Luana se aproxima."
    u "Oi, gente. Desculpa a intromissão, mas eu adoro animais e vi a foto de longe. Esse é seu [chosen_pet], Lucas?"

    narrator "Lucas fica nervoso, olha para você."

    menu:
        "Incentivar Lucas a responder sussurrando":
            p "Vai, conversa com ela, é sua chance."
            l "(respira fundo e sorri) É. Adotei ele nas férias. Você também tem um?"
            narrator "Início de uma conversa real entre Lucas e Luana. Ele se sente mais confiante."

        "Responder no lugar de Lucas":
            p "É sim, o nome dele é em referência ao Batman, sabe o Alfred…"
            l "(fica um pouco sem graça, mas continua) Pois é…"
            narrator "Lucas fica sem graça, mas Luana continua interessada e conversa com os dois."

        "Ficar quieto e observar":
            p "(Você apenas observa a situação.)"
            l "(olha timidamente e apenas acena)"
            narrator "Lucas trava e só responde com aceno. Luana sorri educadamente e vai embora, perdendo a oportunidade de socialização."

    jump scene10  # Próxima cena



# =======================================
# cena10: SALA DE BIOLOGIA (MATHEUS)
# =======================================
label scene10:

    scene bg classroom with fade
    with dissolve

    show zacarias normal at center

    z "Turma, vamos começar a aula de hoje com algo leve. Quero que cada um diga, em poucas palavras, algo que aprendeu e viveu nas férias."

    show alicia feliz at right
    a "Eu viajei com a minha namorada e conheci lugares incríveis. Foi maravilhoso!"

    show nicole feliz at left
    n "Ah, eu fui a muitas festas… nem lembro de tudo, mas foi divertido."

    show lucas pensativo at center
    z "Ótimo. E você, Lucas?"

    l "(hesitante, respirando fundo) Eu… eu adotei um [chosen_pet_name]. Fui a parques, conheci pessoas novas e até fiz alguns amigos. Acho que aprendi bastante nesses dias."

    narrator "A sala fica em silêncio por um instante. Alguns colegas cochicham."

    show zacarias bravo at left
    z "Já chega! Não quero ouvir sussurros sobre isso, aqui na E.E Stefani Joanne G. Lopes Luz não aceitamos esse comportamento!"

    show matheus normal at left
    m "Que comportamento? Só estamos surpreso porque agora ele até fala, que evolução…"

    menu:
        "Pelo menos o Lucas tem alguma coisa boa pra contar, né?":
            p "Pelo menos o Lucas tem alguma coisa boa pra contar, né?"
            narrator "Matheus fica sem graça, alguns colegas riem."
            l "E é verdade. Eu aprendi muito cuidando dele. Não é pouca coisa, não."
            m "(revira os olhos) Você podia aprender com ele."
            narrator "Matheus finge não ligar, mas você percebe que aquilo afetou ele.."
            l "Pois é. Enquanto eu tava aprendendo, você só ficou zoando. Acho que prefiro meu jeito."
            z "Muito bem. Todos merecem respeito. Próximo."

        "Ignorar":
            narrator "Matheus e Nicole riem baixinho."
            l "Você pode achar engraçado, mas cuidar de um animal é responsabilidade. Eu aprendi mais nessas férias do que você imagina."
            u "Concordo. Adotar um animal é uma atitude ótima. Parabéns, Lucas."
            l "Obrigado."
            z "Excelente colocação, Lucas. Todos aprendemos de formas diferentes."

        "Deixar Lucas se defender sozinho":
            l "(respira fundo, olhando para Matheus) Você pode rir, mas eu aprendi muito mais cuidando de um animal do que você aprendeu zombando dos outros."
            narrator "A sala reage com surpresa. Alguns murmuram 'boa!'. Matheus fica vermelho, sem saber o que responder."
            z "Excelente colocação, Lucas. Todos aprendemos de formas diferentes."

    jump scene11



# =======================================
# CENA 11 – CORREDOR APÓS A AULA DE BIOLOGIA
# =======================================
label scene11:

    scene bg school_hall with fade
    with dissolve

    show lucas pensativo at center
    show player normal at left

    l "Você percebeu? Eu falei na frente da sala toda. E… não foi tão ruim assim."

    menu:
        "Você mandou muito bem, eu sabia que conseguiria.":
            p "Você mandou muito bem, eu sabia que conseguiria."
            show lucas feliz
            narrator "Lucas sorri orgulhoso."

        "E o melhor é que o Matheus ficou sem graça.":
            p "E o melhor é que o Matheus ficou sem graça."
            show lucas rindo
            narrator "Lucas ri pela primeira vez de uma provocação envolvendo Matheus."

    l "Hoje foi diferente. Tipo, eu me sinto diferente. E eu sei que não foi só por causa do [chosen_pet] foi porque eu não me senti sozinho."

    menu:
        "Eu sempre vou estar aqui, mas você provou que pode se virar também e isso é muito importante.":
            p "Eu sempre vou estar aqui, mas você provou que pode se virar também e isso é muito importante."
            show lucas feliz

        "Viu? As pessoas só precisavam conhecer o verdadeiro Lucas.":
            p "Viu? As pessoas só precisavam conhecer o verdadeiro Lucas."
            show lucas feliz

        "Tá preparado pra próxima? Porque agora não tem mais volta!":
            p "Tá preparado pra próxima? Porque agora não tem mais volta!"
            show lucas rindo
            narrator "Lucas ri alto."

    narrator "Naquele semestre, Lucas deu seus primeiros passos para fora da zona de isolamento que sempre o cercou. Um novo amigo, um animal de estimação, e pequenas doses de coragem abriram portas que antes pareciam inalcançáveis. Ele ainda tinha desafios — muitos — mas agora sabia que não estava sozinho."

    menu:
        "Dar tchau com um simples aceno":
            p "Tchau!"
            show lucas feliz
            narrator "Lucas retribui, sorrindo discretamente."

        "Dar um abraço rápido de amizade":
            p "Abraço!"
            show lucas feliz
            narrator "Lucas se surpreende, mas corresponde."

        "Brincar dizendo 'Até amanhã, Batman'":
            p "Até amanhã, Batman!"
            show lucas feliz
            narrator "Lucas ri genuinamente, marcando um momento de cumplicidade."

    return
