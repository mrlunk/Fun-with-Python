import time

def binary_clock():
    while True:
        # get current time
        current_time = time.localtime()
        hours = bin(current_time.tm_hour)[2:].zfill(5)
        minutes = bin(current_time.tm_min)[2:].zfill(6)
        seconds = bin(current_time.tm_sec)[2:].zfill(7)

        # print binary clock
        print(f"{hours}/{minutes}/{seconds}", end="\r")

        # wait for one second
        time.sleep(1)

if __name__ == '__main__':
    binary_clock()

# Script by: MrLunk
# https://github.com/mrlunk/ 
