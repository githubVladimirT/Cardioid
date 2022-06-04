#!/usr/bin/env python3

# Created by: @githubVladimirT


"""
                                My github:
                    https://github.com/githubVladimirT

            You can distribute this project, but you should point me

             This project was been created by githubVladimirT
                    This is a main file of Cardioid
            If you want edit settings, go to file config.cfg
"""


__version__ = "1.0.69"
__author__ = "githubVladimirT"


try:
    from os import environ
    import pygame
    import math
    import sys
    import logging
    import confparse

    global CONF
    CONF = confparse.read()

except ModuleNotFoundError:
    logging.warning("error: moudle not found.  -  file: main.py")
except ImportError:
    logging.fatal("error: import error.  -  file: main.py")


"""
    This class drawing the Cardioid on screen.
"""
class Cardioid:
    # This is a constructor of main cardioid class
    def __init__(self, app):
        self.app = app
        self.radius = CONF["radius"]
        self.num_lines = CONF["num_lines"]
        self.translate = self.app.screen.get_width() // 2, self.app.screen.get_height() // 2

        if CONF["color_mode"] == "multi":
            self.counter, self.inc = 0, 0.01

    # This function per by getting color for multicolor mode
    def get_color(self):
        self.counter += self.inc
        self.counter, self.inc = (self.counter, self.inc) \
                                  if 0 < self.counter < 1 \
                                  else (max(min(self.counter, 1), 0), -self.inc)

        return pygame.Color(CONF["multi_color_1"])\
               .lerp(CONF["multi_color_2"], self.counter)

    # This function per by logic and drawing Cardioid
    def draw(self):
        time = pygame.time.get_ticks()
        if CONF["pulsing"]:
            self.radius = 250 + 50 * abs(math.sin(time * 0.004) - 0.5)

        factor = 1 + CONF["anim_speed"] * time

        for i in range(self.num_lines):
            theta = (2 * math.pi / self.num_lines) * i
            axis_x1 = int(self.radius * math.cos(theta)) + self.translate[0]
            axis_y1 = int(self.radius * math.sin(theta)) + self.translate[1]
            axis_x2 = int(self.radius * math.cos(factor * theta)) + self.translate[0]
            axis_y2 = int(self.radius * math.sin(factor * theta)) + self.translate[1]
            axis_1 = (axis_x1, axis_y1)
            axis_2 = (axis_x2, axis_y2)

            if CONF["color_mode"] == 'mono':
                pygame.draw.aaline(self.app.screen, CONF["mono_color"], axis_1, axis_2)
            elif CONF["color_mode"] == 'multi':
                pygame.draw.aaline(self.app.screen, self.get_color(), axis_1, axis_2)

"""
    This is a main class of this application.
"""
class App:
    # This is a constructor of main app class
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.cardioid = Cardioid(self)

    # This function per by drawing all components on the screen
    def draw_main(self):
        self.screen.fill(CONF["bg_color"])
        pygame.display.set_icon(pygame.image.load("./assets/img/icon_min.png"))

        self.cardioid.draw()
        pygame.display.flip()

    # This function per by start app
    def run(self):
        volume = 0.5
        run = True
        pause = False

        while run:
            self.draw_main()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    logging.warning("interrupted.  -  file: main.py")
                    run = False
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        logging.warning("interrupted.  -  file: main.py")
                        run = False
                        sys.exit(0)

                    if event.key == pygame.K_q and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        logging.warning("interrupted.  -  file: main.py")
                        run = False
                        sys.exit(0)
                    if event.key == pygame.K_w and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        logging.warning("interrupted.  -  file: main.py")
                        run = False
                        sys.exit(0)

                    if CONF["music_path"] is not None:
                        if event.key == pygame.K_UP or event.key == pygame.K_o:
                            volume += 0.05
                            pygame.mixer.music.set_volume(volume)
                        if event.key == pygame.K_DOWN or event.key == pygame.K_k:
                            if volume != 0.0:
                                volume -= 0.05
                            pygame.mixer.music.set_volume(volume)
                        if event.key == pygame.K_SPACE:
                            if pause:
                                pause = False
                                pygame.mixer.music.unpause()
                            else:
                                pause = True
                                pygame.mixer.music.pause()

            self.clock.tick(CONF["fps"])
"""
This function per by playing background music.
"""
def music(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1)

"""
This function per by starting class App.
"""
def main():
    try:
        environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

        if CONF["music_path"] is not None:
            try:
                music(CONF["music_path"])
            except Exception:
                logging.fatal("error: invalid music file or path.  -  file: main.py")

                sys.exit(1)

        app = App()
        app.run()

    except KeyboardInterrupt:
        logging.warning("interrupted.  -  file: main.py")
    except FileNotFoundError:
        logging.fatal("error: music file not found.  -  file: main.py")


if __name__ == '__main__':
    logging.basicConfig(filename='main.log',
                        filemode='a',
                        format='%(asctime)s - %(name)s - [  %(levelname)s  ] - %(message)s')
    main()
