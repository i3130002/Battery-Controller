import os

percentage = 53
command = f"echo {percentage} | sudo tee /sys/class/power_supply/BAT1/charge_control_end_threshold"
os.system(command)

os.system("cat /sys/class/power_supply/BAT1/charge_control_end_threshold")