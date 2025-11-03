################################################################################
## Inicialização
################################################################################

init offset = -1


################################################################################
## Estilos
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


# Tela genérica de botão voltar
screen back_button(title_text=""):
    
    hbox:
        xalign 1.0      # Alinha à direita
        yalign 0.02     # Pequeno espaçamento do topo
        spacing 20

        # Botão voltar
        textbutton _("Voltar"):
            style "return_button"
            action Return()

        # Título do menu (opcional)
        if title_text != "":
            label title_text:
                style "menu_title"




################################################################################
## Telas no jogo
################################################################################


## Diga a tela #################################################################
##
## A tela say é usada para exibir o diálogo para o jogador. Ela recebe dois
## parâmetros, who e what, que são o nome do personagem que fala e o texto a ser
## exibido, respectivamente. (O parâmetro who pode ser None (Nenhum) se nenhum
## nome for fornecido).
##
## Essa tela deve criar um texto exibível com o id "what", pois o Ren'Py o
## utiliza para gerenciar a exibição de texto. Ela também pode criar exibíveis
## com id "who" e id "window" para aplicar propriedades de estilo.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Se houver uma imagem lateral, exiba-a acima do texto. Não exiba na
    ## variante do telefone - não há espaço.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Disponibilize a caixa de nome para estilização por meio do objeto Character.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Tela de entrada #############################################################
##
## Essa tela é usada para exibir renpy.input. O parâmetro prompt é usado para
## passar um prompt de texto.
##
## Essa tela deve criar um displayable de entrada com id "input" para aceitar
## os vários parâmetros de entrada.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Tela de escolha #############################################################
##
## Essa tela é usada para exibir as opções no jogo apresentadas pela instrução
## de menu. O único parâmetro, itens, é uma lista de objetos, cada um com campos
## de legenda e ação.
##
## https://www.renpy.org/doc/html/screen_special.html#choice
init python:
    # Lista de imagens da galeria
    gallery_images = [
        {"title": "Cena 1", "file": "images/bg1.jpg", "unlocked": True},
        {"title": "Cena 2", "file": "images/bg2.jpg", "unlocked": False},
        {"title": "Cena 3", "file": "images/bg3.jpg", "unlocked": True},
    ]

    # Calcula quantas linhas são necessárias para o grid de 2 colunas
    gallery_rows = (len(gallery_images) + 1) // 2

screen gallery():

    tag menu

    frame:
        style "gallery_frame"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5

            label "Galeria" style "gallery_title"

            # Grid de 2 colunas, linhas calculadas
            grid 2 gallery_rows xspacing 20 yspacing 20:

                for img in gallery_images:
                    if img["unlocked"]:
                        textbutton img["title"]:
                            action Show("gallery_view", img_file=img["file"])
                            style "gallery_button"
                    else:
                        textbutton img["title"]:
                            action Null()  # bloqueado
                            sensitive False  # desativa clique
                            style "gallery_locked_button"

            # Botão de voltar
            textbutton "Voltar":
                action Return()
                style "gallery_back_button"

##############################
# ESTILOS ACESSÍVEIS TEA     #
##############################

# Caixa que agrupa os botões de escolha
style choice_vbox:
    xalign 0.5          # centralizado horizontalmente
    yalign 0.5          # centralizado verticalmente
    spacing 30          # espaço maior entre os botões
    padding (20, 20)

# Botões de escolha
style choice_button:
    background Frame(Solid("#B78AE0"), 25, 25)      # lilás
    hover_background Frame(Solid("#FF69B4"), 25, 25)  # rosa ao passar mouse
    xminimum 550           # largura maior
    yminimum 80            # altura maior
    padding (20, 15)
    xalign 0.5
    outlines [(2, "#000000", 0, 0)]                 # contorno preto
    hover_outlines [(3, "#FFFFFF", 0, 0)]          # contorno branco ao passar mouse
    focus_mask True

    # Texto do botão
    font "DejaVuSans.ttf"
    size 32                  # maior para visibilidade
    bold True
    color "#FFFFFF"          # texto branco
    hover_color "#FFFF00"    # amarelo de alto contraste ao hover




