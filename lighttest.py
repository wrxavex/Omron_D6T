from signal import pause
from time import sleep
import random

from phue import Bridge
import logging

import thread

logging.basicConfig()

lightrunning = {1:False, 2:False, 3:False}

b = Bridge('192.168.1.178', 'YxPYRWNawywC-sKHkjuRho7iOwMMSrn3di2ETF74')  # Enter bridge IP here.

lights = b.get_light_objects()



class light_status():

    def __init__(self):

        self.light1_status = 0
        self.light2_status = 0
        self.light3_status = 0
        self.light4_status = 0
        self.light5_status = 0
        self.light6_status = 0

ls = light_status()


def light_1(sleeptime, *args):
    print("light 1 on")
    lights[0].on = True

    while(1):

        lights[0].brightness = 30
        lights[0].hue = 20000
        if ls.light1_status > 10:
            sleep(5);
        elif ls.light1_status > 5:
            sleep(2)
        lights[0].hue = 50000
        lights[0].brightness = 250
        if ls.light1_status > 10:
            sleep(5)
        elif ls.light1_status > 5:
            sleep(2)
        else:
            sleep(1)

        print("light 1 active")

        if ls.light1_status > 0:
            ls.light1_status -= 1


    for light in lights:
        light.on = False

    print("light 1 off")
    ls.light1_status = 0


def light_2(sleeptime, *args):
    print("light 2 on")

    while(1):
        lights[1].on = True
        lights[1].brightness = 32
        lights[1].xy = [0.139, 0.031]
        if ls.light1_status > 10:
            sleep(random.random()*2)
        elif ls.light1_status > 5:
            sleep(random.random()*5)
        else:
            sleep(random.random() * 20)
        lights[1].xy = [0.245, 0.1214]
        lights[1].brightness = 250
        if ls.light1_status > 10:
            sleep(random.random()*2)
        elif ls.light1_status > 5:
            sleep(random.random()*5)
        else:
            sleep(random.random() * 20)

        if ls.light1_status > 0:
            ls.light1_status -= 1

        print("light 2 active")

    for light in lights:
        light.on = False



    print("light 2 off")
    ls.light2_status = 0


def light_3(sleeptime, *args):
    print("light 3 on")

    while(1):
        lights[2].on = True
        lights[2].brightness = 32
        lights[2].xy = [0.139, 0.031]
        if ls.light1_status > 10:
            sleep(random.random() * 2)
        elif ls.light1_status > 5:
            sleep(random.random() * 5)
        else:
            sleep(random.random() * 20)
        lights[2].xy = [0.245, 0.1214]
        lights[2].brightness = 250
        if ls.light1_status > 10:
            sleep(random.random() * 5)
        elif ls.light1_status > 5:
            sleep(random.random() * 3)
        else:
            sleep(random.random() * 2)

        if ls.light1_status > 0:
            ls.light1_status -= 1

        print("light 3 active")

    for light in lights:
        light.on = False

    print("light 3 off")
    ls.light1_status = 0


def light_4(sleeptime, *args):
    print("light 4 on")

    while(1):
        lights[3].on = True
        lights[3].brightness = 32
        lights[3].xy = [0.139, 0.031]
        if ls.light2_status > 10:
            sleep(random.random() * 2)
        elif ls.light2_status > 5:
            sleep(random.random() * 5)
        else:
            sleep(random.random() * 20)
        lights[3].xy = [0.245, 0.1214]
        lights[3].brightness = 250
        if ls.light2_status > 10:
            sleep(random.random() * 2)
        elif ls.light2_status > 5:
            sleep(random.random() * 5)
        else:
            sleep(random.random() * 20)

        if ls.light2_status > 0:
            ls.light2_status -= 1

        print("light 4 active")

    for light in lights:
        light.on = False

    print("light 4 off")
    ls.light2_status = 0


def light_5(sleeptime, *args):
    print("light 5 on")

    while(1):
        lights[4].on = True
        lights[4].brightness = 32
        lights[4].xy = [0.139, 0.031]
        if ls.light2_status > 10:
            sleep(random.random() * 2)
        elif ls.light2_status > 5:
            sleep(random.random() * 5)
        else:
            sleep(random.random() * 20)
        lights[4].xy = [0.245, 0.1214]
        lights[4].brightness = 250
        if ls.light2_status > 10:
            sleep(random.random() * 2)
        elif ls.light2_status > 5:
            sleep(random.random() * 5)
        else:
            sleep(random.random() * 20)

        if ls.light2_status > 0:
            ls.light2_status -= 1

        print("light 5 active")

    for light in lights:
        light.on = False

    print("light 5 off")
    ls.light2_status = 0


def light_6(sleeptime, *args):
    print("light 5 on")

    while(1):
        lights[5].on = True
        lights[5].brightness = 127
        lights[5].xy = [0.139, 0.031]
        if ls.light2_status > 10:
            sleep(random.random() * 2)
        elif ls.light2_status > 5:
            sleep(random.random() * 5)
        else:
            sleep(random.random() * 20)
        lights[5].xy = [0.245, 0.1214]
        lights[5].brightness = 250
        if ls.light2_status > 10:
            sleep(random.random() * 2)
        elif ls.light2_status > 5:
            sleep(random.random() * 5)
        else:
            sleep(random.random() * 20)

        if ls.light2_status > 0:
            ls.light2_status -= 1

    for light in lights:
        light.on = False

    print("light 5 off")
    ls.light2_status = 0


def open_light1():
    if ls.light1_status == 0:
        ls.light1_status = 0
        thread.start_new_thread(light_1, (1, ""))

def open_light2():
    if ls.light2_status == 0:
        ls.light2_status = 1
        thread.start_new_thread(light_2, (1, ""))


def open_light3():
    if ls.light3_status == 0:
        ls.light3_status = 1
        thread.start_new_thread(light_3, (1, ""))


def open_light4():
    if ls.light4_status == 0:
        ls.light4_status = 1
        thread.start_new_thread(light_4, (1, ""))


def open_light5():
    if ls.light5_status == 0:
        ls.light5_status = 1
        thread.start_new_thread(light_5, (1, ""))


def open_light6():
    if ls.light6_status == 0:
        ls.light6_status = 1
        thread.start_new_thread(light_6, (1, ""))


open_light1()
open_light2()
open_light3()
open_light4()
open_light5()
open_light6()


def lightSet1Active():
    ls.light1_status +=50
    print('pir1 active')


def lightSet2Active():
    ls.light2_status +=50
    print('pir2 active')

while(1):
    print('running')
    pass