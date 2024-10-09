import cv2

video = cv2.VideoCapture(0) # 0 é o numero se é a primeira webcam, se não for ver outros
sucess, frame = video.read()

height = frame.shape[0]
width = frame.shape[1]

face_cascade = cv2.CascadeClassifier("automation\\video processing\\files\\faces.xml")
output = cv2.VideoWriter("automation\\video processing\\files\\output.avi",cv2.VideoWriter_fourcc(*"DIVX"),30,(width,height))



while sucess:
    faces = face_cascade.detectMultiScale(frame,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),4)
    cv2.imshow("recording",frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    output.write(frame)
    sucess, frame = video.read()

output.release()
video.release()
cv2.destroyAllWindows()