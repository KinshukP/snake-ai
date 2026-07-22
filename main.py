import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 800
CELL_SIZE = 40

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake AI")

clock = pygame.time.Clock()

snake = [
    (100, 100),
    (60, 100),
    (20, 100),
]

direction_x = CELL_SIZE
direction_y = 0

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                direction_x = 0
                direction_y = -CELL_SIZE

            elif event.key == pygame.K_s:
                direction_x = 0
                direction_y = CELL_SIZE

            elif event.key == pygame.K_a:
                direction_x = -CELL_SIZE
                direction_y = 0

            elif event.key == pygame.K_d:
                direction_x = CELL_SIZE
                direction_y = 0

    head_x, head_y = snake[0]

    new_head = (
        head_x + direction_x,
        head_y + direction_y,
    )

    snake.insert(0, new_head)
    snake.pop()

    screen.fill((30, 30, 30))

    for segment in snake:
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (*segment, CELL_SIZE, CELL_SIZE),
        )

    pygame.display.flip()
    clock.tick(8)

pygame.quit()