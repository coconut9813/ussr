from pygame import *

window = display.set_mode((1200, 600))
display.set_caption('Лабиринт')
background = transform.scale(image.load("COMMUNISM.png"),(1200, 600))
mixer.init()
mixer.music.load('RADIO TAPOK - SOVIET MARCH.mp3')
mixer.music.play()


class GaySprite(sprite.Sprite):
    def __init__(self, image1, x, y, speed):
        self.image = transform.scale(image.load(image1), (80, 80))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def recet(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GaySprite):
    def update(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_w]: #and self.rect.y > 5:
            self.rect.y -= self.speed

        if key_pressed[K_d]: #and self.rect.x < 1100:
            self.rect.x += self.speed

        if key_pressed[K_s]: #and self.rect.y < 500:
            self.rect.y += self.speed

        if key_pressed[K_a]: #and self.rect.x > 5:
            self.rect.x -= self.speed

        if self.rect.x > 1200 :
            self.rect.x = 0

        if self.rect.x < 0:
            self.rect.x = 1200

        if self.rect.y > 600 :
            self.rect.y = 0

        if self.rect.y < 0:
            self.rect.y = 600

class Enemy(GaySprite):
    direction = 'left'
    def update(self):
        if self.rect.y <= 245:
            self.direction = 'right'
        if self.rect.y >= 520:
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed

class Wall(sprite.Sprite):
    def __init__(self, width, height, image2, x, y, color_1, color_2, color_3):
        self.width = width
        self.height = height
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.image = transform.scale(image.load(image2), (80, 80))
        self.image = Surface((self.width, self.height))
        self.image.fill((self.color_1, self.color_2, self.color_3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




game = True
finish = False
goodman = Player('cyborg.png', 1000, 38, 2) 
badguy = Enemy('hero.png', 450, 250, 2)
money = GaySprite('treasure.png', 250, 350, 10)
wall1 = Wall(700, 10, 'wall.jpg', 830, 430, 255, 0, 0)
wall2 = Wall(10, 300, 'wall.jpg', 990, 0, 255, 0, 0)
wall3 = Wall(10, 500, 'wall.jpg', 830, 100, 255, 0, 0)
wall4 = Wall(690, 10, 'wall.jpg', 150, 100, 255, 0, 0)
wall5 = Wall(840, 10, 'wall.jpg', 0, 230, 255, 0, 0)
wall6 = Wall(10, 270, 'wall.jpg', 100, 230, 255, 0, 0)
wall7 = Wall(860, 10, 'wall.jpg', 0, 0, 255, 0, 0)
wall8 = Wall(10, 270, 'wall.jpg', 200, 230, 255, 0, 0)
wall9 = Wall(250, 10, 'wall.jpg', 200, 490, 255, 0, 0)

font.init()
font = font.Font(None, 170)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE and finish == True:
                goodman.rect.x = 1000
                goodman.rect.y = 38
                finish = False


    if finish != True:
        window.blit(background,(0, 0)) 
        goodman.recet()
        badguy.recet() 
        money.recet()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        wall9.draw_wall()
        goodman.update()
        badguy.update()

        if sprite.collide_rect(goodman, badguy):
            finish = True
            win = font.render("WE LOSE!", True, (255, 255 ,0))
            window.fill((0, 0, 255))
            window.blit(win, (400, 200))

        if sprite.collide_rect(goodman, money): 
            finish = True
            win = font.render("WE WIN!", True, (255, 255 ,0))
            window.fill((255, 0, 0))
            window.blit(win, (400, 200))

        if sprite.collide_rect(goodman, wall1): 
            finish = True
            win = font.render("WE LOSE!", True, (255, 255 ,0))
            window.fill((0, 0, 255))
            window.blit(win, (400, 200))

        if sprite.collide_rect(goodman, wall2): 
            finish = True
            win = font.render("WE LOSE!", True, (255, 255 ,0))
            window.fill((0, 0, 255))
            window.blit(win, (400, 200))

        if sprite.collide_rect(goodman, wall3): 
            finish = True
            win = font.render("WE LOSE!", True, (255, 255 ,0))
            window.fill((0, 0, 255))
            window.blit(win, (400, 200))

        if sprite.collide_rect(goodman, wall4): 
            finish = True
            win = font.render("WE LOSE!", True, (255, 255 ,0))
            window.fill((0, 0, 255))
            window.blit(win, (400, 200))

        if sprite.collide_rect(goodman, wall5): 
            finish = True
            win = font.render("WE LOSE!", True, (255, 255 ,0))
            window.fill((0, 0, 255))
            window.blit(win, (400, 200))

        if sprite.collide_rect(goodman, wall6) or sprite.collide_rect(goodman, wall7) or sprite.collide_rect(goodman, wall8) or sprite.collide_rect(goodman, wall9): 
            finish = True
            win = font.render("WE LOSE!", True, (255, 255 ,0))
            window.fill((0, 0, 255))
            window.blit(win, (400, 200))

        

        
        


    

    display.update()