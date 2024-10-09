import cv2
import webbrowser

detector = cv2.QRCodeDetector()

def read_image(location):
    image = cv2.imread(location)
    url, coords, pixels = detector.detectAndDecode(image)
    print(url, coords, pixels)

    webbrowser.open(url)

def read_from_camera():
    video = cv2.VideoCapture(1)
    sucess,frame = video.read()
    
    while sucess:
        url, coords, pixels = detector.detectAndDecode(frame)
        if url:
            webbrowser.open(url)
            break

        cv2.imshow("frame",frame)

        if cv2.waitKey(1) == ord("q"):
            break

        sucess,frame = video.read()

    video.release()
    cv2.destroyAllWindows()

read_image("automation\\qr code\\code\\qr.png")