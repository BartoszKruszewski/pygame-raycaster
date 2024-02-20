from pygame import Vector2, K_w, K_a, K_s, K_d
from pygame.key import get_pressed
from pygame.draw import circle as draw_circle, line as draw_line
from const import *
from math import sin, cos, tau

class Player:
    def __init__(self):
        self.pos = Vector2(START_POS) * SCALE
        self.angle = 0

    @property
    def map_pos(self):
        return self.pos // SCALE

    def move(self, dt, map):
        keys = get_pressed()

        if keys[K_a]: self.angle -= dt * ROTATION_SPEED
        if keys[K_d]: self.angle += dt * ROTATION_SPEED
        self.angle %= tau

        sin_a = sin(self.angle)
        cos_a = cos(self.angle)

        last_pos = self.pos.copy()

        speed = Vector2(cos_a, sin_a) * MOVEMENT_SPEED * dt

        if keys[K_w]: self.pos += speed
        if keys[K_s]: self.pos -= speed

        if map.is_wall(self.map_pos):
            self.pos = last_pos.copy()

    def draw(self, surf):
        draw_circle(surf, (255, 0, 0), self.pos, 15)
        draw_line(
            surf, (255, 0, 0), self.pos,
            self.pos + Vector2(cos(self.angle), sin(self.angle)) * 100
        )

