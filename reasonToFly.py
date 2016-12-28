from gpiozero import MotionSensor
import time
import random

pir1 = MotionSensor(4)
pir2 = MotionSensor(17)
pir3 = MotionSensor(18)

from phue import Bridge
import logging

logging.basicConfig()

b = Bridge('192.168.1.178', 'YxPYRWNawywC-sKHkjuRho7iOwMMSrn3di2ETF74')  # Enter bridge IP here.

lights = b.get_light_objects()

class Stage:

    def __init__(self):
        self.state = 1
        self.stage_count = 0
        self.stage_next = 0
        self.stage_show_time = 0

s = Stage()


class LightS:

    def __init__(self):
        self.no = 0
        self.h = 0
        self.s = 254
        self.b = 254
        self.state = 0
        self.power = 0

    def toggle(self, state):
        self.state = state

    def update(self, temp_h, temp_s, temp_b):
        self.h = temp_h
        self.s = temp_s
        self.b = temp_b

        lights[self.no].hue = self.h
        lights[self.saturation] = self.s
        lights[self.no].brightness = self.b

    def on(self):
        self.power = 1
        lights[self.no] = True

    def off(self):
        self.power = 0
        lights[self.no] = False


bulbs = {}

for bulb in range(0, 15):
    bulbs[bulb] = LightS()


class PirS:

    def __init__(self):
        self.state = 0
        self.show_time = 0
        self.count = 0
        self.next = 0
        self.toggle_time = 0

    def detect(self):
        self.state = 1
        self.count = 0
        self.next = 0
        self.show_time = 0
        self.toggle_time = time.time()

    def check(self):
        if time.time() - self.toggle_time > 10:
            self.state = 0

pirs = {}

for sensor in range(0, 3):
    pirs[sensor] = PirS()


def mot1():
    print('motion sensor1')
    pirs[0].state = 1


def mot2():
    print('motion sensor2')
    pirs[1].state = 1


def mot3():
    print('motion sensor3')
    pirs[2].state = 1

pir1.when_motion = mot1
pir2.when_motion = mot2
pir3.when_motion = mot3


def light_check():

    if pirs[0].state == 1 and pirs[1].state == 1 and pirs[2].state == 1:
        s.state = 2
        for bulb in range(0, 15):
            bulbs[bulb].state = 2
    else:
        s.state = 1

        print('s.state = 1')

        if pirs[0].state == 1:

            print('set bulbs to 1')

            for bulb in range(0, 5):
                bulbs[bulb].state = 1

        if pirs[0].state == 0:

            print('set bulbs to 0')

            for bulb in range(0, 5):
                bulbs[bulb].state = 0

        if pirs[1].state == 1:
            for bulb in range(5, 10):
                bulbs[bulb].state = 1

        if pirs[1].state == 0:
            for bulb in range(5, 10):
                bulbs[bulb].state = 0

        if pirs[2].state == 1:
            for bulb in range(10, 15):
                bulbs[bulb].state = 1

        if pirs[2].state == 0:
            for bulb in range(10, 15):
                bulbs[bulb].state = 0


while True:

    light_check()
    print(time.time() - s.stage_show_time)
    print('s.stage_count:' + str(s.stage_count))

    for pir in range(0, 3):
        pirs[pir].check()

    if s.state == 2:
        print('mode 2')
        if time.time() - s.stage_show_time > 0.2:
            if bulbs[s.stage_count].state == 2:
                if s.stage_next % 2 == 0:
                    bulbs[s.stage_count].h = 30000
                    bulbs[s.stage_count].b = 215

                if s.stage_next % 2 == 1:
                    bulbs[s.stage_count].h = 50000
                    bulbs[s.stage_count].b = 15

                s.stage_count += 1
                # s.stage_show_time = time.time()
                print('update show_time')

                if s.stage_count >= 15:
                    s.stage_next += 1
                    s.stage_count = 0

    if s.state == 1:
        print('mode 1')
        if time.time() - s.stage_show_time > 0.2:
            print('time to show')
            if bulbs[s.stage_count].state == 1:
                if s.stage_next % 2 == 0:
                    print('%2 == 0')
                    bulbs[s.stage_count].h += 1500
                    bulbs[s.stage_count].b = 120

                if s.stage_next % 2 == 1:
                    print ('%2 == 1')
                    bulbs[s.stage_count].h += 1500
                    bulbs[s.stage_count].b = 60

                s.stage_count += 1
                s.stage_show_time = time.time()
                print('update show_time')

                if s.stage_count >= 15:
                    s.stage_next += 1
                    s.stage_count = 0

        if pirs[0].state == 1:
            print ('pirs[0] == 1')
            if time.time() - pirs[0].show_time > 1:
                if pirs[0].count % 2 == 0:
                    for bulb in range(0, 5):
                        bulbs[bulb].h = 20000

                if pirs[0].count % 2 == 1:
                    for bulb in range(0, 5):
                        bulbs[bulb].h = 40000

                pirs[0].count += 1
                if pirs[0].count >= 5:
                    pirs[0].next += 1
                    pirs[0].count = 0
                pirs[0].show_time = time.time()

        if pirs[1].state == 1:
            print('pirs[1] == 1')
            if time.time() - pirs[1].show_time > 1:
                if pirs[1].count % 2 == 0:
                    for bulb in range(5, 10):
                        bulbs[bulb].h = 20000

                if pirs[1].count % 2 == 1:
                    for bulb in range(5, 10):
                        bulbs[bulb].h = 40000

                pirs[1].count += 1
                if pirs[1].count >= 5:
                    pirs[1].next += 1
                    pirs[1].count = 0
                pirs[1].show_time = time.time()

        if pirs[2].state == 1:
            print('pirs[2] == 1')
            if time.time() - pirs[2].show_time > 1:
                if pirs[2].count % 2 == 0:
                    for bulb in range(10, 15):
                        bulbs[bulb].h = 20000

                if pirs[2].count % 2 == 1:
                    for bulb in range(10, 15):
                        bulbs[bulb].h = 40000

                pirs[2].count += 1
                if pirs[2].count >= 5:
                    pirs[2].next += 1
                    pirs[2].count = 0
                pirs[2].show_time = time.time()






