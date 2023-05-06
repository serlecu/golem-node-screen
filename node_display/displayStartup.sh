#! usr/bin/bash
cd ~/Desktop/golem-node-screen
git pull || echo "no connection" 

echo "Check requirements"
pip install -r node_display/requirements.txt

echo "Config Bluetooth"
# some lines may not be required on each reboot
sudo hciconfig hci0 piscan
sudo systemctl daemon-reload
sudo service bluetooth restart
sudo sdptool add SP
sudo chmod o+rw /var/run/sdp
sudo hciconfig hci0 piscan

echo "Config Rail i2C for Hyperp-Pixel"
sudo ln -s /dev/i2c-11 /dev/i2c-1

echo "run python"
python ~/Desktop/golem-node-screen/node_display/node-display.py

# echo "run processing"
#~/Desktop/golem-node-screen/node_display/application.linux-arm64/node_display &

# == Do perform only once == wait...
# add user to bluetooth group
# ~ sudo usermod -a -G bluetooth $USER
# previously add 'ExecStart=-/usr/lib/bluetooth/bluetoothd -- experimental'  to 'nano /etc/systemd/system/bluetooth.target.wants/bluetooth.service
# restart bluetooth
# ~ udo systemctl daemon-reload
# ~ sudo systemctl restart bluetooth.service
# ==========================