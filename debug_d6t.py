#! /usr/bin/python

import smbus
import sys
import getopt
import time
import pigpio
import datetime
import sys
import os
import json

import spidev

try:
    import paho.mqtt.publish as publish
except ImportError:
    import os
    import inspect

    cmd_subfolder = os.path.realpath(
            os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "../src")))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
        import paho.mqtt.publish as publish

count = 0

os.environ['TZ'] = 'Asia/Taipei'
time.tzset()

block1 = 0
block2 = 0
block3 = 0
block4 = 0
block5 = 0
block6 = 0
block7 = 0
block8 = 0
block9 = 0
block10 = 0
block11 = 0
block12 = 0
block13 = 0
block14 = 0
block15 = 0
block16 = 0


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


columns = [0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8]


Initialise()





i2c_bus = smbus.SMBus(1)
OMRON_1 = 0x0a  # 7 bit I2C address of Omron MEMS Temp Sensor D6T-44L
OMRON_BUFFER_LENGTH = 35  # Omron data buffer size
temperature_data = [0] * OMRON_BUFFER_LENGTH  # initialize the temperature data list
p = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

D6T_value = {
    "1": "0",
    "2": "0",
    "3": "0",
    "4": "0",
    "5": "0",
    "6": "0",
    "7": "0",
    "8": "0",
    "9": "0",
    "10": "0",
    "11": "0",
    "12": "0",
    "13": "0",
    "14": "0",
    "15": "0",
    "16": "0"
}
tPATA = 0
tP = [0]*16
tPEC = 0

# intialize the pigpio library and socket connection to the daemon (pigpiod)
pi = pigpio.pi()  # use defaults
version = pi.get_pigpio_version()
print('PiGPIO version = ' + str(version))
handle = pi.i2c_open(1, 0x0a)  # open Omron D6T device at address 0x0a on bus 1

# initialize the device based on Omron's appnote 1
result = i2c_bus.write_byte(OMRON_1, 0x4c);
# print 'write result = '+str(result)

# for x in range(0, len(temperature_data)):
# print x
# Read all data  tem
# temperature_data[x]=i2c_bus.read_byte(OMRON_1)
count = 0

