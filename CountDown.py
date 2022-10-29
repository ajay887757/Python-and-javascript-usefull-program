# inputData=input("Enter")    
# if inputData=="1":
#     break
import threading
import time
import sys

def CountDown(time_sec):
    value = ""
    print("1. Stop \n2. Pause \n3.Reset \n4.Resume")
    print("\t\t"+"Count Down")
    # while True
    while time_sec:
        min,sec=divmod(time_sec,60)
        if min >60:
            hours ,min =divmod(min,60)
            time_format='{:02d}:{:02d}:{:02d}'.format(hours,min,sec)
        else:
            time_format='{:02d}:{:02d}'.format(min,sec)
        print("\t\t"+time_format,end="\r")  #same line overlapping
        # print(time_format)
        time.sleep(1)
        time_sec-=1

    print("Count Down Complited")


# t = int(input("Enter the time in seconds: "))
# result=CountDown(t)

thread = threading.Thread(target=CountDown.run, args=(30))
thread.start()

time.sleep(3)
CountDown.pause()