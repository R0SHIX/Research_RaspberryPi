import picamera 
import io
import threading
import os


class CameraFeed:
    def __init__(self, save_path):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (640, 480)
        self.stream = io.BytesIO()
        self.is_recording = False
        self.thread = None
        self.save_path = save_path

    def start_recording(self) :
        self.is_recording = True
        self.thread = threading.Thread(target = self._record)
        self.thread.start()

    def stop_recording(self):
        self.is_recording =False
        if self.thread:
            self.thread.join()
    
    def _record(self):
        while self.is_recording:
            self.camera.capture(self.stream, format = 'jpeg')
            self.stream.seek(0)