## Tela do menu rápido #########################################################
##
## O menu rápido é exibido no jogo para fornecer acesso fácil aos menus fora do
## jogo.

screen quick_menu():

    ## Certifique-se de que isso apareça na parte superior de outras telas.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("Voltar") action Rollback()
            textbutton _("Histórico") action ShowMenu('history')
            textbutton _("Pular") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Automotivo") action Preference("auto-forward", "toggle")
            textbutton _("Salvar") action ShowMenu('save')
            textbutton _("Q.Salvar") action QuickSave()
            textbutton _("Q. Carga") action QuickLoad()
            textbutton _("Preferências") action ShowMenu('preferences')


## Esse código garante que a tela quick_menu seja exibida no jogo, sempre que o
## jogador não tiver ocultado explicitamente a interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Telas do menu principal e do menu do jogo
################################################################################

## Tela de navegação ###########################################################
##
## Essa tela está incluída nos menus principal e do jogo e fornece navegação
## para outros menus e para iniciar o jogo.

screen navigation():

    frame:
        background Frame(Solid("#F2BDBD"), 25, 25)
        xalign 0.03
        yalign 0.5
        xsize 320
        yfill True
        padding (30, 30)

        vbox:
            style_prefix "navigation"
            spacing 15
            xalign 0.5

            if main_menu:
                textbutton _("Início") action Start()
            else:
                textbutton _("Histórico") action ShowMenu("history")
                textbutton _("Salvar") action ShowMenu("save")

            textbutton _("Carga") action ShowMenu("load")
            textbutton _("Preferências") action ShowMenu("preferences")

            if _in_replay:
                textbutton _("Fim da reprodução") action EndReplay(confirm=True)
            elif not main_menu:
                textbutton _("Menu principal") action MainMenu()

            textbutton _("Sobre") action ShowMenu("about")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                textbutton _("Ajuda") action ShowMenu("help")

            if renpy.variant("pc"):
                textbutton _("Sair") action Quit(confirm=not main_menu)


###########################
# Estilos personalizados  #
###########################

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    background Frame(Solid("#9373D9"), 20, 20)
    hover_background Frame(Solid("#FF69B4"), 20, 20)
    xminimum 250
    yminimum 120
    padding (15, 10)
    outlines [(2, "#000000", 0, 0)]
    hover_outlines [(2, "#FFFFFF", 0, 0)]
    xalign 0.5

style navigation_button_text:
    color "#FFFFFF"
    hover_color "#FFFFFF"
    font "DejaVuSans.ttf"
    size 24
    bold True
    text_align 0.5
    xalign 0.5

## Tela do menu principal ######################################################
##
## Usado para exibir o menu principal quando o Ren'Py é iniciado.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

# Definição do Circle (DynamicDisplayable)
# ======= DEFINIÇÃO DO CÍRCULO =======
# Definição do Circle (DynamicDisplayable)
screen main_menu():
    tag menu

    # Fundo
    add "#F2BDBD"

    # Círculos roxos usando imagens prontas de círculo
    add "images/circle.png" xalign -1.2 yalign 0.3 zoom 4.0
    add "images/circle.png" xalign 2.1 yalign 0.3 zoom 4.0

    # Personagem à esquerda
    add "images/player.png" xalign -0.3 yalign 0.3 zoom 5.0
    
    # Personagem à direita
    add "images/lucas.png" xalign 1.2 yalign 0.3 zoom 5.0


    # Logo
    add "images/logo.png" xalign 0.5 yalign -0.3 zoom 0.5

    # Botões locais
    vbox:
        xalign 0.5
        yalign 0.8
        spacing 15

        textbutton "Iniciar" action Start() style "menu_button" text_style "menu_button_text"
        textbutton "Carregar Jogo" action ShowMenu("load") style "menu_button"
        textbutton "Configurações" action ShowMenu("preferences") style "menu_button"
        textbutton "Galeria" action ShowMenu("gallery") style "menu_button"
        textbutton "Sair" action Quit(confirm=True) style "menu_button"

        

