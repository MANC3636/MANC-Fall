import pygame as pg
WIDTH=800; HEIGHT = 800
pg.init()
FPS= 5
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock=pg.time.Clock()
updated_time=0
x=0

#1.load the drawings in as you see with lines 17-19
run1=pg.image.load("run1.png")
run2=pg.image.load("run2.png")
run3=pg.image.load("run3.png")

#2.get the rects for the loaded images

runner_motion=[run1, run2, run3]

class Animated():
    def __init__(self):
        self.x=500
        self.y=300
        self.anime_speed_init=10
        self.anime_speed=self.anime_speed_init
        #3. put the images into a list

        self.anime_list=runner_motion
        self.anime_pos=0
        self.image=self.anime_list[self.anime_pos]

        self.anime_max=len(self.anime_list)-1
        self.update(0)

    def update(self, pos):
        if pos !=0:
            self.anime_speed-=1
            self.x-=pos
            if self.anime_speed!=0:
                self.image=self.anime_list[self.anime_pos]
                if self.anime_pos==self.anime_max:
                    self.anime_pos=0
                else:self.anime_pos+=1

        screen.blit(self.image, (self.x, self.y))
pos=0
animated_obj=Animated()

#game loop------------------------------------
yellow_grapes=True
while yellow_grapes:
    clock.tick(FPS)
    last_time_update = 0
    screen.fill((100, 100, 100))
    for event in pg.event.get():
        if event.type==pg.QUIT:
            yellow_grapes=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_LEFT:
                pos=1

    #update-----------------------------------
    pg.display.update()

    animated_obj.update(pos)

    #draw------------------------------------




    pg.display.flip()
pg.quit()