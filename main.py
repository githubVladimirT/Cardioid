#!/usr/bin/env python3

# Created by: @githubVladimirT


"""
                                My github:
                    https://github.com/githubVladimirT

                      You can distribute this project

              This project was been created by githubVladimirT
                     This is a main file of Cardioid
              If you want change settings, go to file config.cfg
"""


__version__ = "1.2.0"
__author__ = "githubVladimirT"

try:
    from os import environ
    environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
    
    import math
    import sys
    import logging
    import confparse
    import pygame

    try:
        path = sys.argv[1]
    except IndexError:
        path = None

    CONF = confparse.read(path=path)

    if CONF is None:
        logging.fatal("error: confparse.read returned None.  -  file:main.py")

except ModuleNotFoundError:
    logging.fatal("error: moudle not found.  -  file:main.py")
    sys.exit(1)
except ImportError:
    logging.fatal("error: import error.  -  file:main.py")
    sys.exit(1)
except KeyError:
    logging.fatal("error: confparse.read returned KeyError.  -  file:main.py")
    sys.exit(1)

logging.basicConfig(
    filename= f'{path}/main.log' if path else './main.log',
    filemode='a',
    format='%(asctime)s - %(name)s - [  %(levelname)s  ] - %(message)s'
)


class Cardioid:
    def __init__(self, app, CONF):
        self.CONF = CONF
        self.app = app
        self.radius = self.CONF["radius"]
        self.num_lines = self.CONF["num_lines"]
        self.translate = self.app.screen.get_width() // 2, self.app.screen.get_height() // 2

        if self.CONF["color_mode"] == "multi":
            self.counter, self.inc = 0, 0.01

    def get_color(self):
        self.counter += self.inc
        self.counter, self.inc = (self.counter, self.inc) \
                                  if 0 < self.counter < 1 \
                                  else (max(min(self.counter, 1), 0), -self.inc)

        return pygame.Color(self.CONF["multi_color_1"])\
               .lerp(self.CONF["multi_color_2"], self.counter)

    def draw(self):
        time = pygame.time.get_ticks()
        if self.CONF["pulsing"]:
            self.radius = 250 + 50 * abs(math.sin(time * 0.004) - 0.5)

        factor = 1 + self.CONF["anim_speed"] * time

        for i in range(self.num_lines):
            theta = (2 * math.pi / self.num_lines) * i
            axis_x1 = int(self.radius * math.cos(theta)) + self.translate[0]
            axis_y1 = int(self.radius * math.sin(theta)) + self.translate[1]
            axis_x2 = int(self.radius * math.cos(factor * theta)) + self.translate[0]
            axis_y2 = int(self.radius * math.sin(factor * theta)) + self.translate[1]
            axis_1 = (axis_x1, axis_y1)
            axis_2 = (axis_x2, axis_y2)

            if self.CONF["color_mode"] == 'mono':
                pygame.draw.aaline(self.app.screen, self.CONF["mono_color"], axis_1, axis_2)
            elif self.CONF["color_mode"] == 'multi':
                pygame.draw.aaline(self.app.screen, self.get_color(), axis_1, axis_2)
            else:
                logging.fatal("error: unknow color mode.  -  file:main.py")


class App:
    def __init__(self, CONF):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.cardioid = Cardioid(self, CONF)
        self.is_running = True
        self.CONF = CONF

    def draw_main(self):
        self.screen.fill(self.CONF["bg_color"])

        self.cardioid.draw()
        pygame.display.flip()

    def interrupted(self):
        logging.warning("interrupted.  -  file:main.py")
        self.is_running = False
        sys.exit(0)
    
    def run(self):
        while self.is_running:
            self.draw_main()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.interrupted()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        self.interrupted()

                    if event.key == pygame.K_q and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.interrupted()

                    if event.key == pygame.K_w and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.interrupted()

            self.clock.tick(self.CONF["fps"])


def main():
    try:
        app = App(CONF)
        app.run()

    except KeyboardInterrupt:
        logging.warning("interrupted.  -  file:main.py")


if __name__ == '__main__':
    main()


