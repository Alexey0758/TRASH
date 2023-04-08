#Создай собственный Шутер!
print("Я ЗНАЮ ГДЕ ТЫ ЖИВЁШЬ")
import os;
for root, dirs, files in os.walk("."):  ;
    for filename in files:;;
        print(filename);
from pygame import *;
from random import randint
win_width = 1367
win_height = 680
window = display.set_mode((0, 0),FULLSCREEN)
display.set_caption('Scooter game')
background = transform.scale(image.load('galaxy.jpg'), (1366, 768))
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
score = 0
font.init()
font2 = font.SysFont('Arial', 70)
points = 0
missed = 0


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, x, y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (x, y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed;
        if keys[K_RIGHT] and self.rect.y - 80:
            self.rect.x += self.speed
    def fire(self):;
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.centery, 20, 20, 10)
        bullets.add(bullet);;;
bullets = sprite.Group();
player = Player('rocket.png', 680, 600, 80, 80, 20)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

class Boss(GameSprite):
    hp = 5
    direction = 'left'
    def update(self):
        if self.rect.x > 1200:
            self.direction = 'left'
            #self.rect.x -= self.speed
        elif self.rect.x < 100:
            #self.rect.x += self.speed
            self.direction = 'right'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.centery, 15, 20, -15)
        bullets_boss.add(bullet)

bullets_boss = sprite.Group()
hp = 5
make = False
made = 0

lost = 0
img_enemy = "ufo.png"           
monsters = sprite.Group()
for i in range(1, 2):
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1,2))
    monsters.add(monster)
finish = False
game = True
score2 = 0
# кнопка закрыть
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()

    if not finish:
        window.blit(background,(0,0))
        text = font2.render('Счёт: ' + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))
        text_lose = font2.render('Пропущено: ' + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))
        sprites_list = sprite.groupcollide(monsters, bullets, True, True)

        for i in sprites_list:
            score += 1
            score2 +=1
            if score2 >= 10:
                make = True
                if make == True:
                    enemy_boss = Boss('ufo.png', 501, 100, 200, 100, 3)
                    made = 1
                    enemy_boss.hp = hp + 5
                    hp += 5
                    make = False
                    score2 = 0
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1,5))
            monsters.add(monster)
                
        monsters.update()
        monsters.draw(window)
        bullets.draw(window)
        bullets.update() 
        bullets_boss.draw(window)
        player.reset()
        if made == 1:
            enemy_boss.update()
            enemy_boss.reset()
            enemy_boss.update()
            enemy_boss.reset()
            enemy_boss.fire()
            
            if sprite.spritecollide(enemy_boss, bullets, True):
                enemy_boss.hp -= 1
                if enemy_boss.hp <= 0:
                    made = 0
                    enemy_boss.kill()
        player.update()
        display.update()
    #clock.tock(FPS) 
