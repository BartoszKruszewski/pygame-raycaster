from const import *
from pygame.draw import rect as draw_rect 

class Map:
    def __init__(self):
        self.map = [line.rstrip() for line in open('map.txt', 'r').readlines()]
        self.size = (len(self.map[0]), len(self.map))

    def is_wall(self, p):
        x, y = int(p.x), int(p.y)
        if x < 0 or x >= self.size[0] or y < 0 or y >= self.size[1]:
            return True
        return self.map[y][x] == '1'

    def draw(self, surf):
        [
            draw_rect(
                surf, (255, 255, 255), (x * SCALE, y * SCALE, SCALE, SCALE)
            ) 
            for y, row in enumerate(self.map)
            for x, field in enumerate(row)
            if field == '1'
        ]
                    