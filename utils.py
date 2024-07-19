import os
SETTINGS_PERCENTAGE_PATH = "/tmp/BatteryChargePercentage"
CHARGING_PERCENTAGE_PATH = "/sys/class/power_supply/BAT1/charge_control_end_threshold"

def get_charging_percentage():
    with open(CHARGING_PERCENTAGE_PATH, "rt") as file:
        battery_percentage = file.read()
        return int(battery_percentage)

def set_charging_percentage(percentage:int):
    last_percentage = get_charging_percentage()
    if last_percentage == percentage:
        print(f"No need to set the percentage. Required:{percentage}, Current:{last_percentage}")
        return True
    command = f"echo {percentage} | pkexec tee {CHARGING_PERCENTAGE_PATH}"
    os.system(command)
    battery_percentage = get_charging_percentage()
    if int(battery_percentage) != percentage:
        print(f"Unable to set the percentage. Required:{percentage}, Current:{battery_percentage}")
        return False
    print(f"Battery charge percentage changed from:{last_percentage} to:{battery_percentage}")
    return True