style menu_button:
    background "#9373D9"
    hover_background "#FF69B4"
    color "#FFFFFF"
    font "DejaVuSans.ttf"
    size 28
    bold True
    padding (30, 15)
    xminimum 300
    yminimum 80
    xalign 0.5
    outlines [ (2, "#ffffff", 0, 0) ]
    hover_outlines [ (2, "#FFFFFF", 0, 0) ]
    text_align 0.5


style menu_button_text:
    color "#FFFFFF"
    hover_color "#ffffff"
    size 28
    bold True
    text_align 0.5
    xalign 0.5



## Tela do menu do jogo ########################################################
##
## Isso estabelece a estrutura básica comum de uma tela de menu de jogo. Ela é
## chamada com o título da tela e exibe o plano de fundo, o título e a navegação.
##
## O parâmetro de rolagem pode ser Nenhum ou um dos parâmetros "viewport"
## ou "vpgrid". Essa tela deve ser usada com um ou mais filhos, que são
## transcluídos (colocados) dentro dela.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    # Fundo lilás do menu
    if main_menu:
        add Solid("#F2BDBD")
    else:
        add Solid("#b68ae03b")

    # Moldura principal
    frame:
        style "game_menu_outer_frame"

        hbox:

            # Navegação lateral
            frame:
                style "game_menu_navigation_frame"

            # Área principal de conteúdo
            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True

                        vbox:
                            spacing spacing
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        spacing spacing

                        transclude

                else:
                    transclude

    # Navegação lateral reutilizando seu estilo
    use navigation

    # Botão de retorno
    textbutton _("Voltar"):
        style "return_button"
        action Return()

    # Título do menu
    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


##########################
# ESTILOS PERSONALIZADOS #
##########################

style game_menu_outer_frame:
    background Frame(Solid("#F2BDBD"), 25, 25)
    bottom_padding 45
    top_padding 100
    left_padding 30
    right_padding 30

style game_menu_navigation_frame:
    background Frame(Solid("#ffffff00"), 20, 20)
    xsize 350
    yfill True
    padding (20, 20)

style game_menu_content_frame:
    background Frame(Solid("#FFFFFFCC"), 25, 25)  # branco translúcido
    left_margin 40
    right_margin 40
    top_margin 30
    bottom_margin 30
    padding (30, 30)
    xfill True
    yfill True

style game_menu_label:
    xpos 450
    ypos 50
    ysize 100

style game_menu_label_text:
    color "#ffffff"
    size 48
    font "DejaVuSans.ttf"
    bold True
    outlines [(2, "#000000", 0, 0)]
    text_align 0.5
    xalign 0.5

style return_button is navigation_button
style return_button_text is navigation_button_text

style return_button:
    background Frame(Solid("#B78AE0"), 20, 20)
    hover_background Frame(Solid("#FF69B4"), 20, 20)
    xpos 0.06
    yalign 1.0
    yoffset -35
    xsize 280
    yminimum 60
    outlines [(2, "#ffffff", 0, 0)]
    hover_outlines [(2, "#000000", 0, 0)]



## Sobre a tela ################################################################
##
## Essa tela fornece informações de crédito e direitos autorais sobre o jogo e
## Ren'Py.
##
## Não há nada de especial nessa tela e, portanto, ela também serve como
## exemplo de como criar uma tela personalizada.

screen about():

    tag menu

    # Inclui o layout padrão do game_menu, mas com fundo personalizado
    use game_menu(_("Sobre"), scroll="viewport"):

        style_prefix "about"

        # Janela com fundo personalizado
        window:
            background Solid("#ffffff00")  # fundo branco
            xalign 0.2
            yalign 0.2

        vbox:
            spacing 20

            # Informações fixas
            text "Informações sobre Nuance" color "#000000"
            text "Desenvolvedores: PrismaTech" color "#000000"
            text "Versão: 1.0" color "#000000"

            textbutton "Fechar" action Return()

            # Conteúdo dinâmico do Ren'Py
            vbox:
                text "[config.name!t]" color "#000000"
                text _("Versão [config.version!t]\n") color "#000000"

                if gui.about:
                    text "[gui.about!t]\n" color "#000000"

                text _("Feito com {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] .\n\n[renpy.license!t]") color "#000000"


