import pygame as pg
import sys

WIDTH= 500; HEIGHT= 500
price = 0
center_y = 100

pg.init()
screen=pg.display.set_mode((WIDTH, HEIGHT))
font = pg.font.Font('freesansbold.ttf',20)

menu_item_list = [{'name': 'pie', 'price': 2.50, 'color': (55, 2, 222)}, 
            {'name': 'half-sandwich', 'price': 4.50, 'color': (55, 199, 22)},
            {'name': 'soda', 'price': 1.52, 'color': (220, 23, 2)},
            {'name': 'chips', 'price': 1.75, 'color': (0, 35, 250)}]

for i, menu_item in enumerate(menu_item_list):
    menu_item['text'] = menu_item['name'] + ': $' + str(menu_item['price'])
    menu_item['surface'] = font.render(menu_item['text'], True, menu_item['color'], (0,0,0))
    menu_item['rect'] = menu_item['surface'].get_rect(center = (100, (center_y + i * 40)))

while True:
    collides_and_price = [[pg.Rect.collidepoint(menu_item['rect'], pg.mouse.get_pos()), menu_item['price']]  for menu_item in menu_item_list]
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            for collide_price in collides_and_price:
                if collide_price[0]: price += collide_price[1] 

    screen.fill((100,100,199))
    for menu_item in menu_item_list:
        screen.blit(menu_item['surface'], menu_item['rect'])

    price_sum_surface = font.render(str(price), True, (255, 100, 100))
    screen.blit(price_sum_surface, price_sum_surface.get_rect(center = (WIDTH - 50, 100)))

    pg.display.flip()
