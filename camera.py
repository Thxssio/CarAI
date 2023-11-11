import numpy as np
import cv2 as cv
import time

cap = cv.VideoCapture(0)
#cap.set(cv.CAP_PROP_FPS, int(60))
#cap.set(cv.CV_CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 380)

prev_frame_time = 0
new_frame_time = 0



if not cap.isOpened():
    print("Não foi possivel abrir a camera.")
    exit()
while True:

    ret, frame = cap.read()


    if not ret:
        print("Não foi possivel abrir a stream. Saindo...")
        break
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    width = frame.shape[1]
    height = frame.shape[0]

    print(width)
    print(height)

    start_point = (0, 240) 
    end_point = (640, 240)
    color = (0, 255, 0)
    thickness = 3

    center_coordinates = (320, 240)
    radius = 20
    colorCircle = (255, 0, 0)
    thicknessCircle = 2 


    cam = cv.line(frame, start_point, end_point, color, thickness) 
    cam = cv.circle(frame,  center_coordinates, radius, colorCircle, thicknessCircle)

    



    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time 
    fps = int(fps)
    fps = str(fps)
    font = cv.FONT_HERSHEY_SIMPLEX 
    cv.putText(frame, fps, (7, 70), font, 3, (100, 255, 0), 3, cv.LINE_AA)
    cv.imshow('frame', cam)


    if cv.waitKey(1) == ord('q'):
        break   

cap.release()
cv.destroyAllWindows()