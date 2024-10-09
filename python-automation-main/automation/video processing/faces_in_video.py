import cv2

video = cv2.VideoCapture("automation\\video processing\\files\\video.mp4")

sucess, frame = video.read()

face_cascade = cv2.CascadeClassifier("automation\\video processing\\files\\faces.xml")

height = frame.shape[0]
width = frame.shape[1]
output = cv2.VideoWriter("automation\\video processing\\files\\output.avi",cv2.VideoWriter_fourcc(*"DIVX"),30,(width,height))

while sucess:
    faces = face_cascade.detectMultiScale(frame,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),4)
    output.write(frame)
    sucess, frame = video.read()

output.release()