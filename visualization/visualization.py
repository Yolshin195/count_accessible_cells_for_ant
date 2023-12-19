import pygame
import sys
from enum import Enum

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 900
CELL_SIZE = 80
center_x, center_y = 0, 0


# Цвета
class Colors(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)


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
        return Colors.RED.value

    if is_accessible(1000 + (y - center_y), 1000 + (x - center_x)):
        return Colors.GREEN.value

    return Colors.BLUE.value


def draw_grid():
    for i in range(11):
        for j in range(11):
            rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, get_color(j, i), rect, 1)

            font = pygame.font.Font(None, 18)
            text = font.render(
                f"{1000 + (j - center_x)},{1000 + (i - center_y)}",
                True,
                Colors.WHITE.value,
            )
            screen.blit(text, (rect.x + 5, rect.y + 5))


def main():
    global center_x, center_y

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and center_y > -1000:
            center_y -= 1
        elif keys[pygame.K_DOWN] and center_y < 1000:
            center_y += 1
        elif keys[pygame.K_LEFT] and center_x > -1000:
            center_x -= 1
        elif keys[pygame.K_RIGHT] and center_x < 1000:
            center_x += 1

        screen.fill(Colors.BLACK.value)
        draw_grid()

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
