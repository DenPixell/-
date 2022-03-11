class Settings():
    def __init__(self):
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
        # Настройки корабля
        self.ship_speed_factor = 2
        # Параметры пули
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 50