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
        self.main_color = 20000

s = Stage()


class LightS:

    def __init__(self):
        self.no = 0
        self.h = 20000
        self.s = 254
        self.b = 254
        self.state = 0
        self.power = 0

    def toggle(self, state):
        self.state = state

    # def update(self, temp_h, temp_s, temp_b):
    #     self.h = temp_h
    #     self.s = temp_s
    #     self.b = temp_b
    #
    #     lights[self.no].hue = self.h
    #     lights[self.saturation] = self.s
    #     lights[self.no].brightness = self.b

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
        if time.time() - self.toggle_time > 15:
            self.state = 0

pirs = {}

for sensor in range(0, 3):
    pirs[sensor] = PirS()


def mot1():
    print('motion sensor1')
    pirs[0].detect()


def mot2():
    print('motion sensor2')
    pirs[1].detect()


def mot3():
    print('motion sensor3')
    pirs[2].detect()

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

        if pirs[0].state == 1:
            for bulb in range(0, 5):
                bulbs[bulb].state = 1

        if pirs[0].state == 0:

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
    # print ('L.state: 1:{0:0d} 2:{1:1d} 5:{2:2d} 6:{3:3d} 10:{4:4d} 11:{5:5d}'.format(bulbs[0].state, bulbs[1].state, bulbs[5].state, bulbs[6].state, bulbs[10].state, bulbs[11].state))

    for pir in range(0, 3):
        pirs[pir].check()

    if s.state == 2:

        if time.time() - s.stage_show_time > 0.2:

            print('time to show 2 state')

            print('P: 1:{0:0d} 2:{1:1d} 3:{2:2d}'.format(pirs[0].state, pirs[1].state, pirs[2].state))

            print(time.time() - s.stage_show_time)

            print(
                'H:1:{0:0d} 2:{1:1d} 3:{2:2d} 4:{3:3d} 5: {4:4d}'.format(bulbs[0].h, bulbs[1].h, bulbs[2].h, bulbs[3].h,
                                                                         bulbs[4].h))
            print('H:6:{0:0d} 7:{1:1d} 8:{2:2d} 9:{3:3d} 10: {4:4d}'.format(bulbs[5].h, bulbs[6].h, bulbs[7].h,
                                                                            bulbs[8].h,
                                                                            bulbs[9].h))
            print('H:11:{0:0d} 12:{1:1d} 13:{2:2d} 14:{3:3d} 15: {4:4d}'.format(bulbs[10].h, bulbs[11].h, bulbs[12].h,
                                                                                bulbs[13].h, bulbs[14].h))

            print(
                'B:1:{0:0d} 2:{1:1d} 3:{2:2d} 4:{3:3d} 5: {4:4d}'.format(bulbs[0].b, bulbs[1].b, bulbs[2].b, bulbs[3].b,
                                                                         bulbs[4].b))
            print('B:6:{0:0d} 7:{1:1d} 8:{2:2d} 9:{3:3d} 10: {4:4d}'.format(bulbs[5].b, bulbs[6].b, bulbs[7].b,
                                                                            bulbs[8].b,
                                                                            bulbs[9].b))
            print('B:11:{0:0d} 12:{1:1d} 13:{2:2d} 14:{3:3d} 15: {4:4d}'.format(bulbs[10].b, bulbs[11].b, bulbs[12].b,
                                                                                bulbs[13].b, bulbs[14].b))

            s.stage_show_time = time.time()

            if bulbs[s.stage_count].state == 2:

                # bulbs[s.stage_count].h = 30000
                # bulbs[s.stage_count].b = 215
                #
                # lights[s.stage_count].hue = bulbs[s.stage_count].h
                # lights[s.stage_count].brightness = bulbs[s.stage_count].b

                if s.stage_next % 2 == 0:
                    bulbs[s.stage_count].h = 46580 + random.randrange(500)
                    bulbs[s.stage_count].b = 254

                    lights[s.stage_count].hue = bulbs[s.stage_count].h
                    lights[s.stage_count].brightness = bulbs[s.stage_count].b

                if s.stage_next % 2 == 1:
                    bulbs[s.stage_count].h = 32768 + random.randrange(1000)
                    bulbs[s.stage_count].b = 15

                    lights[s.stage_count].hue = bulbs[s.stage_count].h
                    lights[s.stage_count].brightness = bulbs[s.stage_count].b

            s.stage_count += 1

            print('update show 2 time')

            if s.stage_count >= 15:
                s.stage_next += 1
                s.stage_count = 0

    if s.state == 1:
        if time.time() - s.stage_show_time > 0.4:
            print('time to show 1 state')

            print('P: 1:{0:0d} 2:{1:1d} 3:{2:2d}'.format(pirs[0].state, pirs[1].state, pirs[2].state))

            print('H:1:{0:0d} 2:{1:1d} 3:{2:2d} 4:{3:3d} 5: {4:4d}'.format(bulbs[0].h, bulbs[1].h, bulbs[2].h, bulbs[3].h, bulbs[4].h))
            print('H:6:{0:0d} 7:{1:1d} 8:{2:2d} 9:{3:3d} 10: {4:4d}'.format(bulbs[5].h, bulbs[6].h, bulbs[7].h, bulbs[8].h, bulbs[9].h))
            print('H:11:{0:0d} 12:{1:1d} 13:{2:2d} 14:{3:3d} 15: {4:4d}'.format(bulbs[10].h, bulbs[11].h, bulbs[12].h,bulbs[13].h, bulbs[14].h))

            print('B:1:{0:0d} 2:{1:1d} 3:{2:2d} 4:{3:3d} 5: {4:4d}'.format(bulbs[0].b, bulbs[1].b, bulbs[2].b, bulbs[3].b, bulbs[4].b))
            print('B:6:{0:0d} 7:{1:1d} 8:{2:2d} 9:{3:3d} 10: {4:4d}'.format(bulbs[5].b, bulbs[6].b, bulbs[7].b, bulbs[8].b, bulbs[9].b))
            print('B:11:{0:0d} 12:{1:1d} 13:{2:2d} 14:{3:3d} 15: {4:4d}'.format(bulbs[10].b, bulbs[11].b, bulbs[12].b, bulbs[13].b, bulbs[14].b))

            if bulbs[s.stage_count].state == 0:

                print('bulbs active')

                print('%2 == 0')
                bulbs[s.stage_count].h = s.main_color
                bulbs[s.stage_count].b = 254
                bulbs[s.stage_count].s = 254


                lights[s.stage_count].hue = bulbs[s.stage_count].h
                lights[s.stage_count].brightness = bulbs[s.stage_count].b
                lights[s.stage_count].saturation = bulbs[s.stage_count].s



                # if s.stage_next % 2 == 0:
                #     print('%2 == 0')
                #     bulbs[s.stage_count].h = s.main_color
                #     bulbs[s.stage_count].b = 120
                #
                #     lights[s.stage_count].hue = bulbs[s.stage_count].h
                #     lights[s.stage_count].brightness = bulbs[s.stage_count].b
                #
                # if s.stage_next % 2 == 1:
                #     print ('%2 == 1')
                #     bulbs[s.stage_count].h = s.main_color
                #     bulbs[s.stage_count].b = 60
                #
                #     lights[s.stage_count].hue = bulbs[s.stage_count].h
                #     lights[s.stage_count].brightness = bulbs[s.stage_count].b

            s.stage_count += 1
            s.main_color += 100
            if s.main_color > 45000:
                s.main_color = 20000
            s.stage_show_time = time.time()
            print('update show_time')

            if s.stage_count >= 15:
                s.stage_next += 1
                s.stage_count = 0

        if pirs[0].state == 1:

            if time.time() - pirs[0].show_time > 0.5:
                if pirs[0].next % 2 == 0:
                    for bulb in range(0, 5):
                        if bulbs[bulb].state == 1:
                            bulbs[bulb].h = 20000
                            bulbs[bulb].b = 254

                            lights[s.stage_count].hue = bulbs[s.stage_count].h
                            # lights[s.stage_count].brightness = bulbs[s.stage_count].b

                if pirs[0].next % 2 == 1:
                    for bulb in range(0, 5):
                        if bulbs[bulb].state == 1:
                            bulbs[bulb].h = 30000
                            bulbs[bulb].b = 1

                            lights[s.stage_count].hue = bulbs[s.stage_count].h
                            # lights[s.stage_count].brightness = bulbs[s.stage_count].b

                pirs[0].show_time = time.time()
                pirs[0].count += 1
                if pirs[0].count >= 5:
                    pirs[0].next += 1
                    pirs[0].count = 0

        if pirs[1].state == 1:
            if time.time() - pirs[1].show_time > 0.5:
                if pirs[1].next % 2 == 0:
                    for bulb in range(5, 10):
                        if bulbs[bulb].state == 1:
                            bulbs[bulb].h = 20000
                            bulbs[bulb].b = 254

                            lights[s.stage_count].hue = bulbs[s.stage_count].h
                            # lights[s.stage_count].brightness = bulbs[s.stage_count].b

                if pirs[1].next % 2 == 1:
                    for bulb in range(5, 10):
                        if bulbs[bulb].state == 1:
                            bulbs[bulb].h = 30000
                            bulbs[bulb].b = 1

                            lights[s.stage_count].hue = bulbs[s.stage_count].h
                            # lights[s.stage_count].brightness = bulbs[s.stage_count].b

                pirs[1].count += 1
                if pirs[1].count >= 5:
                    pirs[1].next += 1
                    pirs[1].count = 0
                pirs[1].show_time = time.time()

        if pirs[2].state == 1:
            if time.time() - pirs[2].show_time > 0.5:
                if pirs[2].next % 2 == 0:
                    for bulb in range(10, 15):
                        if bulbs[bulb].state == 1:
                            bulbs[bulb].h = 20000
                            bulbs[bulb].b = 254

                            lights[s.stage_count].hue = bulbs[s.stage_count].h
                            # lights[s.stage_count].brightness = bulbs[s.stage_count].b

                if pirs[2].next % 2 == 1:
                    for bulb in range(10, 15):
                        if bulbs[bulb].state == 1:
                            bulbs[bulb].h = 30000
                            bulbs[bulb].b = 1

                            lights[s.stage_count].hue = bulbs[s.stage_count].h
                            # lights[s.stage_count].brightness = bulbs[s.stage_count].b

                pirs[2].count += 1
                if pirs[2].count >= 5:
                    pirs[2].next += 1
                    pirs[2].count = 0
                pirs[2].show_time = time.time()






