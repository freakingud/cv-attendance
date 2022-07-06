import cv2
import loadcam

cam = cv2.VideoCapture(0) # create camera object

while True:
    ret, frame = cam.read() # read from camera

    # detech face
    face_locations, face_name =

    cv2.imshow("Frame", frame) #shows current frame

    key = cv2.waitKey(1)
    if key == 27:
        break;

cam.release()
cv2.destroyAllWindows()