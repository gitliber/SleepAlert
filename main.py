from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import imutils
import time
import dlib
import cv2
import datetime

#start web cam
webcam = VideoStream(src=0).start()
time.sleep(1.0)

landmarks = dlib.shape_predictor("model/shape_predictor_68_face_landmarks.dat")
face_recognition = dlib.get_frontal_face_detector()

sleep_count = 0
max_sleep_count = 30

normal = False
normal_count = 0.0
normal_eye_ratio = 0

frame = webcam.read()
frame = imutils.resize(frame, width=450)
img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

 # insert information text to video frame
font = cv2.FONT_HERSHEY_SIMPLEX
input_frame = img




now = datetime.datetime.now()
CurrentTime= now.strftime("%Y-%m-%d %H:%M:%d")
cv2.putText(frame, "Sleep Detector: " + str(CurrentTime), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0xFF, 0xFF, 0xFF0), 2)
def eye_ratio(eye):
    avg_height = (abs(eye[1][1]-eye[5][1])+abs(eye[2][1]-eye[4][1]))/2
    width = abs(eye[0][0]-eye[3][0])

    return avg_height/width
while True:
    #get the image corresponding to a frame
    frame = webcam.read()
    frame = imutils.resize(frame, width=450)
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_recognition(img, 0)
        
    if(not(normal) and normal_count<47):

 # insert information text to video frame
    
        cv2.rectangle(input_frame, (1, 50), (50, 80), (180, 132, 109), -1)
        cv2.putText(
            input_frame,
            'ATTENTION PLEASE - Your activities are being logged',
            (60, 70),
            font,
            0.5,
            (0xFF, 0xFF, 0xFF),
            1,
            cv2.FONT_HERSHEY_SIMPLEX,
            )

 #       cv2.putText(frame, "FOCUS YOUR NORMAL EYES", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
    for face in faces:
        #get the landmark data for the face as numpy array
        face_data = face_utils.shape_to_np(landmarks(img,face))
        
        #left eye positions are from 36th index to 41st index
        #right eye positions are from 42th index to 47st index
        
        #get eye data and show in the frame 
        left_eye = face_data[36:42]
        right_eye = face_data[42:48]
        
        leftEyeHull = cv2.convexHull(left_eye)
        rightEyeHull = cv2.convexHull(right_eye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        
        eye_avg_ratio = eye_ratio(left_eye)+eye_ratio(right_eye)/2.0
        #print(eye_avg_ratio)
        if(not(normal)):
            if(normal_count<50):
               normal_eye_ratio = normal_eye_ratio+eye_avg_ratio
            else:
                normal_eye_ratio = normal_eye_ratio/normal_count
                normal = True
                cv2.putText(frame, "Sleep Detector: " + str(CurrentTime), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0xFF, 0xFF, 0xFF0), 2)
 #               cv2.putText(frame, "LETS START!", (140, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (150, 0, 255), 3)
                print(normal_eye_ratio)
                
        normal_count=normal_count+1
            
    else:
            #print(normal_eye_ratio-eye_avg_ratio)
            if(normal_eye_ratio-eye_avg_ratio>0.05):
                sleep_count = sleep_count+1
                GPA=sleep_count/30
                
                if(sleep_count>max_sleep_count):
                     now = datetime.datetime.now()
                     CurrentTime= now.strftime("%Y-%m-%d %H:%M:%S")
                     cv2.putText(frame, "Sleep Detector: " + str(CurrentTime), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0xFF, 0xFF, 0xFF0), 2)
                     cv2.putText(frame, "Sleeping time (seconds):" + str("%6.0f " % GPA), (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0xFF, 0xFF, 0xFF0), 2)
                if ((GPA > 2) and (GPA < 5)):
                     cv2.putText(frame, "Alert! You should take a rest", (10, 230), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                print("Sleeping log - Time: " + str(CurrentTime) + " Duration: " + str("%6.0f" % GPA))
            else:
                sleep_count = 0
        
    #show web cam frame 
    cv2.imshow("Frame", frame)
    if(normal_count==51):
        cv2.waitKey(1000)
        normal_count = 0
    else:
        wait = cv2.waitKey(1)
        if wait==ord("q"):
            cv2.destroyAllWindows()
            webcam.stop()
            break
