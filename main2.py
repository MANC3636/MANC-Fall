import pygame as pg
import sys
from os import path
from settings import *
from sprites import *


class Game:
    def __init__(self): #helps initialize game
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        #pg.key.set_repeat(500, 100)
        self.load_data()

    def draw_text(self, text, font_name, size, color, x, y, align="nw"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)




    def load_data(self): #helps initialize game
        #game_folder = path.dirname(__file__)
        self.map_data = []
        self.title_font=pg.font.match_font("stencil", 12)

        with open('revised_map.txt', 'rt') as f:
            for line in f:
                self.map_data.append(line)


    def new(self): #helps initialize game
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.floors=pg.sprite.Group()
        self.tables=pg.sprite.Group()

        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == "2":
                    Table(self, col, row)

                if tile == 'P':
                    self.player= Player(self, col, row)


    def run(self):
        # game loop - set self.playing = False to end the game
        #self.show_start_screen()
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events() #collects user input
            self.update() #2 processes that input
            self.draw() #3blits the results of the input to the screen
            # for table_tile in self.tables:
            #     self.screen.blit(table_tile.image, table_tile.rect)

    def quit(self):
        self.show_gameover_screen()
        pg.quit()
        sys.exit()

    def update(self): #1 process user input
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):#part of the blit results
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):#part of blit results
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # collect user inputs here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)

    def show_start_screen(self):
        self.screen.fill(BLACK)
        self.draw_text("Start Game", self.title_font, 100, RED,
                       WIDTH / 3, HEIGHT / 3, align="center")
        self.draw_text("Press a key to start", self.title_font, 75, WHITE,
                       WIDTH / 2, HEIGHT / 4, align="se")
        pg.display.flip()
        self.wait_for_key()


    def show_gameover_screen(self):

        self.screen.fill(BLACK)
        self.draw_text("GAME OVER", self.title_font, 100, RED,
                       WIDTH / 2, HEIGHT / 2, align="center")
        self.draw_text("Quit, then Run to Restart", self.title_font, 75, WHITE,
                       WIDTH / 2, HEIGHT / 4, align="center")
        pg.display.flip()
        self.wait_for_key()


    def wait_for_key(self):
        pg.event.wait()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_gameover_screen()