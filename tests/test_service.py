import os
import time

SETTINGS_PERCENTAGE_PATH = "/tmp/BatteryChargePercentage"
CHARGING_PERCENTAGE_PATH = "/sys/class/power_supply/BAT1/charge_control_end_threshold"

last_percentage = 100

if not os.path.exists(SETTINGS_PERCENTAGE_PATH):
    with open(SETTINGS_PERCENTAGE_PATH, "wt") as file:
        file.write(str(last_percentage))

def get_charging_percentage():
    with open(CHARGING_PERCENTAGE_PATH, "rt") as file:
        battery_percentage = file.read()
        return int(battery_percentage)

def set_charging_percentage(percentage:int):
    command = f"echo {percentage} | sudo tee {CHARGING_PERCENTAGE_PATH}"
    os.system(command)
    battery_percentage = get_charging_percentage()
    if int(battery_percentage) != percentage:
        print(f"Unable to set the percentage. Required:{percentage}, Current:{battery_percentage}")
        return False
    print(f"Battery charge percentage changed from {last_percentage} to:{battery_percentage}")
    return True

def get_settings_percentage():
    with open(SETTINGS_PERCENTAGE_PATH, "rt") as file:
        percentage = file.read()
        percentage_int = int(percentage)
        percentage_int = max(53, percentage_int)
        percentage_int = min(100, percentage_int)
        return percentage_int


last_percentage = get_settings_percentage()
print(f"Current battery percentage target is {last_percentage}")

while True:
    percentage_int = get_settings_percentage()
    if percentage_int == last_percentage:
        continue
    set_charging_percentage(percentage_int)
    last_percentage = percentage_int

    time.sleep(1)
