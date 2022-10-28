from ast import While
import random as rn
from turtle import back
from matplotlib.pyplot import pink
import pygame as pg

## Oppgave 1##
pg.init()

w = 600
h = 650

WHITE = 255, 255, 255
RED = 255, 0, 0
YELLOW = 255, 255, 0
BLUE = 0, 255, 255
GREEN = 0, 255, 0
PINK = 255, 0, 255

background = pg.display.set_mode((w, h))
pg.display.set_caption =('Oppgave_medium')
pg.display.flip()

size = 10,10
colors = [WHITE, RED, YELLOW, BLUE, GREEN, PINK]
a = rn.randint(1, 500)
b = rn.randint(1, 500)
c = rn.randint(1, 500)
d = rn.randint(1, 500)
e = rn.randint(1, 500)
f = rn.randint(1, 500)
g = rn.randint(1, 500)
h = rn.randint(1, 500)
i = rn.randint(1, 500)
j = rn.randint(1, 500)
k = rn.randint(1, 500)
l = rn.randint(1, 500)
coord1=(a,b)
coord2=(c,d)
coord3=(e,f)
coord4=(g,h)
coord5=(i,j)
coord6=(k,l)

def draw_shapes():
    pg.draw.rect(background, (rn.choice(colors)), [(coord1), (50, 50)], 0)
    pg.draw.rect(background, (rn.choice(colors)), [(coord2), (50, 50)], 0)
    pg.draw.rect(background, (rn.choice(colors)), [(coord3), (50, 50)], 0)
    pg.draw.rect(background, (rn.choice(colors)), [(coord4), (50, 50)], 0)
    pg.draw.rect(background, (rn.choice(colors)), [(coord5), (50, 50)], 0)
    pg.draw.rect(background, (rn.choice(colors)), [(coord6), (50, 50)], 0)
    pg.display.update()

draw_shapes()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    


'''
Variablene a og b inneholder tilfedige verdier mellom 1 og 30 (a), og mellom 30 og 40 (b). Variabelen coord1
inneholder verdiene av a og b. 

Opprett en funksjon som kan tegne tilfeldige figurer. For å løse denne oppgaven må du lage flere variabler som 
brukes som koordinate-punkter for å tegne figurer for eksempel:


'''