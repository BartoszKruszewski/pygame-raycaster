import pygame as pg
from player import Player
from map import Map
from raycaster import Raycaster
from const import *

class Main:
    def __init__(self):
        pg.init()
        
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        self.dt = 1

        self.map = Map()
        self.player = Player()
        self.raycaster = Raycaster()

        while not pg.event.get(pg.WINDOWCLOSE):
            self.update()

    def update(self):
        self.player.move(self.dt, self.map)
        self.screen.fill((0, 0, 0))

        #self.map.draw(self.screen)
        #self.player.draw(self.screen)

        self.raycaster.update(self.player, self.map, self.screen)
        
        self.dt = self.clock.tick(FRAMERATE) * FRAMERATE / 1000
        pg.display.update()

if __name__ == '__main__':
    Main()