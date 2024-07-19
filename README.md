
![Tray Demo](screenshots/TrayDemo.jpeg)


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

# Tested On
* Asus TUF A15


# License
This software is for personal use only without the right to distribute or sell it.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# Service (QT issues)
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

# Asset attribution
* [Ui icons created by Yudhi Restu - Flaticon](https://www.flaticon.com/free-icons/ui)
* [Power icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/power)