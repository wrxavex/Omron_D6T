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


def light_1(sleeptime, *args):
    print("light 1 on")
    led.on()

    lights[0].on = True
    lights[0].brightness = 200
    lights[0].xy = [random.random(), random.random()]
    sleep(5)

    for light in lights:
        light.on = False

    led.off()
    print("light 1 off")


def light_2(sleeptime, *args):
    print("light 2 on")
    led.on()

    lights[2].on = True
    lights[2].brightness = 200
    lights[2].xy = [random.random(), random.random()]
    sleep(5)

    for light in lights:
        light.on = False

    led.off()
    print("light 2 off")


def open_light1:
    thread.start_new_thread(light_1, (1, ""))

def open_light2:
    thread.start_new_thread(light_2, (1, ""))

button1.when_pressed = open_light1
button2.when_pressed = open_light2

pause()