## Carregar e salvar telas #####################################################
##
## Essas telas são responsáveis por permitir que o jogador salve o jogo
## e o carregue novamente. Como elas têm quase tudo em comum, ambas são
## implementadas em termos de uma terceira tela, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load


###########################################################
# ESTILOS GERAIS DOS SLOTS DE ARQUIVO
###########################################################

# Botão do slot
style file_slot_button:
    xpadding 15
    ypadding 10
    background "#FDEFF3"
    hover_background "#F8DCE9"
    xalign 0.5
    yalign 0.5
    hover_sound "audio/hover.ogg"
    activate_sound "audio/click.ogg"

# Texto dentro do botão do slot
style file_slot_button_text:
    color "#000000"
    hover_color "#B03060"
    size 22

###########################################################
# ESTILOS DE NAVEGAÇÃO (A, Q, 1–9, <, >, etc)
###########################################################

# Estilo base dos botões de página
style page_button:
    background None
    hover_background None
    xpadding 12
    ypadding 4

# Texto dos botões de página (números, A, Q, <, >)
style page_button_text:
    color "#800080"        # Roxo padrão
    hover_color "#FF69B4"  # Rosa no hover
    size 26
    bold True

# Mantém seu estilo original de navegação (não alterado)
style navigation_button_text is gui_text:
    color "#FFFFFF"         # Branco
    hover_background "#800080"  # Fundo roxo
    hover_color "#ffffff"       # Texto branco ao passar o mouse
    size 26
    bold True

###########################################################
# ESTILOS INTERNOS DOS SLOTS DE ARQUIVO
###########################################################

# Índice de cada slot (número do slot)
style file_slot_index:
    color "#800080"
    hover_color "#FF69B4"
    bold True
    size 28

# Nome de cada slot
style file_slot_label:
    color "#800080"
    hover_color "#FF69B4"
    size 22

# Data e hora do slot salvo
style file_slot_time_text:
    color "#B03060"
    hover_color "#800080"
    size 20
    italic True

###########################################################
# TELAS DE SALVAR E CARREGAR
###########################################################

screen save():
    tag menu
    use file_slots(_("Salvar"))

screen load():
    tag menu
    use file_slots(_("Carregar"))

###########################################################
# TELA DE SLOTS DE ARQUIVO
###########################################################

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(
        pattern=_("Página {}"),
        auto=_("Salvamentos automáticos"),
        quick=_("Salvamentos rápidos")
    )

    use game_menu(title):

        fixed:
            order_reverse True

            ## Nome da página editável
            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## Grade de slots
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1

                    button:
                        action FileAction(slot)
                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("slot vazio")):
                            style "file_slot_time_text"

                        text FileSaveName(slot):
                            style "file_slot_label"

                        key "save_delete" action FileDelete(slot)

            ## Botões de navegação
            vbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5
                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            style "navigation_button_text"
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Baixar o Sync"):
                            style "navigation_button_text"
                            action DownloadSync()
                            xalign 0.5


