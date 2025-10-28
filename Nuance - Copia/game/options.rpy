## ========================================================================== ##
## OPTIONS.RPY – Configurações e padrões do jogo
## ========================================================================== ##

## Noções básicas ##############################################################

define config.name = _("Nuance")          # Nome do jogo
define gui.show_name = True               # Mostrar nome na tela principal
define config.version = "1.0"             # Versão do jogo
define gui.about = _p("""""")
define build.name = "Nuance"              # Nome curto para executáveis/diretórios

## Cores principais ###########################################################

define COLOR_PRIMARY = "#B78AE0"      # lilás do fundo
define COLOR_HOVER   = "#FF69B4"      # rosa do hover
define COLOR_TEXT    = "#FFFFFF"      # branco do texto
define COLOR_OUTLINE = "#000000"      # preto das bordas

## Sons e música ###############################################################

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

init python:
    # Música do menu principal
    config.main_menu_music = "audio/musics/inicio.mp3"

## Transições ##################################################################

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

## ========================================================================== ##
## BRILHO PERSONALIZADO
## ========================================================================== ##

default preferences.brightness = 2  # 0=Muito escuro, 1=Escuro, 2=Normal, 3=Claro, 4=Muito claro

init python:

    def apply_brightness():
        # níveis de brilho do overlay (preto transparente)
        levels = [0.0, 0.25, 0.5, 0.75, 1.0]
        # aplicar brilho com base na preferência do jogador
        renpy.show_screen("brightness_overlay", alpha=levels[preferences.brightness])

screen brightness_overlay(alpha=0.5):
    add Solid("#000") alpha alpha
    zorder 1000

## Estilos ####################################################################

style gallery_title is default:
    font "DejaVuSerif-Bold.ttf"
    size 40
    color COLOR_TEXT
    xalign 0.5
    yalign 0.5

style return_button:
    background Frame(Solid(COLOR_PRIMARY), 20, 20)
    hover_background Frame(Solid(COLOR_HOVER), 20, 20)
    xminimum 180
    yminimum 20
    padding (10, 5)
    xalign 1.0
    outlines [(2, COLOR_OUTLINE, 0, 0)]
    hover_outlines [(2, "#FFFFFF", 0, 0)]

style menu_title:
    color COLOR_TEXT
    font "DejaVuSans.ttf"
    size 28
    bold True
    xalign 1.0

## Gerenciamento de janelas ###################################################

# Evita que a janela de diálogo apareça junto das escolhas
define config.window = "hide"
define config.window_show_transition = Dissolve(0.2)
define config.window_hide_transition = Dissolve(0.2)
define config.window_icon = "gui/window_icon.png"

## ========================================================================== ##
## Preferências do jogador (variáveis que podem ser salvas) ##################

# Velocidade do texto
default preferences.text_cps = 0

# Tempo do encaminhamento automático (0 a 30)
default preferences.afm_time = 15

# Volume
default preferences.music_volume = 1.0
default preferences.all_mute = False

# Opções de pular
default preferences.skip = False
default preferences.after_choices = False
default preferences.transitions = True

# Tela
default preferences.display = "window"  # "window" ou "fullscreen"

## ========================================================================== ##
## Classificação de arquivos para compilação #################################

init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    build.documentation('*.html')
    build.documentation('*.txt')

## ========================================================================== ##
## ESCOLHAS PERSONALIZADAS (com fundo preto translúcido e botões largos) ######
## ========================================================================== ##

screen choice(items):
    # Fundo preto translúcido ocupando boa parte da tela com fade suave
    add Solid("#00000080") at fade_in_choice

    vbox:
        spacing 25
        xalign 0.5
        yalign 0.6  # posição um pouco mais baixa no centro

        for i in items:
            textbutton i.caption action i.action:
                style "choice_button"
                at choice_anim

# ===============================
# Estilo dos botões de escolha
# ===============================
style choice_button is default:
    background Frame(Solid(COLOR_PRIMARY), 40, 40)           # Fundo lilás com bordas suaves
    hover_background Frame(Solid(COLOR_HOVER), 40, 40)       # Fundo rosa no hover
    xminimum 700                                             # Botões largos
    yminimum 100
    padding (25, 20)
    xalign 0.5
    yalign 0.5
    outlines [(2, "#FFFFFF", 0, 0)]                          # Borda branca leve
    hover_outlines [(3, "#FFFFFF", 0, 0)]

style choice_button_text is default:
    color COLOR_TEXT
    hover_color "#000000"
    size 38
    bold True
    text_align 0.5
    outlines [(2, "#000000", 0, 0)]

# ===============================
# Animação de hover dos botões
# ===============================
transform choice_anim:
    on hover:
        ease 0.15 zoom 1.05
    on idle:
        ease 0.15 zoom 1.0

# ===============================
# Animação de fade-in do fundo preto
# ===============================
transform fade_in_choice:
    alpha 0.0
    linear 0.3 alpha 1.0
