import pygame
import sys

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 900
CELL_SIZE = 80
center_x, center_y = 0, 0

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = "red"
GREEN = "green"
BLUE = "blue"

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Centered Player")

clock = pygame.time.Clock()


def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))


def is_accessible(x, y):
    return sum_of_digits(x) + sum_of_digits(y) <= 25


def get_color(x, y):
    if y == center_y and x == center_x:
        return RED

    if is_accessible((1000 + (y - center_y)), (1000 + (x - center_x))):
        return GREEN

    return BLUE


def draw_grid():
    for i in range(11):
        for j in range(11):
            pygame.draw.rect(
                screen,
                get_color(j, i),
                (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                1,
            )
            font = pygame.font.Font(None, 24)
            text = font.render(
                f"{1000 + (j - center_x)},{1000 + (i - center_y)}", True, WHITE
            )
            screen.blit(text, (j * CELL_SIZE + 5, i * CELL_SIZE + 5))


def draw_player():
    pygame.draw.rect(
        screen,
        WHITE,
        (
            SCREEN_WIDTH // 2 - CELL_SIZE // 2,
            SCREEN_HEIGHT // 2 - CELL_SIZE // 2,
            CELL_SIZE,
            CELL_SIZE,
        ),
    )


def main():
    global center_x, center_y

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and center_y > -1000:
                    center_y -= 1
                elif event.key == pygame.K_DOWN and center_y < 1000:
                    center_y += 1
                elif event.key == pygame.K_LEFT and center_x > -1000:
                    center_x -= 1
                elif event.key == pygame.K_RIGHT and center_x < 1000:
                    center_x += 1
                print(center_x, center_y)

        screen.fill(BLACK)
        draw_grid()

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