screen preferences():

    tag menu

    # Usamos o game_menu como base, com scroll para casos de conteúdo grande
    use game_menu(_("Preferências"), scroll="viewport"):

        style_prefix "preferences"

        vbox:
            spacing 20

            ## Seção: Tela
            frame:
                background Frame(Solid("#B78AE0"), 25, 25)
                padding (20, 20)
                xfill True

                vbox:
                    spacing 10
                    label _("Tela") style "preferences_label"
                    hbox:
                        spacing 15
                        textbutton _("Janela") action Preference("display", "window") style "preferences_button"
                        textbutton _("Tela cheia") action Preference("display", "fullscreen") style "preferences_button"

            ## Seção: Pular
            frame:
                background Frame(Solid("#B78AE0"), 25, 25)
                padding (20, 20)
                xfill True

                vbox:
                    spacing 10
                    label _("Pular") style "preferences_label"
                    hbox:
                        spacing 15
                        textbutton _("Texto invisível") action Preference("skip", "toggle") style "preferences_button"
                        textbutton _("Após as escolhas") action Preference("after choices", "toggle") style "preferences_button"
                        textbutton _("Transições") action InvertSelected(Preference("transitions", "toggle")) style "preferences_button"

            ## Seção: Sliders
            frame:
                background Frame(Solid("#B78AE0"), 25, 25)
                padding (20, 20)
                xfill True

                vbox:
                    spacing 15

                    # Velocidade do texto
                    label _("Velocidade do texto") style "preferences_label"
                    bar value Preference("text speed") style "preferences_slider"

                    # Tempo do encaminhamento automático
                    label _("Tempo do encaminhamento automático") style "preferences_label"
                    bar value Preference("auto-forward time") style "preferences_slider"

                    # Luminosidade
                    label _("Luminosidade") style "preferences_label"
                    hbox:
                        spacing 10
                        $ brightness_values = [
                            ("Muito claro", 0),
                            ("Claro", 1),
                            ("Normal", 2),
                            ("Escuro", 3),
                        ]
                        for txt, val in brightness_values:
                            textbutton txt:
                                style "preferences_button"
                                action [SetVariable("preferences.brightness", val), Function(apply_brightness)]

                    # Volumes
                    if config.has_music:
                        label _("Volume da música") style "preferences_label"
                        bar value Preference("music volume") style "preferences_slider"

                    if config.has_sound:
                        label _("Volume do som") style "preferences_label"
                        bar value Preference("sound volume") style "preferences_slider"
                        if config.sample_sound:
                            textbutton _("Teste") action Play("sound", config.sample_sound) style "preferences_button"

                    if config.has_voice:
                        label _("Volume da voz") style "preferences_label"
                        bar value Preference("voice volume") style "preferences_slider"
                        if config.sample_voice:
                            textbutton _("Teste") action Play("voice", config.sample_voice) style "preferences_button"

                    # Botão Silenciar tudo
                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("Silenciar tudo"):
                            action Preference("all mute", "toggle")
                            style "preferences_button"


