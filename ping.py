from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill((100, 155, 255))

clock = time.Clock()
game = True
FPS = 60
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width=100, height=100, typ=1):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.speed = player_speed
        self.directx = self.speed
        self.directy = self.speed
        self.typ = typ
        # self.image.set_colorkey((255, 255, 255))
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        speed_up = 0.2
        self.rect.x += self.directx
        self.rect.y += self.directy
        self.speed += speed_up
        if self.rect.colliderect(player1.rect):
            self.directx = self.speed
        elif self.rect.colliderect(player2.rect):
            self.directx = -self.speed
        else:
            self.speed -= speed_up
        if self.rect.y <= 0 or self.rect.y >= 400:
            self.directy *= -1

class Player(GameSprite):
    def update(self):
        global num_fire
        global delay
        keys = key.get_pressed()
        if self.typ == 2:
            key1 = K_UP
            key2 = K_DOWN
        else:
            key1 = K_w
            key2 = K_s
        if keys[key1]:
            self.rect.y -= self.speed
        elif keys[key2]:
            self.rect.y += self.speed
player1 = Player("banan.png", 30, 200, 7, 100, 150, 1)
player2 = Player("banan.png", 520, 200, 7, 100, 150, 2)
ball = GameSprite('лол.png', 300, 200, 4, 100, 100)                  

font.init()
font = font.Font(None, 35)
lose1 = font.render('Player 1 lose', True, (180, 0, 0))
lose2 = font.render('Player 2 lose', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((100, 155, 255))
    if ball.rect.x < -50:
        window.blit(lose2, (200, 200))
    elif ball.rect.x > 500:
        window.blit(lose1, (200, 200))
    else:
        player1.reset()
        player2.reset()
        player1.update()
        player2.update()
        ball.reset()
        ball.update()
    display.update()
    clock.tick(FPS)