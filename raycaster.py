from const import *
from math import sin, cos
from pygame.draw import line as draw_line, rect as draw_rect
from pygame import Vector2

class Raycaster:
    def update(self, player, map, surf):
        pos = player.pos / SCALE
        m_pos = player.map_pos
        ray_angle = player.angle - FOV / 2 + NULL

        for ray in range(RAYS_NUMBER):
            sin_a = sin(ray_angle)
            cos_a = cos(ray_angle)

            h = Vector2(0, 0)
            v = Vector2(0, 0)
            d = Vector2(0, 0)

            # horizontal
            h.y, d.y = (m_pos.y + 1, 1) if sin_a > 0 else (m_pos.y - NULL, -1)

            h_depth = (h.y - pos.y) / sin_a
            h.x = pos.x + h_depth * cos_a
            delta_depth = d.y / sin_a
            d.x = delta_depth * cos_a

            while not map.is_wall(h):
                h += d
                h_depth += delta_depth

            # vertical 
            v.x, d.x = (m_pos.x + 1, 1) if cos_a > 0 else (m_pos.x - NULL, -1) 

            v_depth = (v.x - pos.x) / cos_a
            v.y = pos.y + v_depth * sin_a
            delta_depth = d.x / cos_a
            d.y = delta_depth * sin_a

            while not map.is_wall(v):
                v += d
                v_depth += delta_depth

            depth = min(h_depth, v_depth)

            # draw_line(
            #     surf,
            #     (255, 255, 0),
            #     player.pos,
            #     ((pos.x + depth * cos_a) * SCALE, (pos.y + depth * sin_a) * SCALE)
            # )

            # remove fishbowl
            depth *= cos(player.angle - ray_angle)

            # projection
            projection_height = SCREEN_DISTANCE / (depth + NULL)
            color = max(0, min(255, 255 / depth * LIGHT))

            draw_rect(
                surf, (color, color, color),
                (
                    ray * RAY_WIDTH,
                    (SCREEN_SIZE[1] - projection_height) // 2,
                    RAY_WIDTH,
                    projection_height
                )
            )

            ray_angle += DELTA_ANGLE
