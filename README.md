# pi-camera-stream

## pre-requisites

```bash
sudo apt install -y python3-opencv python3-picamera2 python3-pip
```

```
mkdir pi-camera-stream

cd pi-camera-stream

python3 -m venv .venv --system-site-packages
source .venv/bin/activate

pip3 install Flask
```

## start on boot
```bash
sudo nano /etc/systemd/system/pi_camera_stream.service
```

```ini
[Unit]
Description=PI Camera Stream
After=network.target

[Service]
WorkingDirectory=/home/pi/pi-camera-stream/
ExecStart=/home/pi/pi-camera-stream/.venv/bin/python3 /home/pi/pi-camera-stream/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable pi_camera_stream
sudo systemctl start pi_camera_stream    
sudo systemctl status pi_camera_stream
sudo systemctl restart pi_camera_stream
sudo systemctl stop pi_camera_stream
```
