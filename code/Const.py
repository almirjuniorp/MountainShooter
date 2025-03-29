# c
import pygame

COLOR_ORANGE = (255,128,0)
COLOR_WHITE = (255,255,255)
COLOR_YELLOW = (255,255,0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Player1' : 5,
    'Player2' : 5,
    'Enemy1':3,
    'Enemy2':3
}

#E
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Player1': 300,
    #'Player1Shot': 999,
    'Player2': 300,
    #'Player2Shot': 999,
    'Enemy1': 50,
    #'Enemy1Shot': 999,
    'Enemy2': 60,
    #'Enemy2Shot': 999,


}

#S
SPAWN_TIME = 2000
# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2':pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2':pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2':pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2':pygame.K_d}
PLAYER_KEY_SHOOT= {'Player1': pygame.K_RCTRL,
                 'Player2':pygame.K_LCTRL}

# W
WIN_WIDTH = 900
WIN_EIGHT = 506