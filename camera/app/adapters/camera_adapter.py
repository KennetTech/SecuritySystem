import cv2
import datetime
import time
from app.adapters.rabbitmq_adapter import RabbitMQAdapter

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

video_capture = cv2.VideoCapture(0)

# Starting RabbitMQ adapter to communicate with backend

rabbit = RabbitMQAdapter()

class Camera:
    def __init__(self):
        self.detection = False
        self.detection_stopped_time = None
        self.timer_started = False
        self.SECONDS_TO_RECORD_AFTER_DETECTION = 5
        self.out = None

        startCapture(self, video_capture)

        video_capture.release()
        cv2.destroyAllWindows()
    
              
def startCapture(self, video_capture):
    while True:
        ret, frame = video_capture.read()
        if frame is None:
            break


        detectAndCapture(self, frame)

        if cv2.waitKey(1) == ord('q'):
            break
        
      
    
def detectAndCapture(self, frame):    

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, 1.3, 5)
    bodies = body_cascade.detectMultiScale(grey, 1.3, 5)
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    frame_size = (int(video_capture.get(3)), int(video_capture.get(4))) 

    if len(faces) + len(bodies) > 0:
        if self.detection:
            self.timer_started = False
        else:
            self.detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            self.out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
            print("Started Recording!")
    if self.detection:
        if self.timer_started:
            if time.time() - self.detection_stopped_time >= self.SECONDS_TO_RECORD_AFTER_DETECTION:
                self.detection = False
                self.timer_started = False
                self.out.release()
                print("stopped Recording!")
                rabbit.publish_message("VideoFileID")
        else:
            self.timer_started = True
            self.detection_stopped_time = time.time()

    if self.detection:
        self.out.write(frame)

    



        


    