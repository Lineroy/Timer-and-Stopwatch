import time
import os

times = int(input("Time: "))

hours = times // 3600
minutes = (times - hours * 3600) // 60
seconds = times - (hours * 3600) - (minutes * 60)

seconds_start = seconds
times_counter = 0

os.system("CLS || clear")
print(f"{str(hours).rjust(2, '0')} : {str(minutes).rjust(2, '0')} : {str(seconds).rjust(2, '0')}")
time.sleep(1)
while times_counter != times:
    for i in range(1, seconds_start + 1):
        seconds = seconds_start
        seconds -= i
        times_counter += 1
        os.system("CLS || clear")
        print(f"{str(hours).rjust(2, '0')} : {str(minutes).rjust(2, '0')} : {str(seconds).rjust(2, '0')}")
        time.sleep(1)

    if minutes == 0 or str(minutes)[0] == "-" and times >= 3600:
        hours -= 1
        minutes = 60
        pass

    minutes -= 1
    seconds_start = 60
