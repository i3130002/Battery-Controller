import os
import time

path = "/tmp/BatteryChargePercentage"
last_percentage = 100

if not os.path.exists(path):
    with open(path, "wt") as file:
        file.write(str(last_percentage))

while True:
    with open(path, "rt") as file:
        percentage = file.read()
        percentage_int = int(percentage)
        if percentage_int == last_percentage:
            continue
        print(f"battery percentage changed from {last_percentage} to:{percentage_int}")
        last_percentage = percentage_int

    time.sleep(1)
