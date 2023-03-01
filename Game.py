import pygame
import spritesheet


pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game')



sprite = pygame.image.load('index\python\project\img\TAP_anim_v2\Animations ver2\Char1\Char1_idle_16px.png').convert_alpha()
sprite_i = (spritesheet.SpriteSheet(sprite))
sprite = pygame.image.load('index\python\project\img\TAP_anim_v2\Animations ver2\Char1\Char1_Sword_32px.png').convert_alpha()
sprite_a = (spritesheet.SpriteSheet(sprite))
sprite = pygame.image.load('index\python\project\img\TAP_anim_v2\Animations ver2\Char1\Char1_walk_16px.png').convert_alpha()
sprite_w = (spritesheet.SpriteSheet(sprite))
tileset = pygame.image.load("index\python\project\img\Serene_Village_revamped_v1.9\SERENE_VILLAGE_REVAMPED\Serene_Village_32x32.png").convert_alpha()
tile = spritesheet.SpriteSheet(tileset)

BG = (50, 50, 50)
BLACK = (0, 0, 0)

#animation lists

map = []

for i in range(45):
    for y in range(19):
        map.append(tile.get_image(y, i, 32, 32, 1, BLACK))


idle = []
attack = []
walk = []

animation = []
animation_steps = 4
last_update = pygame.time.get_ticks()
animation_cooldown = 200
frame = 0
d = 0
action = 0


for d in range(animation_steps):
    for x in range(animation_steps):
        idle.append(sprite_i.get_image(x, d, 16, 16, 2, BLACK))
        attack.append(sprite_a.get_image(x, d, 32, 32, 2, BLACK))
        walk.append(sprite_w.get_image(x, d, 16, 16, 2, BLACK))

animation = [idle,attack,walk]


run = True

d = 0

animate = 0
xvel = 0
yvel = 0
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            frame = 0
        if keys[pygame.K_s]:
            d = 0
            action = 2
            yvel += 10
        if keys[pygame.K_a]:
            d = 1
            action = 2
            xvel -= 10
        if keys[pygame.K_w]:
            d = 2
            action = 2
            yvel -= 10
        if keys[pygame.K_d]:
            d = 3
            action = 2
            xvel += 10
        if keys[pygame.K_SPACE]:
            action = 1
            animation_cooldown = 75
        elif event.type == pygame.KEYUP:
            if not action == 1:
                action = 0
                animation_cooldown = 200

	#update background
    
    screen.fill(BG)
	
    #show frame image

    # update frame
    current_time = pygame.time.get_ticks()
    time_check = (current_time - last_update)
    
    if  time_check >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame > 3  and action == 1:
            action = 0
            animation_cooldown = 200
            frame = 0
        elif frame > animation_steps - 1:
            frame = 0
    
    t = 0

    for i in range(45):
        for v in range(19):
            screen.blit(map[t],(-xvel + v * 35,-yvel + i * 35))
            t += 1

    if not action == 1:
        screen.blit(animation[action][4*d+frame], (500, 350))
    else:
        screen.blit(animation[action][4*d+frame], (484, 334))
    pygame.display.update()
    

pygame.quit()