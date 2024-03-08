import os
import cv2
import imageio
from greenlet import getcurrent
import threading
import time
import subprocess

from core.settings import DATA_PATH
from core.commands import singleton, logger

def getIndex(pos):
    """
    Calcula un índice a partir de una posición dada.

    Esta función toma una posición representada como un diccionario con las claves 'x' y 'y'.
    Luego, normaliza las coordenadas dividiéndolas por 100 y aplica una serie de cálculos
    para calcular un índice basado en la posición. El cálculo del índice se realiza de la siguiente manera:

    - La coordenada x se redondea hacia abajo y se le suma 4, luego se agrega el aporte x multiplicado por el decimal restante de la coordenada x.
    - La coordenada y se redondea hacia abajo, se le suma 4 y se multiplica por 9. Luego se resta el aporte y multiplicado por el decimal restante de la coordenada y.

    Parámetros:
    pos (dict): Un diccionario que representa la posición con las claves 'x' y 'y'.

    Returns:
    float: El índice calculado basado en la posición dada.

    Ejemplos:
    >>> getIndex({'x': 150, 'y': 250})
    62.5
    >>> getIndex({'x': 300, 'y': 500})
    62.5
    """
    aportex = 0.1
    aportey = 1

    posA = pos
    
    posA['x'] = posA['x']/100 
    posA['y'] = posA['y']/100

    x = (posA['x'] - posA['x']%1 + 4) + (posA['x']%1 * aportex)
    y = ((-posA['y'] + posA['y']%1 + 4) * 9) - ((posA['y']%1 * aportey))
    #(f"X({pos[0]} Y({pos[1]}))",x+y)
    return x+y


def cameraInfo(camera = None):
    """
    Recupera información sobre una cámara de video.

    Esta función toma el nombre de la cámara como argumento opcional. Si no se proporciona el nombre de la cámara,
    la función no hace nada y devuelve None. Si se proporciona el nombre de la cámara, la función busca el dispositivo
    correspondiente en la lista de dispositivos de video utilizando el comando 'v4l2-ctl --list-devices'. Luego, busca
    la resolución de video admitida para ese dispositivo utilizando el comando 'v4l2-ctl -d <id> --list-formats-ext',
    donde <id> es el ID del dispositivo encontrado. La función devuelve el ID del dispositivo y su resolución.

    Parámetros:
    camera (str, opcional): El nombre de la cámara (definido en la variable de entorno) para buscar en la lista de dispositivos.

    Returns:
    tuple: Una tupla que contiene el ID del dispositivo de video y su resolución, o None si no se proporciona el nombre de la cámara.

    Ejemplo:
    >>> camera_id, camera_resolution = cameraInfo('MY_CAMERA')
    >>> print(camera_id, camera_resolution)
    1, [1280, 720]
    """
    if not camera:
        return
    else:
        id = 0
        resolution = [0,0]
        res = subprocess.run(['v4l2-ctl','--list-devices'], stdout=subprocess.PIPE)
        resDecoded = res.stdout.decode().split('\n')
        for i in range(len(resDecoded)):
            if os.environ[camera] in resDecoded[i]:
                id = int(resDecoded[i+1].strip('\t/dev/video'))
                temp = subprocess.Popen(['v4l2-ctl', '-d', f'{id}', '--list-formats-ext'], stdout=subprocess.PIPE)
                temp2 = subprocess.check_output(('grep', 'x'), stdin=temp.stdout)
                resolution = temp2.decode('utf-8').split('\n')[0].split('\t')[2].split(' ')[-1].split('x')
        return id, resolution


class CameraEvent(object):
    """
    Una clase que implementa una primitiva de sincronización para eventos entre hilos.
    """
    def __init__(self):
        """
        Inicializa una nueva instancia de la clase CameraEvent.
        """
        self.events = {}

    def wait(self):
        """
        Espera a que ocurra un evento.

        Devuelve:
            Un bool que indica si el evento ocurrió.
        """
        ident = getcurrent()
        if ident not in self.events:
            self.events[ident] = [threading.Event(), time.time()]
        return self.events[ident][0].wait()

    def set(self):
        """
        Establece el evento.
        """
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
        """
        Borra el evento.
        """
        self.events[getcurrent()][0].clear()

