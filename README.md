# pi-camera-stream

## pre-requisites

```bash
sudo apt install python3-opencv python3-picamera2

pip install Flask
```

## start on boot

> sudo nano /etc/systemd/system/pi_camera_stream.service:

```ini
[Unit]
Description=PI Camera Stream
After=network.target

[Service]
WorkingDirectory=/home/pi/pi-camera-stream/
ExecStart=/usr/bin/python /home/pi/pi-camera-stream/main.py
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
