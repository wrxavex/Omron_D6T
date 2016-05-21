import os
import time
import platform
from time import sleep
import subprocess
import thread

hostname = platform.node()
os.environ['TZ'] = 'Asia/Taipei'
time.tzset()

def get_env(sleeptime, *args):
	global env_text
	while True:
		env_text = subprocess.check_output(["sudo", "python", "/home/pi/d6t/d6t.py"])
		print(env_text)
		sleep(1)


def main():
    time_now = time.strftime('%X')
    date_now = time.strftime('%x %w')
    print('this')
    thread.start_new_thread(get_env, (1, ""))
    # thread.start_new_thread(update_LCD, (time_now, date_now))

    while True:
        sleep(1)

if __name__ == '__main__':
    print ("Display info")
    main()
