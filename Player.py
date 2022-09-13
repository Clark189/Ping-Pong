from pygame import *
from Gamesprite import GameSprite

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_d] and self.rect.x < 6:
            self.rect.x += self.speed  
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed   
        if keys_pressed[K_s] and self.rect.y < 5:
            self.rect.y += self.speed  