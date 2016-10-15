

from pythonosc import dispatcher
from pythonosc import osc_server
import _thread


def display_osc_master_message(unused_addr, args1, args2, args3, args4, args5, args6, args7, args8, args9, args10, args11, args12,
                args13, args14, args15):
    try:

        ds.device_status[1] = args1     # osc source
        ds.device_status[2] = args2     # to message
        ds.device_status[3] = args3     # played counts
        ds.device_status[4] = args4     # 1st device status
        ds.device_status[5] = args5     # 2rd device status
        ds.device_status[6] = args6     # 3th device status
        ds.device_status[7] = args7
        ds.device_status[8] = args8
        ds.device_status[9] = args9
        ds.device_status[10] = args10
        ds.device_status[11] = args11
        ds.device_status[12] = args12
        ds.device_status[13] = args13
        ds.device_status[14] = args14
        ds.device_status[15] = args15

        if ds.device_status[4] == 1:
            ds.last_play = time.time()

        # print('args={0} args2={1} args3={2} args4={3}'.format( ds.device_status[1], ds.device_status[2], ds.device_status[3], ds.device_status[4]))
        # print(args1)
        # print(args2)
        # print(args3)
        # print(args4)
    except:
        pass
        print("osc message error")

def main(threadName, delay):
    print ("main")




if __name__ == '__main__':
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/omxplayer", display_osc_master_message)
    print("Osc dispatcher ")

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))

    # 用多線程執行main
    try:
        _thread.start_new_thread(main, ("main", 0))
    except:
        print("something wrong")

    # 持續osc接收
    server.serve_forever()

