
from greenlet import getcurrent
import time 
import threading
import cv2 
import os
from core.settings import MEDIA_ROOT

class CameraEvent(object):
    def __init__(self):
        self.events = {}

    def wait(self):
        ident = getcurrent()
        if ident not in self.events:
            self.events[ident] = [threading.Event(), time.time()]
        return self.events[ident][0].wait()

    def set(self):
        now = time.time()
        remove = None
        for ident, event in self.events.items():

            if not event[0].isSet():
                event[0].set()
                event[1] = now
            else:
                if now - event[1] > 5:
                    remove = ident
        if remove:
            del self.events[remove]

    def clear(self):
        self.events[getcurrent()][0].clear()

class Camera:
    def __init__(self, source=0, cname='superior', resolution=[640,320]):
        self.resolution = resolution
        self.source = source
        self.cname = cname
        self.frame = None
        self.frameData = None
        self.thread = None
        self.last_access = 0
        self.event = CameraEvent()
        
    def create_thread(self):
        if self.thread is None:
            self.camera = cv2.VideoCapture(self.source)
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, int(self.resolution[0]))
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, int(self.resolution[1]))
            self.last_access = time.time()

            self.thread = threading.Thread(target=self.thread_function) # type: ignore
            self.thread.start()

            self.event.wait()
        
    def thread_function(self):
        for_frames = self.frames()
        for frame in for_frames:
            self.frame = frame
            self.event.set()
            if time.time() - self.last_access > 1:
                for_frames.close()
                self.camera.release()
                break
        self.thread = None

    def frames(self):
        while True:
            success, img = self.camera.read()
            if not success:
                break
            ret, buffer = cv2.imencode('.jpg', img) 
            self.frameData = img
            yield buffer.tobytes()
    
    def get_frame(self):
        self.last_access = time.time()
        self.event.wait()
        self.event.clear()
        return self.frame

    def save_frame(self, path=MEDIA_ROOT):
        elementos = os.listdir(f"{path}/fotos/{self.cname}/")
        print (elementos)
        id = len(elementos) if elementos else 0
        os.makedirs(f"{path}/fotos/{self.cname}/", exist_ok=True)
        self.create_thread()
        cv2.imwrite(f"{path}/fotos/{self.cname}/captura{id}.png",self.frameData)
        print(path)

if __name__ == '__main__':
    camera = Camera()
    camera.create_thread()
    print(dir(camera))