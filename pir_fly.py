from gpiozero import LED, Button
from signal import pause
from time import sleep

from phue import Bridge
import logging

lightrunning = {1:False, 2:False, 3:False}

b = Bridge('192.168.1.178', 'YxPYRWNawywC-sKHkjuRho7iOwMMSrn3di2ETF74')  # Enter bridge IP here.

lights = b.get_light_objects()

def lights_change():




led = LED(27)
button = Button(17, pull_up=False)

def light_3second():
  print("light")
  led.on()

  for light in lights:
      light.brightness = 250
      light.xy = [random.random(), random.random()]
      sleep(2)
  led.off()

button.when_pressed = light_3second

pause()