## Tela de histórico ###########################################################
##
## Essa é uma tela que exibe o histórico de diálogo para o jogador. Embora não
## haja nada de especial nessa tela, ela precisa acessar o histórico de diálogo
## armazenado em _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Evite prever essa tela, pois ela pode ser muito grande.
    predict False

    use game_menu(_("Histórico"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Isso organiza as coisas corretamente se history_height for
                ## None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Pegue a cor do texto who do caractere, se definido.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("O histórico de diálogo está vazio.")


## Isso determina quais tags podem ser exibidas na tela de histórico.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


###########################################################
# HELP SCREENS COMPLETO
###########################################################

# Sub-telas de ajuda detalhadas e amigáveis
screen keyboard_help_black():
    vbox:
        spacing 15
        text "🡆 Use as setas do teclado para mover o personagem." color "#000000"
        text "🡆 Pressione Enter para confirmar escolhas." color "#000000"
        text "🡆 Pressione ESC para voltar ao menu." color "#000000"
        text "Dica: Vá devagar e respire fundo se sentir sobrecarga." color "#000000"

screen mouse_help_black():
    vbox:
        spacing 15
        text "🡆 Use o mouse para clicar nos botões do menu." color "#000000"
        text "🡆 Movimente o cursor para explorar opções." color "#000000"
        text "🡆 Clique ESC para voltar ao menu." color "#000000"
        text "Dica: Se parecer difícil, peça ajuda." color "#000000"

screen gamepad_help_black():
    vbox:
        spacing 15
        text "🡆 Use o joystick para navegar entre opções." color "#000000"
        text "🡆 Botão A para confirmar escolhas." color "#000000"
        text "🡆 Botão B para voltar ao menu." color "#000000"
        text "Dica: Respire fundo e vá no seu ritmo." color "#000000"

# Estilo para botões do Help
style help_button is default:
    color "#000000"  # texto preto
    xpadding 20
    ypadding 10
    size 30  # botões maiores e legíveis
    background Frame(Solid("#FF69B4"), 20, 20)  # rosa por padrão
    hover_background Frame(Solid("#B78AE0"), 20, 20)  # roxo suave ao passar o mouse

# Menu Help principal
screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Ajuda"), scroll="viewport"):

        style_prefix "help"

        window:
            background Solid("#00000000")  # fundo azul claro, suave
            xalign 0.5
            yalign 0.5
            xsize 1800
            ysize 900
            xpadding 200
            ypadding 200

            # viewport para rolagem se o conteúdo for maior
            viewport:
                id "help_scroll"
                mousewheel True
                scrollbars "vertical"

                vbox:
                    spacing 25

                    # Botões de dispositivo
                    hbox:
                        spacing 15
                        textbutton _("Teclado") action SetScreenVariable("device", "keyboard") style "help_button"
                        textbutton _("Mouse") action SetScreenVariable("device", "mouse") style "help_button"
                        if GamepadExists():
                            textbutton _("Controle de jogo") action SetScreenVariable("device", "gamepad") style "help_button"

                    # Sub-telas detalhadas
                    if device == "keyboard":
                        use keyboard_help_black
                    elif device == "mouse":
                        use mouse_help_black
                    elif device == "gamepad":
                        use gamepad_help_black

                    # Informação extra
                    vbox:
                        spacing 15
                        text _("Ajuda do jogo") color "#000000" size 28
                        text _("Se precisar, visite {a=https://www.renpy.org/}Ren'Py{/a} para mais informações.") color "#000000" size 24


###########################################################
# CONFIRM SCREEN
###########################################################

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"

    frame:
        style "confirm_frame"

        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5

            label _(message) style "confirm_prompt_text" xalign 0.5

            hbox:
                spacing 50
                xalign 0.5
                textbutton _("Sim") action yes_action style "confirm_button"
                textbutton _("Não") action no_action style "confirm_button"

    key "game_menu" action no_action

style confirm_frame:
    background Frame(Solid("#B78AE0"), 20, 20)
    xpadding 30
    ypadding 30
    xalign 0.5
    yalign 0.5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"
    color "#FFFFFF"

style confirm_button:
    properties gui.button_properties("confirm_button")
    background Frame(Solid("#9373D9"), 20, 20)
    hover_background Frame(Solid("#FF69B4"), 20, 20)
    color "#FFFFFF"
    outlines [(2, "#000000", 0, 0)]
    hover_outlines [(2, "#FFFFFF", 0, 0)]

style confirm_button_text:
    properties gui.text_properties("confirm_button")


###########################################################
# SKIP INDICATOR
###########################################################

screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:
        style "skip_frame"

        hbox:
            spacing 9
            text _("Pular") style "skip_text"
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

transform delayed_blink(delay, cycle):
    alpha 0.5
    pause delay
    block:
        linear 0.2 alpha 1.0
        pause 0.2
        linear 0.2 alpha 0.5
        pause (cycle - 0.4)
        repeat

style skip_frame:
    ypos gui.skip_ypos
    background Frame(Solid("#B78AE0"), 20, 20)
    padding (10, 10, 10, 10)

style skip_text:
    size gui.notify_text_size
    color "#FFFFFF"

style skip_triangle:
    font "DejaVuSans.ttf"
    size gui.notify_text_size
    color "#FFFFFF"


## Tela de notificação #########################################################
##
## A tela de notificação é usada para mostrar uma mensagem ao jogador. (Por
## exemplo, quando o jogo é salvo rapidamente ou quando uma captura de tela é
## feita).
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

################################################################################
## Notify
################################################################################

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos
    background Frame(Solid("#B78AE0"), 15, 15)
    padding (15, 15, 15, 15)

style notify_text:
    properties gui.text_properties("notify")


################################################################################
## NVL
################################################################################

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


style nvl_window is default
style nvl_entry is default
style nvl_label is say_label
style nvl_dialogue is say_dialogue
style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True
    background Frame(Solid("#B78AE0"), 20, 20)
    padding (15, 15, 15, 15)

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


################################################################################
## Bubble
################################################################################

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc


style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5
    background Frame(Solid("#B78AE0"), 20, 20)
    
style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },
    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },
    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },
    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },
    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}


###########################################################
# BUBBLE SCREEN
###########################################################

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"
        style "bubble_window"

        if who is not None:
            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"
                    style "bubble_who"

        text what:
            id "what"
            style "bubble_what"

        default ctc = None
        showif ctc:
            add ctc

