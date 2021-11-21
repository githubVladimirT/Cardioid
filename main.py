#!/usr/bin/env python3

# Class: Cardioid drawing the cardioid on screen
class Cardioid:
    def __init__(self, app):
        self.app = app
        self.radius = settings.radius
        self.num_lines = settings.num_lines
        self.translate = self.app.screen.get_width() // 2, self.app.screen.get_height() // 2
        if settings.mode == 'multicolor':
            self.counter, self.inc = 0, 0.01

    def get_color(self):
        self.counter += self.inc
        self.counter, self.inc = (self.counter, self.inc) if 0 < self.counter < 1 else (max(min(self.counter, 1), 0), -self.inc)
        
        return pg.Color(settings.multicolor_cardioid_color_1).lerp(settings.multicolor_cardioid_color_2, self.counter)

    def draw(self):
        time = pg.time.get_ticks()
        if settings.pulsing:
            self.radius = 250 + 50 * abs(math.sin(time * 0.004) - 0.5)

        factor = 1 + settings.animation_speed * time

        for i in range(self.num_lines):
            theta = (2 * math.pi / self.num_lines) * i
            x1 = int(self.radius * math.cos(theta)) + self.translate[0]
            y1 = int(self.radius * math.sin(theta)) + self.translate[1]

            x2 = int(self.radius * math.cos(factor * theta)) + self.translate[0]
            y2 = int(self.radius * math.sin(factor * theta)) + self.translate[1]

            if settings.mode == 'monocolor':
                pg.draw.aaline(self.app.screen, settings.monocolor_cardioid_color, (x1, y1), (x2, y2))
            elif settings.mode == 'multicolor':
                pg.draw.aaline(self.app.screen, self.get_color(), (x1, y1), (x2, y2))


# Class: App the main class of the program
class App:
    def __init__(self):
        self.screen = pg.display.set_mode(settings.screen_resolution, pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        self.cardioid = Cardioid(self)

    def draw_main(self):
        self.screen.fill(settings.background_color)
        pg.display.set_icon(pg.image.load("./img/icon_min.png"))
        self.cardioid.draw()

        pg.display.flip()


    def run(self):
        while True:
            self.draw_main()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    log.write("\n[  OK  ] datetime: " + now.strftime("%Y-%m-%d %H:%M:%S") + "  -  file: main.py")
                    exit(0)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        log.write("\n[  OK  ] datetime: " + now.strftime("%Y-%m-%d %H:%M:%S") + "  -  file: main.py")
                        exit()
                    
                    if event.key == pg.K_q and pg.key.get_mods() & pg.KMOD_CTRL or event.key == pg.K_w and pg.key.get_mods() & pg.KMOD_CTRL:
                        exit()

            self.clock.tick(settings.fps)


if __name__ == '__main__':
    with open("main.log", "a") as log:
        try:
            import pygame as pg
            import settings
            import datetime
            import math
            
            now = datetime.datetime.now()
            app = App()
            app.run()
            log.write("\n[  OK  ] datetime: " + now.strftime("%Y-%m-%d %H:%M:%S") + "  -  file: helper.py")

        except KeyboardInterrupt:
            log.write("\n[  OK  ] datetime: " + now.strftime("%Y-%m-%d %H:%M:%S") + "  -  file: main.py")
        except ModuleNotFoundError:
            log.write("\n[  FAIL  ] datetime: " + now.strftime("%Y-%m-%d %H:%M:%S" + " Module not found") + "  -  file: main.py")
        except ImportError:
            log.write("\n[  FAIL  ] datetime: " + now.strftime("%Y-%m-%d %H:%M:%S" + " Import Error") + "  -  file: main.py")
