from pygame import *
from GameSprite import GameSprite
from Player import Player

game = True
clock = time.Clock()
FPS = 60
finish = False

player = Player('platform.jpeg')
ball = GameSprite('ball.png')

def mane:

    font.init()
    font1 = font.Font(None, 35)

    win = font1.render('CONGRAT!', True, (255, 255, 255))
    lose = font1.render('WASTED', True, (180, 0, 0))

    win_width = 1200
    win_height = 900
    display.set_caption("Ping Pong")
    window = display.set_mode((win_width, win_height))
    background = transform.scale('background.png', (win_width, win_height))

    display.update()
    clock.tick(FPS)