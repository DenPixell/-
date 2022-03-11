import sys
import pygame
from Settings import Settings
from ship import Ship
from game_functions import check_events
def run_game():
# Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
#цвет фона.
    ship: Ship = Ship(screen)
    bg_color = (230, 230, 230)
# Запуск основного цикла игры.
    while True:
        check_events()
        check_events(ship)
        screen.fill(ai_settings.bg_color)
        ship.blitme()
# Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.rect.centerx += 1

# Отображение последнего прорисованного экрана.
        pygame.display.flip()
run_game()