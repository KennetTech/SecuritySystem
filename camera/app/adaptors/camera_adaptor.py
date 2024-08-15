import cv2

class CameraAdaptor:

    def __init__(self):
        cap = cv2.VideoCapture(0)

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

        while True:
            ret, frame = cap.read()
            if frame is None:
                break

            detectAndCapture(frame, face_cascade, body_cascade)

            if cv2.waitKey(1) == ord('q'):
                break
    
        cap.release()
        cv2.destroyAllWindows()
    
              
    
    
def detectAndCapture(frame,face_cascade, body_cascade):
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, 1.3, 5)
    bodies = body_cascade.detectMultiScale(grey, 1.3, 5)

    cv2.imshow("Camera", frame)

CameraAdaptor()

        


    