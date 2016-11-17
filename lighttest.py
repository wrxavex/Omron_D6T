from gpiozero import MotionSensor
from gpiozero import LED
from signal import pause
from time import sleep
import random

pir1 = MotionSensor(17)
pir2 = MotionSensor(27)
pir3 = MotionSensor(22)
# led1 = LED(5)
# led2 = LED(4)

from phue import Bridge
import logging

import thread

logging.basicConfig()

lightrunning = {1:False, 2:False, 3:False}

b = Bridge('192.168.1.178', 'YxPYRWNawywC-sKHkjuRho7iOwMMSrn3di2ETF74')  # Enter bridge IP here.

lights = b.get_light_objects()



# class light_status():
#
#     def __init__(self):
#
#         self.sensor1 = 0
#         self.sensor2 = 0
#         self.sensor3 = 0
#         self.light9_status = 0
#         self.light10_status = 0
#         self.light11_status = 0
#         self.light12_status = 0
#         self.light13_status = 0
#         self.light14_status = 0
#         self.light15_status = 0
#
# ls = light_status()
#
#
# def light_9(sleeptime, *args):
#     print("light 9 on")
#     lights[8].on = True
#     lights[8].saturation = 254
#
#     while(1):
#
#         lights[8].brightness = 1
#         lights[8].hue = 20000
#         if ls.sensor1 > 10:
#             sleep(5)
#         elif ls.sensor1 > 5:
#             sleep(2)
#         else:
#             sleep(1)
#         lights[8].hue = 45000
#         lights[8].brightness = 254
#         if ls.sensor1 > 10:
#             sleep(5)
#         elif ls.sensor1 > 5:
#             sleep(2)
#         else:
#             sleep(1)
#
#         print("light 9 active")
#
#         if ls.sensor1 > 1:
#             ls.sensor1 -= 1
#
#
# def light_10(sleeptime, *args):
#
#     lights[9].on = True
#     lights[9].saturation = 254
#     print("light 10 on")
#
#     while(1):
#
#         lights[9].brightness = 1
#         lights[9].hue = 20000
#         if ls.sensor1 > 10:
#             sleep(5)
#         elif ls.sensor1 > 5:
#             sleep(2)
#         else:
#             sleep(1)
#             lights[9].hue = 45000
#         lights[9].brightness = 254
#         if ls.sensor1 > 10:
#             sleep(5)
#         elif ls.sensor1 > 5:
#             sleep(2)
#         else:
#             sleep(1)
#
#         if ls.sensor1 > 1:
#             ls.sensor1 -= 1
#
#         print("light 10 active")
#
#
# def light_11(sleeptime, *args):
#
#     lights[10].on = True
#     lights[10].saturation = 254
#     print("light 11 on")
#
#     while(1):
#
#         lights[10].brightness = 1
#         lights[10].hue = 20000
#         if ls.sensor2 > 10:
#             sleep(5)
#         elif ls.sensor2 > 5:
#             sleep(2)
#         else:
#             sleep(1)
#         lights[10].hue = 45000
#         lights[10].brightness = 254
#         if ls.sensor2 > 10:
#             sleep(5)
#         elif ls.sensor2 > 5:
#             sleep(2)
#         else:
#             sleep(1)
#
#         if ls.sensor2 > 1:
#             ls.sensor2 -= 1
#
#         print("light 11 active")
#
#
# def light_12(sleeptime, *args):
#     lights[11].on = True
#     lights[11].saturation = 254
#     print("light 12 on")
#
#     while(1):
#
#         lights[11].brightness = 1
#         lights[11].hue = 20000
#         if ls.sensor2 > 10:
#             sleep(5)
#         elif ls.sensor2 > 5:
#             sleep(2)
#         else:
#             sleep(1)
#
#         lights[11].hue = 45000
#         lights[11].brightness = 254
#         if ls.sensor2 > 10:
#             sleep(5)
#         elif ls.sensor2 > 5:
#             sleep(2)
#         else:
#             sleep(1)
#
#         if ls.sensor2 > 1:
#             ls.sensor2 -= 1
#
#         print("light 12 active")
#
#
# def light_13(sleeptime, *args):
#     lights[12].on = True
#     lights[12].saturation = 254
#     print("light 13 on")
#
#     while(1):
#
#         lights[12].brightness = 1
#         lights[12].hue = 20000
#         if ls.sensor2 > 10:
#             sleep(5)
#         elif ls.sensor2 > 5:
#             sleep(2)
#         else:
#             sleep(1)
#         lights[12].hue = 45000
#         lights[12].brightness = 254
#         if ls.sensor2 > 10:
#             sleep(5)
#         elif ls.sensor2 > 5:
#             sleep(2)
#         else:
#             sleep(1)
#
#         if ls.sensor2 > 1:
#             ls.sensor2 -= 1
#
#         print("light 13 active")
#
#
# def light_14(sleeptime, *args):
#
#     lights[13].on = True
#     lights[13].saturation = 254
#     print("light 14 on")
#     while(1):
#
#         lights[13].brightness = 1
#         lights[13].hue = 20000
#         if ls.sensor2 > 10:
#             sleep(5)
#         elif ls.sensor2 > 5:
#             sleep(2)
#         else:
#             sleep(1)
#         lights[13].hue = 45000
#         lights[13].brightness = 254
#         if ls.sensor2 > 10:
#             sleep(5)
#         elif ls.sensor2 > 5:
#             sleep(2)
#         else:
#             sleep(1)
#
#         if ls.sensor2 > 1:
#             ls.sensor2 -= 1
#
#         print("light 14 active")
#
#
# def light_15(sleeptime, *args):
#
#     lights[14].on = True
#     lights[14].saturation = 254
#     print("light 15 on")
#     while(1):
#
#         lights[14].brightness = 1
#         lights[14].hue = 20000
#         if ls.sensor2 > 10:
#             sleep(5)
#         elif ls.sensor2 > 5:
#             sleep(2)
#         else:
#             sleep(1)
#         lights[14].hue = 45000
#         lights[14].brightness = 254
#         if ls.sensor2 > 10:
#             sleep(5)
#         elif ls.sensor2 > 5:
#             sleep(2)
#         else:
#             sleep(1)
#
#         if ls.sensor2 > 1:
#             ls.sensor2 -= 1
#
#         print("light 15 active")
#
#
# def open_light9():
#     if ls.light9_status == 0:
#         ls.light9_status = 1
#         thread.start_new_thread(light_9, (1, ""))
#
#
# def open_light10():
#     if ls.light10_status == 0:
#         ls.light10_status = 1
#         thread.start_new_thread(light_10, (1, ""))
#
#
# def open_light11():
#     if ls.light11_status == 0:
#         ls.light11_status = 1
#         thread.start_new_thread(light_11, (1, ""))
#
#
# def open_light12():
#     if ls.light12_status == 0:
#         ls.light12_status = 1
#         thread.start_new_thread(light_12, (1, ""))
#
#
# def open_light13():
#     if ls.light13_status == 0:
#         ls.light13_status = 1
#         thread.start_new_thread(light_13, (1, ""))
#
#
# def open_light14():
#     if ls.light14_status == 0:
#         ls.light14_status = 1
#         thread.start_new_thread(light_14, (1, ""))
#
#
# def open_light15():
#     if ls.light15_status == 0:
#         ls.light15_status = 1
#         thread.start_new_thread(light_15, (1, ""))
#
#
# open_light9()
# sleep(0.3)
# open_light10()
# sleep(0.3)
# open_light11()
# sleep(0.3)
# open_light12()
# sleep(0.3)
# open_light13()
# sleep(0.3)
# open_light14()
# sleep(0.3)
# open_light15()
#
#
# def lightSet1Active():
#     ls.sensor1 +=50
#     print('pir1 active')
#
#
# def lightSet2Active():
#     ls.sensor2 +=50
#     print('pir2 active')

def mot1():
    print('motion sensor1')
    # led1.on()
    lights[5].on = True
    lights[5].brightness = 127
    sleep(30)
    lights[5].on = False
    # led1.off()


def mot2():
    print('motion sensor2')
    # led2.on()
    lights[6].on = True
    lights[6].brightness = 127
    sleep(30)
    lights[6].on = False
    # led2.off()


def mot3():
    print('motion sensor2')
    # led2.on()
    lights[7].on = True
    lights[7].brightness = 127
    sleep(30)
    lights[7].on = False
    # led2.off()


pir1.when_motion = mot1
pir2.when_motion = mot2
pir3.when_motion = mot3
pause()
