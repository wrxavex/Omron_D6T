import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)

def Initialise():
    # decoding :BCD
    spi.writebytes([0x09])
    spi.writebytes([0x00])

    # brightness
    spi.writebytes([0x0a])
    spi.writebytes([0x03])

    # scanlimit; 8 LEDs
    spi.writebytes([0x0b])
    spi.writebytes([0x07])

    # power-down mode: 0. normal mode:1
    spi.writebytes([0x0c])
    spi.writebytes([0x01])

    # test display: 1; EOT. display: 0
    spi.writebytes([0x0f])
    spi.writebytes([0x00])

d6t1 = 0xC0
d6t2 = 0x30
d6t3 = 0x0C
d6t4 = 0x03

d6t = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

columns = [0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8]

b1 = 1
b2 = 1
b3 = 1
b4 = 1
b5 = 1
b6 = 1
b7 = 1
b8 = 1

if b1 == 1:
    d6t[0] |= 0xC0
    d6t[1] |= 0xC0
if b2 == 1:
    d6t[0] |= 0x30
    d6t[1] |= 0x30

if b3 == 1:
    d6t[0] |= 0x0C
    d6t[1] |= 0x0C

if b4 == 1:
    d6t[0] |= 0x03
    d6t[1] |= 0x03

if b5 == 1:
    d6t[2] |= 0xC0
    d6t[3] |= 0xC0

if b6 == 1:
    d6t[2] |= 0x30
    d6t[3] |= 0x30

if b7 == 1:
    d6t[2] |= 0x0C
    d6t[3] |= 0x0C

if b8 == 1:
    d6t[2] |= 0x03
    d6t[3] |= 0x03

Initialise()

for i in range(0,8):
    resp = spi.xfer([columns[i], d6t[i]])

spi.close