while True:
    count = count + 1
    p = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    D6T_value = {
        "0": "0",
        "1": "0",
        "2": "0",
        "3": "0",
        "4": "0",
        "5": "0",
        "6": "0",
        "7": "0",
        "8": "0",
        "9": "0",
        "10": "0",
        "11": "0",
        "12": "0",
        "13": "0",
        "14": "0",
        "15": "0"
    }

    # print ('count:',count)

    (bytes_read, temperature_data) = pi.i2c_read_device(handle, len(temperature_data))


    # Display data
    # print(bytes_read)
    if bytes_read == 35:

        tPATA = 256 * temperature_data[1] + temperature_data[0]
        print("tPATA: %d" % tPATA )

        tP[0] = 256 * temperature_data[3] + temperature_data[2]
        tP[1] = 256 * temperature_data[5] + temperature_data[4]
        tP[2] = 256 * temperature_data[7] + temperature_data[6]
        tP[3] = 256 * temperature_data[9] + temperature_data[8]
        tP[4] = 256 * temperature_data[11] + temperature_data[10]
        tP[5] = 256 * temperature_data[13] + temperature_data[12]
        tP[6] = 256 * temperature_data[15] + temperature_data[14]
        tP[7] = 256 * temperature_data[17] + temperature_data[16]
        tP[8] = 256 * temperature_data[19] + temperature_data[18]
        tP[9] = 256 * temperature_data[21] + temperature_data[20]
        tP[10] = 256 * temperature_data[23] + temperature_data[22]
        tP[11] = 256 * temperature_data[25] + temperature_data[24]
        tP[12] = 256 * temperature_data[27] + temperature_data[26]
        tP[13] = 256 * temperature_data[29] + temperature_data[28]
        tP[14] = 256 * temperature_data[31] + temperature_data[30]
        tP[15] = 256 * temperature_data[33] + temperature_data[32]

        tPEC = temperature_data[34]

        # for n in range(16):
        #     print("tP[%d] = %d" % (n, tP[n]))

        print("tPEC:%d" % tPEC)

        for x in range(16):
            p[x] = tP[x] - tPATA
            if p[x] > 10:
                p[x] = 1
            else:
                p[x] = 0


        # for x in range(bytes_read):
        #
        #     ts = time.time()
        #     timenow = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        #     # print(temperature_data[x]),
        #     if x == 2:
        #         if (temperature_data[x]) >= (temperature_data[0]) + 35:
        #             # print('block 0 is On')
        #             p[0] = 1
        #             D6T_value["0"] = "1"
        #
        #             block1 = block1 + 1
        #             # publish.single("/D6T/Time", timenow, hostname="www.znh.tw")
        #             # publish.single("/D6T/Block1", block1, hostname="www.znh.tw")
        #             # print ("%s %s" % (timenow, block1))
        #
        #     if x == 4:
        #         if (temperature_data[x]) >= (temperature_data[0]) + 35:
        #             # print('block 1 is On')
        #             p[1] = 1
        #             D6T_value["1"] = "1"
        #
        #             block2 = block2 + 1
        #             # publish.single("/D6T/Time", timenow, retain=True, hostname="www.znh.tw")
        #             # publish.single("/D6T/Block2", block2, retain=True, hostname="www.znh.tw")
        #             # print ("%s %s" % (timenow, block2))
        #
        #     if x == 6:
        #         if (temperature_data[x]) >= (temperature_data[0]) + 35:
        #             # print('block 2 is On')
        #             p[2] = 1
        #             D6T_value["2"] = "1"
        #
        #             block3 = block3 + 1
        #             # publish.single("/D6T/Time", timenow, retain=True, hostname="www.znh.tw")
        #             # publish.single("/D6T/Block3", block3, retain=True, hostname="www.znh.tw")
        #             # print ("%s %s" % (timenow, block3))
        #
        #     if x == 8:
        #         if (temperature_data[x]) >= (temperature_data[0]) + 35:
        #             # print('block 3 is On')
        #             p[3] = 1
        #             D6T_value["3"] = "1"
        #
        #             block4 = block4 + 1
        #             # publish.single("/D6T/Time", timenow, retain=True, hostname="www.znh.tw")
        #             # publish.single("/D6T/Block4", block4, retain=True, hostname="www.znh.tw")
        #             # print ("%s %s" % (timenow, block4))
        #
        #     if x == 10:
        #         if (temperature_data[x]) >= (temperature_data[0]) + 35:
        #             # print('block 4 is On')
        #             p[4] = 1
        #             D6T_value["4"] = "1"
        #
        #             block5 = block5 + 1
        #             # publish.single("/D6T/Time", timenow, retain=True, hostname="www.znh.tw")
        #             # publish.single("/D6T/Block5", block5, retain=True, hostname="www.znh.tw")
        #
        #             pi.write(17, 1)
        #         else:
        #             pi.write(17, 0)
        #     if x == 12:
        #         if (temperature_data[x]) >= (temperature_data[0]) + 35:
        #             # print('block 5 is On')
        #             p[5] = 1
        #             D6T_value["5"] = "1"
        #             block6 = block6 + 1
        #             # publish.single("/D6T/Time", timenow, retain=True, hostname="www.znh.tw")
        #             # publish.single("/D6T/Block6", block6, retain=True, hostname="www.znh.tw")
        #             pi.write(27, 1)
        #         else:
        #             pi.write(27, 0)
        #     if x == 14:
        #         if (temperature_data[x]) >= (temperature_data[0]) + 35:
        #             # print('block 6 is On')
        #             p[6] = 1
        #             D6T_value["6"] = "1"
        #
        #             block7 = block7 + 1
        #             # publish.single("/D6T/Time", timenow, retain=True, hostname="www.znh.tw")
        #             # publish.single("/D6T/Block7", block7, retain=True, hostname="www.znh.tw")
        #             pi.write(22, 1)
        #         else:
        #             pi.write(22, 0)
        #     if x == 16:
        #         if (temperature_data[x]) >= (temperature_data[0]) + 35:
        #             # print('block 7 is On')
        #             p[7] = 1
        #             D6T_value["7"] = "1"
        #             block8 = block8 + 1
        #             # publish.single("/D6T/Time", timenow, retain=True, hostname="www.znh.tw")
        #             # publish.single("/D6T/Block8", block8, retain=True, hostname="www.znh.tw")
        #             pi.write(18, 1)
        #         else:
        #             pi.write(18, 0)
        #     if x == 18:
        #         if (temperature_data[x]) >= (temperature_data[0]) + 35:
        #             # print('block 8 is On')
        #             p[8] = 1
        #             D6T_value["8"] = "1"
        #
        #             block9 = block9 + 1
        #             # publish.single("/D6T/Time", timenow, retain=True, hostname="www.znh.tw")
        #             # publish.single("/D6T/Block9", block9, retain=True, hostname="www.znh.tw")
        #
        #     if x == 10:
        #         if (temperature_data[x]) >= (temperature_data[0]) + 35:
        #             # print('block 9 is On')
        #             p[9] = 1
        #             D6T_value["9"] = "1"
        #
        #             block10 = block10 + 1
        #             # publish.single("/D6T/Time", timenow, retain=True, hostname="www.znh.tw")
        #             # publish.single("/D6T/Block10", block10, retain=True, hostname="www.znh.tw")
        #     if x == 22:
        #         if (temperature_data[x]) >= (temperature_data[0]) + 35:
        #             # print('block 10 is On')
        #             p[10] = 1
        #             D6T_value["10"] = "1"
        #
        #             block11 = block11 + 1
        #             # publish.single("/D6T/Time", timenow, retain=True, hostname="www.znh.tw")
        #             # publish.single("/D6T/Block11", block11, retain=True, hostname="www.znh.tw")
        #     if x == 24:
        #         if (temperature_data[x]) >= (temperature_data[0]) + 35:
        #             # print('block 11 is On')
        #             p[11] = 1
        #             D6T_value["11"] = "1"
        #
        #             block12 = block12 + 1
        #             # publish.single("/D6T/Time", timenow, retain=True, hostname="www.znh.tw")
        #             # publish.single("/D6T/Block12", block12, retain=True, hostname="www.znh.tw")
        #     if x == 26:
        #         if (temperature_data[x]) >= (temperature_data[0]) + 35:
        #             # print('block 12 is On')
        #             p[12] = 1
        #             D6T_value["12"] = "1"
        #
        #             block13 = block13 + 1
        #             # publish.single("/D6T/Time", timenow, retain=True, hostname="www.znh.tw")
        #             # publish.single("/D6T/Block13", block13, retain=True, hostname="www.znh.tw")
        #     if x == 28:
        #         if (temperature_data[x]) >= (temperature_data[0]) + 35:
        #             # print('block 13 is On')
        #             p[13] = 1
        #             D6T_value["13"] = "1"
        #
        #             block14 = block14 + 1
        #             # publish.single("/D6T/Time", timenow, retain=True, hostname="www.znh.tw")
        #             # publish.single("/D6T/Block14", block14, retain=True, hostname="www.znh.tw")
        #     if x == 10:
        #         if (temperature_data[x]) >= (temperature_data[0]) + 35:
        #             # print('block 14 is On')
        #             p[14] = 1
        #             D6T_value["14"] = "1"
        #
        #             block15 = block15 + 1
        #             # publish.single("/D6T/Time", timenow, retain=True, hostname="www.znh.tw")
        #             # publish.single("/D6T/Block15", block15, retain=True, hostname="www.znh.tw")
        #     if x == 32:
        #         if (temperature_data[x]) >= (temperature_data[0]) + 35:
        #             # print('block 15 is On')
        #             p[15] = 1
        #             D6T_value["15"] = "1"
        #
        #             block16 = block16 + 1
        #             # publish.single("/D6T/Time", timenow, retain=True, hostname="www.znh.tw")
        #             # publish.single("/D6T/Block16", block16, retain=True, hostname="www.znh.tw")

    else:
        print('not 45')
        print(bytes_read)
        pi.i2c_close(handle)
        pi.stop()
        print('pigpio stop')
        i2c_bus = smbus.SMBus(1)
        OMRON_1 = 0x0a  # 7 bit I2C address of Omron MEMS Temp Sensor D6T-44L
        OMRON_BUFFER_LENGTH = 35  # Omron data buffer size
        temperature_data = [0] * OMRON_BUFFER_LENGTH  # initialize the temperature data list
        pi = pigpio.pi()
        handle = pi.i2c_open(1, 0x0a)
        result = i2c_bus.write_byte(OMRON_1, 0x4c);
        sleep(0.5)
    # print(str(D6T_value))
    print("\n")
    D6T_json = json.dumps(D6T_value)
    # publish.single("/D6T/Blocks", str(p), retain=True, hostname="www.znh.tw")
    # publish.single("/D6T/Blocks", str(D6T_value), retain=True, hostname="www.znh.tw")
    # publish.single("/D6T/Blocks", D6T_json, retain=True, hostname="localhost")

    print (tP[3], tP[2], tP[1], tP[0])
    print (tP[7], tP[6], tP[5], tP[4])
    print (tP[11], tP[10], tP[9], tP[8])
    print (tP[15], tP[14], tP[13], tP[12])

    print (p[3], p[2], p[1], p[0])
    print (p[7], p[6], p[5], p[4])
    print (p[11], p[10], p[9], p[8])
    print (p[15], p[14], p[13], p[12])

    pi.set_mode(17, pigpio.INPUT)
    print(pi.read(17))

    d6t = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

    if p[3] == 1:
        d6t[0] |= 0xC0
        d6t[1] |= 0xC0

    if p[2] == 1:
        d6t[0] |= 0x30
        d6t[1] |= 0x30

    if p[1] == 1:
        d6t[0] |= 0x0C
        d6t[1] |= 0x0C

    if p[0] == 1:
        d6t[0] |= 0x03
        d6t[1] |= 0x03

    if p[7] == 1:
        d6t[2] |= 0xC0
        d6t[3] |= 0xC0

    if p[6] == 1:
        d6t[2] |= 0x30
        d6t[3] |= 0x30

    if p[5] == 1:
        d6t[2] |= 0x0C
        d6t[3] |= 0x0C

    if p[4] == 1:
        d6t[2] |= 0x03
        d6t[3] |= 0x03

    if p[12] == 1:
        d6t[4] |= 0xC0
        d6t[5] |= 0xC0

    if p[11] == 1:
        d6t[4] |= 0x30
        d6t[5] |= 0x30

    if p[10] == 1:
        d6t[4] |= 0x0C
        d6t[5] |= 0x0C

    if p[9] == 1:
        d6t[4] |= 0x03
        d6t[5] |= 0x03

    if p[15] == 1:
        d6t[6] |= 0xC0
        d6t[7] |= 0xC0

    if p[14] == 1:
        d6t[6] |= 0x30
        d6t[7] |= 0x30

    if p[13] == 1:
        d6t[6] |= 0x0C
        d6t[7] |= 0x0C

    if p[12] == 1:
        d6t[6] |= 0x03
        d6t[7] |= 0x03



    for i in range(0, 8):
        resp = spi.xfer([columns[i], d6t[i]])


    time.sleep(0.64)

# print 'done'

pi.i2c_close(handle)
pi.stop()

spi.close
