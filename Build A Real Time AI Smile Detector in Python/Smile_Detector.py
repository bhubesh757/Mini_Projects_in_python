import cv2
import numpy

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')
eye_detector  = cv2.CascadeClassifier('haarcascade_eye.xml')

# Grabbing the webcam feed

webcam = cv2.VideoCapture(0)

a = 1
while True:
    a = a+1
    successful_frame_read , frame = webcam.read()
    print(frame)
    
    frame_grayscale = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)  # blck and white 
    
    # detect the faces 
    
    faces = face_detector.detectMultiScale(frame_grayscale)
    
    
    # drawing the rectangles
    
    for(x,y,w,h) in faces:
        cv2.rectangle(frame , (x,y) , (x+w, y+h) , (100,200,4),4)
        
        
        # get the sub face of the face image using the numpy!
        the_face = frame[y:y+h , x:x+w]
        
        # changing to the grayscale
        face_grayscale = cv2.cvtColor(the_face , cv2.COLOR_BGR2GRAY)
        
        smiles  = smile_detector.detectMultiScale(face_grayscale , scaleFactor = 1.7 , minNeighbors = 20)
        
        
        # eye detecor detecting the eye!!
        eyes = eye_detector.detectMultiScale(face_grayscale,scaleFactor = 1.1, minNeighbors = 10)
        
        for(x_,y_,w_,h_) in smiles:
            cv2.rectangle(the_face , (x_,y_) , (x_+w_, y_+h_) , (255 , 255 , 255),4)
        
        # find all the smiles in the faces
        for(x__,y__,w__,h__) in eyes:
            cv2.rectangle(the_face , (x__,y__) , (x__+w__, y__+h__) , (50,50,200),4)
         
         
        if len(smiles) > 0:
             cv2.putText(frame , 'Smiling' , (x , y+h+40) , fontScale = 3,
                         fontFace  = cv2.FONT_HERSHEY_PLAIN , color = (255,255,255))

        
    # shows the current frame
    resize = cv2.resize(frame, (640, 480))
    cv2.imshow('face Recognition' , resize)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
# cleaning up
cv2.destroyAllWindows()
webcam.release()

 



