import pgzrun
import random
from time import time

WIDTH=800
HEIGHT=600

satellites=[]
lines=[]

nextsat=0
starttime=0
totaltime=0
num_sat=8

def createsatellite():
    global starttime
    for i in range(8):
        sat=Actor('satellite')
        sat.pos=random.randint(20,700),random.randint(0,500)
        satellites.append(sat)
    starttime=time()

def draw():
    screen.blit('space',(0,0))
    number=1
    for i in satellites:
        i.draw()
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        number=number+1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))

def update():
    pass

def on_mouse_down(pos):
    global nextsat, lines, sat
    if nextsat < num_sat:
        if satellites[nextsat].collidepoint(pos):
            if nextsat:
                lines.append((satellites[nextsat-1].pos,satellites[nextsat].pos))
            nextsat=nextsat+1
        else:
            lines=[]
            nextsat=0

createsatellite()
pgzrun.go() 