class Camera:
    """
    Una clase que representa una cámara.
    """
    def __init__(self, cname):
        """
        Inicializa una nueva instancia de la clase Camera.

        Args:
            cname (str): El nombre de la cámara.
        """
        self.cname = cname
        self.frame = None
        self.frameData = None
        self.last_access = 0
        self.event = CameraEvent()
        self.thread = None
        
    def create_thread(self):
        """
        Crear un hilo para leer fotogramas de la cámara.
        """
        if self.thread is None:
            self.source, self.resolution = cameraInfo(self.cname)
            self.camera = cv2.VideoCapture(self.source)
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, int(self.resolution[0]))
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, int(self.resolution[1]))
            self.last_access = time.time()

            self.thread = threading.Thread(target=self.thread_function) # type: ignore
            self.thread.start()

            self.event.wait()
        
    def thread_function(self):
        """
        La función que se ejecuta en el hilo para leer fotogramas de la cámara.
        """
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
        """
        Un generador que produce fotogramas de la cámara.
        """
        while True:
            success, img = self.camera.read()
            if not success:
                break
            ret, buffer = cv2.imencode('.jpg', img) 
            self.frameData = img
            yield buffer.tobytes()
    
    def get_frame(self):
        """
        Obtiene el último fotograma de la cámara.

        Devuelve:
            El último fotograma de la cámara.
        """
        self.last_access = time.time()

        self.event.wait()
        self.event.clear()
        return self.frame

    def save_frame(self, pos, prueba, path=DATA_PATH):
        """
        Guarda un fotograma de la cámara.

        Args:
            pos (dict): La posición de la cámara.
            prueba (str): El nombre de la prueba.
            path (str, opcional): La ruta en la que guardar el fotograma. Por defecto es DATA_PATH.
        """
        os.makedirs(f"{path}/{prueba}/fotos/{self.cname}/", exist_ok=True)
        self.create_thread()
        cv2.imwrite(f"{path}/{prueba}/fotos/{self.cname}/{getIndex(pos)}_{pos}.png", self.frameData)


@singleton
class AboveCamera(Camera):
    """
    Clase que representa la cámara de arriba.
    """
    def __init__(self):
        """
        Inicializa una nueva instancia de la clase AboveCamera.
        """
        Camera.__init__(self, 'ABOVE_CAMERA')

@singleton
class BelowCamera(Camera):
    """
    Clase que representa la cámara inferior.
    """
    def __init__(self):
        """
        Inicializa una nueva instancia de la clase BelowCamera.
        """
        Camera.__init__(self, 'BELOW_CAMERA')

def gen_frame(camera):
    """
    Genera un fotograma desde la cámara especificada.

    Args:
        camera (Cámara): La cámara desde la que generar el fotograma.

    Produce:
        Un fotograma de la cámara especificada.
    """
    camera.create_thread()
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    
def gen_screenshot(self, camera):
    """
    Genera una captura de pantalla desde la cámara especificada.

    Args:
        camera (Cámara, opcional): La cámara desde la que generar la captura de pantalla. Por defecto es None.

    Devuelve:
        La captura de pantalla de la cámara especificada.
    """
    if camera:
        camera.create_thread()
        screenshot = camera.get_frame()
        return screenshot
    return ''


def exportGif(prueba):
    """
    Exporta un gif de la prueba especificada.

    Args:
        prueba (str): El nombre de la prueba.
    """
    try:
        cameras = ['superior', 'inferior']
        for camera in cameras:
            path = f'{DATA_PATH}/{prueba}/fotos/{camera}'
            names = os.listdir(path)
            names.sort()
            images = []
            for n in names:
                images.append(imageio.imread(f'{path}/{n}'))
                imageio.imread(f'{path}/{n}')
            imageio.mimsave(f'{path}.gif', images)
    except Exception as error:
        logger.error(f"{type(error)} error")