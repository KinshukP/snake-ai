import pygame
pygame.init()

width = 1000
height = 800

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake AI")

running = True

square_x = 100
square_y = 100
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        square_y -= 5
    if keys[pygame.K_a]:
        square_x -= 5
    if keys[pygame.K_s]:
        square_y += 5
    if keys[pygame.K_d]:
        square_x += 5
    
    screen.fill((30,30,30))
    pygame.draw.rect(screen, (0, 255, 0), (square_x, square_y, 40, 40))

    pygame.display.flip()
    #square_y += 1
    #square_x += 1
    clock.tick(380)
pygame.quit()