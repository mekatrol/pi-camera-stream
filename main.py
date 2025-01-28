from flask import Flask, Response
from picamera2 import Picamera2
import cv2

app = Flask(__name__)

camera = Picamera2()
camera.configure(camera.create_preview_configuration(main={"format": 'XRGB8888', "size": (1920, 1080)}))
camera.start()

def generate_frames():
    while True:
        # Capture a frame
        frame = camera.capture_array()
        
        # Convert to color format
        frameBGR = cv2.cvtColor(frame , cv2.COLOR_RGB2BGR)
        
        # Create jpg image from frame
        _, buffer = cv2.imencode('.jpg', frameBGR)
        
        # Convert to bytes
        frame = buffer.tobytes()
        
        # Yeild this frame with jpg content type (note specific line breaks are required)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/live-feed')
def live_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8123)
