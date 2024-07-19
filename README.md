
# Service
`sudo gedit /etc/systemd/system/batterycontrol.service`
```
[Unit]
Description=Battery Charge Controller
After=network.target
StartLimitIntervalSec=0
[Service]
Type=simple
Restart=no
RestartSec=10
User=user
ExecStart=python3 /home/user/Documents/Projects/Python/BatteryChargeLimitter/service.py

[Install]
WantedBy=multi-user.target
```

# Desktop application shortcut
path: `~/.local/share/applications/battery-controller.desktop`

```
[Desktop Entry]
Name=Battery Charge Controller 
Version=1.0
Comment=A gui app Battery Controller for linux
Exec=python3 /home/user/Documents/Projects/Python/BatteryChargeLimitter/desktop.py
Icon=/home/user/Documents/Projects/Python/BatteryChargeLimitter/assets/battery_not_charging.png
Terminal=false
Type=Application
```

# Asset attribution
* [Ui icons created by Yudhi Restu - Flaticon](https://www.flaticon.com/free-icons/ui)
* [Power icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/power)