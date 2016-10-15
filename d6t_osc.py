

from pythonosc import dispatcher
from pythonosc import osc_server

import argparse

import _thread


def display_osc_master_message(unused_addr, args1, args2, args3, args4, args5, args6, args7, args8, args9, args10, args11, args12,
                args13, args14, args15):
    try:
        print(args1)

        # args1 is osc source
        # args2 is to message
        # played counts
        # 1st device status
        # 2rd device status
        # 3th device status

    except:
        pass
        print("osc message error")

def main(threadName, delay):
    print ("main")




if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="192.168.1.139", help="The ip to listen on")
    parser.add_argument("--port",
                        type=int, default=9997, help="The port to listen on")
    args = parser.parse_args()

    client = udp_client.UDPClient(args.ip, args.port)

    for x in range(10):
        msg = osc_message_builder.OscMessageBuilder(address="/d6t1")
        msg.add_arg(random.random())
        msg = msg.build()
        client.send(msg)
        time.sleep(1)


    # dispatcher = dispatcher.Dispatcher()
    # dispatcher.map("/omxplayer", display_osc_master_message)
    # print("Osc dispatcher ")

    # server = osc_server.ThreadingOSCUDPServer(
    #     (args.ip, args.port), dispatcher)
    # print("Serving on {}".format(server.server_address))

    # 用多線程執行main
    # try:
    #     _thread.start_new_thread(main, ("main", 0))
    # except:
    #     print("something wrong")

    # 持續osc接收
    # server.serve_forever()

