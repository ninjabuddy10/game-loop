import pygame

pygame.init()

SCREEN_H = 608
SCREEN_W = 672



screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
pygame.display.set_caption("tile editor")


bg = pygame.image.load("index\python\project\img\g.png").convert_alpha()
bg = pygame.transform.scale(bg,(SCREEN_W,SCREEN_H))


run = True
BG = 50,50,50

scrollx = 0
scrolly = 0
while run:

    screen.fill((50,50,50))
    for i in range(2):
        screen.blit(bg,((i * 672)-scrollx,-scrolly))

        
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and scrolly < 608:
            scrolly += 10
        if keys[pygame.K_s] and scrolly > 0:
            scrolly -= 10
        if keys[pygame.K_a] and scrollx < 672:
            scrollx += 10
        if keys[pygame.K_d] and scrollx > 0:
            scrollx -= 10
        if event.type == pygame.QUIT:
            run = False  


    pygame.display.update()

pygame.quit()