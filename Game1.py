import pygame
pygame.init()

screenLength=1000
screenWidth=500
win = pygame.display.set_mode((screenLength,screenWidth))
pygame.display.set_caption("Test Game")

isJump = False
jumpCount = 5

x = 50
y = 50
width = 40
height = 60
speed = 6


running = True
while running:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed

    if keys[pygame.K_RIGHT] and x < screenWidth - width - speed:
        x += speed

    if not(isJump):
        if keys[pygame.K_UP] and y > speed:
            y -=speed

        if keys[pygame.K_DOWN] and y  < screenLength- height - speed:
            y += speed

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount > -5:
            neg = 1
            if jumpCount < 0 :
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 5
            


    win.fill((0,0,0))
    pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    pygame.display.update()

pygame.quit()