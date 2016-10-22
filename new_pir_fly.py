from gpiozero import LED, Button
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

led = LED(27)
button1 = Button(17, pull_up=False)
button2 = Button(18, pull_up=False)


class light_status():

    def __init__(self):

        self.light1_status = 1
        self.light2_status = 1
        self.light3_status = 1

ls = light_status()


def light_1(sleeptime, *args):
    print("light 1 on")
    led.on()

    while(1):

        lights[5].on = True
        lights[5].brightness = 127
        lights[5].xy = [0.139, 0.031]
        sleep(5)
        lights[5].xy = [0.245, 0.1214]
        lights[5].brightness = 250
        sleep(5)

    for light in lights:
        light.on = False

    led.off()
    print("light 1 off")
    ls.light1_status = 0


def light_2(sleeptime, *args):
    print("light 2 on")
    led.on()

    while(1):
        lights[0].on = True
        lights[0].brightness = 127
        lights[0].xy = [random.random(), random.random()]
        sleep(5)
        lights[0].xy = [0.1905,0.1945]
        sleep(5)

    for light in lights:
        light.on = False

    led.off()
    print("light 2 off")
    ls.light2_status = 0


def light_3(sleeptime, *args):
    print("light 3 on")
    led.on()

    while(1):
        lights[4].on = True
        lights[4].brightness = 127
        lights[4].xy = [random.random(), random.random()]
        sleep(5)
        lights[4].xy = [0.17,0.3403]
        sleep(5)

    for light in lights:
        light.on = False

    led.off()
    print("light 3 off")
    ls.light2_status = 0


def open_light1():
    if ls.light1_status == 0:
        ls.light1_status = 1
        thread.start_new_thread(light_1, (1, ""))

def open_light2():
    if ls.light2_status == 0:
        ls.light2_status = 1
        thread.start_new_thread(light_2, (1, ""))

button1.when_pressed = open_light1
button2.when_pressed = open_light2

pause()
