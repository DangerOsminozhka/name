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
    def __init__(self, player_image, player_x, player_y, player_speed, width=100, height=100):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        # self.image.set_colorkey((255, 255, 255))
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        global num_fire
        global delay
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > self.speed:
            self.rect.x -= self.speed
        elif keys[K_RIGHT] and self.rect.x < win_width - 100:
            self.rect.x += self.speed
        if keys[K_SPACE]:
            if delay <= 0:
                bullets.add(Bullet("smetanaept.png", self.rect.x, self.rect.y - 30, 5, 50, 55))
                delay = 30
                smetan.play()
                num_fire += 1
                if num_fire == 5:
                    num_fire = 0
                    delay += 90
            elif delay <= 30:
                delay += 0.5
        if delay != 0:
            delay -= 1



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()