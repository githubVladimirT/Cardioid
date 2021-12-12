#!/usr/bin/env python3

# Class: Cardioid drawing the cardioid on screen
class Cardioid:
    def __init__(self, app, settings, pg, math):
        self.app = app
        self.settings = settings
        self.pg = pg
        self.math = math
        self.radius = settings.radius
        self.num_lines = settings.num_lines
        self.translate = self.app.screen.get_width() // 2, self.app.screen.get_height() // 2
        if settings.mode == 'multicolor':
            self.counter, self.inc = 0, 0.01

    def get_color(self):
        self.counter += self.inc
        self.counter, self.inc = (self.counter, self.inc) if 0 < self.counter < 1 else (max(min(self.counter, 1), 0), -self.inc)
        
        return self.pg.Color(self.settings.multicolor_cardioid_color_1).lerp(self.settings.multicolor_cardioid_color_2, self.counter)

    def draw(self):
        time = self.pg.time.get_ticks()
        if self.settings.pulsing:
            self.radius = 250 + 50 * abs(self.math.sin(time * 0.004) - 0.5)

        factor = 1 + self.settings.animation_speed * time

        for i in range(self.num_lines):
            theta = (2 * self.math.pi / self.num_lines) * i
            x1 = int(self.radius * self.math.cos(theta)) + self.translate[0]
            y1 = int(self.radius * self.math.sin(theta)) + self.translate[1]

            x2 = int(self.radius * self.math.cos(factor * theta)) + self.translate[0]
            y2 = int(self.radius * self.math.sin(factor * theta)) + self.translate[1]

            if self.settings.mode == 'monocolor':
                self.pg.draw.aaline(self.app.screen, self.settings.monocolor_cardioid_color, (x1, y1), (x2, y2))
            elif self.settings.mode == 'multicolor':
                self.pg.draw.aaline(self.app.screen, self.get_color(), (x1, y1), (x2, y2))


# Class: App the main class of the program
class App:
    def __init__(self, pg, settings, log, now, math):
        self.pg = pg
        self.math = math
        self.settings = settings
        self.log = log
        self.now = now
        
        self.screen = self.pg.display.set_mode(settings.screen_resolution, self.pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        self.cardioid = Cardioid(self, self.settings, self.pg, self.math)

    def draw_main(self):
        self.screen.fill(self.settings.background_color)
        self.pg.display.set_icon(self.pg.image.load("./assets/img/icon_min.png"))

        self.cardioid.draw()
        self.pg.display.flip()


    def run(self):
        volume = 0.5

        while True:
            self.draw_main()
            for event in self.pg.event.get():
                if event.type == self.pg.QUIT:
                    self.log.write("\n[  OK  ] datetime: " + self.now.strftime("%Y-%m-%d %H:%M:%S") + "  -  file: master.py")
                    exit(0)
                if event.type == self.pg.KEYDOWN:
                    if event.key == self.pg.K_ESCAPE:
                        self.log.write("\n[  OK  ] datetime: " + self.now.strftime("%Y-%m-%d %H:%M:%S") + "  -  file: master.py")
                        exit()
                    
                    if event.key == self.pg.K_q and self.pg.key.get_mods() & self.pg.KMOD_CTRL or event.key == self.pg.K_w and self.pg.key.get_mods() & self.pg.KMOD_CTRL:
                        exit()

                    if self.settings.path_to_music != None:
                        if event.key == self.pg.K_UP or event.key == self.pg.K_o:
                            volume += 0.05
                            self.pg.mixer.music.set_volume(volume)
                        if event.key == self.pg.K_DOWN or event.key == self.pg.K_k:
                            if volume != 0.0:
                                volume -= 0.05
                            self.pg.mixer.music.set_volume(volume)

            self.clock.tick(self.settings.fps)

def music(settings, pg):
    pg.mixer.init()
    pg.mixer.music.load(settings.path_to_music)
    pg.mixer.music.play(-1)


def master():
    with open("./master.log", "a") as log:
        try:
            from os import environ
            environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

            import pygame as pg
            import settings
            import datetime
            import math

            now = datetime.datetime.now()

            if settings.path_to_music != None:
                try:
                    music(settings, pg)
                except:
                    from colorama import Fore
                    log.write("\n[  FAIL  ] datetime: " + now.strftime("%Y-%m-%d %H:%M:%S" + " ; Error: Music file not found.") + "  -  file: master.py")
                    print(Fore.RED + "\nError! For details open file master.log\n" + Fore.RESET)
                    exit(1)

            app = App(pg, settings, log, now, math)
            app.run()

        except KeyboardInterrupt:
            log.write("\n[  OK  ] datetime: " + now.strftime("%Y-%m-%d %H:%M:%S") + "  -  file: master.py")
        except ModuleNotFoundError:
            log.write("\n[  FAIL  ] datetime: " + now.strftime("%Y-%m-%d %H:%M:%S" + " ; Error: Module not found") + "  -  file: master.py")
        except ImportError:
            log.write("\n[  FAIL  ] datetime: " + now.strftime("%Y-%m-%d %H:%M:%S" + " ; Error: Import Error") + "  -  file: master.py")
        except FileNotFoundError:
            log.write("\n[  FAIL  ] datetime: " + now.strftime("%Y-%m-%d %H:%M:%S" + " ; Error: File not found. Maybe music file doesn't exist.") + "  -  file: master.py")


if __name__ == '__main__':
    master()