###########################################################
# BUBBLE STYLES
###########################################################

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 10
    bottom_padding 10
    background Frame(Solid("#B78AE0"), 20, 20)

style bubble_namebox:
    xalign 0.5
    ypadding 5
    background Frame(Solid("#9373D9"), 10, 10)

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#FFFFFF"
    outlines [(1, "#000000", 0, 0)]

style bubble_what:
    xalign 0.5
    textalign 0.5
    layout "subtitle"
    color "#FFFFFF"
    outlines [(1, "#000000", 0, 0)]


###########################################################
# BUBBLE FRAMES
###########################################################

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}


###########################################################
# CELULAR / QUICK MENU
###########################################################

screen quick_menu():
    variant "touch"
    zorder 100

    if quick_menu:
        hbox:
            style "quick_menu"
            style_prefix "quick"
            spacing 12

            textbutton _("Voltar") action Rollback() style "quick_button"
            textbutton _("Pular") action Skip() alternate Skip(fast=True, confirm=True) style "quick_button"
            textbutton _("Automotivo") action Preference("auto-forward", "toggle") style "quick_button"
            textbutton _("Menu") action ShowMenu() style "quick_button"


###########################################################
# CORES PRINCIPAIS (tema Nuance)
###########################################################

define COLOR_PRIMARY = "#B78AE0"      # Lilás do fundo
define COLOR_HOVER   = "#FF69B4"      # Rosa do hover
define COLOR_TEXT    = "#FFFFFF"      # Branco do texto
define COLOR_OUTLINE = "#000000"      # Preto das bordas


###########################################################
# QUICK MENU STYLES
###########################################################

style quick_button:
    background Frame(Solid(COLOR_PRIMARY), 15, 15)
    hover_background Frame(Solid(COLOR_HOVER), 15, 15)
    xpadding 30
    ypadding 18
    outlines [(2, COLOR_OUTLINE, 0, 0)]
    hover_outlines [(2, COLOR_OUTLINE, 0, 0)]

style quick_button_text is default:
    color COLOR_TEXT
    hover_color COLOR_HOVER
    outlines [(2, COLOR_OUTLINE, 0, 0)]
    size 32  # ← aqui sim o tamanho da fonte funciona

style quick_menu:
    spacing 10
    xalign 0.5
    yalign 0.95

style quick_button_text is default:
    color COLOR_TEXT
    hover_color "#FFFFFF"
    outlines [(1, COLOR_OUTLINE, 0, 0)]


###########################################################
# CORES PRINCIPAIS
###########################################################
define COLOR_PRIMARY = "#59191E"   # cor principal de fundo
define COLOR_HOVER = "#7F2A33"     # cor ao passar o mouse
define COLOR_TEXT = "#FFFFFF"      # cor do texto principal
define COLOR_OUTLINE = "#FFD700"   # cor de destaque/hover
define COLOR_BG_MENU = "#f0f0f0"   # fundo claro para menus (Sobre, Ajuda etc.)

###########################################################
# ESTILOS GERAIS
###########################################################
style window is default:
    background COLOR_PRIMARY
    color COLOR_TEXT

style default:
    color COLOR_TEXT

style text is default:
    color COLOR_TEXT

style h1 is default:
    color COLOR_HOVER
    bold True

###########################################################
# BOTÕES LATERAIS (menu principal e ajuda)
###########################################################
style menu_button is button:
    background COLOR_PRIMARY
    hover_background COLOR_HOVER

style menu_button_text is default:
    color COLOR_TEXT
    hover_color COLOR_OUTLINE

###########################################################
# ABAS (Teclado / Mouse / Controle)
###########################################################
style radio_button is button:
    background COLOR_PRIMARY
    hover_background COLOR_HOVER

style radio_button_text is default:
    color COLOR_TEXT
    hover_color COLOR_OUTLINE

###########################################################
# BOTÃO “Voltar” E OUTROS PADRÕES
###########################################################
style button is default:
    background COLOR_PRIMARY
    hover_background COLOR_HOVER

style button_text is default:
    color COLOR_TEXT
    hover_color COLOR_OUTLINE
