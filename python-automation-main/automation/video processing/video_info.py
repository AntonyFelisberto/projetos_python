import cv2

video = cv2.VideoCapture("automation\\video processing\\files\\video.mp4")

width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_WIDTH)
nr_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
fps = video.get(cv2.CAP_PROP_FPS)
print(width,height,nr_frames,fps)

