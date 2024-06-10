import pygame
pygame.init()
back = (200, 252, 252)
mw = pygame.display.set_mode((700, 500)) 
Clock = pygame.time.Clock()
mw.fill(back)

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=back):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def outline(self, frame_color, thickness):
        pygame.draw.rect(mw, frame_color, self.rect, thickness)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Label(Area):
    def set_text(self, text, fsize=12, text_color = (0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x , y)
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        super().__init__(x=x, y=y, width=width, height=height, color=back)
        self.image = pygame.image.load(filename)
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
game_over = False
move_up1 = False
move_down1 = False
move_up2 = False
move_down2 = False
monstersCountInLine = 9
monsters = list()
x = 0
y = 0
Ball = Picture('bal.png', 250,  250, 100, 100)
Platform1 = Picture('racket.png', 5, 300, 26, 140)
Platform2 = Picture('racket.png', 670, 300, 26, 140)
speed_x = 3
speed_y = 3
while not game_over:
    mw.fill(back)
    #Platform1.fill()
    #Platform2.fill()
    #Ball.fill()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_up1 = True
            if event.key == pygame.K_DOWN:
                move_down1 = True
            if event.key == pygame.K_w:
                move_up2 = True
            if event.key == pygame.K_s:
                move_down2 = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_up1 = False
            if event.key == pygame.K_DOWN:
                move_down1 = False
            if event.key == pygame.K_w:
                move_up2 = False
            if event.key == pygame.K_s:
                move_down2 = False
    Ball.rect.x += speed_x
    Ball.rect.y += speed_y
    if pygame.sprite.collide_rect(Platform1, Ball) or pygame.sprite.collide_rect(Platform2, Ball):
        speed_x *= -1
    if Ball.rect.y <= 0 or Ball.rect.y >= 500:
        speed_y *= -1
    if Ball.rect.x > 700:
        time_text = Label(150, 150, 50, 50, back)
        time_text.set_text('левый выйграл', 60, (255,0,0))
        time_text.draw(10, 10)
    if Ball.rect.x < 0:
        time_text = Label(150, 150, 50, 50, back)
        time_text.set_text('правый выйграл', 60, (255,0,0))
        time_text.draw(10, 10)
    if move_down1:
        Platform2.rect.y +=3
    if move_up1:
        Platform2.rect.y -=3
    if move_down2:
        Platform1.rect.y +=3
    if move_up2:
        Platform1.rect.y -=3
    Ball.draw()
    Platform1.draw()
    Platform2.draw()
    pygame.display.update()
    Clock.tick(40)