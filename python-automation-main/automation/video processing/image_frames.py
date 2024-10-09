import cv2

video = cv2.VideoCapture("automation\\video processing\\files\\video.mp4")
print(video)
print(video.read())

sucess, frame = video.read()

count = 1
while sucess:
    sucess, frame = video.read()
    cv2.imwrite(f"automation\\video processing\\images\\{count}.jpg",frame)
    count += 1